"""
@author: luciasuelves
"""

import requests
from bs4 import BeautifulSoup

def country_code(country):
    try:
        country_data = requests.get(f"https://restcountries.eu/rest/v2/name/{country}?fullText=true").json()
        return[country['alpha3Code'] for country in country_data][0]
    except:
        return None

#I changed the code null values to the real ones, the API could not find
def replace_code(happy_data, correction):
    for (country, code) in correction:
        happy_data.loc[happy_data['Country or region'] == country, 'Code'] = code
    return happy_data.head()


def suicide_rate(row):
    try:
        info = row.find_all('td')
        return {
            'Country': info[1].select('a[href][title]')[0].text,
            'Continent': info[2].text.strip(),
            'Suicide per 1000': info[3].text.strip()
        }
    except:
        return None
    
def suicides():
    res = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate")
    soup = BeautifulSoup(res.text,'html.parser')
    table = soup.find_all('tbody')[3]
    rows = table.find_all('tr')
    return [suicide_rate(row) for row in rows][2:]

def what(happy_data, country, suicidals):
    try: 
        suicide = suicidals.loc[suicidals['Country'] == country]['Suicide per 1000'].iloc[0]
        continent = suicidals.loc[suicidals['Country'] == country]['Continent'].iloc[0]
        happy_data.loc[happy_data['Country or region'] == country, 'Suicide per 1000'] = suicide
        happy_data.loc[happy_data['Country or region'] == country, 'Continent'] = continent
        print(continent, suicide)
        print(happy_data.loc[happy_data['Country or region'] == country]['Suicide per 1000'])
        return (happy_data.loc[happy_data['Country or region'] == country]['Continent'])
    except:
        happy_data.loc[happy_data['Country or region'] == country, 'Suicide per 1000'] = None
        return None
    