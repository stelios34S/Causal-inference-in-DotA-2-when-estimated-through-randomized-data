import pandas as pd
import numpy as np
import datetime
import os
from os.path import exists
import json
import requests
import time
import dota2


def extractMatchInfo(data):
    '''
    A function used to extract info from string data of one match into dataframes.

    INPUT:
    data - data of one match in dictionary (originally obtained from https://api.opendota.com/api/publicMatches)

    OUTPUT:
    arr - a list of match information: match_id, time, game_mode,
    '''
    arr = []
    # Save match_id
    arr.append(data['match_id'])

    # Save game_mode. In this exercise, we are looking for matches with game_mode 2
    arr.append(data['game_mode'])

    # Save start_time converted to datetime format
    arr.append(datetime.datetime.fromtimestamp(int(data['start_time'])).strftime('%Y-%m-%d %H:%M:%S'))

    # Save duration
    arr.append(data['duration'])

    # Save lobby_type
    arr.append(data['lobby_type'])

    # Save picks for both teams: team radiant goes first
    radiant = [int(i) for i in data['radiant_team'].split(",")]
    dire = [int(i) for i in data['dire_team'].split(",")]
    arr.extend(radiant)
    arr.extend(dire)

    # Save result: radiant_win
    arr.append(data['radiant_win'])

    return arr


'''
Calls the API to retrieve data regarding public games.
'''
flag = True # used in the program in order to call certain part of the code once.
while True:
    df = []

    if exists('match_df.csv'):  #if the match.csv file is already present then we read the values from it.
        df = pd.read_csv('match_df.csv')
        pf = df
        df = df.values.tolist() # we convert it into a list to append the new data on it.

    '''
    Crucial Part of the API calling script
    we can either take the newest games and start going back from that, or take the oldest game in our dataset go back
    from that.
    '''
    if flag :
        '''
        Uncomment the 2 following lines  and comment the third to switch from most recent games to getting older games.
        and vice versa.
        '''
        #match_id = pf.iloc[len(pf)-1]['match_id'] #
        #r  = requests.get('https://api.opendota.com/api/publicMatches?less_than_match_id={}'.format(match_id))
        r  = requests.get('https://api.opendota.com/api/publicMatches')
        data = r.json()
        for m in data:
            if m['game_mode'] == 5: #game mode 5 equals the all random gamemode.
                arr = extractMatchInfo(m)
                df.append(arr)
            match_id = m['match_id']
        flag = False
    '''
        Crucial Part of the API calling script
    '''
    # For each query, we could obtain data for 100 matches. The following codes keeps querying for multiple times to obtain data for more matches.

    '''
    As soon as we ahve done our first call to the api , then we have already gotted a match_id to retrieve more data on.
    '''
    for _ in range(50): # choose whatever number of rounds you'd like to have for your dataset
        r = requests.get('https://api.opendota.com/api/publicMatches?less_than_match_id={}'.format(match_id))
        data = r.json()
        for m in data:
            if m['game_mode'] == 5:
                arr = extractMatchInfo(m)
                df.append(arr)
            match_id = m['match_id']


    df = pd.DataFrame(df)
    df.rename(columns={0: "match_id", 1: "game_mode", 2: "start_time", 3: "duration", 4: "lobby_type",
                       5: "radiant_1", 6: "radiant_2", 7: "radiant_3", 8: "radiant_4", 9: "radiant_5",
                       10: "dire_1", 11: "dire_2", 12: "dire_3", 13: "dire_4", 14: "dire_5", 15: "radiant_win"}, inplace = True)
    # Rename columns and save to a .csv file, such that we could read and load the data for future analysis
    df.drop_duplicates(subset = ['match_id'], inplace = True, keep = 'last')
    df = df.sort_values(by='match_id', ascending= False)
    df.to_csv('match_df.csv', index=False) #and we save our newest data onto a csv file with the old data.
    time.sleep(120) #in order to do proper calls to the API and not overuse it, as consecutive calls result in a
                    # cooldown

# We can also extract heroes' information from Dota2 API.
#os.system("curl https://api.opendota.com/api/heroes > /content/heroes.json")