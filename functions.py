#### Import Necessary Libraries ####
import json
import requests
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib as plt
import sklearn as skl
import sportsreference.ncaab.teams as ncaab
import sportsreference.ncaaf.teams as ncaaf
import sportsreference.nfl.teams as nfl
import sportsreference.nba.teams as nba
import sportsreference.mlb.teams as mlb
from bs4 import BeautifulSoup
import requests
import csv

#### Function Definitions Below ####
def get_average_possessions(year):
  teams = ncaab.Teams(year)
  total = 0
  for x in teams:
    total = total + x.pace
  return (total / len(teams))

def get_ncaab_historical_data():
  
