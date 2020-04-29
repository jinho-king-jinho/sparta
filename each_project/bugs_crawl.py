import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

db.bugs_korea_crawl.drop()
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://music.bugs.co.kr/chart',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music_info_bugs_korea = soup.select('#CHARTrealtime > table > tbody > tr')
# print(music_info_mellon)
rank= 0
like= 0
#CHARTrealtime > table > tbody > tr:nth-child(1) > th > p > a
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a
#lst50 > td:nth-child(8) > div > button > span.cnt
for music_el_bugs_korea in music_info_bugs_korea :
    music_title = music_el_bugs_korea.select('th > p.title > a')
    music_singer = music_el_bugs_korea.select('td > p > a')

    music_name = music_title[0].text
    music_artist = music_singer[0].text
    # music_heart = music_like[0].text.split("총건수")[1].lstrip()
    rank+=1
    print(rank, music_name, music_artist, like)
    db.bugs_korea_crawl.insert_one({'rank': rank, 'title': music_name, 'singer': music_artist, 'like': like})
