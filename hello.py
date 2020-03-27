import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################

movie_title = soup.select('#old_content > table > tbody > tr > td >div.tit5')[0].text
print(movie_title)
# for movie in movie_title :
#     title = movie.text
#     print(title)
# 왜 그냥 치면 나오고 저렇게 안 안들어가서 치면 안나오
# movie_title = soup.select('div.tit5')

# movie_title = soup.select('#old_content > table > tbody > tr')
# # print(movie_title)
# rank = 0
# for movie in movie_title :
#     title_el = movie.select('a')
#     point_el = movie.select('td.point')
#     if len(title_el) > 0 :
#         title = title_el[0].text
#         point = point_el[0].text
#         rank +=1
#         print(rank,'.', title, point)
# #왜 이건 작동안함...(왜 if 안해주면 작동안함?)

