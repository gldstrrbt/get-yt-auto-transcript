import sounddevice as sd
import numpy as np
import time, os
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import _find_element
import selenium.webdriver.common.action_chains
from selenium.webdriver.common.action_chains import ActionChains



# https://www.youtube.com/results?search_query=ted+cruz&page=&utm_source=opensearch
# https://www.youtube.com/results?search_query=ted+cruz&sp=EgIoAQ%253D%253D

# https://www.youtube.com/results?search_query=cory+booker
# https://www.youtube.com/results?search_query=cory+booker

# ADD AT END OF URL TO FILTER FOR CLOSED CAPTIONS &sp=EgIoAQ%253D%253D

def enter_query():
	print("Enter a public figure's name: ")
	a = input()
	return a

def load_video_results(name_query):
	scroll_counter 	= 0
	driver 			= webdriver.Firefox(executable_path="./geckodriver")
	a 				= name_query.replace(" ", "+").lower()
	b 				= "https://www.youtube.com/results?search_query=" + str(a) + "&sp=EgIoAQ%253D%253D"
	driver.get(b)
	SCROLL_PAUSE_TIME = 1

	time.sleep(2)
	# Get scroll height
	last_height = driver.execute_script("return document.body.scrollHeight")

	while scroll_counter < 10:
		print(scroll_counter)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(SCROLL_PAUSE_TIME)
		new_height = driver.execute_script("return document.body.scrollHeight")
		last_height = new_height
		scroll_counter+=1
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	time.sleep(1)
	c = driver.page_source
	return c

def get_results_entries(page_source):
	a = soup(page_source)
	b = a.findAll("a", {"id": "video-title"})
	return b

def get_results_hrefs(entries):
	a = []
	for b in entries:
		try:
			if len(b["title"]) > 0:
				a.append({"title":b["title"], "href":b["href"]})
		except:
			pass
	return a

# def get_video_menu():
# 	# https://www.youtube.com/watch?v=niOcdMl_0fQ
# 	# https://www.youtube.com/results?search_query=ted+cruz&sp=EgIoAQ%253D%253D
# 	a = "button"
# 	a.click()
# 	element_tag_name = "yt-formatted-string"
# 	if element_tag_name.text == "Open transcript":
# 		continue

def youtube_dl():
	a = "https://www.youtube.com"
	b = open("ted_cruz_yt.txt", "r+")
	for c in b:
		print(str(a) + str(c))
		os.system("youtube-dl --write-auto-sub " + str(a) + str(c))

def init():
	# a = enter_query()
	# b = load_video_results(a)
	# c = get_results_entries(b)
	# d = get_results_hrefs(c)
	# print(d)
	youtube_dl()

init()

# def get_transcription_button():

# def check_auto_transcription():




# <ytd-menu-service-item-renderer role="menuitem" class="style-scope ytd-menu-popup-renderer" tabindex="0">
	
#     <paper-item class="style-scope ytd-menu-service-item-renderer" role="option" tabindex="0" aria-disabled="false">
	
	
#       <yt-icon class="style-scope ytd-menu-service-item-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
#         <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zM4 12h4v2H4v-2zm10 6H4v-2h10v2zm6 0h-4v-2h4v2zm0-4H10v-2h10v2z" class="style-scope yt-icon"></path>
#       </g></svg>
	
	
#   </yt-icon>
#       <yt-formatted-string class="style-scope ytd-menu-service-item-renderer">Open transcript</yt-formatted-string>
	
#   </paper-item>
#   </ytd-menu-service-item-renderer>