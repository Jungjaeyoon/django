import requests

servicekey = 'frADo038kgfNyLptLgZuTcL+yP+C0Q63TpqFJEiLZzuHThgvUgb8LuLEd9kIdfOrSP0TA4lYbWqzqQRlxtSyGg=='



import requests

url = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList'
params ={'serviceKey' : servicekey, 'stationId' : '200000078' }

response = requests.get(url, params=params)
print(response.content)f