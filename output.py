""" 
@author: luciasuelves
"""
import pandas as pd

happy_enriched = pd.read_csv('happy_data_enriched.csv', engine = 'python')

def get_df(countries, variables):
    variables= ['Country or region'] + variables
    print(pd.concat([happy_enriched[happy_enriched['Country or region'] == country][variables] for country in countries]))

def get_mean(country, variables, oper):
    #devolver dataframe con la media de las variables, si hay paises considerar paises si no del total
    if country:
        df = pd.concat([happy_enriched[happy_enriched['Country or region'] == c] for c in country])
        mean = [{variable + " mean": df[variable].mean()
                } for variable in variables]
        print(mean)
    else:
        mean = [{variable + " mean": happy_enriched[variable].mean()
                } for variable in variables]
        print(mean)
