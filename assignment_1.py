#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:24:09 2022

@author: draco
"""

from traitlets.traitlets import CaselessStrEnum
from typing import Optional
import random
import numpy as np
import matplotlib.pyplot as plt
import random





def host_opendoor(player_door, prize_door,num_door, case):
  if(case == 0):

    if (player_door == prize_door):
    
      option = num_door.pop(num_door.index(player_door)) 
      hostoption = random.choice(num_door)
      rem = num_door.pop(num_door.index(hostoption))
    else:
     
      option = num_door.pop(num_door.index(player_door)) 
     
      for i in num_door: 
       
        if i != prize_door:
          host_option = i    
      hostoption = num_door.pop(num_door.index(host_option)) 
  if(case ==1):
    option = num_door.pop(num_door.index(player_door))
    hostoption = random.choice(num_door)




  return(hostoption,player_door,prize_door, num_door)




def result(sw, num_test):
  win_switch = 0
  win_no_switch = 0
  lose_switch = 0
  lose_no_switch = 0
  win_r_s=0
  lose_r_s =0
  win_r_ns =0
  lose_r_ns =0
  dont_count=0
  
  for i in range(num_test):
    case=random.randint(0,1)
    
    num_door = [0,1,2]
    
    prize_door = random.choice((num_door))

    player_door = random.choice((num_door))
    hostdoor,playerdoor,prizedoor,nd = host_opendoor(player_door, prize_door,num_door, case)
    if(case == 0):
      if(sw == True):
        playerdoor = nd[0]
  
      if(sw == True and playerdoor == prizedoor ):
        win_switch +=1
      if(sw == True and playerdoor != prizedoor ):
        lose_switch +=1
      if(sw == False and playerdoor == prizedoor ):
        win_no_switch +=1
      if(sw == False and playerdoor != prizedoor ):
        lose_no_switch +=1
    if(case ==1):
      #print(nd)
      #print(hostdoor)
      if(sw == True):
        nd.pop(nd.index(hostdoor))
        playerdoor = nd[0]
      
      #print(playerdoor)
      #print(prizedoor)
      if(hostdoor != prizedoor and playerdoor == prizedoor and sw == True):
        win_r_s += 1
      if(hostdoor != prizedoor and playerdoor != prizedoor and sw == True):
        lose_r_s += 1
      if(hostdoor != prizedoor and playerdoor == prizedoor and sw == False):
        win_r_ns += 1
      if(hostdoor != prizedoor and playerdoor != prizedoor and sw == False):
        lose_r_ns += 1
      if(hostdoor == prizedoor):
        dont_count +=1


  print((win_switch+win_r_s)/(num_test-dont_count),(win_no_switch+win_r_ns)/(num_test-dont_count))#lose_switch,lose_no_switch, win_r_s , lose_r_s,win_r_ns, lose_r_ns, dont_count)

result(False,10000)