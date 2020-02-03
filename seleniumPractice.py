#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:12:00 2020

@author: luciasuelves
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class PageGetter:
    driver = False
    def __init__(self, defaultBrowser='firefox'):
        if defaultBrowser == 'firefox':
            self.driver = webdriver.Firefox()
        elif defaultBrowser == 'chrome':
            self.driver = webdriver.Chrome("/Users/luciasuelves/Downloads/chromedriver") 
        else:
            raise Exception('Not a browser')

    def getPage(self, url):
        if not self.driver:
            raise Exception("You should start a browser connection")
        self.driver.get(url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def close(self):
        self.driver.quit()
        
pg = PageGetter("chrome")
hdr_data = pg.getPage("https://www.bbc.com/sport/olympics/rio-2016/medals/countries")
pg.close()

def find_medal(medal):
    try:
        return {
            "Country": medal.find('abbr')['title'],
            "Medals": medal.select('td.medals-table__total')[0].text.strip()
        }
    except: 
        return None
    
def medals(happy_data, country):
    medals = hdr_data.find_all('table')[0].find_all('tr')[1:]
    table = pd.DataFrame([find_medal(medal) for medal in medals])
    try: 
        medal = table.loc[table['Country'] == country]['Medals'].iloc[0]
        happy_data.loc[happy_data['Country or region'] == country, 'Olympic medals'] = medal
        return happy_data.loc[happy_data['Country or region'] == country]
    except:
        happy_data.loc[happy_data['Country or region'] == country, 'Suicide per 1000'] = None
        return None