from selenium import webdriver
import os
from os import listdir
from os.path import isfile, join

from tqdm import tqdm
import json
import sys

# 輸入PDF保存的路徑
mypath = os.getcwd()
if not os.path.isdir(mypath+'/pdf'):
    os.mkdir(mypath+"/pdf")
files = [join(mypath+'/html', f) for f in listdir(mypath+'/html') if isfile(join(mypath+'/html', f)) and f[-5:] == '.html']

PDF_savepath = mypath+"/pdf"
chrome_options = webdriver.ChromeOptions()
appState = {
   'recentDestinations': [
      {
           'id': 'Save as PDF',
           'origin': 'local',
           'account': ''
      }
  ],
   'selectedDestinationId': 'Save as PDF',
   'version': 2,
   "isHeaderFooterEnabled": False
}
prefs = {
   'printing.print_preview_sticky_settings.appState': json.dumps(appState), 
   'savefile.default_directory': PDF_savepath
}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
# 輸入chromedriver的路徑
for f in files:
    driver = webdriver.Chrome(
       r'./chromedriver', options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(f'file://{f}')
    driver.execute_script('window.print();')
    driver.close()
