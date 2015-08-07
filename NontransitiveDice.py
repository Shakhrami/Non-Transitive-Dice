#?/usr/bin/env python

# I've always wanted a pair of Non-transitive Dice.
# This version is inspired by Dr. James Grime from the University of Cambridge.

#Version 1.11 : Multiple rolls with simple summary of who won.
import random

def player1_die_pick(die):
    p1Die =""
    valid1 = False
    while not valid1:
        p1Die = raw_input("Player 1, pick your die:")
        if(p1Die in die):
            p1Die = die[p1Die]
            valid1 = True
            print "P1's die: ", p1Die
        else:
            print "invalid"
    return p1Die

def player2_die_pick(die, p1Choice):
    p2Die = ""
    valid2 = False
    while not valid2:
        p2Die = raw_input("Player 2, pick your die:")
        if(p2Die in die):
            p2DieTest = die[p2Die]
            if(p2DieTest == p1Choice):
                print "die already selected."
            else:
                p2Die = p2DieTest
                valid2 = True
                print "P2's die: ", p2Die
        else:
            print "invalid"
    return p2Die

def get_rolls():
    # Still need to correct for 0 number of rolls.
    validInt = False
    while not validInt:
        numOfRolls = raw_input("Enter a positive number of rolls (Int):")
        if(numOfRolls.isdigit() > 0):
            validInt = True
    return int(numOfRolls)

def players_rolls(die, number):
    rolls = []
    for i in range(0, number):
        rolls.append(random.choice(die))
    return rolls

def compair_rolls(p1, p2):
    p1Wins = 0
    p2Wins = 0
    for i in range(0, len(p1)):
        if (p1[i] > p2[i]):
            p1Wins += 1
        else:
            p2Wins += 1
    p1Mu = p1Wins / float(len(p1))
    p2Mu = p2Wins / float(len(p1))   
    if(p1Wins > p2Wins):
        print "Player one won the most rolls:", p1Mu * 100, "% victory rate."
    else:
        print "Player two won the most rolls:", p2Mu * 100, "% victory rate."
    
    
die = {"Red" : [4,4,4,4,4,9],
       "Yellow" : [3,3,3,3,8,8],
       "Blue" : [2,2,2,7,7,7],
       "Magenta" : [1,1,6,6,6,6],
       "Olive" : [0,5,5,5,5,5]}

for dice in die:
    print dice,":" ,die[dice]
print "-------------------------------------------------"       

p1Die = player1_die_pick(die)
p2Die = player2_die_pick(die, p1Die)

"""
Roll multiple times.
"""
numOfRolls = get_rolls()

p1Roll = players_rolls(p1Die, numOfRolls)
p2Roll = players_rolls(p2Die, numOfRolls)

print "P1's roll:", p1Roll
print "P2's roll:", p2Roll

compair_rolls(p1Roll, p2Roll)