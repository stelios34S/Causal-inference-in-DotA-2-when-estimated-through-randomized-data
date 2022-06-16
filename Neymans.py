import pandas as pd
import numpy as np
import datetime
import os
from os.path import exists
import json
import requests
import time
import math
import dota2


####USED TO COUNT HOW MANY WINS AND LOSSES, AND HOW MANY GAMES IT HAS BEEN IN (EACH HERO) ############
def neymanCal(df, estimandsForAll):
    for id in estimandsForAll:
        for ind in df.index:
            flag = False
            if df['radiant_1'][ind] == id or df['radiant_2'][ind] == id or df['radiant_3'][ind] == id or df['radiant_4'][ind] == id or df['radiant_5'][ind] == id:
                estimandsForAll[id]['gamesWith'] +=1
                flag = True
                if df['radiant_win'][ind] == True :
                    estimandsForAll[id]['Win'] +=1
                else:
                    estimandsForAll[id]['Loss']+=1
            if df['dire_1'][ind] == id or df['dire_2'][ind] == id or df['dire_3'][ind] == id or df['dire_4'][ind] == id or df['dire_5'][ind] == id:
                estimandsForAll[id]['gamesWith']+=1
                flag = True
                if df['radiant_win'][ind] == True :
                    estimandsForAll[id]['Loss'] +=1
                else:
                    estimandsForAll[id]['Win']+=1
            if not flag:
                estimandsForAll[id]['gamesWithout']+=1
                if df['radiant_win'][ind] == True :
                    estimandsForAll[id]['NoWin'] +=1
                else:
                    estimandsForAll[id]['NoLoss']+=1


    return estimandsForAll

####USED TO COUNT HOW MANY WINS AND LOSSES, AND HOW MANY GAMES IT HAS BEEN IN (EACH HERO) ############



######USED TO CALCULATE THE AVERAGE CAUSAL EFFECT OF A HERO , PLUS THE VARIANCE OF THE DATA#############
def calculcateVariance(id,estimandsForAll):

    if estimandsForAll[id]['gamesWith'] == 0 or estimandsForAll[id]['gamesWithout'] == 0:
        estimandsForAll[id]['averageCausal'] = 0
        estimandsForAll[id]['variance'] = 0
    else:
        mean1 = (estimandsForAll[id]['Win'] / estimandsForAll[id]['gamesWith'])
        mean0 = (estimandsForAll[id]['NoWin'] / estimandsForAll[id]['gamesWithout'])
        estimandsForAll[id]['averageCausal'] = mean1 - mean0
        sum0 = 0
        sum1 = 0
        for i in range((estimandsForAll[id]['NoWin'])):
            sum0 += math.pow(1 - mean0, 2)
        for i in range((estimandsForAll[id]['NoLoss'])):
            sum0 += math.pow(0 - mean0, 2)
        sum0 = sum0 / (estimandsForAll[id]['gamesWithout'] - 1)

        for i in range((estimandsForAll[id]['Win'])):
            sum1 += math.pow(1 - mean1, 2)
        for i in range((estimandsForAll[id]['Loss'])):
            sum1 += math.pow(0 - mean1, 2)
        sum1 = sum1 / (estimandsForAll[id]['gamesWith'] - 1)
        estimandsForAll[id]['variance'] = sum1 / estimandsForAll[id]['gamesWith'] + sum0 / estimandsForAll[id][
            'gamesWithout']
        estimandsForAll[id]['uncertainty'] = math.sqrt(estimandsForAll[id]['variance'])
    return estimandsForAll[id]


######USED TO CALCULATE THE AVERAGE CAUSAL EFFECT OF A HERO , PLUS THE VARIANCE OF THE DATA#############


##### USED TO CALCULATE THE VARIANCE OF THE DATA FOR EACH HERO, ON DIFFERENT AMOUNTS OF DATA
def calculcateVarianceRow(estimandsForAll):
    if estimandsForAll['gamesWith'] == 0 or estimandsForAll['gamesWithout'] == 0:
       return 0
    else:
        mean1 = (estimandsForAll['Win'] / estimandsForAll['gamesWith'])
        mean0 = (estimandsForAll['NoWin'] / estimandsForAll['gamesWithout'])
        sum0 = 0
        sum1 = 0
        for i in range((estimandsForAll['NoWin'])):
            sum0 += math.pow(1 - mean0, 2)
        for i in range((estimandsForAll['NoLoss'])):
            sum0 += math.pow(0 - mean0, 2)
        sum0 = sum0 / (estimandsForAll['gamesWithout'] - 1)

        for i in range((estimandsForAll['Win'])):
            sum1 += math.pow(1 - mean1, 2)
        for i in range((estimandsForAll['Loss'])):
            sum1 += math.pow(0 - mean1, 2)
        sum1 = sum1 / (estimandsForAll['gamesWith'] - 1)
        var = sum1 / estimandsForAll['gamesWith'] + sum0 / estimandsForAll[
            'gamesWithout']
        return var


