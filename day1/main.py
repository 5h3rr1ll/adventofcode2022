#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open("f.txt", "r") as f:
    list1 = []
    list2 = []
    for line in f:
        if line != "\n":
            list2.append(int(line.replace("\n", "")))
        else:
            list1.append(list2)
            list2 = []
    
    list3 = []
    for list in list1:
        list3.append(sum(list))
        
    # print("Max is: ", max(list3))
    
    # print(list3)
    
    three_most = []
    
    while len(three_most) < 3:
        three_most.append(max(list3))
        list3.remove(max(list3))
        
    print(sum(three_most))