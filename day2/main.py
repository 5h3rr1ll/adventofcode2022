#!/usr/bin/env python3
#-*- coding: utf-8 -*-


objects = {
    "A":{"name":"rock", "value": 1},
    "B":{"name":"paper", "value": 2},
    "C":{"name":"scissors", "value": 3},
    "X":{"name":"rock", "value": 1},
    "Y":{"name":"paper", "value": 2},
    "Z":{"name":"scissors", "value": 3}
} 


score = 0

def win_logic(a, b):
    object_value_a, object_value_b = objects[a]["value"], objects[b]["value"]
    if objects[a]["name"] == objects[b]["name"]:
        return 3
    elif objects[a]["name"] == "rock" and objects[b]["value"] == 2:
        return 6
    elif objects[a]["name"] == "paper" and objects[b]["value"] == 3:
        return 6
    elif objects[a]["name"] == "scissors" and objects[b]["value"] == 1:
        return 6
    else:
        return 0

def object_logic(objec_name):
    match objec_name:
        case "rock":
            return 1
        case "paper":
            return 2
        case "scissors":
            return 3


with open("f.txt", "r") as f:
    for line in f:
        a,b = line.split(" ")
        a,b = a.replace("\n", ""), b.replace("\n", "")
        print(objects[a]["name"], objects[b]["name"])
        win = win_logic(a,b)
        obj_value = object_logic(objects[b]["name"])
        score += win + obj_value
        # userinput = input(f"Your score is {score}. Press enter to continue")
    print(score)