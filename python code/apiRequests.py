"""
@author: luciasuelves
"""
import requests

#New column with average anual temperature 2012 (could not find data for 2019)
def temperature(code):
    try:
        temp_resp =  requests.get(f"http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/{code}.json").json()
        return [temp['data'] for temp in temp_resp if temp['year'] == 2012][0]
    except: 
        return None

def precipitations(code):
    try:
        temp_resp =  requests.get(f"http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/pr/year/{code}.json").json()
        return [temp['data'] for temp in temp_resp if temp['year'] == 2012][0]
    except: 
        return None