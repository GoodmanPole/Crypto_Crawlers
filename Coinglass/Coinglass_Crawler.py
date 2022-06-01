import json

import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup


# Setting up the soup object
url='https://fapi.coinglass.com/api/exchange/chain/balance/list'


dataDict=json.loads(requests.get(url).content)["data"]

df= pd.DataFrame(dataDict)

df.to_csv('Coinglass.csv')

print(df)




