"""
@author: luciasuelves
"""
import pandas as pd
from parser import parser
from output import get_df, get_mean
from shootMail import send_mail

happy_enriched = pd.read_csv('../input/happy_data_enriched.csv', engine = 'python')

#Plots 
[happy_enriched.plot(x = 'Overall rank', y = variable, kind = 'scatter') for variable in ['Average Temperature', 'Average Precipitations','Suicide per 1000', 'Olympic medals']]

#Get a smaller df with a representative country for each continent to send mail
sub_happy = pd.concat([happy_enriched.loc[happy_enriched['Country or region'] == country] for country in ["Spain","United States","Australia","Burundi","China"]])
sub_happy = sub_happy[['Country or region', 'Overall rank', 'Score', 'GDP per capita', 'Social support', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Suicide per 1000', 'Average Temperature', 'Average Precipitations']]
sub_happy

#send mail
to = input("Who do you want to send an email to?: ")
send_mail(sub_happy, to)

    
if __name__ == "__main__":
    country, variables, oper = parser()
    if oper:
        get_mean(country, variables, oper)
    else:
        get_df(country, variables)

    