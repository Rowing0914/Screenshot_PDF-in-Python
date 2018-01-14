"""
openChrome
make another directory
take scrrenshot of ML ppt
save them in directory
combine all png to one
"""

import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# take a screenshot
def screenshot(filename):
	pyautogui.screenshot(region=(200,130,1000,700)).save(filename)
	return True

# open Chrome with specific url and take a sceenshot until the last page
def openChrome(url, pages, img_path, count):
	if count < 1:
		driver = webdriver.Chrome()
	driver.get(url)
	driver.switch_to_window(driver.window_handles[-1])
	action = ActionChains(driver)
	action.key_down(Keys.SPACE)
	for i in range(1, pages+1):
		action.perform()
		sleep(1)
		while screenshot(img_path + str(i)+'.png') != True:
			screenshot(img_path + str(i)+'.png')

# make directory
def mkDir(dirname, marker):
	path = str(dirname) + str(marker)
	if os.path.exists(path):
		return path + '/'
	else:
		os.mkdir(path)
		return  path + '/'

if __name__ == '__main__':

	pages = [88, 83, 113, 60, 73, 61, 36, 14, 40, 43, 64, 47, 38, 68, 47, 48, 44, 53, 59, 56, 61, 33, 53]
	# openChrome(url="http://nineties.github.io/prml-seminar/7.html#/", pages=pages)

	for a in range(0,23):
		img_path = mkDir(dirname='/Users/user/Desktop/captures/lecture_', marker=str(a+1))
		url = "http://nineties.github.io/prml-seminar/" + str(a+1) + ".html#/"
		openChrome(url=url, pages=int(int(pages[a]) + 20), img_path=img_path, count=a)
	driver.close()
