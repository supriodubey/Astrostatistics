#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:48:03 2022

@author: draco
"""

import numpy as np
import matplotlib.pyplot as plt 
import random
from scipy.stats import norm



##call dicethrow with 1st variable input as the number of throws, second as no. of dice and the mode.The default mode is sum. In case of abs diff the number mode =! sum and to be noted that it only works when the number of dice is two \n" )
## question 1,2,5 solution ##
def dicethrow(no_throws,no_dice,mode ='add'):

    dice_sum_outcome = []# the elements in number of sum should be the sum of the dices.
#def throws ()
    for i in range (1,no_throws+1):
        #print("number of throw", i)
        dice_face = []
    
        for j in range(1,no_dice+1):
        
            dice = random.randint(1,6)
            #print(dice)
            dice_face.append(dice)
            #print (dice_face)
        if mode == 'add':
            out_add = sum(dice_face)
                #print (out_add) 
                       
       
        else:
                ######## only in case of two dice ######## for absolute difference##
            print(dice_face)
            out_add = abs(dice_face[0]-dice_face[1])
        dice_sum_outcome.append(out_add)    
    return dice_sum_outcome

####call diceinteg for Q 6. plot ####

def diceinteg(no_throws, no_dice):   
    Dice=np.zeros((6 , no_dice))
    for r in range (no_dice) :
        Dice [:,r]=np.array ( [ 0 , 1 , 2 , 3 , 4 , 5 ] )*6**r
    #print ( Dice )
    output_sum = np.zeros(no_throws)
    for i in range (no_throws):
        #print("throw number",i)
        for j in range(no_dice):
            dice_output = random.choice(Dice[:,j])
            output_sum[i] += dice_output
            #print("the dice shows", dice_output)
    dice_sum_outcome = output_sum
    return (dice_sum_outcome)

no_dice=2
no_throws=10000000

#dice_sum_output =  dicethrow(no_throws,no_dice)
dice_sum_output = diceinteg(no_throws,no_dice)


mu = np.mean(dice_sum_output)
sigma = np.var(dice_sum_output)
print(mu,sigma)

########## Plot ########

plt.hist(dice_sum_output)
plt.ylabel("PDF")
plt . xlabel("SUM")
plt.tight_layout()
plt.title(" %s dice with %s throws has a mean %s and variance %s." %(no_dice,no_throws,mu,sigma))
plt.show()