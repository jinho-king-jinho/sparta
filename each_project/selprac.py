import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "/Users/JINHO/OneDrive - Moe, Inc/chromedriver"
driver = webdriver.Chrome(path)
# driver = webdriver.PhantomJS("/Users/JINHO/OneDrive - Moe, Inc/phantomjs-2.1.1-macosx/bin/phantomjs-2.1.1")
driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0900#params%5BgnrCode%5D=GN0900&params%5BdtlGnrCode%5D=GN0901&params%5BorderBy%5D=POP&params%5BsteadyYn%5D=N&po=pageObj&startIndex=1")

# source - driver.page_source

#
# loca = driver.find_element_by_class_name('last on')
# loca.click()

a = driver.find_elements_by_xpath('//*[@id="frm"]/div/div/div/a[2]')
driver.get(a[0].get_attribute('href'))

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
music_info_mellon_pop = soup.slect('#frm > div > table > tbody > tr')

for music_el_mellon_pop in music_info_mellon_pop:
    music_title = music_el_mellon_pop('div.ellipsis.rank01 > span > a')
    music_name = music_title[0].text
    print(music_name)
