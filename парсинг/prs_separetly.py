import pickle
import requests
from bs4 import BeautifulSoup
from random import randint

with open('dict_all_web', 'rb') as f:
    d = pickle.load(f)
print(d)
new_d = {}


def data_get(URL):
    respones = requests.get(URL)
    respones = respones.content
    soup = BeautifulSoup(respones, "html.parser")
    tr_tags = soup.find("table", {"class": "table"}).find_all('tr')[7].find_all('td')[2].text.replace(' ', '')
    return int(tr_tags) + randint(100, 300)


for k, v in d.items():
    try:
        new_d[k] = data_get(v)
    except IndexError:
        print(k, v)
print(new_d)
with open('../prices', 'wb') as f:
    pickle.dump(new_d, f, pickle.HIGHEST_PROTOCOL)
