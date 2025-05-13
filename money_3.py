import matplotlib.pyplot as plt
import numpy as np
import random

# Начальные параметры
initial_users = 3000
premium_rate = 0.01  # 1% пользователей покупают премиум
premium_price = 1000  # Стоимость полугодовой премиум-подписки
ad_companies_initial = 5  # Начальное количество компаний
ad_increase = 2  # Увеличение компаний в месяц
ad_price = 400  # Стоимость рекламы
server_cost = 5000  # Постоянные издержки
months = 12
month_names = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']

# Инициализация списков
users = [initial_users]
premium_revenue = []
ad_revenue = []
total_revenue = []
profit = []
companies = []
active_premium_users = []  # Список для отслеживания активных премиум-подписок

# Расчет за 12 месяцев
for month in range(months):
    # Текущее количество пользователей
    current_users = users[-1]
    
    # Доход от премиум-статусов
    # Новые премиум-пользователи (1% от текущих пользователей)
    new_premium_users = int(current_users * premium_rate)
    
    # Добавляем новых премиум-пользователей
    if month == 0:
        active_premium_users.append(new_premium_users)
    else:
        # Удаляем пользователей, у которых истек срок подписки (те, кто подписался 6 месяцев назад)
        if month >= 6:
            active_premium_users.append(new_premium_users - active_premium_users[month-6])
        else:
            active_premium_users.append(new_premium_users)
    
    # Доход от премиум-подписок (только от новых подписок)
    premium_rev = new_premium_users * premium_price
    premium_revenue.append(premium_rev)
    
    # Доход от рекламы
    ad_companies = ad_companies_initial + month * ad_increase
    companies.append(ad_companies)
    ad_rev = ad_companies * ad_price
    ad_revenue.append(ad_rev)
    
    # Общий доход
    total_rev = premium_rev + ad_rev
    total_revenue.append(total_rev)
    
    # Прибыль (доход - издержки)
    month_profit = total_rev - server_cost
    profit.append(month_profit)
    
    # Рост пользователей (случайно от 50 до 100)
    user_growth = random.randint(50, 100)
    users.append(current_users + user_growth)

# Настройка стиля
plt.style.use('bmh')
plt.rcParams['font.family'] = 'DejaVu Sans'

# Создание графика с двумя осями Y
fig, ax1 = plt.subplots(figsize=(15, 8))
fig.patch.set_alpha(0)  # Делаем фон фигуры прозрачным

# Первая ось Y (прибыль)
color1 = '#ada0f2'
ax1.set_xlabel('Месяц', fontsize=16, labelpad=15, color='white')
ax1.set_ylabel('Прибыль (₽)', color=color1, fontsize=16, labelpad=15)
line1 = ax1.plot(month_names, profit, marker='o', linewidth=3, markersize=12, color=color1, label='Прибыль')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.tick_params(axis='x', labelcolor='white')

# Вторая ось Y (пользователи и компании)
ax2 = ax1.twinx()
color2 = '#fdd98d'  # Зеленый для пользователей
color3 = '#71cac5'  # Красный для компаний
ax2.set_ylabel('Количество', color=color2, fontsize=16, labelpad=15)
line2 = ax2.plot(month_names, users[:-1], marker='s', linewidth=3, markersize=8, color=color2, label='Пользователи')
line3 = ax2.plot(month_names, companies, marker='^', linewidth=3, markersize=8, color=color3, label='Компании')
ax2.tick_params(axis='y', labelcolor=color2)

# Настройка сетки
ax1.grid(True, linestyle='--', alpha=0.7)

# Убираем рамку
for spine in ax1.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

plt.xticks(rotation=45, fontsize=12)

# Добавление аннотаций для значений прибыли
for i, p in enumerate(profit):
    ax1.annotate(f'{int(p):,}₽'.replace(',', ' '), 
                (month_names[i], p), 
                textcoords="offset points", 
                xytext=(0, 15), 
                ha='center', 
                fontsize=12,
                fontweight='bold',
                color=color1)

# Добавление аннотаций для количества пользователей (только для четных месяцев, начиная со второй точки)
for i, u in enumerate(users[:-1]):
    if i % 2 == 1:  # Только для нечетных месяцев (начиная со второй точки)
        ax2.annotate(f'{int(u):,}'.replace(',', ' '), 
                    (month_names[i], u), 
                    textcoords="offset points", 
                    xytext=(0, -25), 
                    ha='center', 
                    fontsize=10,
                    color=color2)

# Добавление аннотаций для количества компаний (только для четных месяцев)
for i, c in enumerate(companies):
    if i % 2 == 0:  # Только для четных месяцев
        ax2.annotate(f'{int(c)}', 
                    (month_names[i], c), 
                    textcoords="offset points", 
                    xytext=(0, 25), 
                    ha='center', 
                    fontsize=10,
                    color=color3)

# Добавление легенды
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=12)

# Настройка внешнего вида
plt.tight_layout()

# Сохранение графика в высоком разрешении с прозрачным фоном
plt.savefig('profit_graph_3.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close() 