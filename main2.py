import pandas as pd
import matplotlib.pyplot as plt


file_name = 'comptagevelo2009.csv'

try:
    df = pd.read_csv(file_name)
    print("Файл успішно завантажено.\n")
except FileNotFoundError:
    print(f"Помилка: Файл {file_name} не знайдено.")
    exit()

# Перевірка основних характеристик 
print(">>> Перші 5 рядків датафрейму:")
print(df.head())

print("\n>>> Інформація про датафрейм (info):")
print(df.info())

print("\n>>> Описова статистика (describe):")
print(df.describe())

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

df.set_index('Date', inplace=True)

if 'Unnamed: 1' in df.columns:
    df.drop(columns=['Unnamed: 1'], inplace=True)

total_cyclists = df.sum().sum()
print(f"\n>>> Загальна кількість велосипедистів за рік на всіх доріжках: {int(total_cyclists)}")

print("\n>>> Кількість велосипедистів за рік по кожній доріжці:")
print(df.sum())

monthly_counts = df.resample('M').sum()

selected_paths = ['Berri1', 'Maisonneuve_1', 'Maisonneuve_2']

print("\n>>> Найбільш популярний місяць для обраних доріжок:")
for path in selected_paths:
    if path in monthly_counts.columns:
        peak_month_date = monthly_counts[path].idxmax()
        peak_value = monthly_counts[path].max()
        month_name = peak_month_date.strftime('%B')
        print(f"  - {path}: {month_name} (Кількість: {peak_value})")

plt.figure(figsize=(10, 6))

plt.plot(monthly_counts.index, monthly_counts['Berri1'], marker='o', linestyle='-', label='Berri1')

plt.title('Завантаженість велодоріжки Berri1 по місяцям (2009)')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.grid(True)
plt.legend()

# Відображення графіка
plt.show()