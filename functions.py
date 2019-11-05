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

def get_ncaab_historical_betting_data():
  data = pd.read_csv('ncaa basketball 2018-19.csv', delimiter=',')

def get_ncaab_advanced_statistivs(year=''):
  if year == '':
    url = 'https://kenpom.com/index.php?y=' + year
    page = requests.get(url)
  else:
    page = requests.get('https://kenpom.com/index.php')
  pagetext = page.text
  soup = BeautifulSoup(pagetext, 'html.parser')
  temp_stats = []
  for row in soup.find_all('tr'):
    count = 0
    temp = {}
    for col in row.find_all('td'):
      if count == 0:
        temp['adj_em_rank'] = int(col.text)
      elif count == 1:
        temp['team'] = str(col.text)
      elif count == 4:
        temp['adj_em'] = float(col.text)
      elif count == 5:
        temp['adj_o'] = float(col.text)
      elif count == 6:
        temp['adj_o_rank'] = int(col.text)
      elif count == 7:
        temp['adj_d'] = float(col.text)
      elif count == 8:
        temp['adj_d_rank'] = int(col.text)
      count = count + 1
    if len(temp) > 1:
      temp_stats.append(temp)
  return pd.DataFrame(temp_stats)

