import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Sample movie dataset
data = {
    'title': [
        'The Matrix', 'Inception', 'Interstellar', 'The Notebook', 'The Lion King'
    ],
    'genre': [
        'Action Sci-Fi', 'Action Sci-Fi', 'Adventure Drama', 'Romance Drama', 'Animation Family'
    ],
    'overview': [
        'A computer hacker learns about the true nature of reality and his role in the war.',
        'A thief steals corporate secrets through dream-sharing technology.',
        'A team travels through a wormhole to save humanity.',
        'A young couple falls in love in the 1940s.',
        'A lion cub grows up and reclaims his kingdom.'
    ]
}

df = pd.DataFrame(data)

# Combine genre and overview for content filtering
df['content'] = df['genre'] + " " + df['overview']

# Vectorize text using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['content'])

# Get cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend_movies(movie_title, user_mood):
    print(Fore.CYAN + f"\n🎬 Looking for recommendations based on: {movie_title}")
    
    # Find index of the movie
    try:
        idx = df[df['title'].str.lower() == movie_title.lower()].index[0]
    except IndexError:
        print(Fore.RED + "Movie not found in the dataset.")
        return
    
    # Sentiment analysis of user mood
    mood_sentiment = TextBlob(user_mood).sentiment.polarity
    print(Fore.YELLOW + f"😊 Detected mood polarity: {mood_sentiment:.2f}")

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]  # Top 3 similar movies

    print(Fore.GREEN + "\n📽 Recommended Movies:")
    for i, score in sim_scores:
        movie_sentiment = TextBlob(df.iloc[i]['overview']).sentiment.polarity
        mood_match = abs(mood_sentiment - movie_sentiment) < 0.3
        mood_color = Fore.BLUE if mood_match else Fore.RED
        print(f"{mood_color}- {df.iloc[i]['title']} (Sentiment Match: {'Yes' if mood_match else 'No'})")

# Example usage
recommend_movies("The Matrix", user_mood="I'm feeling excited and adventurous")
