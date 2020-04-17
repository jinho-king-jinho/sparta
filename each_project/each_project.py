# import requests
# from bs4 import BeautifulSoup
#
# 타겟 URL을 읽어서 HTML를 받아오고,론

# -----지니
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)
#
# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
# soup = BeautifulSoup(data.text, 'html.parser')
#
# music_info_genie = soup.select('#body-content > div > div > table > tbody > tr')
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# # print(music_title)
# rank = 0
# for music_el in music_info_genie :
#     music_title = music_el.select('td.info > a.title.ellipsis')
#     music_singer = music_el.select('td.info > a.artist.ellipsis')
#     music_name = music_title[0].text.lstrip()
#     music_artist = music_singer[0].text.lstrip()
#     rank +=1
#     print(rank, '.', music_name, '-' ,music_artist)

# -----------멜
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/index.htm',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music_info_mellon = soup.select('#lst50')
# print(music_info_mellon)
rank= 0
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a
#lst50 > td:nth-child(8) > div > button > span.cnt
for music_el_mellon in music_info_mellon :
    music_title = music_el_mellon.select('td > div > div > div.ellipsis.rank01 > span > a')
    music_singer = music_el_mellon.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
    music_like = music_el_mellon.select('td:nth-child(8) > div > button > span.cnt')
    # print(music_like)
    # ------
    music_name = music_title[0].text
    music_artist = music_singer[0].text
    music_heart = music_like[0].text.split("총건수")[1].lstrip()
    rank+=1
    print(rank, music_name, music_artist, music_heart)

    # print(rank, music_name, music_artist, music_heart)
