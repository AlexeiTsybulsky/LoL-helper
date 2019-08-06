import requests
import json
from numpy import zeros
import champdict
import queuedict

api_key = 'RGAPI-846a026f-c30e-48b0-9c9c-3b16bc3b2869'

summoner_name = 'Icarus142'

response = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={key}'.format(name=summoner_name, key=api_key))
summoner_info = response.json()

account_id = summoner_info["accountId"]

response2 = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{account}?api_key={key}'.format(key=api_key, account=account_id))
data = response2.json()


matchesplayed = zeros((4,5,600),dtype=int)

queue = {
        400: 3,
        420: 0,
        430: 2,
        440: 1,
        
        3: 400,
        0: 420,
        2: 430,
        1: 440
        }

roles = {
        "TOP": 0,
        "JUNGLE": 1,
        "MID": 2,
        "BOTTOM": 3,
        "NONE": 4,
        
        0: "TOP",
        1: "JUNGLE",
        2: "MID",
        3: "BOTTOM",
        4: "SUPPORT"
        }


for i in data["matches"]:
    if i["queue"] in [400,420,430,440]:
        x = i["champion"]
        matchesplayed[queue[i["queue"]]][roles[i["lane"]]][x] = matchesplayed[queue[i["queue"]]][roles[i["lane"]]][x] + 1

for a,i in enumerate(matchesplayed):
    print()
    print(queuedict.queues[queue[a]])
    for b,j in enumerate(matchesplayed[a]):
        print()
        print(roles[b])
        for k in champions:
            if matchesplayed[a][b][k] > 0:
                print(champdict.champions[k] + ': ' + str(matchesplayed[a][b][k]))

