from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
content = response.text

top_100_movies = []
soup = BeautifulSoup(content, "html.parser")
movies = soup.find_all(name="h3", class_="_h3_cuogz_1")
print(movies)
movie_number = ""
movie_name = ""
for movie in movies:
    top_100_movies.append(movie.getText().split("\xa0"))

top_100_movies = [movie.getText() for movie in soup.find_all(name="h3", class_="_h3_cuogz_1")]
del top_100_movies[-1]
index = 0
for movie in top_100_movies:
    top_100_movies[index] =  movie.replace("\xa0","")
    index+=1

for n in range(0, len(top_100_movies)):
    print(top_100_movies[n])

with open("Top_100_Movies.tex", mode="w") as file:
    for movie in top_100_movies:
        file.write(f"{movie}\n")