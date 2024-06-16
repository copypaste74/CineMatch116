import json

def load_movies_from_json(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def calculate_rating(movie):
    nominees_weight = 0.1
    awards_weight = 0.2
    industry_weight = 0.3
    director_weight = 0.2
    actors_weight = 0.2

    rating = (nominees_weight * movie.get('nominees', 0) +
              awards_weight * movie.get('awards', 0) +
              industry_weight * movie.get('industry', 0) +
              director_weight * len(movie.get('director', '').split()) +
              actors_weight * len(movie.get('actors', [])) +
              movie.get('base_rating', 0))

    return round(rating, 2)

def load_movies_from_json(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def save_movies_to_json(json_file, movies_list):
    with open(json_file, 'w') as file:
        json.dump(movies_list, file, indent=4)