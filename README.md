# Happiness-data-analysis

In this project we study variables that may have an effect on happiness index for countries.
The variables that determine happiness index by countries are:
    -GDP per capita
    -Generosity
    -Freedom to make life choices
    -Perceptions of corruption
    -Healthy life expectancy
    -Social support
I have studied the correlation between happiness and the following:
    -Average temperature
    -Average precipitations
    -Suicide per 1000
    -Medals won in 2016 olimpic games.

## Packages 

I have used python packages such as: pandas, requests, numpy, dotenv, sendgrid, smtplib. You can install them from the command line using the following commands: 

```bash
pip install pandas
```

```bash
pip install requests
```

```bash
pip install dotenv
```

```bash
pip install sendgrid
```

The only API that requires token is sengrid, you can get your api key here: 
the free plan allows for 40k emails per day.

## Usage

With this dataframe you can compare factors to see if there is any correlation between them. For example 

```python
happy_data.plot(x = 'Overall rank', y = 'Healthy life expectancy', kind = 'scatter') # returns scatter plot comparing Happiness score and Health life expectancy of countries
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

If you think of another factor that may determine happiness index of countries feel free to add another column to the dataframe and study its effect by using plots or other statistics resources.
