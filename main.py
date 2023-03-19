from weatherdata import getWeatherData
from jsonFunctions import read
from newsGetter import getpage
import time

town = read('data.json')['town']
api = read('data.json')['api']
rss = read('data.json')['rssLink']


while True:


    data = getWeatherData(api, town)
    print(f"\n\n\nThe temperature in {town}: {data[0]}")
    print(f"The atmospheric pressure is {data[1]}")
    print(f"{data[2]}% humidity")
    print(f"Description: {data[3]}")
    articles = getpage(rss)
    for article in articles:
        print(f"{article['title']}\n")
    time.sleep(60)