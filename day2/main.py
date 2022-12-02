#!/usr/bin/env python3
#-*- coding: utf-8 -*-


objects = {
    "A":{"name":"rock", "value": 1, "X": "scissors", "Z": "paper", "Y": "rock"},
    "B":{"name":"paper", "value": 2, "X": "rock", "Z": "scissors", "Y": "paper"},
    "C":{"name":"scissors", "value": 3, "X": "paper", "Z": "rock", "Y": "scissors"},
    "X":{"name":"rock", "value": 1, "X": "scissors", "Z": "paper", "Y": "rock"},
    "Y":{"name":"paper", "value": 2, "X": "rock", "Z": "scissors", "Y": "paper"},
    "Z":{"name":"scissors", "value": 3, "X": "paper", "Z": "rock", "Y": "scissors"}
} 

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
        
def win_lose_pat(xyz):
    match xyz:
        case "X":
            return 0
        case "Y":
            return 3
        case "Z":
            return 6

def choose_the_right_object(object, instruction):
    return object_logic(objects[object][instruction])

def part1():
    score = 0
    with open("f.txt", "r") as f:
        for line in f:
            a,b = line.split(" ")
            a,b = a.replace("\n", ""), b.replace("\n", "")
            win = win_logic(a,b)
            obj_value = object_logic(objects[b]["name"])
            score += win + obj_value
            # userinput = input(f"Your score is {score}. Press enter to continue")
        print(score)

def part2():
    score = 0
    with open("f.txt", "r") as f:
        for line in f:
            a,b = line.split(" ")
            a,b = a.replace("\n", ""), b.replace("\n", "")
            instructions = win_lose_pat(b)
            obj_value = choose_the_right_object(a, b)
            score += instructions + obj_value
            # userinput = input(f"Your score is {score}. Press enter to continue")
        print(score)

part1()
part2()