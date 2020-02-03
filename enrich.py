"""
@author: luciasuelves
"""
import pandas as pd
from isoCode import country_code, suicides, what
from hola import replace_code, temperature, precipitations
from seleniumPractice import medals

#Import happy data API, already clean
happy_data = pd.read_csv('Happy2019.csv', engine = 'python')

#Add Code country column, to use code and search in temperature Api
countries = happy_data['Country or region']
happy_data['Code'] = [country_code(country) for country in countries]

#Countries of which we could not find the ISO code, we look for it and change it 
null_codes = happy_data[happy_data['Code'].isnull() == True]['Country or region'].tolist()
real_code = ["GBR","USA", "TTO", "RKS", "KOR", "BOL", "CYP", "RUS", "MDA", "MKD", "VNM","COD","VEN","PSE","IRN","COD","SYR","TZA"]
correction = zip(null_codes,real_code)
replace_code(happy_data, correction)

#Add column for average temperature
codes = happy_data['Code'].tolist()
temperatures = [temperature(code) for code in codes]
happy_data['Average Temperature'] = temperatures
happy_data.head()

#Add column for average precipitations
precipitations = [precipitations(code) for code in codes]
happy_data['Average Precipitations'] = precipitations

#Add column for suicide rate using web scraping
suicides()
suicidals = pd.DataFrame(suicides())

#Añadir suicides y continent al dataframe
happy_data['Suicide per 1000'] = 0
happy_data['Continent'] = ''
[what(happy_data, country, suicidals) for country in countries]

#Add columns for medals won in the Olympic Games 2016 with selenium
happy_data['Olympic medals'] = 0
[medals(happy_data, country) for country in happy_data['Country or region'].tolist()]

#GroupBy continent and get the mean of overall rank and suicide per 1000
avg_happy = happy_data.groupby('Continent', as_index = False).agg({'Overall rank':'mean'})
avg_happy.columns = ['Continent', 'Avg continent happiness']
happy_data = pd.merge(happy_data, avg_happy, on="Continent")

happy_data["Suicide per 1000"] = pd.to_numeric(happy_data['Suicide per 1000'])
avg_suicide = happy_data.groupby('Continent', as_index = False).agg({'Suicide per 1000':'mean'})
avg_suicide.columns = ['Continent', 'Avg continent suicide']
happy_data = pd.merge(happy_data, avg_suicide, on="Continent")

#Bins para deducir si el nivel de felicidad es alto o bajo
happy_labels = ['Very High','High', 'Moderate', 'Low','Very Low']
bins = pd.cut(happy_data['Overall rank'],[0,35,70,105,140,160], labels=happy_labels)
bins.head(10)
happy_data['Happiness'] = bins

#export
happy_data.to_csv('happy_data_enriched.csv', index=False)


