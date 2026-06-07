import pandas as pd

movies = pd.read_csv(r'C:\Users\USER\Desktop\netology_homework\Домашнее задание 9\movies.csv')
ratings = pd.read_csv(r'C:\Users\USER\Desktop\netology_homework\Домашнее задание 9\ratings.csv')

best_id = ratings[ratings['rating'] == 5.0]['movieId'].value_counts().idxmax()
print(movies[movies['movieId'] == best_id]['title'].values[0])