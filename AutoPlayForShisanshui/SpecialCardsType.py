#!/usr/bin/env python
# -*- coding:utf-8 -*-
import PlayCards
import CommonCardsType

# 该模块中list_list和Cardlist的内容一样

# 这个函数用于计算手牌中各种牌面的张数，接收一个手牌列表作为参数，返回一个记录各种牌面张数列表
def GetList_count(Cardlist=[]):
    list_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for item in Cardlist:
        number = item[0]
        list_count[number] = list_count[number] + 1
    return list_count


def IsZhizhunqinglong(Cardlist=[]):
    list_list = list.copy(Cardlist)
    flag1 = 1
    flag2 = 1
    for i in range(1, 13):
        if (list_list[i][1] != list_list[i - 1][1]):
            flag1 = 0
            break

    for i in range(1, 13):
        if (list_list[i][0] - list_list[i - 1][0] != 1):
            flag2 = 0
            break
    if (flag1 == 1 and flag2 == 1):
        return True
    else:
        return False


def IsYitiaolong(Cardlist=[]):
    list_list = list.copy(Cardlist)
    flag = 1
    for i in range(1, 13):
        if (list_list[i][0] - list_list[i - 1][0] != 1):
            flag = 0
            break
    if (flag == 1):
        return True
    else:
        return False


def IsShierhuangzu(Cardlist=[]):
    list_list = list.copy(Cardlist)
    count = 0
    for i in range(0, 13):
        if (list_list[i][0] > 10):
            count = count + 1
    if (count >= 12):
        return True
    else:
        return False


def IsSantonghuashun(Cardlist=[]):
    temp_Sanshunzi = []  # 存放在查找过程中可能存在的三顺子的一部分
    list_list = list.copy(Cardlist)  # Cardlist的副本
    Sanshunzi = []
    SanTonghuashun = []
    temp_list1 = []  # 存放去掉一个顺子后的手牌
    temp_list2 = []  # 存放去掉两个顺子后的手牌
    Shunzi1 = []  # 第一层循环中所有的顺子
    Shunzi2 = []  # 第二层循环中所有的顺子
    Shunzi1 = CommonCardsType.FindShunzi(list_list)
    if (Shunzi1 != []):
        for item1 in Shunzi1:
            temp_list1 = PlayCards.CalculateSub(list_list, item1)
            Shunzi2 = CommonCardsType.FindShunzi(temp_list1)
            if (Shunzi2 != []):
                for item2 in Shunzi2:
                    temp_list2 = PlayCards.CalculateSub(temp_list1, item2)
                    temp_list2.sort()
                    if (temp_list2[0][0] + 1 == temp_list2[1][0]
                            and temp_list2[1][0] + 1 == temp_list2[2][0]):
                        temp_Sanshunzi.append(temp_list2)
                        if (item1[4][0] >= item2[4][0]):
                            temp_Sanshunzi.append(item2)
                            temp_Sanshunzi.append(item1)
                        else:
                            temp_Sanshunzi.append(item1)
                            temp_Sanshunzi.append(item2)
                        if temp_Sanshunzi not in Sanshunzi:
                            Sanshunzi.append(temp_Sanshunzi)
                            temp_Sanshunzi = []
    if (Sanshunzi != []):
        for item in Sanshunzi:  # item是一个三顺子
            flag = 1  # flag=0时表示这一个三顺子不是三同花顺
            for dun in item:  # dun是一个墩
                for i in range(len(dun) - 1):  # i是墩中的一张牌的下标
                    if (dun[i][1] != dun[i + 1][1]):
                        flag = 0
            if (flag == 1):
                SanTonghuashun.append(item)
    if (SanTonghuashun != []):
        return True
    else:
        return False


def IsSanfentianxia(Cardlist=[]):
    list_list = list.copy(Cardlist)
    list_count = GetList_count(list_list)
    count = 0
    for i in range(0, 13):
        if (list_count[i] == 4):
            count = count + 1
    if (count == 3):
        return True
    else:
        return False


def IsQuanda(Cardlist=[]):
    list_list = list.copy(Cardlist)
    count = 0
    for i in range(0, 13):
        if (list_list[i][0] >= 8):
            count = count + 1
    if (count == 13):
        return True
    else:
        return False


def IsQuanxiao(Cardlist=[]):
    list_list = list.copy(Cardlist)
    count = 0
    for i in range(0, 13):
        if (list_list[i][0] <= 8):
            count = count + 1
    if (count == 13):
        return True
    else:
        return False


def IsCouyise(Cardlist=[]):
    list_list = list.copy(Cardlist)
    Meihua = 0
    Fangkuai = 0
    for i in range(0, 13):
        if (list_list[i][1] == '*'):
            Meihua = Meihua + 1
        elif (list_list[i][1] == '#'):
            Fangkuai = Fangkuai + 1
    if (Meihua + Fangkuai == 13 or Meihua + Fangkuai == 0):
        return True
    else:
        return False


def IsShuangguaichongsan(Cardlist=[]):
    list_list = list.copy(Cardlist)
    list_count = GetList_count(list_list)
    count2 = 0
    count3 = 0
    count4 = 0
    for i in range(0, 13):
        if (list_count[i] == 2):
            count2 = count2 + 1
        elif (list_count[i] == 3):
            count3 = count3 + 1
        elif (list_count == 4):
            count4 = count4 + 1
    if (count2 == 3 and count3 == 2
            or count2 == 3 and count3 == 1 and count4 == 1
            or count2 == 2 and count3 == 3
            or count2 == 1 and count3 == 2 and count4 == 1):
        return True
    else:
        return False


def IsSitaosantiao(Cardlist=[]):
    list_list = list.copy(Cardlist)
    list_count = GetList_count(list_list)
    count = 0
    for i in range(0, 13):
        if (list_count[i] >= 3):
            count = count + 1
    if (count == 4):
        return True
    else:
        return False


def IsWuduisantiao(Cardlist=[]):
    list_list = list.copy(Cardlist)
    list_count = GetList_count(list_list)
    count2 = 0
    count3 = 0
    count4 = 0
    for i in range(0, 13):
        if (list_count[i] == 2):
            count2 = count2 + 1
        elif (list_count[i] == 3):
            count3 = count3 + 1
        elif (list_count[i] == 4):
            count4 = count4 + 1
    if (count2 == 5 and count3 == 1
            or count2 == 3 and count3 == 1 and count4 == 1
            or count2 == 1 and count3 == 1 and count4 == 2):
        return True
    else:
        return False


def IsLiuduiban(Cardlist=[]):
    list_list = list.copy(Cardlist)
    list_count = GetList_count(list_list)
    count = 0
    for i in range(0, 13):
        if (list_count[i] == 4):
            count = count + 2
        elif (list_count[i] == 3 or list_count[i] == 2):
            count = count + 1
    if (count == 6):
        return True
    else:
        return False


def IsSanshunzi(Cardlist=[]):
    temp_Sanshunzi = []  # 存放在查找过程中可能存在的三顺子的一部分
    list_list = list.copy(Cardlist)  # Cardlist的副本
    Sanshunzi=[]
    temp_list1 = []  # 存放去掉一个顺子后的手牌
    temp_list2 = []  # 存放去掉两个顺子后的手牌
    Shunzi1 = []  # 第一层循环中所有的顺子
    Shunzi2 = []  # 第二层循环中所有的顺子
    Shunzi1 = CommonCardsType.FindShunzi(list_list)
    if (Shunzi1 != []):
        for item1 in Shunzi1:
            temp_list1 = PlayCards.CalculateSub(list_list, item1)
            Shunzi2 = CommonCardsType.FindShunzi(temp_list1)
            if (Shunzi2 != []):
                for item2 in Shunzi2:
                    temp_list2 = PlayCards.CalculateSub(temp_list1, item2)
                    temp_list2.sort()
                    if (temp_list2[0][0] + 1 == temp_list2[1][0]
                            and temp_list2[1][0] + 1 == temp_list2[2][0]):
                        temp_Sanshunzi.append(temp_list2)
                        if (item1[4][0] >= item2[4][0]):
                            temp_Sanshunzi.append(item2)
                            temp_Sanshunzi.append(item1)
                        else:
                            temp_Sanshunzi.append(item1)
                            temp_Sanshunzi.append(item2)
                        if temp_Sanshunzi not in Sanshunzi:
                            Sanshunzi.append(temp_Sanshunzi)
                            temp_Sanshunzi = []
    if (Sanshunzi != []):
        return True
    else:
        return False


def IsSantonghua(Cardlist=[]):
    list_list = list.copy(Cardlist)
    Fangkuai = 0
    Meihua = 0
    Heitao = 0
    Hongxing = 0
    for i in range(0, 13):
        if (list_list[i][1] == '#'):
            Fangkuai = Fangkuai + 1
        elif (list_list[i][1] == '*'):
            Meihua = Meihua + 1
        elif (list_list[i][1] == '$'):
            Heitao = Heitao + 1
        else:
            Hongxing = Hongxing + 1
    templist = [Fangkuai, Meihua, Heitao, Hongxing]
    templist.sort()
    if (templist[0] == 0 and templist[1] == 3 and templist[2] == 5 and templist[3] == 5):
        return True
    else:
        return False


