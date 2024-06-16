import json

class MovieRecommender:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            self.movies = json.load(file)
        self.user_movies = []

    def add_movie(self, title):
        title_lower = title.lower()  # Convert input to lowercase
        for movie_title, details in self.movies.items():
            if title_lower == movie_title.lower():  # Compare lowercase titles
                self.user_movies.append(details)
                return True
        return False

    def delete_movie(self, title):
        for movie in self.user_movies:
            if movie['title'].lower() == title.lower():  # Compare lowercase titles
                self.user_movies.remove(movie)
                return True
        return False

    def recommend_movie(self):
        if not self.user_movies:
            return None
        sorted_movies = self.merge_sort(self.user_movies, key=lambda x: x['base_rating'], reverse=True)
        return sorted_movies[0] if sorted_movies else None

    def merge_sort(self, array, key=lambda x: x, reverse=False):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = self.merge_sort(array[:mid], key, reverse)
        right = self.merge_sort(array[mid:], key, reverse)
        return self.merge(left, right, key, reverse)

    def merge(self, left, right, key, reverse):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if (key(left[i]) > key(right[j])) ^ reverse:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
