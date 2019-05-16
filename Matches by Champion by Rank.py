import requests
import json
from numpy import zeros
import champdict

api_key = 'RGAPI-5478c4a3-e795-497b-9463-19f2a3c723e4'

players = requests.get('https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/IRON/IV?page=1&api_key={key}'.format(key=api_key))
playersdata = players.json()

matchesplayed = zeros([600],dtype=int)

for i in playersdata[:9]:
    summoner = i["summonerName"]
    account = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{sum}?api_key={key}'.format(key=api_key,sum=summoner))
    accountdata = account.json()
    accountid = accountdata["accountId"]
    response = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{id}?api_key={key}'.format(key=api_key,id=accountid))
    data = response.json()
    
    for i in data["matches"]:
        x = i["champion"]
        matchesplayed[x] = matchesplayed[x] + 1

for i in champions:
    if matchesplayed[i] > 0:
        print(champdict.champions[i] + ': ' + str(matchesplayed[i]))