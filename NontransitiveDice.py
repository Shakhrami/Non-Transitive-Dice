#?/usr/bin/env python

# I've always wanted a pair of Non-transitive Dice.
# This version is inspired by Dr. James Grime from the University of Cambridge.

#Version 1.0 : 1 die and 1 roll per player.
import random

die = {"Red" : [4,4,4,4,4,9],
       "Yellow" : [3,3,3,3,8,8],
       "Blue" : [2,2,2,7,7,7],
       "Magenta" : [1,1,6,6,6,6],
       "Olive" : [0,5,5,5,5,5]}

for dice in die:
    print dice,":" ,die[dice]
print "-------------------------------------------------"       

valid1 = False
while not valid1:
    p1Die = raw_input("Player 1, pick your die:")
    if(p1Die in die):
        p1Die = die[p1Die]
        valid1 = True
        print "P1's die: ", p1Die
    else:
        print "invalid"


valid2 = False
while not valid2:
    p2Die = raw_input("Player 2, pick your die:")
    if(p2Die in die):
        p2DieTest = die[p2Die]
        if(p2DieTest == p1Die):
            print "die already selected."
        else:
            p2Die = p2DieTest
            valid2 = True
            print "P2's die: ", p2Die
    else:
        print "invalid"
print "-------------------------------------------------"        
p1Roll = random.choice(p1Die)
p2Roll = random.choice(p2Die)

print "P1's roll:", p1Roll
print "P2's roll:", p2Roll

if (p1Roll > p2Roll):
    print "Player 1 wins!"
else:
    print "Player 2 wins!"
