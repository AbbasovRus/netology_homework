import pandas as pd

df = pd.read_csv(r'C:\Users\USER\Desktop\netology_homework\Итоговое задание\movies_stats.csv')

years = list(range(1950, 2011))

def production_year(title):
    for year in years:
        if str(year) in str(title):
            return year
    return 1900

df['year'] = df['title'].apply(production_year)

result = df.groupby('year')['rating'].mean().sort_values(ascending=False)

print(result)