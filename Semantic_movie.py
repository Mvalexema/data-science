# Movie recommendation based on user's preferences
import spacy  
nlp = spacy.load('en_core_web_md')




# The user watched 'Planet Hulk' movie with the following description
planet_hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator'

# Function calculates the maximum score based on simantic similarity of Hulk and each of movies in the text file converted into disctionary
def movie_recom(movies: dict[str,str], text_desc: str) -> dict[str,float]:
    max_score = 0
    result = dict()
    desc = nlp(text_desc)
    for movie_name in movies.keys():
        movie_desc = nlp(movies[movie_name])
        score_movie = movie_desc.similarity(desc)
        if score_movie >= max_score:
            max_score = score_movie
            result = {movie_name: max_score}
    return result

# Function opens the text file as distionary
def get_recom(filename: str, text_desc: str) -> dict[str, float]:
    movies = dict()
    with open(filename) as file:
        for line in file:
            key,value = line.rstrip().split(" :")
            movies[key] = value
   
    return movie_recom(movies = movies, text_desc = text_desc)

if __name__ == "__main__":
    result = get_recom(filename = 'movies.txt', text_desc = planet_hulk)
    print(result)

