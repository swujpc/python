#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020-11-24
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    if name=="ʯͷ":# ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
        name=0
    elif name=="ʷ����":
        name=1
    elif name=="ֽ":
        name=2
    elif name=="����":
        name=3
    elif name=="����":
        name=4
    return name# ��Ҫ���Ƿ��ؽ��



def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    if number=="0":# ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
        number="ʯͷ"
    elif number == 1:
            number = "ʷ����"
    elif number == 2:
            number = "ֽ"
    elif number == 3:
            number = "����"
    else:
            number = "����"
    return number# ��Ҫ���Ƿ��ؽ��


def rpsls(player_choice):# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """

    player_choice=name_to_number(choice_name)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    comp_number=random.randint(0,4)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    object=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    print("�������ѡ��Ϊ"+(object))# ����Ļ����ʾ�����ѡ����������

    if comp_number==player_choice:# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
        print("���ͼ��������һ����") # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
    if comp_number==0 and (player_choice==3 or player_choice==4):
        print("�����Ӯ��")
    elif comp_number==1 and (player_choice==4 or player_choice==0):
        print("�����Ӯ��")
    elif comp_number == 2 and (player_choice ==0 or player_choice == 1):
        print("�����Ӯ��")
    elif comp_number == 3 and (player_choice == 1 or player_choice == 2):
        print("�����Ӯ��")
    elif comp_number == 4 and (player_choice == 2 or player_choice == 3):
        print("�����Ӯ��")
    elif player_choice==0 and (comp_number==3 or comp_number==4):
        print("��Ӯ��")
    elif player_choice==1 and (comp_number==4 or comp_number==0):
        print("��Ӯ��")
    elif player_choice==2 and (comp_number==0 or comp_number==1):
        print("��Ӯ��")
    elif player_choice==3 and (comp_number==1 or comp_number==2):
        print("��Ӯ��")
    elif player_choice==4 and (comp_number==2 or comp_number==3):
        print("��Ӯ��")


# �Գ�����в���

print("��ӭʹ��RPSLS��Ϸ")
print("����������ѡ��:")
choice_name = input()
if choice_name=="ʯͷ" or choice_name=="ʷ����" or choice_name=="��" or choice_name=="����" or choice_name=="����":
    print("----------------")#����"----------------"���зָ�
    print("����ѡ��Ϊ��"+(choice_name))
    rpsls(choice_name)
else:
    print("Error: No Correct Name")


