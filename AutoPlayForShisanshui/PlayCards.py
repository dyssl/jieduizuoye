#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import SpecialCardsType
import CommonCardsType
import flask

server = flask.Flask(__name__)  # __name__代表当前的python文件。把当前的python文件当做一个服务启动

Sanpai_Weight_1 = [0, 0, 0, 0, 0, 289, 1158, 2895, 5791, 10135, 16217, 24325, 34751, 47782, 63710]
# 散牌出现在前墩时各种牌面的权值，按最大牌算权值，前墩最小权值对应的牌为5
Sanpai_Weight_2 = [0, 0, 0, 0, 0, 0, 0, 0, 156, 706, 2040, 4748, 9654, 17857, 30769]
# 散牌出现在中墩是各种牌面的权值，按最大牌算权值，中墩最小权值对应的牌为7
# 不可能出现后墩是散牌的情况

Duizi_Weight_1 = [0, 0, 82823, 84126, 85429, 86733, 88036, 89339, 90642, 91945, 93248, 94552, 95855, 97158, 98461]
# 对子出现在前墩时各种牌面的权值，按对子牌面算权值
Duizi_Weight_2 = [0, 0, 50156, 53407, 56658, 59908, 63159, 66409, 69660, 72910, 76161, 79411, 82662, 85912, 89163]
# 对子出现在中墩时各种牌面的权值，按对子牌面算权值
Duizi_Weight_3 = [0, 0, 0, 6521, 13043, 19564, 26086, 32607, 39129, 45650, 52172, 58693, 65215, 71736, 78258]
# 对子出现在后墩时各种牌面的权值，按对子牌面算权值

Erdui_Weight_2 = [0, 0, 0, 0, 92413, 92474, 92596, 92779, 93023, 93328, 93693, 94120, 94607, 95156, 95765]
# 二对出现在中墩时各种牌面的权值，按对子牌面算权值
Erdui_Weight_3 = [0, 0, 0, 0, 84779, 84902, 85146, 85513, 86002, 86614, 87347, 88203, 89182, 90282, 91505]
# 二对出现在后墩时各种牌面的权值，按对子牌面算权值

Liandui_Weight_2 = [0, 0, 0, 96436, 96497, 96558, 96619, 96680, 96741, 96802, 96863, 96924, 96984, 97045, 97106]
# 连对出现在中墩时各种牌面的权值，按对子牌面算权值
Liandui_Weight_3 = [0, 0, 0, 92850, 92972, 93094, 93217, 93339, 93461, 93584, 93706, 93828, 93950, 94073, 94195]
# 连对出现在后墩时各种牌面的权值，按对子牌面算权值

Santiao_Weight_1 = [0, 0, 99764, 99782, 99800, 99819, 99837, 99855, 99873, 99891, 99909, 99927, 99945, 99963, 99981]
# 三条出现在前墩时各种牌面的权值，按三条牌面算权值
Santiao_Weight_2 = [0, 0, 97167, 97330, 97492, 97655, 97817, 97980, 98142, 98305, 98468, 98630, 98793, 98955, 99118]
# 三条出现在中墩时各种牌面的权值，按三条牌面算权值
Santiao_Weight_3 = [0, 0, 94317, 94643, 94969, 95295, 95622, 95948, 96274, 96600, 96926, 97252, 97578, 97904, 98230]
# 三条出现在后墩时各种牌面的权值，按三条牌面算权值

Shunzi_Weight_2 = [0, 0, 0, 0, 0, 0, 99280, 99319, 99359, 99398, 99437, 99476, 99516, 99555, 99594]
# 顺子出现在中墩时各种牌面的权值，按最大牌面算权值
Shunzi_Weight_3 = [0, 0, 0, 0, 0, 0, 98556, 98635, 98714, 98792, 98871, 98950, 99029, 99107, 99186]
# 顺子出现在后墩时各种牌面的权值，按最大牌面算权值

Tonghua_Weight_2 = [0, 0, 0, 0, 0, 0, 0, 99633, 99634, 99636, 99641, 99652, 99671, 99703, 99754]
# 同花出现在中墩时各种牌面的权值，按最大牌面算权值
Tonghua_Weight_3 = [0, 0, 0, 0, 0, 0, 0, 99265, 99266, 99270, 99281, 99302, 99341, 99405, 99507]
# 同花出现在后墩时各种牌面的权值，按最大牌面算权值

Hulu_Weight_2 = [0, 0, 99830, 99841, 99852, 99863, 99874, 99885, 99897, 99908, 99919, 99930, 99941, 99952, 99963]
# 葫芦出现在中墩时各种牌面的权值，按其中三条的值算权值
Hulu_Weight_3 = [0, 0, 99660, 99682, 99704, 99726, 99748, 99771, 99793, 99815, 99837, 99860, 99882, 99904, 99926]
# 葫芦出现在后墩时各种牌面的权值，按其中三条的值算权值

Zhadan_Weight_2 = [0, 0, 99974, 99976, 99978, 99980, 99981, 99983, 99985, 99987, 99989, 99991, 99993, 99994, 99996]
# 炸弹出现在后墩时各种牌面的权值，按炸弹的大小算权值
Zhadan_Weight_3 = [0, 0, 99949, 99952, 99956, 99960, 99963, 99967, 99971, 99974, 99978, 99982, 99986, 99989, 99993]
# 炸弹出现在后墩时各种牌面的权值，按炸弹的大小算权值

Tonghuashun_Weight_2 = [0, 0, 0, 0, 0, 0, 99998, 99998, 99998, 99999, 99999, 99999, 99999, 99999, 99999]
# 同花顺出现在中墩时各种牌面的权值，按最大牌的大小算权值
Tonghuashun_Weight_3 = [0, 0, 0, 0, 0, 0, 99997, 99997, 99997, 99998, 99998, 99998, 99999, 99999, 99999]


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
@server.route('/PostCards', methods=['post'])  # 第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
def PostCards(str_data):
    Cardlist = GetCardlist(str_data)
    temp_Cardlist = list.copy(Cardlist)
    '''
    # 以下是判断是否出现特殊牌型，如果是，直接返回原列表
    if (SpecialCardsType.IsZhizhunqinglong(temp_Cardlist)):
        print("至尊清龙")
        return temp_Cardlist
    elif (SpecialCardsType.IsYitiaolong(temp_Cardlist)):
        print("一条龙")
        return temp_Cardlist
    elif (SpecialCardsType.IsShierhuangzu(temp_Cardlist)):
        print("十二皇族")
        return temp_Cardlist
    elif (SpecialCardsType.IsSantonghuashun(temp_Cardlist)):
        print("三同花顺")
        return temp_Cardlist
    elif (SpecialCardsType.IsSanfentianxia(temp_Cardlist)):
        print("三分天下")
        return temp_Cardlist
    elif (SpecialCardsType.IsQuanda(temp_Cardlist)):
        print("全大")
        return temp_Cardlist
    elif (SpecialCardsType.IsQuanxiao(temp_Cardlist)):
        print("全小")
        return temp_Cardlist
    elif (SpecialCardsType.IsCouyise(temp_Cardlist)):
        print("凑一色")
        return temp_Cardlist
    elif (SpecialCardsType.IsShuangguaichongsan(temp_Cardlist)):
        print("双怪冲三")
        return temp_Cardlist
    elif (SpecialCardsType.IsSitaosantiao(temp_Cardlist)):
        print("四套三条")
        return temp_Cardlist
    elif (SpecialCardsType.IsWuduisantiao(temp_Cardlist)):
        print("五对三条")
        return temp_Cardlist
    elif (SpecialCardsType.IsLiuduiban(temp_Cardlist)):
        print("六对半")
        return temp_Cardlist
    elif (SpecialCardsType.IsSanshunzi(temp_Cardlist)):
        print("三顺子")
        return temp_Cardlist
    elif (SpecialCardsType.IsSantonghua(temp_Cardlist)):
        print("三同花")
        return temp_Cardlist'''
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


