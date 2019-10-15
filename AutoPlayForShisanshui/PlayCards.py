#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import SpecialCardsType
import CommonCardsType
import flask

Sanpai_Weight_1 = [0, 0, 0, 0, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
# 散牌出现在前墩时各种牌面的权值，按最大牌算权值，前墩最小权值对应的牌为5
Sanpai_Weight_2 = [0, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]
# 散牌出现在中墩是各种牌面的权值，按最大牌算权值，中墩最小权值对应的牌为7
# 不可能出现后墩是散牌的情况

Duizi_Weight_1 = [0, 0, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400]
# 对子出现在前墩时各种牌面的权值，按对子牌面算权值
Duizi_Weight_2 = [0, 0, 1400, 2023, 2646, 3269, 3892, 4515, 5138, 5761, 6384, 7007, 7630, 8253, 8876]
# 对子出现在中墩时各种牌面的权值，按对子牌面算权值
Duizi_Weight_3 = [0, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]
# 对子出现在后墩时各种牌面的权值，按对子牌面算权值

Erdui_Weight_2 = [0, 0, 0, 0, 10000, 10723, 12169, 14338, 17230, 20846, 25184, 30245, 36030, 42538, 49768]
# 二对出现在中墩时各种牌面的权值，按对子牌面算权值
Erdui_Weight_3 = [0, 0, 0, 0, 1000, 1795, 3386, 5772, 8953, 12930, 17702, 23270, 29633, 36791, 44745]
# 二对出现在后墩时各种牌面的权值，按对子牌面算权值

Liandui_Weight_2 = [0, 0, 0, 57722, 58445, 59168, 59891, 60614, 61337, 62060, 62783, 63506, 64230, 64953, 65676]
# 连对出现在中墩时各种牌面的权值，按对子牌面算权值
Liandui_Weight_3 = [0, 0, 0, 53494, 54290, 55085, 55880, 56676, 57471, 58266, 59062, 59857, 60653, 61448, 62243]
# 连对出现在后墩时各种牌面的权值，按对子牌面算权值

Santiao_Weight_1 = [0, 0, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000]
# 三条出现在前墩时各种牌面的权值，按三条牌面算权值
Santiao_Weight_2 = [0, 0, 66399, 68327, 70255, 72183, 74111, 76040, 77968, 79896, 81824, 83752, 85681, 87609, 89537]
# 三条出现在中墩时各种牌面的权值，按三条牌面算权值
Santiao_Weight_3 = [0, 0, 63039, 65160, 67281, 69402, 71523, 73644, 75765, 77886, 80007, 82128, 84249, 86370, 88491]
# 三条出现在后墩时各种牌面的权值，按三条牌面算权值

Shunzi_Weight_2 = [0, 0, 0, 0, 0, 0, 91465, 91931, 92396, 92862, 93328, 93793, 94259, 94724, 95190]
# 顺子出现在中墩时各种牌面的权值，按最大牌面算权值
Shunzi_Weight_3 = [0, 0, 0, 0, 0, 0, 90612, 91124, 91636, 92148, 92660, 93173, 93685, 94197, 94709]
# 顺子出现在后墩时各种牌面的权值，按最大牌面算权值

Tonghua_Weight_2 = [0, 0, 0, 0, 0, 0, 0, 95656, 95663, 95688, 95751, 95877, 96105, 96486, 97087]
# 同花出现在中墩时各种牌面的权值，按最大牌面算权值
Tonghua_Weight_3 = [0, 0, 0, 0, 0, 0, 0, 95221, 95229, 95257, 95326, 95464, 95715, 96135, 96796]
# 同花出现在后墩时各种牌面的权值，按最大牌面算权值

Hulu_Weight_2 = [0, 0, 97989*2, 98121*2, 98252*2, 98384*2, 98515*2, 98646*2, 98778*2, 98909*2, 99041*2, 99172*2, 99304*2, 99435*2, 99567*2]
# 葫芦出现在中墩时各种牌面的权值，按其中三条的值算权值
Hulu_Weight_3 = [0, 0, 97788, 97933, 98077, 98222, 98367, 98511, 98656, 98800, 98945, 99090, 99234, 99379, 99523]
# 葫芦出现在后墩时各种牌面的权值，按其中三条的值算权值

Zhadan_Weight_2 = [0, 0, 99698*8, 99720*8, 99742*8, 99764*8, 99786*8, 99808*8, 99830*8, 99852*8, 99874*8, 99895*8, 99917*8, 99939*8, 99961*8]
# 炸弹出现在后墩时各种牌面的权值，按炸弹的大小算权值
Zhadan_Weight_3 = [0, 0, 99668*4, 99692*4, 99716*4, 99740*4, 99765*4, 99789*4, 99813*4, 99837*4, 99861*4, 99885*4, 99909*4, 99933*4, 99957*4]
# 炸弹出现在后墩时各种牌面的权值，按炸弹的大小算权值

Tonghuashun_Weight_2 = [0, 0, 0, 0, 0, 0, 99983*10, 99985*10, 99987*10, 99989*10, 99990*10, 99992*10, 99994*10, 99996*10, 99998*10]
# 同花顺出现在中墩时各种牌面的权值，按最大牌的大小算权值
Tonghuashun_Weight_3 = [0, 0, 0, 0, 0, 0, 99981*5, 99983*5, 99985*5, 99987*5, 99989*5, 99991*5, 99993*5, 99995*5, 99997*5]


# 同花顺出现在后墩时各种牌面的权值，按最大牌的大小算权值


# 获取后墩牌的权值
def GetWeight_Houdun(Cardlist=[]):
    flag = 0  # flag用来标记是哪种牌型
    weight = 0  # 权值
    flag = Judge(Cardlist)
    if (flag == 9):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Tonghuashun_Weight_3[number]
    elif (flag == 8):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Zhadan_Weight_3[number]
    elif (flag == 7):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Hulu_Weight_3[number]
    elif (flag == 6):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Tonghua_Weight_3[number]
    elif (flag == 5):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Shunzi_Weight_3[number]
    elif (flag == 4):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Santiao_Weight_3[number]
    elif (flag == 3):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Liandui_Weight_3[number]
    elif (flag == 2):
        Cardlist.sort()
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Erdui_Weight_3[number]
    elif (flag == 1):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Duizi_Weight_3[number]
    else:
        print(Cardlist)
        print("error in GetWeight_Houdun")
    return weight


# 获取中墩牌的权值
def GetWeight_Zhongdun(Cardlist=[]):
    flag = 0  # flag用来标记是哪种牌型
    weight = 0  # 权值
    flag = Judge(Cardlist)
    if (flag == 9):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Tonghuashun_Weight_2[number]
    elif (flag == 8):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Zhadan_Weight_2[number]
    elif (flag == 7):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Hulu_Weight_2[number]
    elif (flag == 6):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Tonghua_Weight_2[number]
    elif (flag == 5):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Shunzi_Weight_2[number]
    elif (flag == 4):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Santiao_Weight_2[number]
    elif (flag == 3):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Liandui_Weight_2[number]
    elif (flag == 2):
        Cardlist.sort()
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Erdui_Weight_2[number]
        # if (Cardlist[0][0] + 1 == Cardlist[2][0]):
        # weight = weight + 13 #连对情况
    elif (flag == 1):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Duizi_Weight_2[number]
    elif (flag == 0):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Sanpai_Weight_2[number]
    else:
        print("error in GetWeight_Zhongdun")
    return weight


def Getweight_Qiandun(Cardlist=[]):
    weight = 0  # 权值
    if (len(Cardlist) == 1):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Sanpai_Weight_1[number]
    elif (len(Cardlist) == 2):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Duizi_Weight_1[number]
    elif (len(Cardlist) == 3):
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        weight = Santiao_Weight_1[number]
    else:
        print("error in GetWeight_Qiandun")
    return weight


# 这个函数用于列表的差集运算，返回Cardlist1-Cardlist2,要求Cardlist2是Cardlist1的子集
def CalculateSub(Cardlist1=[], Cardlist2=[]):
    chaji = list.copy(Cardlist1)  # 最后要返回的差集
    for item in Cardlist2:
        if (item in Cardlist1):
            chaji.remove(item)
        else:
            print(item)
            print("error in fun CalculateSub")
    return chaji


# 用到这个函数的时候，有两种按情况，一是单纯的要找到最大的牌，二是剩下的牌是散牌，要找到最大的牌赋权值
# 传入的参数格式应如下 Cardslist=[[2, '*'], [2, '*'], [3, '#'], [3, '#'].......]
def FindBiggestCard(Cardslist=[]):
    Cardslist.sort()
    lenth = len(Cardslist)
    temp_card = Cardslist[lenth - 1]
    return temp_card


def GetCardlist(str_data):
    list_list = []  # 每张牌以list的形式存储在这个list中，例如梅花三被存储为[3，'*']
    # 将原始数据即str_data中所有的牌提取出来以字符串形式存储在这个列表中，例如['*2','$6',......]
    list_str = str_data.split(' ')

    for item in list_str:
        symbol = item[0]
        number = item[1:]
        if number == 'J':
            number = '11'
        elif number == 'Q':
            number = '12'
        elif number == 'K':
            number = '13'
        elif number == 'A':
            number = '14'

        number = int(number)
        list_temp = [number, symbol]
        list_list.append(list_temp)
    list_list.sort()
    return list_list


def FindAllCardsCombination(Cardlist=[]):
    temp_Cardlist = list.copy(Cardlist)
    AllCardsCombination = []
    temp_list = CommonCardsType.FindTonghuashun(temp_Cardlist)
    if (temp_list != []):
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = CommonCardsType.FindZhadan(temp_Cardlist)
    if (temp_list != []):
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = CommonCardsType.FindHulu(temp_Cardlist)
    if (temp_list != []):
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = CommonCardsType.FindTonghua(temp_Cardlist)
    if (temp_list != []):
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = CommonCardsType.FindShunzi(temp_Cardlist)
    if (temp_list != []):
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = CommonCardsType.FindSantiao(temp_Cardlist)
    if (temp_list != []):
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = CommonCardsType.FindLiandui(temp_Cardlist)
    if (temp_list != []):
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = CommonCardsType.FindErdui(temp_Cardlist)
    if (temp_list != []):
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = CommonCardsType.FindDuizi(temp_Cardlist)
    if (temp_list != []):
        for item in temp_list:
            AllCardsCombination.append(item)
    return AllCardsCombination


def Judge(Cardlist=[]):
    temp_Cardlist = list.copy(Cardlist)
    if (CommonCardsType.FindTonghuashun(temp_Cardlist) != []):
        return 9
    elif (CommonCardsType.FindZhadan(temp_Cardlist) != []):
        return 8
    elif (CommonCardsType.FindHulu(temp_Cardlist) != []):
        return 7
    elif (CommonCardsType.FindTonghua(temp_Cardlist) != []):
        return 6
    elif (CommonCardsType.FindShunzi(temp_Cardlist) != []):
        return 5
    elif (CommonCardsType.FindSantiao(temp_Cardlist) != []):
        return 4
    elif (CommonCardsType.FindLiandui(temp_Cardlist) != []):
        return 3
    elif (CommonCardsType.FindErdui(temp_Cardlist) != []):
        return 2
    elif (CommonCardsType.FindDuizi(temp_Cardlist) != []):
        return 1
    else:
        return 0


def Compare(Cardlist1=[], Cardlist2=[]):
    flag1 = Judge(Cardlist1)
    flag2 = Judge(Cardlist2)
    list_count1 = CommonCardsType.GetList_count(Cardlist1)
    list_count2 = CommonCardsType.GetList_count(Cardlist2)
    bigCard1 = -1
    bigCard2 = -2
    if (flag2 > flag1):
        return True
    elif (flag1 == flag2):
        if (flag1 == flag2 == 7):
            for i in range(15):
                if (list_count1[i] == 3):
                    bigCard1 = i
                if (list_count2[i] == 3):
                    bigCard2 = i
            if (bigCard2 >= bigCard1):
                return True
            else:
                return False
        else:
            bigCard1 = FindBiggestCard(Cardlist1)
            bigCard2 = FindBiggestCard(Cardlist2)
            if (bigCard2 >= bigCard1):
                return True
            else:
                return False
    else:
        return False


# 发牌函数，根据权值最大原则给出三墩牌，形式为[[前墩]，[中墩]，[后墩]]
# 如果是特殊牌型，直接将接收的列表返回
def PostCards(str_data):
    Cardlist = GetCardlist(str_data)
    temp_Cardlist = list.copy(Cardlist)
    # 接下来开始按权值最大原则墩牌
    Weight_All = 0  # 某一种出牌方式的权值
    Post_Cards = []  # 最后返回的列表
    Weight_Qiandun = 0  # 前墩的权值
    Weight_Zhongdun = 0  # 中墩的权值
    Weight_Houdun = 0  # 后墩的权值
    Cards_Qiandun = []  # 前墩的牌
    Cards_Zhongdun = []  # 中墩的牌
    Cards_Houdun = []  # 后墩的牌
    AllCardsCombination_AfterTakeHoudun = []  # 拿出后墩牌后剩下的牌所有对子以上的牌型
    AllCardsCombination_AfterTakeZhongdun = []  # 拿出中墩牌后剩下的牌所有对子、三条的列表
    Cardlist_AfterTakeHoudun = []  # 拿出后墩后剩下的牌
    Cardlist_AfterTakeZhongdun = []  # 拿出中墩、后墩后剩下的牌
    Cardlist_AfterTakeQiandun = []  # 拿出中墩、后墩、前墩后剩下的牌，因为拿出的中墩、后墩、前墩不是完整的
    AllCardsCombination_FromAllcards = []  # 13张牌中所有对子及以上的牌型
    AllCardsCombination_FromAllcards = FindAllCardsCombination(temp_Cardlist)
    for item1 in AllCardsCombination_FromAllcards:  # 先拿出后墩
        Cardlist_AfterTakeHoudun = CalculateSub(temp_Cardlist, item1)
        AllCardsCombination_AfterTakeHoudun = FindAllCardsCombination(Cardlist_AfterTakeHoudun)
        if (AllCardsCombination_AfterTakeHoudun != []):
            for item2 in AllCardsCombination_AfterTakeHoudun:
                Cardlist_AfterTakeZhongdun = CalculateSub(Cardlist_AfterTakeHoudun, item2)
                AllCardsCombination_AfterTakeZhongdun = CommonCardsType.FindDuizi(
                    Cardlist_AfterTakeZhongdun) + CommonCardsType.FindSantiao(Cardlist_AfterTakeZhongdun)
                if (AllCardsCombination_AfterTakeZhongdun != []):
                    for item3 in AllCardsCombination_AfterTakeZhongdun:
                        Cardlist_AfterTakeQiandun = CalculateSub(Cardlist_AfterTakeZhongdun, item3)
                        Cards_Qiandun = list.copy(item3)
                        Cards_Zhongdun = list.copy(item2)
                        Cards_Houdun = list.copy(item1)
                        Weight_Qiandun = Getweight_Qiandun(Cards_Qiandun)
                        Weight_Zhongdun = GetWeight_Zhongdun(Cards_Zhongdun)
                        Weight_Houdun = GetWeight_Houdun(Cards_Houdun)
                        if (Weight_Qiandun + Weight_Zhongdun + Weight_Houdun > Weight_All
                                and Compare(Cards_Qiandun, Cards_Zhongdun) and Compare(Cards_Zhongdun, Cards_Houdun)):
                            Weight_All = Weight_Qiandun + Weight_Zhongdun + Weight_Houdun
                            if (Cardlist_AfterTakeQiandun != []):
                                for card in Cardlist_AfterTakeQiandun:
                                    if (len(Cards_Qiandun) < 3):
                                        Cards_Qiandun.append(card)
                                    elif (len(Cards_Zhongdun) < 5):
                                        Cards_Zhongdun.append(card)
                                    else:
                                        Cards_Houdun.append(card)
                            Post_Cards = []
                            Post_Cards.append(Cards_Qiandun)
                            Post_Cards.append(Cards_Zhongdun)
                            Post_Cards.append(Cards_Houdun)
                        Cards_Qiandun = []
                        Cards_Zhongdun = []
                        Cards_Houdun = []
                else:
                    Cards_Qiandun.append(FindBiggestCard(Cardlist_AfterTakeZhongdun))
                    Cardlist_AfterTakeQiandun = CalculateSub(Cardlist_AfterTakeZhongdun, Cards_Qiandun)
                    Cards_Houdun = list.copy(item1)
                    Cards_Zhongdun = list.copy(item2)
                    Weight_Houdun = GetWeight_Houdun(Cards_Houdun)
                    Weight_Zhongdun = GetWeight_Zhongdun(Cards_Zhongdun)
                    Weight_Qiandun = Getweight_Qiandun(Cards_Qiandun)
                    if (Weight_Qiandun + Weight_Zhongdun + Weight_Houdun > Weight_All
                            and Compare(Cards_Qiandun, Cards_Zhongdun) and Compare(Cards_Zhongdun, Cards_Houdun)):
                        Weight_All = Weight_Qiandun + Weight_Zhongdun + Weight_Houdun
                        if (Cardlist_AfterTakeQiandun != []):
                            for card in Cardlist_AfterTakeQiandun:
                                if (len(Cards_Qiandun) < 3):
                                    Cards_Qiandun.append(card)
                                elif (len(Cards_Zhongdun) < 5):
                                    Cards_Zhongdun.append(card)
                                else:
                                    Cards_Houdun.append(card)
                        Post_Cards = []
                        Post_Cards.append(Cards_Qiandun)
                        Post_Cards.append(Cards_Zhongdun)
                        Post_Cards.append(Cards_Houdun)
                    Cards_Qiandun = []
                    Cards_Zhongdun = []
                    Cards_Houdun = []

        else:
            Cards_Zhongdun.append(FindBiggestCard(Cardlist_AfterTakeHoudun))
            Weight_Zhongdun = GetWeight_Zhongdun(Cards_Zhongdun)
            Cardlist_AfterTakeZhongdun = CalculateSub(Cardlist_AfterTakeHoudun, Cards_Zhongdun)
            Cards_Qiandun.append(FindBiggestCard(Cardlist_AfterTakeZhongdun))
            Weight_Qiandun = Getweight_Qiandun(Cards_Qiandun)
            Cardlist_AfterTakeQiandun = CalculateSub(Cardlist_AfterTakeZhongdun, Cards_Qiandun)
            Cards_Houdun = list.copy(item1)
            Weight_Houdun = GetWeight_Houdun(Cards_Houdun)
            if (Weight_Qiandun + Weight_Zhongdun + Weight_Houdun > Weight_All
                    and Compare(Cards_Qiandun, Cards_Zhongdun) and Compare(Cards_Zhongdun, Cards_Houdun)):
                Weight_All = Weight_Qiandun + Weight_Zhongdun + Weight_Houdun
                if (Cardlist_AfterTakeQiandun != []):
                    for card in Cardlist_AfterTakeQiandun:
                        if (len(Cards_Qiandun) < 3):
                            Cards_Qiandun.append(card)
                        elif (len(Cards_Zhongdun) < 5):
                            Cards_Zhongdun.append(card)
                        else:
                            Cards_Houdun.append(card)
                Post_Cards = []
                Post_Cards.append(Cards_Qiandun)
                Post_Cards.append(Cards_Zhongdun)
                Post_Cards.append(Cards_Houdun)
            Cards_Qiandun = []
            Cards_Zhongdun = []
    return Post_Cards


if __name__ == '__main__':
    card = PostCards("$10 &J $2 $6 &8 &3 *K $A #J #3 $Q &9 #A")
    print(card)
    print(Tonghuashun_Weight_2)