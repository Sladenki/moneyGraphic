import matplotlib.pyplot as plt
import numpy as np
import random

# Начальные параметры
initial_users = 3000
premium_rate = 0.02  # 2% пользователей покупают премиум
premium_price = 100  # Стоимость премиум-статуса
ad_companies_initial = 5  # Начальное количество компаний
ad_increase = 2  # Увеличение компаний в месяц
ad_price = 400  # Стоимость рекламы
server_cost = 5000  # Постоянные издержки
months = 12
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Инициализация списков
users = [initial_users]
premium_revenue = []
ad_revenue = []
total_revenue = []
profit = []

# Расчет за 12 месяцев
for month in range(months):
    # Текущее количество пользователей
    current_users = users[-1]
    
    # Доход от премиум-статусов
    premium_users = current_users * premium_rate
    premium_rev = premium_users * premium_price
    premium_revenue.append(premium_rev)
    
    # Доход от рекламы
    ad_companies = ad_companies_initial + month * ad_increase
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

# Создание графика
plt.figure(figsize=(12, 6))
plt.plot(month_names, profit, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=8, label='Profit')

# Настройка графика
plt.title('Monthly Profit (Jan 2025 - Dec 2025)', fontsize=16, pad=15)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Profit (RUB)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()

# Добавление аннотаций для значений прибыли
for i, p in enumerate(profit):
    plt.annotate(f'{int(p)}₽', (month_names[i], p), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

# Сохранение графика
plt.savefig('profit_graph.png')