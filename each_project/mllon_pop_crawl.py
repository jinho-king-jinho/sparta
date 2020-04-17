
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.




headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0900#params%5BgnrCode%5D=GN0900&params%5BdtlGnrCode%5D=GN0901&params%5BorderBy%5D=POP&params%5BsteadyYn%5D=N&po=pageObj&startIndex=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music_info_mellon_pop = soup.select('#frm > div > table > tbody > tr')
rank= 0

for music_el_mellon_pop in music_info_mellon_pop :
    music_title = music_el_mellon_pop.select('div.ellipsis.rank01 > span > a')
    music_singer = music_el_mellon_pop.select('div.ellipsis.rank02 > a')
    music_like = music_el_mellon_pop.select('div > table > tbody > tr > td > div > button > span.cnt')
    # print(music_like)
    # ------
    music_name = music_title[0].text
    music_artist = music_singer[0].text
    music_heart = music_like[0].text.split("총건수")[1].lstrip()
    rank+=1
    # db.users.insert_one({'name': 'john', 'age': 30})
    db.mellon_pop_crawl.insert_one({'rank': rank, 'title': music_name, 'singer': music_artist})
    print(rank, music_name, music_artist, music_heart)

