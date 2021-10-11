import requests
import json
import pandas as pd
from requests.sessions import default_headers


url = "https://covid-19-data.p.rapidapi.com/country"

headers = {
    'x-rapidapi-key': "6b66845ba6mshff843390cdc612bp13dd8cjsna20ccd577cd7",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }



response = requests.request("GET",url,headers=headers,params={"name":"india"}).json()

ds = pd.Series(response)

print(*[x for x in ds.items()])