#?/usr/bin/env python

# I've always wanted a pair of Non-transitive Dice.
# This version is inspired by Dr. James Grime from the University of Cambridge.

#Version 2.1 : Multiple die per player.

#One die guide:
#winning chain 1: Alphabetical: Blue>Magenta>Olive>Red>Yellow>Blue
#winning chain 2: Word-length : Red>Blue>Olive>Yellow>Magenta>Red

#Two die guide:
#winning chain 1: Alphabetical R-O switch: Blue>Magenta>Red>Olive>Yellow>Blue
#winning chain 2: Reverse word-length:     Magenta>Yellow>Olive>Blue>Red>Magenta
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
    elif(p1Wins < p2Wins):
        print "Player two won the most rolls:", p2Mu * 100, "% victory rate."
    else:
        print "Tie game!"

def two_die_rolls(die, numOfRolls):
    rollSum = []
    for i in range(0, numOfRolls):
        roll1 = random.choice(die)
        roll2 = random.choice(die)
        rollSum.append(roll1 + roll2)
    return rollSum
    
def game_start(die):
    for dice in die:
        print dice,":" ,die[dice]
    print "-------------------------------------------------"
    numOfDie =  raw_input("1 or 2 die per player?")
    while True:
        if(numOfDie == "1.0" or numOfDie == "2.0" or
           numOfDie == "1" or numOfDie == "2"):
            numOfDie = int(numOfDie)
            break
        else:
            print "Invalid number of die."
            numOfDie =  raw_input("1 or 2 die per player?")
    if(numOfDie == 1):
        p1Die = player1_die_pick(die)
        p2Die = player2_die_pick(die, p1Die)
        numOfRolls = get_rolls()
        p1Roll = players_rolls(p1Die, numOfRolls)
        p2Roll = players_rolls(p2Die, numOfRolls)
        print "P1's roll:", p1Roll
        print "P2's roll:", p2Roll
        compair_rolls(p1Roll, p2Roll)
    else:
        p1Die1 = player1_die_pick(die)
        p2Die1 = player2_die_pick(die, p1Die1)
        numOfRolls = get_rolls()
        p1Rolls = two_die_rolls(p1Die1, numOfRolls)
        p2Rolls = two_die_rolls(p2Die1, numOfRolls)
        print "P1 roll sums:", p1Rolls
        print "P2 roll sums:", p2Rolls
        compair_rolls(p1Rolls, p2Rolls)

def replay(die):
    replay = raw_input("Want to play again?")
    while True:
        if(replay == "Y" or replay == "y" or replay == "Yes" or replay == "yes"):
            replay = ""
            game_start(die)
        elif(replay == "N" or replay == "n" or replay == "No" or replay == "no"):
            print "Thanks for playing!"
            break
        else:
            replay = raw_input("Want to play again?")
    
    
   
die = {"Red" : [4,4,4,4,4,9],
       "Yellow" : [3,3,3,3,8,8],
       "Blue" : [2,2,2,7,7,7],
       "Magenta" : [1,1,6,6,6,6],
       "Olive" : [0,5,5,5,5,5]}

game_start(die)
replay(die)

