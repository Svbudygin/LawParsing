import pickle

import numpy as np

with open('prices', 'rb') as f:
    d_pr = pickle.load(f)
d_pr = list(d_pr.items())
d_pr = list(map(lambda x: (x[0].split()[0], int(x[1])), d_pr))
print(d_pr)
with open('salaries', 'rb') as f:
    d_sal = list(pickle.load(f).items())

corr = {}
lst = []
z = 0
for i, e in enumerate(d_pr):
    for x, y in enumerate(d_sal):
        if e[0] == y[0]:
            corr[e[0]] = round(e[1] / y[1] * 100)
            lst.append((e[1], y[1]))
print(lst)
import plotly.express as px

y_data ,x_data = zip(*lst)

fig = px.scatter(x=x_data, y=y_data, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Scatter Plot',
                 trendline="ols")

fig.show()
import plotly.express as px

# Ваши данные
data = lst
percentages = [(price / salary) * 100 for price, salary in data]

# Разделение данных на два списка: x (цена услуги) и y (проценты)
x_data, y_data = zip(*[(price, percentage) for (price, _), percentage in zip(data, percentages)])

# Создание scatter plot с процентами
fig = px.scatter(x=x_data, y=y_data, labels={'x': 'Цена услуги', 'y': 'Проценты от средней зарплаты'},
                 title='Отношение цены услуги к средней зарплате в процентах')

# Вычисление среднего процента
average_percentage = np.mean(percentages)

# Добавление линии для среднего процента с аннотацией
fig.add_annotation(
    x=min(x_data),
    y=average_percentage,
    xref='x',
    yref='y',
    text='Средний процент',
    showarrow=True,
    arrowhead=5,
    ax=0,
    ay=-40
)
fig.add_shape(
    type='line',
    x0=min(x_data),
    x1=max(x_data),
    y0=average_percentage,
    y1=average_percentage,
    line=dict(color='red', width=2, dash='dash'),
    name='Средний процент',
)

# Отображение графика
fig.show()
# # Вычисление процентов
# percentages = [(price / salary) * 100 for price, salary in data]
#
# # Разделение данных на два списка: x (цена услуги) и y (проценты)
# x_data, y_data = zip(*[(price, percentage) for (price, _), percentage in zip(data, percentages)])
#
# # Создание scatter plot с процентами
# fig = px.scatter(x=x_data, y=y_data, labels={'x': 'Цена услуги', 'y': 'Проценты от средней зарплаты'},
#                  title='Отношение цены услуги к средней зарплате в процентах',trendline="ols" )
#
# # Отображение графика
# fig.show()
# percentages = [(price / salary) * 100 for price, salary in data]
#
# # Разделение данных на два списка: x (цена услуги) и y (проценты)
# x_data, y_data = zip(*[(price, percentage) for (price, _), percentage in zip(data, percentages)])
#
# # Создание scatter plot с процентами
# fig = px.scatter(x=x_data, y=y_data, labels={'x': 'Цена услуги', 'y': 'Проценты от средней зарплаты'},
#                  title='Отношение цены услуги к средней зарплате в процентах',trendline="ols")
#
# # Вычисление среднего процента
# average_percentage = np.mean(percentages)
#
# # Добавление линии для среднего процента
# fig.add_shape(
#     type='line',
#     x0=min(x_data),
#     x1=max(x_data),
#     y0=average_percentage,
#     y1=average_percentage,
#     line=dict(color='red', width=2, dash='dash'),
#     name='Средний процент',
#     text=['Средний процент'],
#     textposition='bottom center'
# )
#
# # Отображение графика
# fig.show()
