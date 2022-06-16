from os.path import exists
from scipy.stats import chi2_contingency
import Neymans
import pandas as pd




lp=[]
mp=[]
op=[]
pf = []
'''READS IN  THE ESTIMATED FILES TO CALCULATE THE CHI-SQUARE TEST INDEPDENCE RESULTS'''
if exists('content/estimationsLatestPatch.csv'):
    lp = pd.read_csv('content/estimationsLatestPatch.csv')
if exists('content/estimationsMidPatch.csv'):
    mp = pd.read_csv('content/estimationsMidPatch.csv')
if exists('content/estimationsOldPatch.csv'):
    op = pd.read_csv('content/estimationsOldPatch.csv')
if exists('content/heroes.json'):
    pf = pd.read_json('content/heroes.json')


'''WE DROP THE UNECESSARY INFORMATION'''
lp.drop('NoWin',axis=1,inplace= True)
lp.drop('NoLoss',axis=1,inplace= True)
lp.drop('gamesWithout',axis=1,inplace= True)
lp.drop('averageCausal',axis=1,inplace= True)
lp.drop('variance',axis=1,inplace= True)
lp.drop('Unnamed: 0',axis=1,inplace= True)
lp.drop('gamesWith',axis=1,inplace= True)
lp.drop('uncertainty',axis=1,inplace= True)
lp.drop('localized_name',axis=1,inplace= True)

mp.drop('NoWin',axis=1,inplace= True)
mp.drop('NoLoss',axis=1,inplace= True)
mp.drop('gamesWithout',axis=1,inplace= True)
mp.drop('averageCausal',axis=1,inplace= True)
mp.drop('variance',axis=1,inplace= True)
mp.drop('Unnamed: 0',axis=1,inplace= True)
mp.drop('gamesWith',axis=1,inplace= True)
mp.drop('uncertainty',axis=1,inplace= True)
mp.drop('localized_name',axis=1,inplace= True)

op.drop('NoWin',axis=1,inplace= True)
op.drop('NoLoss',axis=1,inplace= True)
op.drop('gamesWithout',axis=1,inplace= True)
op.drop('averageCausal',axis=1,inplace= True)
op.drop('variance',axis=1,inplace= True)
op.drop('Unnamed: 0',axis=1,inplace= True)
op.drop('gamesWith',axis=1,inplace= True)
op.drop('uncertainty',axis=1,inplace= True)
op.drop('localized_name',axis=1,inplace= True)



'''HERE THE CHI-SQUARE TEST IS USED TO CALCULATE THE STATISTICAL INDEPEDENCE OF GAME UPDATES AND GAME OUT COME
 for EACH HERO'''
result  = ['HeroName','Depedance','pvalue']
result = pd.DataFrame(columns=result)
#pf['localized_name'][i]
for i in range(1,123):
    res = pd.DataFrame(columns =['Win','Loss'])
    res = res.append(lp[i:i+1])
    res = res.append(mp[i:i+1])
    res = res.append(op[i:i+1])
    res = res.values.tolist()
    stat, p ,dof, expected = chi2_contingency(res)
    if p <= 0.05:
        result.loc[i-1]=([pf['localized_name'][i],'Depedent',p])
    else:
        result.loc[i - 1] = ([pf['localized_name'][i], 'Indepedent',p])

result.to_csv('content/PatchDepedenceResults.csv',index = True)


'''HERE THE CHI-SQUARED TEST IS USED TO CALCULATE THE STATISTICAL INDEPEDENCE OF HERO SELECTION AND GAME OUT COME'''
ag = []
if exists('content/estimations.csv'):
    ag = pd.read_csv('content/estimations.csv')
ag.drop('NoWin', axis=1, inplace=True)
ag.drop('NoLoss', axis=1, inplace=True)
ag.drop('gamesWithout', axis=1, inplace=True)
ag.drop('averageCausal', axis=1, inplace=True)
ag.drop('variance', axis=1, inplace=True)
ag.drop('Unnamed: 0',axis=1,inplace= True)
ag.drop('gamesWith',axis=1,inplace= True)
ag.drop('uncertainty',axis=1,inplace= True)
ag.drop('localized_name',axis=1,inplace= True)

ag.drop(103, inplace=True)
print(ag)
ag = ag.values.tolist()
stat1, p1,dof1, expected1 = chi2_contingency(ag)
if p1 <= 0.05:
    print(p1)
    print('depedent1')
else:
    print('Indepedent1')
