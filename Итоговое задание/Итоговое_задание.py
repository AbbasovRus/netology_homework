import pandas as pd

# 1. Загружаем данные (убедись, что путь правильный)
df = pd.read_csv(r'C:\Users\USER\Desktop\netology_homework\Итоговое задание\movies_stats.csv')

# 2. Создаём список годов 1950–2010
years = list(range(1950, 2011))

# 3. Функция извлечения года
def production_year(title):
    title_str = str(title)
    for year in years:
        if str(year) in title_str:
            return year
    return 1900

# 4. Добавляем столбец year
df['year'] = df['title'].apply(production_year)

# 5. Группируем и считаем средний рейтинг
mean_ratings = df.groupby('year')['rating'].mean()

# 6. Сортируем по убыванию
sorted_ratings = mean_ratings.sort_values(ascending=False)

# 7. Выводим результат
print("Средний рейтинг по годам (от высокого к низкому):")
print(sorted_ratings)

# Дополнительно: топы
print("\nТоп-5 лет с самыми высокими рейтингами:")
print(sorted_ratings.head())
print("\nТоп-5 лет с самыми низкими рейтингами:")
print(sorted_ratings.tail())