import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.cricbuzz.com/profiles/25/sachin-tendulkar')

soupobject = BeautifulSoup(response.text, 'html.parser')
Journey_of_Sachin = soupobject.find_all('div', attrs={'class':'cb-plyr-tbl'})
total_matches_played=Journey_of_Sachin[0].find_all('td', attrs={'class':'cb-plyr-tbody text-right'})
total_matches = 0
for matches in total_matches_played:
  total_matches = total_matches + int(matches.text)

print("Total number of matches played by Sachin Tendulkar:", total_matches)
