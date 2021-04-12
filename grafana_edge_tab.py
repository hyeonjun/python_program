from threading import Thread
import threading
import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import sys

a=0
#b=0
b=[]
driver=None
options=None
threadList=[]
class ControlThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__stop = False
		self.__exit = False
		print("autoTabTransform")
	def run(self):
		global dirver, options
		while True:
			while self.__stop:
				print("auto tab stopping")
				time.sleep(1)

			if self.__stop == False:
				global a,b
				print("auto tab starting")
				try:
					for i in b:
						driver.switch_to.window(window_name=driver.window_handles[i])
						driver.refresh()
						if(check_Login_path()):
							time.sleep(2)
						else:
							time.sleep(2)
						if(reConnection(i)):
							time.sleep(2)
						else:
							time.sleep(2)
				except IndexError:
					driver.switch_to.window(window_name=driver.window_handles[1])
					continue

				# try:
				# 	# 	   0 1 2 3
				# 	# b = [1,2,3,4]

				# 	if(b==0):
				# 		b=b+1
				# 	elif (b>=1):
				# 		b=b+1
				# 		if(b>=a):
				# 			b=1
				# 	print("trans index : "+ str(b))				
				# 	driver.switch_to.window(window_name=driver.window_handles[b])
				# 	driver.refresh()
				# 	if(check_Login_path()):
				# 		driver.refresh()
				# 		time.sleep(2)
				# 	else:
				# 		driver.refresh()
				# 		time.sleep(2)
				# 	if(reConnection()):
				# 		time.sleep(2)
				# 	else:
				# 		time.sleep(2)		
				# except IndexError:
				# 	print("Error : curruent index -> " + str(b))
				# 	b=1
				# 	driver.switch_to.window(window_name=driver.window_handles[b])
				# 	driver.refresh()
				# 	if(check_Login_path()):
				# 		driver.refresh()
				# 		time.sleep(2)
				# 	else:
				# 		driver.refresh()
				# 		time.sleep(2)
				# 	if(reConnection()):
				# 		time.sleep(2)
				# 	else:
				# 		time.sleep(2)
			if self.__exit:
				print("Auto Tab transform exit...")
				break
	def suspend(self):
		self.__stop = True
	def restart(self):
		self.__stop = False
	def exit(self):
		self.__exit = True


# class KeyboardThread(threading.Thread):
# 	def __init__(self):
# 		threading.Thread.__init__(self)
# 		self.__exit = False
# 		print("keyboard checking")
# 	def run(self):
# 		global dirver, threadList, b, a
# 		while True:
# 			time.sleep(0.05)
# 			if keyboard.is_pressed('F7'):
# 				threadList[0].suspend()
# 				print("stop")
# 				time.sleep(0.05)
# 				continue
# 			if keyboard.is_pressed('F8'):
# 				threadList[0].restart()
# 				print("restart")
# 				time.sleep(0.05)
# 				continue
# 			if keyboard.is_pressed('right'):
# 				threadList[0].suspend()
# 				try:
# 					if(b==1):
# 						b=(a-1)
# 					else:
# 						b=b-1
# 					threadList[0].suspend()
# 					driver.switch_to.window(window_name=driver.window_handles[b])
# 					continue
# 				except IndexError:
# 					print("keyboard error index : " + str(b))
# 					b=1
# 					threadList[0].suspend()
# 					driver.switch_to.window(window_name=driver.window_handles[b])
# 					continue
# 			if keyboard.is_pressed('left'):
# 				threadList[0].suspend()
# 				try:
# 					if(b>=(a-1)):
# 						b=1
# 					else:
# 						b=b+1
# 					threadList[0].suspend()
# 					driver.switch_to.window(window_name=driver.window_handles[b])
# 					continue
# 				except IndexError:
# 					print("keyboard error index : " + str(b))
# 					b=1
# 					threadList[0].suspend()
# 					driver.switch_to.window(window_name=driver.window_handles[b])
# 					continue
# 			if keyboard.is_pressed('esc'):
# 				print('exit?')
# 				time.sleep(2)
# 				if keyboard.is_pressed('esc'):
# 					print('bye')
# 					time.sleep(0.1)
# 					threadList[0].exit()
# 					threadList[1].exit()
# 					driver.quit()
# 				else:
# 					continue
# 			if keyboard.is_pressed('F9'):
# 				print("Program Restart?")
# 				time.sleep(2)
# 				if keyboard.is_pressed('F9'):
# 					print("Restart Okay")
# 					threadList[0].suspend()
# 					time.sleep(5)
# 					driver.quit()
# 					whether = False
# 					AutoTabStart(whether)
# 				else:
# 					continue
# 			if self.__exit:
# 				print("keyboard checking exit...")
# 				break
# 	def exit(self):
# 		self.__exit = True

def check_dashboard_path():
	try:
		global dirver
		search_path='/html/body/grafana-app/sidemenu/div[2]/div[1]/a/span/div'
		driver.find_element_by_xpath(str(search_path)).click()
	except NoSuchElementException:
		return

def check_element():
	try:
		global dirver
		if(driver.find_element_by_xpath('/html/body/grafana-app/div/div/react-container/div/div[1]/div[6]')):
			return True
	except NoSuchElementException:
		return False


def check_search_path():
	global dirver
	search_path='/html/body/grafana-app/sidemenu/div[2]/div[1]/a/span/div'
	try:
		if(driver.find_element_by_xpath(str(search_path)).click()):
			time.sleep(1)
			return True
	except ElementNotInteractableException:
		time.sleep(1)
		if(driver.find_element_by_xpath(str(search_path)).send_keys(Keys.ENTER)):
			return True
		else:
			return False
	except NoSuchElementException:
		time.sleep(1)
		return False

def check_list_path(list_path):
	global dirver
	try:
		if(driver.find_element_by_xpath(str(list_path)).click()):
			time.sleep(1)
			return True
	except ElementNotInteractableException:
		time.sleep(1)
		if(driver.find_element_by_xpath(str(list_path)).send_keys(Keys.ENTER)):
			return True
		else:
			return False
	except NoSuchElementException:
		time.sleep(1)
		return False

def reConnection(index):
	global dirver
	try:
		time.sleep(1)
		print("reconnection index : " + str(index))
		list_path="/html/body/grafana-app/search-wrapper/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div["+str(index)+"]"
		if(check_element()):
			print('dashboard check complete')
			return True
		elif(check_Login_path()):
			time.sleep(1)
		else:
			if(check_search_path()):
				print('search path checking')
				if(check_list_path(list_path)):
					print('search path and list path check complete!')
					return True
				else:
					print('search path and list path check complete!!')
					return True
			else:
				if(check_list_path(list_path)):
					print('search path and list path check complete!!!')
					return True
				else:
					print('search path and list path check complete!!!!')
					return True
	except NoSuchElementException:
		return False


def check_Login_path():
	global dirver
	try:
		print('check login...')
		time.sleep(1)
		id_path='/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
		if (driver.find_element_by_xpath(str(id_path))):
			print('input ID/PASSWD')
			driver.find_element_by_xpath(str(id_path)).send_keys('admin')
			time.sleep(0.5)
			driver.find_element_by_xpath('/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/div[2]/div[2]/div/div/input').send_keys('a12345!!')
			time.sleep(0.5)
			driver.find_element_by_xpath('/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/button').click()
			return True
	except NoSuchElementException:
		return False
	except ElementNotInteractableException:
		if(driver.find_element_by_xpath('/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/button').send_keys(Keys.ENTER)):
			return True
		else:
			return False
		
	
def early():
	if(check_Login_path()):
		time.sleep(2)
		check_dashboard_path()
		time.sleep(2)
	target=driver.find_elements_by_xpath('/html/body/grafana-app/search-wrapper/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div')
	length=len(target)
	for i in range(length, 0 ,-1):
		dash_path="/html/body/grafana-app/search-wrapper/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div["+str(i)+"]/a"
		OpenTab=driver.find_element_by_xpath(str(dash_path))
		OpenTab.send_keys(Keys.CONTROL+"\n")
	return


def AutoTabStart(whether):
	global a, driver, threadList, options,b
	try:
		if(whether == True):
			early()
			transFormTab=driver.window_handles
			a=len(transFormTab)
			b=[i for i in range(a)[1:]] # [1,2,3,4]
			print(b)
			print(len(b))
			threadList[0].start()
		# elif(whether == False):
		# 	print("chrome restart")
		# 	options=webdriver.ChromeOptions()
		# 	options.add_argument("--no-sandbox")
		# 	driver=webdriver.Chrome('D:\\chromedriver.exe',options=options)
		# 	#driver=webdriver.Edge('D:\\msedgedriver.exe')
		# 	driver.get("http://192.168.110.152:3000")
		# 	time.sleep(5)
		# 	early()
		# 	transFormTab=driver.window_handles
		# 	a=len(transFormTab)
		# 	b=[i for i in range(a)[1:]] # [1,2,3,4]
		# 	print(b)

		# 	threadList[0].restart()
		whether=""
	except NoSuchElementException:
		return
	


def main():
	global options, driver, threadList
	options=webdriver.ChromeOptions()
	options.add_argument("--no-sandbox")
	driver=webdriver.Chrome('C:\\chromedriver.exe',options=options)
	#driver=webdriver.Edge('D:\\msedgedriver.exe')
	driver.get("http://192.168.110.152:3000")
	th = ControlThread()
	time.sleep(0.5)
	# kt = KeyboardThread()
	# time.sleep(0.5)
	threadList.append(th)
	# threadList.append(kt)
	whether = True
	AutoTabStart(whether)


if __name__ == '__main__':
	main()