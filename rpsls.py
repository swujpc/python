#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：蒋鹏成
日期：2020-11-24
"""

import random

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    if name=="石头":# 使用if/elif/else语句将各游戏对象对应到不同的整数
        name=0
    elif name=="史波克":
        name=1
    elif name=="纸":
        name=2
    elif name=="蜥蜴":
        name=3
    elif name=="剪刀":
        name=4
    return name# 不要忘记返回结果



def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    if number=="0":# 使用if/elif/else语句将不同的整数对应到游戏的不同对象
        number="石头"
    elif number == 1:
            number = "史波克"
    elif number == 2:
            number = "纸"
    elif number == 3:
            number = "蜥蜴"
    else:
            number = "剪刀"
    return number# 不要忘记返回结果


def rpsls(player_choice):# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """

    player_choice=name_to_number(choice_name)# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    comp_number=random.randint(0,4)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    object=number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    print("计算机的选择为"+(object))# 在屏幕上显示计算机选择的随机对象

    if comp_number==player_choice:# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
        print("您和计算机出的一样呢") # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
    if comp_number==0 and (player_choice==3 or player_choice==4):
        print("计算机赢了")
    elif comp_number==1 and (player_choice==4 or player_choice==0):
        print("计算机赢了")
    elif comp_number == 2 and (player_choice ==0 or player_choice == 1):
        print("计算机赢了")
    elif comp_number == 3 and (player_choice == 1 or player_choice == 2):
        print("计算机赢了")
    elif comp_number == 4 and (player_choice == 2 or player_choice == 3):
        print("计算机赢了")
    elif player_choice==0 and (comp_number==3 or comp_number==4):
        print("您赢了")
    elif player_choice==1 and (comp_number==4 or comp_number==0):
        print("您赢了")
    elif player_choice==2 and (comp_number==0 or comp_number==1):
        print("您赢了")
    elif player_choice==3 and (comp_number==1 or comp_number==2):
        print("您赢了")
    elif player_choice==4 and (comp_number==2 or comp_number==3):
        print("您赢了")


# 对程序进行测试

print("欢迎使用RPSLS游戏")
print("请输入您的选择:")
choice_name = input()
if choice_name=="石头" or choice_name=="史波克" or choice_name=="布" or choice_name=="蜥蜴" or choice_name=="剪刀":
    print("----------------")#输入"----------------"进行分割
    print("您的选择为："+(choice_name))
    rpsls(choice_name)
else:
    print("Error: No Correct Name")


