import requests
TOKEN = "2619421814940190"
BASE_URL = "https://superheroapi.com/api/" + TOKEN
heros = ["Hulk", "Captain America", "Thanos"]
max_intelligence = 0
max_intelligence_name = ""
for hero in heros:
    url = BASE_URL + "/search/" + hero
    response = requests.get(url).json()
    hero_intelligence = int(response["results"][0]["powerstats"]["intelligence"])
    print("Hero:", hero, " / Intelligence:", hero_intelligence)
    if hero_intelligence > max_intelligence:
        max_intelligence = hero_intelligence
        max_intelligence_name = hero
print("------------------------------------")
print("Winner:", max_intelligence_name, " / Intelligence:", max_intelligence)