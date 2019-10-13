#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
import PlayCards


def testForIllegalDunpai():
    count = 0
    error1 = 0
    error2 = 0
    while (True):

        list = [x for x in range(52)]

        cards = ["*A", "$A", "&A", "#A",
                 "*2", "$2", "&2", "#2",
                 "*3", "$3", "&3", "#3",
                 "*4", "$4", "&4", "#4",
                 "*5", "$5", "&5", "#5",
                 "*6", "$6", "&6", "#6",
                 "*7", "$7", "&7", "#7",
                 "*8", "$8", "&8", "#8",
                 "*9", "$9", "&9", "#9",
                 "*10", "$10", "&10", "#10",
                 "*J", "$J", "&J", "#J",
                 "*Q", "$Q", "&Q", "#Q",
                 "*K", "$K", "&K", "#K", ]
        numbers = random.sample(list, 13)
        str_data = ""
        for i in numbers:
            str_data = str_data + cards[i] + " "
        str_data = str_data[0:len(str_data) - 1]
        print(str_data)
        output = PlayCards.PostCards(str_data)
        print(output)
        count = count + 1
        if (len(output) != 3 and len(output) != 13):
            error1 = error1 + 1
        if (len(output[0]) != 3 or len(output[1]) != 5 or len(output[2]) != 5):
            if (len(output) != 13):
                error2 = error2 + 1
        print(count)
        print(error1)
        print(error2)


def testForChuqian():
    count = 0
    error = 0
    while (True):
        list = [x for x in range(52)]

        cards = ["*A", "$A", "&A", "#A",
                 "*2", "$2", "&2", "#2",
                 "*3", "$3", "&3", "#3",
                 "*4", "$4", "&4", "#4",
                 "*5", "$5", "&5", "#5",
                 "*6", "$6", "&6", "#6",
                 "*7", "$7", "&7", "#7",
                 "*8", "$8", "&8", "#8",
                 "*9", "$9", "&9", "#9",
                 "*10", "$10", "&10", "#10",
                 "*J", "$J", "&J", "#J",
                 "*Q", "$Q", "&Q", "#Q",
                 "*K", "$K", "&K", "#K", ]
        numbers = random.sample(list, 13)
        str_data = ""
        for i in numbers:
            str_data = str_data + cards[i] + " "
        str_data = str_data[0:len(str_data) - 1]
        originalcards = PlayCards.GetCardlist(str_data)
        print(str_data)
        output = PlayCards.PostCards(str_data)
        temp_output = []
        for item in output:
            if (len(output) != 13):
                temp_output = temp_output + item
            else:
                temp_output.append(item)
        temp_output.sort()
        originalcards.sort()
        if (temp_output != originalcards):
            error = error + 1
        print(output)
        count = count + 1
        print(count)
        print(error)
testForIllegalDunpai()
