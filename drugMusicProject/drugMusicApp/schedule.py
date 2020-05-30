import requests
import json

def getSchedule():
    url = 'https://xindieticket.kr/api/performances'
    res = requests.get(url)
    data = json.loads(res.text)
    result =  list(map(parse, data['rows']))
    return result
    # print(data['rows'][0])

def parse(schedule):
    name = schedule['name']
    lineup = schedule['data']['lineup']
    price1 = schedule['price_option']
    price2 = schedule['price_desc']
    link = list(filter(lambda u: len(u) != 0, schedule['data']['reservation_url'].values()))
    if len(link) != 0:
        link = link[0]
    else:
        link = ""
    return {
        "name" : name,
        "lineup" : lineup,
        "link" : link,
        "price1" : price1,
        "price2" : price2
    }