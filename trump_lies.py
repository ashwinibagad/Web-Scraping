import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

soupobject = BeautifulSoup(response.text, 'html.parser')

#soupobject -- examines and understands the HTML code that has been parsed

lies = soupobject.find_all('span', attrs={'class':'short-desc'})

trump_lies=[]
for event in lies:
    date=event.find('strong').text[:-1]
    lie=event.contents[1][1:-2]
    exp=event.find('a').text[1:-1]
    url=event.find('a')['href']
    trump_lies.append((date,lie,exp,url))

df = pd.DataFrame(trump_lies,columns=['Date','Lie','Actual Truth', 'Link of Proof'])

df.columns= ['Date','Lie','Actual Truth', 'Link of Proof']

df.head()
