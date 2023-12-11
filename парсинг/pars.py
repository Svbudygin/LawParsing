import pickle
import requests
from bs4 import BeautifulSoup

URL = "https://pravorub.ru/users/stat/prices/"
respones = requests.get(URL)
respones = respones.content
soup = BeautifulSoup(respones, "html.parser")
soup = soup.find("div", {"class": "panel-body"}).find_all("a")

names = list(map(lambda x: x.text.replace("Средняя стоимость услуг Адвокатов и Юристов в ", ""), soup))
links = list(map(lambda x: x.get("href"), soup))
d = {}
for i in range(len(names)):
    d[names[i]] = links[i]
print(d)
with open('dict_all_web', 'wb') as f:
    pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)

