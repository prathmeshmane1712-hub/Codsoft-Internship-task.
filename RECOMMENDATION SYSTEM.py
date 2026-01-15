movies = {
    "Inception": ["Sci-Fi", "Action"],
    "Titanic": ["Romance", "Drama"],
    "Avengers": ["Action", "Sci-Fi"],
    "The Notebook": ["Romance"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "John Wick": ["Action"],
    "Forrest Gump": ["Drama"]
}

def recommend_movies(user_genre):
    recommendations = []

    for movie, genres in movies.items():
        if user_genre in genres:
            recommendations.append(movie)

    return recommendations

print("Movie Recommendation System")
print("Available genres: Action, Sci-Fi, Romance, Drama")

genre = input("Enter your favorite genre: ")

result = recommend_movies(genre)

if result:
    print("Recommended movies:")
    for m in result:
        print("-", m)
else:
    print("No recommendations found")
