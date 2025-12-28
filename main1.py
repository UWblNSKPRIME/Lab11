import pandas as pd

# Використання даних з Практичної роботи №5 
teams_championship = {
    "Dynamo": 50,
    "Shakhtar": 48,
    "Zorya": 45,
    "Vorskla": 40,
    "Desna": 38,
    "Kolos": 35,
    "Dnipro-1": 30,
    "Lviv": 25,
    "Minaj": 20
}

# Доповнення даних 
teams = list(teams_championship.keys())
points = list(teams_championship.values())

cities = ["Kyiv", "Donetsk", "Luhansk", "Poltava", "Chernihiv", 
          "Kovalivka", "Dnipro", "Lviv", "Uzhhorod"]
regions = ["Center", "East", "East", "Center", "North", 
           "Center", "East", "West", "West"]
ticket_prices = [300, 400, 150, 120, 130, 100, 200, 140, 90]
attendance = [20000, 15000, 5000, 6000, 4000, 3000, 8000, 4500, 2000]

# Створення DataFrame
data = {
    'Команда': teams,
    'Очки': points,
    'Місто': cities,
    'Регіон': regions,
    'Ціна_квитка': ticket_prices,
    'Відвідуваність': attendance
}

df = pd.DataFrame(data)

print("--- Вміст створеного DataFrame ---")
print(df)

# Базовий аналіз даних 
print("\n--- 1. Перші 3 рядки (df.head(3)) ---")
print(df.head(3))

print("\n--- 2. Типи даних (df.dtypes) ---")
print(df.dtypes)

print("\n--- 3. Розмірність (df.shape) ---")
print(f"Рядків: {df.shape[0]}, Стовпців: {df.shape[1]}")

print("\n--- 4. Описова статистика (df.describe()) ---")
print(df.describe())

df['Дохід_за_матч'] = df['Ціна_квитка'] * df['Відвідуваність']
print("\n--- 5. Додано стовпець 'Дохід_за_матч' ---")
print(df[['Команда', 'Дохід_за_матч']].head())

# Фільтрація даних
filtered_df = df[df['Дохід_за_матч'] > 1000000]
print("\n--- 6. Фільтрація (Дохід > 1 млн) ---")
print(filtered_df[['Команда', 'Дохід_за_матч']])

sorted_df = df.sort_values(by='Очки', ascending=False)
print("\n--- 7. Сортування за очками (Top-5) ---")
print(sorted_df[['Команда', 'Очки']].head(5))

# Групування та агрегація 
grouped_mean = df.groupby('Регіон').mean(numeric_only=True)
print("\n--- 8. Середні показники по Регіонах ---")
print(grouped_mean[['Очки', 'Дохід_за_матч']])

aggregation = df.groupby('Регіон').agg({
    'Дохід_за_матч': 'max',  
    'Команда': 'count'       
})
aggregation = aggregation.rename(columns={'Дохід_за_матч': 'Макс_Дохід', 'Команда': 'Кількість_команд'})

print("\n--- 9. Додаткова агрегація (Макс. дохід та к-сть команд) ---")
print(aggregation)