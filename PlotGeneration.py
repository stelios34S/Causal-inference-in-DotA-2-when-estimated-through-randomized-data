from os.path import exists

from numpy.random._examples.cffi.extending import rng

import Neymans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
ag = []
lp = []
mp = []
op = []
pf = {}
vr = []


'''We read all the files to be able to plot them'''
if exists('content/estimationsLatestPatch.csv'):
    lp = pd.read_csv('content/estimationsLatestPatch.csv')
if exists('content/estimationsMidPatch.csv'):
    mp = pd.read_csv('content/estimationsMidPatch.csv')
if exists('content/estimationsOldPatch.csv'):
    op = pd.read_csv('content/estimationsOldPatch.csv')
if exists('content/estimations.csv'):
    ag = pd.read_csv('content/estimations.csv')
if exists('content/heroes.json'):
    pf = pd.read_json('content/heroes.json')
if exists('content/variancesForAll.csv'):
    vr = pd.read_csv('content/variancesForAll.csv')

plt.rcParams["figure.figsize"]=(8,6)

'''FOR RESULT PURPOSES, ADDS ALL AVERAGE CAUSAL EFFECTS NEXT TO EACH OTHER'''
df = {}
i=0
for ind in pf.index:

    heroid = pf['id'][ind]
    #print(heroid)
    potentialOutcomes = {}
    potentialOutcomes['heroid'] = pf['localized_name'][ind]
    potentialOutcomes['P1'] = 0
    potentialOutcomes['uncertainty1']= 0
    potentialOutcomes['P2'] = 0
    potentialOutcomes['uncertainty2'] = 0
    potentialOutcomes['P3'] = 0
    potentialOutcomes['uncertainty3'] = 0
    potentialOutcomes['Overall'] = 0
    potentialOutcomes['uncertaintyall'] = 0
    df[i] = potentialOutcomes
    i+=1
for ind in df:
    #print(op['averageCausal'][3])
    df[ind]['P1'] = op['averageCausal'][ind]
    df[ind]['uncertainty1'] = op['uncertainty'][ind]
    df[ind]['P2'] = mp['averageCausal'][ind]
    df[ind]['uncertainty2'] = mp['uncertainty'][ind]
    df[ind]['P3'] = lp['averageCausal'][ind]
    df[ind]['uncertainty3'] = lp['uncertainty'][ind]
    df[ind]['Overall'] = ag['averageCausal'][ind]
    df[ind]['uncertaintyall'] = ag['uncertainty'][ind]


left =[]
for i in range(0,4):
    left.append(i)
tick_label = ['Overall', '4/05-4/06', '4/04-4/05','23/02-4/04']
height=[df[2]['Overall'],df[2]['P3'],df[2]['P2'],df[2]['P1']]
print(height)
uncertain=[df[15]['uncertaintyall'],df[15]['uncertainty3'],df[15]['uncertainty2'],df[15]['uncertainty1']]
plt.scatter(height,tick_label,c=uncertain,alpha=0.3)
cbar = plt.colorbar()
cbar.set_label('uncertainty')
for i in left:
    plt.plot([-0.04,height[i]],[tick_label[i],tick_label[i]],'--k',lw=0.5,alpha=0.3)
plt.tick_params(axis='x',which = 'major',labelsize = 8)
plt.tick_params(axis='y',which = 'major',labelsize = 9)
#plt.yticks(np.arange(-0.20,+0.20,0.02))
plt.xlabel('THE 3 DIFFERENT INTERVALS')
plt.ylabel('Average Causal Effect')
plt.title('Average Causal Effect of "Bane" in Different Patches')
plt.show()



df = pd.DataFrame(df)
df = df.transpose()
df.to_csv('content/causalEffectsSideBySide.csv',index = True)

'''FOR RESULT PURPOSES, ADDS ALL AVERAGE CAUSAL EFFECTS NEXT TO EACH OTHER'''



'''USED TO PLOT THE AVERAGE CAUSAL EFFECT FOR THE LATEST INTERVAL'''

left =[]
left1 =[]
for i in range(0,62):
    left.append(i)
for i in range(62, 123):
    left1.append(i)

lp = lp.sort_values(by=['averageCausal'],ascending= True)
lp = lp.reset_index()
lp.drop('index',axis=1,inplace=True)
tick_label = []
height = []
uncertain =[]
for i in left:
    tick_label.append(lp['localized_name'][i])
    uncertain.append(lp['uncertainty'][i])
    height.append(lp['averageCausal'][i])
plt.scatter(height,tick_label,c= uncertain,alpha=0.3)
for i in left:
    plt.plot([-0.19,height[i]],[tick_label[i],tick_label[i]],'--k',lw=0.5,alpha=0.3)
plt.plot([0,0],[tick_label[len(left)-1],tick_label[0]],'k',alpha=0.1)
cbar = plt.colorbar()
cbar.set_label('uncertainty')
plt.tick_params(axis='x',which = 'major',labelsize = 6)
plt.tick_params(axis='y',which = 'major',labelsize = 5)
plt.xticks(np.arange(-0.20,+0.20,0.02))
#plt.xticks(left,tick_label)
plt.ylabel('Hero Names')
plt.xlabel('Average Causal Effect')
plt.title('Average Causal Effect of a Hero on Winning, 4/5-4/6')
plt.show()


tick_label = []
height = []
uncertain =[]
for i in left1:
    tick_label.append(lp['localized_name'][i])
    uncertain.append(lp['uncertainty'][i])
    height.append(lp['averageCausal'][i])
plt.scatter(height,tick_label,c= uncertain,alpha=0.3)
for i,_ in enumerate(left1):
    plt.plot([-0.19,height[i]],[tick_label[i],tick_label[i]],'--k',lw=0.5,alpha=0.3)
plt.plot([0,0],[tick_label[len(left1)-1],tick_label[0]],'k',alpha=0.1)
cbar = plt.colorbar()
cbar.set_label('uncertainty')
plt.tick_params(axis='x',which = 'major',labelsize = 6)
plt.tick_params(axis='y',which = 'major',labelsize = 5)
plt.xticks(np.arange(-0.20,+0.20,0.02))
#plt.xticks(left,tick_label)
plt.ylabel('Hero Names')
plt.xlabel('Average Causal Effect')
plt.title('Average Causal Effect of a Hero on Winning, 4/5-4/6')
plt.show()


'''USED TO PLOT THE AVERAGE CAUSAL EFFECT FOR THE LATEST INTERVAL'''



'''USED TO PLOT THE AVERAGE CAUSAL EFFECT FOR THE MID INTERVAL'''

mp = mp.sort_values(by=['averageCausal'],ascending= True)
mp = mp.reset_index()
mp.drop('index',axis=1,inplace=True)
tick_label = []
height = []
uncertain =[]
for i in left:
    tick_label.append(mp['localized_name'][i])
    uncertain.append(mp['uncertainty'][i])
    height.append(mp['averageCausal'][i])
plt.scatter(height,tick_label,c= uncertain,alpha=0.3)
for i in left:
    plt.plot([-0.19,height[i]],[tick_label[i],tick_label[i]],'--k',lw=0.5,alpha=0.3)
plt.plot([0,0],[tick_label[len(left)-1],tick_label[0]],'k',alpha=0.1)
cbar = plt.colorbar()
cbar.set_label('uncertainty')
plt.tick_params(axis='x',which = 'major',labelsize = 6)
plt.tick_params(axis='y',which = 'major',labelsize = 5)
plt.xticks(np.arange(-0.20,+0.20,0.02))
#plt.xticks(left,tick_label)
plt.ylabel('Hero Names')
plt.xlabel('Average Causal Effect')
plt.title('Average Causal Effect of a Hero on Winning, 4/4-4/5')
plt.show()


tick_label = []
height = []
uncertain =[]
for i in left1:
    tick_label.append(mp['localized_name'][i])
    uncertain.append(mp['uncertainty'][i])
    height.append(mp['averageCausal'][i])
plt.scatter(height,tick_label,c= uncertain,alpha=0.3)
for i,_ in enumerate(left1):
    plt.plot([-0.19,height[i]],[tick_label[i],tick_label[i]],'--k',lw=0.5,alpha=0.3)
plt.plot([0,0],[tick_label[len(left1)-1],tick_label[0]],'k',alpha=0.1)
cbar = plt.colorbar()
cbar.set_label('uncertainty')
plt.tick_params(axis='x',which = 'major',labelsize = 6)
plt.tick_params(axis='y',which = 'major',labelsize = 5)
plt.xticks(np.arange(-0.20,+0.20,0.02))
#plt.xticks(left,tick_label)
plt.ylabel('Hero Names')
plt.xlabel('Average Causal Effect')
plt.title('Average Causal Effect of a Hero on Winning, 4/4-4/5')
plt.show()


'''USED TO PLOT THE AVERAGE CAUSAL EFFECT FOR THE MID INTERVAL'''



'''USED TO PLOT THE AVERAGE CAUSAL EFFECT FOR THE OLDEST INTERVAL'''


op = op.sort_values(by=['averageCausal'],ascending= True)
op = op.reset_index()
op.drop('index',axis=1,inplace=True)
tick_label = []
height = []
uncertain =[]
for i in left:
    tick_label.append(op['localized_name'][i])
    uncertain.append(op['uncertainty'][i])
    height.append(op['averageCausal'][i])
plt.scatter(height,tick_label,c= uncertain,alpha=0.3)
for i in left:
    plt.plot([-0.19,height[i]],[tick_label[i],tick_label[i]],'--k',lw=0.5,alpha=0.3)
plt.plot([0,0],[tick_label[len(left)-1],tick_label[0]],'k',alpha=0.1)
cbar = plt.colorbar()
cbar.set_label('uncertainty')
plt.tick_params(axis='x',which = 'major',labelsize = 6)
plt.tick_params(axis='y',which = 'major',labelsize = 5)
plt.xticks(np.arange(-0.20,+0.20,0.02))
#plt.xticks(left,tick_label)
plt.ylabel('Hero Names')
plt.xlabel('Average Causal Effect')
plt.title('Average Causal Effect of a Hero on Winning, 23/02-4/04')
plt.show()


tick_label = []
height = []
uncertain =[]
for i in left1:
    tick_label.append(op['localized_name'][i])
    uncertain.append(op['uncertainty'][i])
    height.append(op['averageCausal'][i])
plt.scatter(height,tick_label,c= uncertain,alpha=0.3)
for i,_ in enumerate(left1):
    plt.plot([-0.19,height[i]],[tick_label[i],tick_label[i]],'--k',lw=0.5,alpha=0.3)
plt.plot([0,0],[tick_label[len(left1)-1],tick_label[0]],'k',alpha=0.1)
cbar = plt.colorbar()
cbar.set_label('uncertainty')
plt.tick_params(axis='x',which = 'major',labelsize = 6)
plt.tick_params(axis='y',which = 'major',labelsize = 5)
plt.xticks(np.arange(-0.20,+0.20,0.02))
#plt.xticks(left,tick_label)
plt.ylabel('Hero Names')
plt.xlabel('Average Causal Effect')
plt.title('Average Causal Effect of a Hero on Winning, 23/02-4/04')
plt.show()

'''USED TO PLOT THE AVERAGE CAUSAL EFFECT FOR THE OLDEST INTERVAL'''

'''USED TO PLOT THE AVERAGE CAUSAL EFFECT FOR THE ALL GAMES'''

ag = ag.sort_values(by=['averageCausal'],ascending= True)
ag = ag.reset_index()
ag.drop('index',axis=1,inplace=True)
tick_label = []
height = []
uncertain =[]
for i in left:
    tick_label.append(ag['localized_name'][i])
    uncertain.append(ag['uncertainty'][i])
    height.append(ag['averageCausal'][i])
plt.scatter(height,tick_label,c= uncertain,alpha=0.3)
for i in left:
    plt.plot([-0.19,height[i]],[tick_label[i],tick_label[i]],'--k',lw=0.5,alpha=0.3)
plt.plot([0,0],[tick_label[len(left)-1],tick_label[0]],'k',alpha=0.1)
cbar = plt.colorbar()
cbar.set_label('uncertainty')
plt.tick_params(axis='x',which = 'major',labelsize = 6)
plt.tick_params(axis='y',which = 'major',labelsize = 5)
plt.xticks(np.arange(-0.20,+0.20,0.02))
#plt.xticks(left,tick_label)
plt.ylabel('Hero Names')
plt.xlabel('Average Causal Effect')
plt.title('Average Causal Effect of a Hero on Winning, All Games')
plt.show()


tick_label = []
height = []
uncertain =[]
for i in left1:
    tick_label.append(ag['localized_name'][i])
    uncertain.append(ag['uncertainty'][i])
    height.append(ag['averageCausal'][i])
plt.scatter(height,tick_label,c= uncertain,alpha=0.3)
for i,_ in enumerate(left1):
    plt.plot([-0.19,height[i]],[tick_label[i],tick_label[i]],'--k',lw=0.5,alpha=0.3)
plt.plot([0,0],[tick_label[len(left1)-1],tick_label[0]],'k',alpha=0.1)
cbar = plt.colorbar()
cbar.set_label('uncertainty')
plt.tick_params(axis='x',which = 'major',labelsize = 6)
plt.tick_params(axis='y',which = 'major',labelsize = 5)
plt.xticks(np.arange(-0.20,+0.20,0.02))
#plt.xticks(left,tick_label)
plt.ylabel('Hero Names')
plt.xlabel('Average Causal Effect')
plt.title('Average Causal Effect of a Hero on Winning, All Games')
plt.show()

'''USED TO PLOT THE AVERAGE CAUSAL EFFECT FOR THE ALL GAMES'''



'''USED TO PLOT  THE VARIANCE FOR DIFFERENT AMOUNTS OF GAMES FOR A SINGULAR HERO'''
tick_label = []
y = []
hero_id = 5
vr.drop(1)

for i in vr:
    if i != 'Unnamed: 0':
        tick_label.append(i)
        y.append(vr[i][hero_id])


#x = np.arange(1,20000,1000)
plt.plot(tick_label,y)


plt.xlabel('amount of games')
plt.ylabel('Variance')
plt.title('Data Variance for Hero "Crystal Maiden"')
plt.show()

'''USED TO PLOT  THE VARIANCE FOR DIFFERENT AMOUNTS OF GAMES FOR A SINGULAR HERO'''






