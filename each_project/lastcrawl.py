import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

#
# # db.geniekoreacrawl.drop()
# # headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# # data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)
# #
# #
# # soup = BeautifulSoup(data.text, 'html.parser')
# #
# # music_info_genie_korea = soup.select('#body-content > div > div > table > tbody > tr')
# # #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# # # print(music_title)
# # rank = 0
# # like = 0
# # for music_el in music_info_genie_korea :
# #     music_title = music_el.select('td.info > a.title.ellipsis')
# #     music_singer = music_el.select('td.info > a.artist.ellipsis')
# #     music_name = music_title[0].text.lstrip()
# #     music_artist = music_singer[0].text.lstrip()
# #     rank +=1
# #     print(rank, '.', music_name, '-' ,music_artist, like)
# #     db.geniekoreacrawl.insert_one({'rank': rank, 'title': music_name, 'singer': music_artist, 'like':like})
#
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)
#
#
# soup = BeautifulSoup(data.text, 'html.parser')
#
#
# # @app.route('/api/delete', methods=['POST'])
# def chart1_delete():
#     # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#     title_receive = request.form["title_give"]
#     # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
#     rank1 = list(db.geniekoreacrawl.find({"title": title_receive}, {"_id": False})

# chart = db.geniekoreacrawl.find_one({"title": title_receive}, {"_id": False})
alist = list(db.mellon_korea_crawl.find({}))

a = []

for n in alist:
    print(n)
    a
    a.append(n)


print(a)

a{}
#
# rank
