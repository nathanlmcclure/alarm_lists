from asyncore import write
from re import S
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv

#The resulting CSV will write to the current directory in your terminal's window
#The file path to your geckodriver.exe file will need to be updated.
#Make sure it's in the main Python directory so that it's included in your PATH variable

s=Service("C:/Python39/geckodriver.exe")
browser = webdriver.Firefox(service=s)
login_url = 'https://cloud.vendor1.com/signin'

u_name = input('Enter your username: ')
p_word = input('Enter your password: ')

browser.get(login_url)
sleep(3)

# Locate the username field on the page, then submit the user's entry

username=browser.find_element(By.XPATH,"//input[@name='email']")
username.send_keys(u_name)
sleep(1)
username.submit()
sleep(1)

#After submitting the username, the page defaults the cursor to the password field

action = ActionChains(browser)
action.send_keys(p_word)
action.send_keys(Keys.ENTER)
action.perform()
sleep(5)

#Each region has its own shutdown alarm list, and each list contains unit numbers assigned to that region
#Create one array of the list ID's, and another to store the list names and unit numbers

regional_list_ids = [193456,354567,195678,192345,190123,269012]
big_list = []

for id in regional_list_ids:

    url = "https://cloud.vendor1.com/o/1234/industry/conf/alarms/edit/"+str(id)+"?alert_category=data_input"

    browser.get(url)
    sleep(10)

#Locate the tile with the list title and append the list name to big_list.  Then, locate the
#unit numbers in the Alert Object tiles and append them.

#Adding an empty value before each list title leaves an empty space in the first column of
#the CSV when it gets written.  That makes it easier to navigate the long lists in Excel.

    list_title = browser.find_element(By.CLASS_NAME,"InlineEditTitle-input")
    list_title_text = list_title.get_attribute('value')
    header_text = ['',list_title_text]
    big_list.append(header_text)

    try:
        html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div', class_='AlertObjectPill-title'):
            input_name = item.text
            first_space = input_name.find(' ')
            gen = input_name[:first_space]
            big_list.append([gen])
    except TimeoutException:
        print('Page Timed Out!')
    except:
        print('An error occurred')
        browser.close()

#print(big_list)

with open('Regional_Shutdown_Alert_Lists.csv','w', newline='') as output:
    writer = csv.writer(output)
    for ind in big_list:
        writer.writerows([ind])


browser.close()