import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


path = "/Users/JINHO/OneDrive - Moe, Inc/chromedriver"
driver = webdriver.Chrome(path)
# driver = webdriver.PhantomJS("/Users/JINHO/OneDrive - Moe, Inc/phantomjs-2.1.1-macosx/bin/phantomjs-2.1.1")
driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0900#params%5BgnrCode%5D=GN0900&params%5BdtlGnrCode%5D=GN0901&params%5BorderBy%5D=POP&params%5BsteadyYn%5D=N&po=pageObj&startIndex=1")

# source - driver.page_source

#
# loca = driver.find_element_by_class_name('last on')
# loca.click()

# a = driver.find_elements_by_xpath('//*[@id="frm"]/div/div/div/a[2]')
# driver.get(a[0].get_attribute('href'))
#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > div > div > div.ellipsis.rank01 > span > a

driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
music_info_mellon_pop = soup.select("#frm > div > table > tbody > tr")
rank =0

db.mellon_pop_crawl.remove()

for music_el_mellon_pop in music_info_mellon_pop:
    music_title = music_el_mellon_pop.select('div.ellipsis.rank01 > span > a')
    music_singer = music_el_mellon_pop.select('div.ellipsis.rank02 > a')
    music_like = music_el_mellon_pop.select('div > table > tbody > tr > td > div > button > span.cnt')

    music_name = music_title[0].text
    music_artist = music_singer[0].text
    music_heart = music_like[0].text.split("총건수")[1].lstrip()
    rank += 1
    # print(music_title)
    print(rank, music_name, music_artist, music_heart)


    db.mellon_pop_crawl.insert_one({'rank': rank, 'title': music_name, 'singer': music_artist, 'like': music_heart})
