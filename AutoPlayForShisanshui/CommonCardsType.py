#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import PlayCards
import itertools


# 这个函数用于计算手牌中各种牌面的张数，接收一个手牌列表作为参数，返回一个记录各种牌面张数列表
def GetList_count(Cardlist=[]):
    list_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for item in Cardlist:
        number = item[0]
        list_count[number] = list_count[number] + 1
    return list_count


# 这个函数用于返回所有的对子，所有对子将被存储于列表中，形如[[[3,'$'],[3,'*']],[[4,'$'],[4,'*']]]
# 并且相同值不同花色的对子将被视为不同的对子，比如[[[3,'$'],[3,'*']],[[3,'$'],[3,'#']]]
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [3, '#'], [3, '#'].......]
def FindDuizi(Cardlist=[]):
    Duizi_list = []  # 最后要返回的列表
    Cardlist.sort()
    list_count = GetList_count(Cardlist)  # 存储每种牌出现的次数
    for i in range(len(list_count)):
        temp_list = []  # 临时列表，存储一个对子
        if (list_count[i] == 2):  # 如果牌面为i的卡牌有2张，就找到一个对子
            for item in Cardlist:
                if (item[0] == i):
                    temp_list.append(item)
            Duizi_list.append(temp_list)
        elif (list_count[i] == 3):  # 如果牌面为i的卡牌有3张，就找到三个对子
            temp_list = []
            for item in Cardlist:
                index = Cardlist.index(item)
                if (item[0] == i):
                    temp_list.append(Cardlist[index])
                    temp_list.append(Cardlist[index + 1])
                    Duizi_list.append(temp_list)
                    temp_list = []
                    temp_list.append(Cardlist[index])
                    temp_list.append(Cardlist[index + 2])
                    Duizi_list.append(temp_list)
                    temp_list = []
                    temp_list.append(Cardlist[index + 1])
                    temp_list.append(Cardlist[index + 2])
                    Duizi_list.append(temp_list)
                    temp_list = []
                    break
        elif (list_count[i] == 4):  # 如果牌面为i的卡牌有3张，就找到六个对子
            for item in Cardlist:
                index = Cardlist.index(item)
                if (item[0] == i):
                    temp_list.append(Cardlist[index])
                    temp_list.append(Cardlist[index + 1])
                    Duizi_list.append(temp_list)
                    temp_list = []
                    temp_list.append(Cardlist[index])
                    temp_list.append(Cardlist[index + 2])
                    Duizi_list.append(temp_list)
                    temp_list = []
                    temp_list.append(Cardlist[index])
                    temp_list.append(Cardlist[index + 3])
                    Duizi_list.append(temp_list)
                    temp_list = []
                    temp_list.append(Cardlist[index + 1])
                    temp_list.append(Cardlist[index + 2])
                    Duizi_list.append(temp_list)
                    temp_list = []
                    temp_list.append(Cardlist[index + 1])
                    temp_list.append(Cardlist[index + 3])
                    Duizi_list.append(temp_list)
                    temp_list = []
                    temp_list.append(Cardlist[index + 2])
                    temp_list.append(Cardlist[index + 3])
                    Duizi_list.append(temp_list)
                    temp_list = []
                    break
    return Duizi_list


# 这个函数找出所有的两对，炸弹不算两对，连对也不当做普通两对，相同值不同花色的对子被视为不同的对子
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [4, '#'], [4, '#'].......]
# 返回格式为[[[2,'*'],[2,'#'],[4,'*'],[4,'&']],......]
def FindErdui(Cardlist=[]):
    Erdui_list = []  # 存储所有的二对
    Duizi_list = FindDuizi(Cardlist)  # 所有的对子
    for item1 in Duizi_list:
        index1 = Duizi_list.index(item1)
        for item2 in Duizi_list:
            index2 = Duizi_list.index(item2)
            # 普通二对不能是炸弹也不能是连对，连对另外考虑
            if (abs(item1[0][0] - item2[0][0]) >= 2 and index2 > index1):
                Erdui_list.append(item1 + item2)
    return Erdui_list


# 这个函数找出所有的连对
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [3, '#'], [3, '#'].......]
# 返回格式为[[[2,'*'],[2,'#'],[3,'*'],[4,'&']],......]
def FindLiandui(Cardlist=[]):
    Erdui_list = []  # 存储所有的二对
    Duizi_list = FindDuizi(Cardlist)  # 所有的对子
    for item1 in Duizi_list:
        index1 = Duizi_list.index(item1)
        for item2 in Duizi_list:
            index2 = Duizi_list.index(item2)
            # 如果两个对子的差的绝对值刚好等于1就是连对
            if (abs(item1[0][0] - item2[0][0]) == 1 and index2 > index1):
                Erdui_list.append(item1 + item2)
    return Erdui_list


# 这个函数找出所有的三张相同牌的组合，遇到炸弹也拆分
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [3, '#'], [3, '#'].......]
# 返回格式为 [[[3,'#'],[3,'&'],[3,'*']],[[4,'#'],[4,'&'],[4,'*']],......]
def FindSantiao(Cardlist=[]):
    Santiao = []  # 最后要返回的列表
    list_temp = []  # 存储三张或四张同样牌面的牌
    list_count = GetList_count(Cardlist)
    for i in range(len(list_count)):
        if (list_count[i] >= 3):
            for item in Cardlist:
                if (item[0] == i):
                    list_temp.append(item)
            for j in itertools.combinations(list_temp, 3):
                Santiao.append(list(j))
            list_temp = []
    return Santiao


# 这个函数找出所有的顺子（5张牌），两个相同牌面的顺子，只要其中有一张牌的花色不同，就视为两个不同的顺子
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [3, '#'], [3, '#'].......]
# 返回格式为[[[3,'$'],[4,'*'],[5,'*'],[6,'#'],[7,'*']],........]
def FindShunzi(Cardlist=[]):
    Shunzi = []  # 最后返回的列表
    temp_list = []  # 存储一个临时顺子
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    list_count = GetList_count(Cardlist)
    Cardlist.sort()
    for i in range(2, 11):
        # 找出所有连续排列且相同数字个数大于等于1的
        if (list_count[i] >= 1 and list_count[i + 1] >= 1 and list_count[i + 2] >= 1
                and list_count[i + 3] >= 1 and list_count[i + 4] >= 1):
            # 将连续的牌分别放在5个列表中
            for item in Cardlist:
                if (item[0] == i):
                    temp1.append(item)
                elif (item[0] == i + 1):
                    temp2.append(item)
                elif (item[0] == i + 2):
                    temp3.append(item)
                elif (item[0] == i + 3):
                    temp4.append(item)
                elif (item[0] == i + 4):
                    temp5.append(item)
            # 列出所有组合
            for item1 in temp1:
                for item2 in temp2:
                    for item3 in temp3:
                        for item4 in temp4:
                            for item5 in temp5:
                                temp_list.append(item1)
                                temp_list.append(item2)
                                temp_list.append(item3)
                                temp_list.append(item4)
                                temp_list.append(item5)
                                Shunzi.append(temp_list)  # 将一个新的顺子放入列表中
                                temp_list = []  # 将临时列表清空
            # 将五个存放连续排列相同数字的列表清空
            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            temp5 = []
    return Shunzi


# 这个函数找出所有的五同花，三同花一定出现在前墩，在墩好后两墩后可以很容易的判断剩下三张牌是不是同花
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [3, '#'], [3, '#'].......]
# 两个相同花色的同花只要有任意一个数字不同就视为两个不同的同花
# 会对每一个同花进行排序
# 返回格式为[[[3,'*'],[5,'*'],[6,'*'],[7,'*'],[10,'*']],.....]
def FindTonghua(Cardlist=[]):
    Tonghua = []  # 最后要返回的列表
    Heitao = []  # 存放所有黑桃色的牌 $
    Hongtao = []  # 存放所有红桃色的牌 &
    Meihua = []  # 存放所有梅花色的牌 *
    Fangkuai = []  # 存放所有方块色的牌 #
    for item in Cardlist:
        if (item[1] == '$'):
            Heitao.append(item)
        elif (item[1] == '&'):
            Hongtao.append(item)
        elif (item[1] == '*'):
            Meihua.append(item)
        else:
            Fangkuai.append(item)
    if (len(Heitao) >= 5):
        for i in itertools.combinations(Heitao, 5):
            Tonghua.append(list(i))
    if (len(Hongtao) >= 5):
        for i in itertools.combinations(Hongtao, 5):
            Tonghua.append(list(i))
    if (len(Meihua) >= 5):
        for i in itertools.combinations(Meihua, 5):
            Tonghua.append(list(i))
    if (len(Fangkuai) >= 5):
        for i in itertools.combinations(Fangkuai, 5):
            Tonghua.append(list(i))
    return Tonghua


# 这个函数找出所有的葫芦，炸弹可能被拆开组成葫芦
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [3, '#'], [3, '#'].......]
# 两个相同值的葫芦只要有一张牌花色不同就视为两个不同的葫芦
# 返回格式为[[[3,'$'],[3,'#'],[3,'*'],[4,'*],[4,'#']],.........]
# 思路：先找出所有可能的三条存放在一个列表里，然后取出每一个三条，用原列表表与这个三条做集合的差运算
# 在差集中找出可能的对子，与三条凑成一个葫芦
def FindHulu(Cardlist=[]):
    Santiao = []  # 存放所有的三条
    Duizi = []  # 存放去除三条后剩下卡牌中所有的对子
    Hulu = []  # 最后要返回的葫芦
    Santiao = FindSantiao(Cardlist)
    for item1 in Santiao:
        temp = list.copy(Cardlist)
        for i in item1:
            temp.remove(i)
        Duizi = FindDuizi(temp)
        for item2 in Duizi:
            Hulu.append(item1 + item2)
    return Hulu


# 这个函数找出所有的炸弹（4张牌）
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [3, '#'], [3, '#'].......]
# 返回格式为[[[3,'$'],[3,'#'],[3,'*'],[3,'&']],.........]
def FindZhadan(Cardlist=[]):
    Zhadan = []  # 最后返回的列表
    temp_Zhadan = []  # 存储一个临时炸弹
    list_count = GetList_count(Cardlist)
    for i in range(len(list_count)):
        if (list_count[i] == 4):
            for item in Cardlist:
                if (item[0] == i):
                    temp_Zhadan.append(item)
            Zhadan.append(temp_Zhadan)
            temp_Zhadan = []
    return Zhadan


# 这个函数找出所有的同花顺
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [3, '#'], [3, '#'].......]
# 返回格式为[[[3,'$'],[4,'$'],[5,'$'],[6,'$'],[7,'$']],.........]
def FindTonghuashun(Cardlist=[]):
    Shunzi = FindShunzi(Cardlist)  # 先找出所有的顺子
    Tonghuashun = []  # 最后返回的列表
    for item in Shunzi:
        if (item[0][1] == item[1][1] and item[1][1] == item[2][1]
                and item[2][1] == item[3][1] and item[3][1] == item[4][1]):
            Tonghuashun.append(item)
    return Tonghuashun

# if __name__ == '__main__':
