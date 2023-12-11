import pickle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('../prices', 'rb') as f:
    d = pickle.load(f)
regions = d.keys()
salaries = list(d.values())
print(regions)
# -----------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(regions, salaries, color='blue')
plt.xlabel('Регионы')
plt.ylabel('Средняя цена за час')
plt.title('Средняя стоимость услуг Юристов и Адвокатов в регионах')
plt.xticks([])
plt.tight_layout()
for salary in range(1000, 6000, 1000):
    plt.axhline(y=salary, color='gray', linestyle='--', linewidth=0.5)
mean_salary = np.mean(salaries)
plt.plot(regions, [mean_salary] * len(regions), color='red', linestyle='--', linewidth=1, label='Средняя зарплата')
plt.savefig("ср_цены_все.png")
plt.show()
# -----------------------------------------------------------------------------
regions = [
    "Москва", "Московская", "Ленинградская", "Самарская",
    "Санкт-Петербург", "Севастополь", "Татарстан",
    "Приморский", "Калининградская", "Новосибирская"
]
salaries = []
for i in regions:
    if i == "Москва" or i == "Московская":
        salaries.append(d['Москва и Московская область'])
    elif i == "Ленинградская" or i == "Санкт-Петербург":
        salaries.append(d["Санкт-Петербург и область"])
    elif i == "Татарстан":
        salaries.append(d["Республика Татарстан"])
    elif i == "Новосибирская":
        salaries.append(d["Новосибирская область"])
    elif i == "Калининградская":
        salaries.append(d["Калининградская область"])
    elif i == "Приморский":
        salaries.append(d["Приморский край"])
    elif i == "Новосибирская":
        salaries.append(d["Новосибирская область"])
    elif i == "Самарская":
        salaries.append(d["Самарская область"])
    elif i == "Севастополь":
        salaries.append(d["Республика Крым"])
print(salaries)
colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink', 'brown', 'cyan', 'magenta', 'yellow'] * 10

plt.figure(figsize=(10, 6))
bars = plt.bar(regions, salaries, color=colors)
plt.legend(bars, regions, title='Регионы')
plt.xticks([])
for bar, salary in zip(bars, salaries):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(salary), ha='center', va='bottom')
plt.ylabel('Средняя цена за час')
plt.xlabel('Регионы')
plt.title('Средняя стоимость услуг Юристов и Адвокатов в регионах')
plt.tight_layout()
plt.savefig("prices_top10.png")
plt.show()
