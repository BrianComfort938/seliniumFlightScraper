import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import numpy as np
import random
import openpyxl

def findDeals(url):
     s = Service('C:\webdrivers\chromedriver.exe')
     driver = webdriver.Chrome(service=s)

     driver.get(url)
     sleep(5)

     destinationList = []
     priceList = []
     dateList = []


     number = 1
     isWorking = True

     while isWorking == True:
         try:
             destination  = driver.find_element(By.XPATH, f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{number}]/div/div[2]/div[1]/h3').text
             price = driver.find_element(By.XPATH, f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{number}]/div/div[2]/div[2]/div/span/span').text
             date = driver.find_element(By.XPATH, f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{number}]/div/div[2]/div[1]/div[1]').text

             destinationList.append(destination)
             priceList.append(price)
             dateList.append(date)

         except:
             isWorking = False

         number += 1


     pdDataFrame = pd.DataFrame(np.column_stack([destinationList, priceList, dateList]))
     print(pdDataFrame)
     randomNumber = random.randint(1, 1000000000000000)
     pdDataFrame.to_excel(fr'A:\excelFiles\flight deals {randomNumber}.xlsx', index=False)
     print('')
     print(fr'A:\excelFiles\flight deals {randomNumber}')


if __name__=="__main__":
    findDeals(url='https://www.google.com/travel/explore?tfs=CBwQAxoVagcIARIDSkZLEgoyMDIyLTEyLTE4GhUSCjIwMjItMTItMjJyBwgBEgNKRktwAoIBCwj___________8BQAFIAZgBAbIBBBgBIAE&tfu=GiwaKAoSCe2kf-3kLlVAEQAAAAAAgGZAEhIJ6eqV1UW2U8ARAAAAAACAZsAgAw')