import requests
import json
import champdict

api_key = 'RGAPI-5478c4a3-e795-497b-9463-19f2a3c723e4'

tier = 'IRON'
division = 'IV'

players = requests.get('https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{division}?page=1&api_key={key}'.format(key=api_key,tier=tier,division=division))
playersdata = players.json()

for i in playersdata[:9]:
    summoner = i["summonerName"]
    account = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{sum}?api_key={key}'.format(key=api_key,sum=summoner))
    accountdata = account.json()
    accountid = accountdata["accountId"]
    response = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{id}?api_key={key}'.format(key=api_key,id=accountid))
    data = response.json()
    
    for i in data["matches"]:
        match_id = i["gameId"]
        print(match_id)