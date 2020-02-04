"""
@author: luciasuelves
"""
from argparse import ArgumentParser

def parser():
    # Create ArgumentParser object
    parser = ArgumentParser(description="Filtering happy Api dataframe")
    parser.add_argument("-Country",type=str, nargs="+", help='Enter as many countries as you want')
    parser.add_argument("-Variables",type=str, nargs="+", help='Enter variables you want to explore, ex: Overall rank, Generosity, GDP per capita, Average temperature')
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-mean", dest="oper", action='store_true', help='Enter -mean to study mean of variables and countries ')
    args = parser.parse_args()
    return (args.Country, args.Variables, args.oper)