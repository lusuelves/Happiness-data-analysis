"""
@author: luciasuelves
"""
from argparse import ArgumentParser

def parser():
    # Create ArgumentParser object
    parser = ArgumentParser(description="Filtering happy Api dataframe")
    parser.add_argument("-Continent",type=str, nargs=1)
    parser.add_argument("-Country",type=str, nargs="+")
    parser.add_argument("-Variables",type=str, nargs="+")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-mean", dest="oper", action='store_true')
    args = parser.parse_args()
    return (args.Country, args.Variables, args.oper)