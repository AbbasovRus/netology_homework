import pandas as pd

movies = pd.read_csv(r'C:\Users\USER\Desktop\netology_homework\Домашнее задание 10\movies.csv')
ratings = pd.read_csv(r'C:\Users\USER\Desktop\netology_homework\Домашнее задание 10\ratings.csv')

def classify_rating(rating):
    if rating <= 2:
        return "низкий рейтинг"
    elif rating <= 4:
        return "средний рейтинг"
    return "высокий рейтинг"

merged_df = pd.merge(movies, ratings, on='movieId')

movie_ratings = merged_df.groupby('movieId').agg({
    'rating': 'mean',
    'title': 'first',
    'genres': 'first'
}).reset_index()

movie_ratings['class'] = movie_ratings['rating'].apply(classify_rating)

print(movie_ratings.head())
    