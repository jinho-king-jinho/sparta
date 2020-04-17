from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "/Users/JINHO/OneDrive - Moe, Inc/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0900#params%5BgnrCode%5D=GN0900&params%5BdtlGnrCode%5D=GN0901&params%5BorderBy%5D=POP&params%5BsteadyYn%5D=N&po=pageObj&startIndex=1")


loca = driver.find_element_by_class_name('last on')
loca.click()

source = driver.page_source