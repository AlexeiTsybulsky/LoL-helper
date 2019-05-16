import requests
import json
from numpy import zeros
import champdict

response = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/YVkEoQp6Jk5pP7mJDnPYMf2NnHWccRYBrIv5LcIjtVFN8c8?api_key=RGAPI-5478c4a3-e795-497b-9463-19f2a3c723e4')
data = response.json()

matchesplayed = zeros([600],dtype=int)

for i in data["matches"]:
    x = i["champion"]
    matchesplayed[x] = matchesplayed[x] + 1

for i in champions:
    if matchesplayed[i] > 0:
        print(champdict.champions[i] + ': ' + str(matchesplayed[i]))