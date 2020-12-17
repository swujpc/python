#coding:gbk
"""
���þ������㷨���з���
���ߣ�������
���ڣ�2020-12-17
"""
import pandas as pd           # ������Ҫ�õĿ�
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb

# ��������
df = pd.read_csv('frenchwine.csv')
df.columns = ['species','alcohol', 'malic_acid', 'ash', 'alcalinity ash', 'magenesium']
# �鿴ǰ5������
df.head()
print(df.head()) 


# �鿴����������ͳ����Ϣ
df.describe()
print(df.describe())

def scatter_plot_by_category(feat, x, y): #���ݵĿ��ӻ� 
    alpha = 0.5
    gs = df.groupby(feat)
    cs = cm.rainbow(np.linspace(0, 1, len(gs)))
    for g, c in zip(gs, cs):
        plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)

plt.figure(figsize=(20,5))
plt.subplot(131)
scatter_plot_by_category('species', 'alcohol', 'ash')
plt.xlabel('alcohol')
plt.ylabel('ash')
plt.title('species')
plt.show()

plt.figure(figsize=(20, 10)) #����seaborn���������frenchwine����ͬ����ͼ
for column_index, column in enumerate(df.columns):
    if column == 'species':
        continue
    plt.subplot(3, 3, column_index + 1)
    sb.violinplot(x='species', y=column, data=df)
plt.show()

# ���ȶ����ݽ����з֣������ֳ�ѵ�����Ͳ��Լ�
from sklearn.model_selection import train_test_split #����sklearn���н�����飬����ѵ�����Ͳ��Լ�
all_inputs = df[['alcohol', 'malic_acid',
                             'ash', 'alcalinity ash','magenesium']].values
all_species = df['species'].values

(X_train,
 X_test,
 Y_train,
 Y_test) = train_test_split(all_inputs, all_species, train_size=0.7, random_state=1)#70%������ѡΪѵ����
 
 


# ʹ�þ������㷨����ѵ��
from sklearn.tree import DecisionTreeClassifier #����sklearn���е�DecisionTreeClassifier������������
# ����һ������������
decision_tree_classifier = DecisionTreeClassifier()

# ѵ��ģ��
model = decision_tree_classifier.fit(X_train, Y_train)
# ���ģ�͵�׼ȷ��
print(decision_tree_classifier.score(X_test, Y_test)) 


# ʹ��ѵ����ģ�ͽ���Ԥ�⣬Ϊ�˷��㣬
# ����ֱ�ӰѲ��Լ�����������ó���������ʵ��ʹ��ʱ�����������в��Լ����ݼ�X_test��ģ�ͽ��в��ԡ�
def chinese(word):
    if word=="Zinfandel":
        return "�ɷ���"
    if word=="Syrah":
        return "����"
    if word=="Sauvignon":
        return "��ϼ��"
print(X_test[:])#�����������ݽ��в��ԣ���ȡ����������Ϊģ�͵������
for x in model.predict(X_test[:]):
    y=chinese(x)
    print(y,end=
          ' ')#������ԵĽ���������ģ��Ԥ��Ľ��
print()
print("----------------------------------------------------")
m=chinese(model.predict([[13.42,3.21,2.62,23.5,95]]))
print(m)
n=chinese(model.predict([[12.32,2.77,2.37,22,90]]))
print(n)
o=chinese(model.predict([[13.75,1.59,2.7,19.5,135]]))
print(o)
#print(model.predict([[12.32,2.77,2.37,22,90]]))

##���������ӻ�
from IPython.display import Image  
# from sklearn.externals.six import StringIO  #sklearn 0.23�汾�Ѿ�ɾ���������,ֱ�Ӱ�װsix����
from six import StringIO
from sklearn.tree import export_graphviz


features = list(df.columns[:-1])
print(features)


import pydotplus
import os #Ҫ��װһ��Graphviz���
os.environ['PATH'] = os.environ['PATH'] + (';c:\\Program Files\\Graphviz\\bin\\') #
dot_data = StringIO()  
export_graphviz(decision_tree_classifier, out_file=dot_data,feature_names=features,filled=True,rounded=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
# Image(graph[0].create_png())  
graph.write_pdf("frenchwine.pdf") #��frenchwine���ݼ����þ������㷨���ӻ�������ֵ�frenchwine.pdf�ļ���


