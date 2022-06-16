from os.path import exists

import pandas as pd
from Neymans import neymanCal, calculcateVariance,  calculcateVarianceRow


'''
Main of the research. Reads the match database and does the necessary calculations, such as the causal effect calculation
variance calculation for the data of each hero , and the variacne calculation for a singular hero depending on the dataset size.
'''
df = []
if exists('match_df.csv'):
    df = pd.read_csv('match_df.csv')
pf = {}
if exists('content/heroes.json'):
    pf = pd.read_json('content/heroes.json')

'''we split the data depending on the 3 intervals that we instantiated.
'''
LatestP =[]
MidP =[]
OldestP =[]
inbetweeners  = df[0:10000] # used to plot the variance for a singular hero
inbetweeners2 =  df[0:14000] #used to plot the variance for a singular hero

for index, row in df.iterrows():
        #print(row)
        month = row['start_time'].split("-")[1]
        day   = row['start_time'].split("-")[2].split(" ")[0]

        if (month=='05' and int(day) >= 4) or month=='06':
            LatestP.append(row)
        elif month == '04' and int(day)>=4:
            MidP.append(row)
        elif month=='05' and int(day)<4:
            MidP.append(row)
        else:
            OldestP.append(row)

LatestP = pd.DataFrame(LatestP)
MidP = pd.DataFrame(MidP)
OldestP = pd.DataFrame(OldestP)

''' the calculations are saved into this dataframes to  be saved as a csv later on'''
estimandsForAll ={}
estimandsLatestPatch = {}
estimandsMidPatch ={}
estimandsOldPatch ={}
inbetweenersCal={} #obnly for plotting the variance
inbetweenersCal2={} #only for plotting the variance


'''Instantiation of all the dataframes to hold our new values'''
#print(pf)
for ind in pf.index:
    heroid = pf['id'][ind]
    #print(heroid)
    potentialOutcomes = {}
    potentialOutcomes['localized_name'] = pf['localized_name'][ind]
    potentialOutcomes['Win'] = 0
    potentialOutcomes['Loss'] = 0
    potentialOutcomes['NoWin'] = 0
    potentialOutcomes['NoLoss'] = 0
    potentialOutcomes['gamesWith'] = 0
    potentialOutcomes['gamesWithout'] = 0
    potentialOutcomes['averageCausal'] = 0
    potentialOutcomes['variance']= 0
    potentialOutcomes['uncertainty'] = 0
    estimandsForAll[heroid] = potentialOutcomes

for ind in pf.index:
    heroid = pf['id'][ind]
    # print(heroid)
    potentialOutcomes = {}
    potentialOutcomes['localized_name'] = pf['localized_name'][ind]
    potentialOutcomes['Win'] = 0
    potentialOutcomes['Loss'] = 0
    potentialOutcomes['NoWin'] = 0
    potentialOutcomes['NoLoss'] = 0
    potentialOutcomes['gamesWith'] = 0
    potentialOutcomes['gamesWithout'] = 0
    potentialOutcomes['averageCausal'] = 0
    potentialOutcomes['variance'] = 0
    potentialOutcomes['uncertainty'] = 0
    estimandsLatestPatch[heroid] = potentialOutcomes

for ind in pf.index:
    heroid = pf['id'][ind]
    # print(heroid)
    potentialOutcomes = {}
    potentialOutcomes['localized_name'] = pf['localized_name'][ind]
    potentialOutcomes['Win'] = 0
    potentialOutcomes['Loss'] = 0
    potentialOutcomes['NoWin'] = 0
    potentialOutcomes['NoLoss'] = 0
    potentialOutcomes['gamesWith'] = 0
    potentialOutcomes['gamesWithout'] = 0
    potentialOutcomes['averageCausal'] = 0
    potentialOutcomes['variance'] = 0
    potentialOutcomes['uncertainty'] = 0
    estimandsMidPatch[heroid] = potentialOutcomes
for ind in pf.index:
    heroid = pf['id'][ind]
    # print(heroid)
    potentialOutcomes = {}
    potentialOutcomes['localized_name'] = pf['localized_name'][ind]
    potentialOutcomes['Win'] = 0
    potentialOutcomes['Loss'] = 0
    potentialOutcomes['NoWin'] = 0
    potentialOutcomes['NoLoss'] = 0
    potentialOutcomes['gamesWith'] = 0
    potentialOutcomes['gamesWithout'] = 0
    potentialOutcomes['averageCausal'] = 0
    potentialOutcomes['variance'] = 0
    potentialOutcomes['uncertainty'] = 0
    estimandsOldPatch[heroid] = potentialOutcomes

for ind in pf.index:
    heroid = pf['id'][ind]
    # print(heroid)
    potentialOutcomes = {}
    potentialOutcomes['localized_name'] = pf['localized_name'][ind]
    potentialOutcomes['Win'] = 0
    potentialOutcomes['Loss'] = 0
    potentialOutcomes['NoWin'] = 0
    potentialOutcomes['NoLoss'] = 0
    potentialOutcomes['gamesWith'] = 0
    potentialOutcomes['gamesWithout'] = 0
    potentialOutcomes['averageCausal'] = 0
    potentialOutcomes['variance'] = 0
    inbetweenersCal[heroid] = potentialOutcomes
for ind in pf.index:
    heroid = pf['id'][ind]
    # print(heroid)
    potentialOutcomes = {}
    potentialOutcomes['localized_name'] = pf['localized_name'][ind]
    potentialOutcomes['Win'] = 0
    potentialOutcomes['Loss'] = 0
    potentialOutcomes['NoWin'] = 0
    potentialOutcomes['NoLoss'] = 0
    potentialOutcomes['gamesWith'] = 0
    potentialOutcomes['gamesWithout'] = 0
    potentialOutcomes['averageCausal'] = 0
    potentialOutcomes['variance'] = 0
    inbetweenersCal2[heroid] = potentialOutcomes


######### BASED ON ALL GAMES , INCLUDES VARIANCE AND CAUSAL EFFECT ##############
estimandsForAll = neymanCal(df,estimandsForAll)
for id in estimandsForAll:
        estimandsForAll[id] = calculcateVariance(id, estimandsForAll)

######### BASED ON ALL GAMES  , INCLUDES VARIANCE AND CAUSAL EFFECT ##############


#### USED FOR PLOTTING DATA VARIANCE FOR EACH HERO ######################
inbetweenersCal = neymanCal(inbetweeners,inbetweenersCal)

inbetweenersCal2 = neymanCal(inbetweeners2,inbetweenersCal2)
####USED FOR PLOTTING DATA VARIANCE FOR EACH HERO ######################



############ INVIDIVUDAL PATCH CALCULATIONS ##############
##INCLUDE VARIANCE AND CAUSAL EFFECT PER HERO ###
##Latest Patch #####
estimandsLatestPatch = neymanCal(LatestP,estimandsLatestPatch)
for id in estimandsLatestPatch:
        estimandsLatestPatch[id] = calculcateVariance(id,estimandsLatestPatch)

##In between patch
estimandsMidPatch = neymanCal(MidP,estimandsMidPatch)
for id in estimandsMidPatch:
        estimandsMidPatch[id] = calculcateVariance(id,estimandsMidPatch)
##Old patch
estimandsOldPatch = neymanCal(OldestP,estimandsOldPatch)
for id in estimandsOldPatch:
        estimandsOldPatch[id] = calculcateVariance(id,estimandsOldPatch)



############ INVIDIVUDAL PATCH CALCULATIONS ##############


#########Calculates the potential outcome variance For each hero, With increasing games ###############
#Variances for each Hero
variancesForAll = {}
for ind in pf.index:
    heroid = pf['id'][ind]
#    #print(heroid)
    variances  = {}
    variancesForAll[heroid] = variances


#Variances for each patch for each hero
for id in variancesForAll:
    exRow = {}
    #old patch
    row1 = estimandsOldPatch[id]
    variancesForAll[id]['Patch1 '+str(row1['gamesWith']+row1['gamesWithout'])] = calculcateVarianceRow(row1)

    #inbetweener
    row2 = inbetweenersCal[id]
    variancesForAll[id][row2['gamesWith'] + row2['gamesWithout']] = calculcateVarianceRow(row2)

    #mid patch
    row3 = estimandsMidPatch[id]
    exRow['Win'] = row1['Win']+row3['Win']
    exRow['Loss']= row1['Loss']+row3['Loss']
    exRow['NoWin'] = row1['NoWin'] + row3['NoWin']
    exRow['NoLoss'] = row1['NoLoss'] + row3['NoLoss']
    exRow['gamesWith'] = row1['gamesWith'] + row3['gamesWith']
    exRow['gamesWithout'] = row1['gamesWithout'] + row3['gamesWithout']
    variancesForAll[id]['Middle Patch '+str(exRow['gamesWith']+exRow['gamesWithout'])] = calculcateVarianceRow(exRow)

    #inbetweener2
    # inbetweener
    row4 = inbetweenersCal2[id]
    variancesForAll[id][row4['gamesWith'] + row4['gamesWithout']] = calculcateVarianceRow(row4)

    #all games
    row5 = estimandsForAll[id]
    variancesForAll[id]['Patch2 '+str(row5['gamesWith']+row5['gamesWithout'])] = calculcateVarianceRow(row5)


#########Calculates the potential outcome variance For each hero, With increasing games ###############




df = pd.DataFrame(variancesForAll)
df = df.transpose()
df.to_csv('content/variancesForAll.csv',index = True)


df = pd.DataFrame(estimandsForAll)
df = df.transpose()
df.to_csv('content/estimations.csv',index = True)

df = pd.DataFrame(estimandsLatestPatch)
df = df.transpose()
df.to_csv('content/estimationsLatestPatch.csv',index = True)

df = pd.DataFrame(estimandsMidPatch)
df = df.transpose()
df.to_csv('content/estimationsMidPatch.csv',index = True)

df = pd.DataFrame(estimandsOldPatch)
df = df.transpose()
df.to_csv('content/estimationsOldPatch.csv',index = True)









