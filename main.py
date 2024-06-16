import tkinter as tk
from tkinter import messagebox
from movie_recommender import MovieRecommender

class MovieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation System")
        self.root.configure(bg='#eab676')

        self.recommender = MovieRecommender('movies.json')

        self.setup_gui()

    def setup_gui(self):
        container = tk.Frame(self.root, bg='#2596be')
        container.pack(padx=20, pady=20)

        tk.Label(container, text="Movie Recommendation System", font=("Arial", 24, "bold"), bg='#2596be', fg='black').grid(row=0, column=0, columnspan=3, pady=10)

        tk.Label(container, text="Enter Movie Name:", font=("Arial", 14), bg='#2596be', fg='black').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.movie_entry = tk.Entry(container, width=50, font=("Arial", 14))
        self.movie_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(container, text="Add Movie", font=("Arial", 14), bg='#4CAF50', width=12, command=self.add_movie).grid(row=1, column=2, padx=10, pady=10)

        tk.Label(container, text="Movies Added:", font=("Arial", 16, "bold"), bg='#2596be', fg='black').grid(row=2, column=0, columnspan=3, pady=10)

        self.movies_listbox = tk.Listbox(container, width=70, height=10, font=("Arial", 14), selectbackground='#ddd')
        self.movies_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        tk.Button(container, text="Delete Selected", font=("Arial", 14), bg='#f44336', width=15, command=self.delete_movie).grid(row=4, column=0, padx=10, pady=10, sticky='w')

        tk.Label(container, text="Recommended Movie:", font=("Arial", 18, "bold"), bg='#2596be', fg='black').grid(row=5, column=0, columnspan=3, pady=10)

        self.recommendation_label = tk.Label(container, text="", font=("Arial", 14), bg='#fff', fg='black', padx=10, pady=10, wraplength=600)
        self.recommendation_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        tk.Button(container, text="Add Movie to JSON File", font=("Arial", 14), bg='#2196F3', width=20, command=self.add_movie_to_json).grid(row=7, column=0, padx=10, pady=10, sticky='w')

        self.update_movies_list()

    def add_movie(self):
        movie_name = self.movie_entry.get().strip()
        if movie_name:
            if self.recommender.add_movie(movie_name):
                self.update_movies_list()
                self.update_recommendation()
                self.movie_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Movie not found in the database.")
        else:
            messagebox.showwarning("Input Error", "Please enter a movie name.")

    def delete_movie(self):
        selected_index = self.movies_listbox.curselection()
        if selected_index:
            movie_name = self.movies_listbox.get(selected_index)
            if self.recommender.delete_movie(movie_name):
                self.update_movies_list()
                self.update_recommendation()
            else:
                messagebox.showerror("Error", "Movie not found in the user's list.")
        else:
            messagebox.showwarning("Selection Error", "Please select a movie to delete.")

    def update_movies_list(self):
        self.movies_listbox.delete(0, tk.END)
        for movie in self.recommender.user_movies:
            self.movies_listbox.insert(tk.END, movie['title'])

    def update_recommendation(self):
        recommended_movie = self.recommender.recommend_movie()
        if recommended_movie:
            self.recommendation_label.config(text=f"{recommended_movie['title']} ({recommended_movie['base_rating']})\nGenre: {recommended_movie['genre']}\nDirector: {recommended_movie['director']}\nActors: {', '.join(recommended_movie['actors'])}")
        else:
            self.recommendation_label.config(text="No movies to recommend.")

    def add_movie_to_json(self):
        new_movie_name = self.movie_entry.get().strip()
        if new_movie_name:
            # Check if movie already exists in user's list
            for movie in self.recommender.user_movies:
                if movie['title'] == new_movie_name:
                    messagebox.showerror("Error", f"Movie '{new_movie_name}' already exists in the user's list.")
                    return

            # Prompt user for movie details
            top = tk.Toplevel(self.root)
            top.title("Add New Movie")
            top.configure(bg='#eab676')

            tk.Label(top, text="Enter Movie Details:", font=("Arial", 14, "bold"), bg='#eab676', fg='black').grid(row=0, column=0, columnspan=2, pady=10)
            tk.Label(top, text="Genre:", font=("Arial", 12), bg='#eab676', fg='black').grid(row=1, column=0, padx=10, pady=10, sticky='w')
            genre_entry = tk.Entry(top, width=50, font=("Arial", 12))
            genre_entry.grid(row=1, column=1, padx=10, pady=10)

            tk.Label(top, text="Director:", font=("Arial", 12), bg='#eab676', fg='black').grid(row=2, column=0, padx=10, pady=10, sticky='w')
            director_entry = tk.Entry(top, width=50, font=("Arial", 12))
            director_entry.grid(row=2, column=1, padx=10, pady=10)

            tk.Label(top, text="Actors (comma-separated):", font=("Arial", 12), bg='#eab676', fg='black').grid(row=3, column=0, padx=10, pady=10, sticky='w')
            actors_entry = tk.Entry(top, width=50, font=("Arial", 12))
            actors_entry.grid(row=3, column=1, padx=10, pady=10)

            tk.Label(top, text="Base Rating:", font=("Arial", 12), bg='#eab676', fg='black').grid(row=4, column=0, padx=10, pady=10, sticky='w')
            base_rating_entry = tk.Entry(top, width=50, font=("Arial", 12))
            base_rating_entry.grid(row=4, column=1, padx=10, pady=10)

            tk.Label(top, text="Nominees:", font=("Arial", 12), bg='#eab676', fg='black').grid(row=5, column=0, padx=10, pady=10, sticky='w')
            nominees_entry = tk.Entry(top, width=50, font=("Arial", 12))
            nominees_entry.grid(row=5, column=1, padx=10, pady=10)

            tk.Label(top, text="Awards:", font=("Arial", 12), bg='#eab676', fg='black').grid(row=6, column=0, padx=10, pady=10, sticky='w')
            awards_entry = tk.Entry(top, width=50, font=("Arial", 12))
            awards_entry.grid(row=6, column=1, padx=10, pady=10)

            tk.Label(top, text="Industry Influence:", font=("Arial", 12), bg='#eab676', fg='black').grid(row=7, column=0, padx=10, pady=10, sticky='w')
            industry_entry = tk.Entry(top, width=50, font=("Arial", 12))
            industry_entry.grid(row=7, column=1, padx=10, pady=10)

            def add_new_movie():
                genre = genre_entry.get().strip()
                director = director_entry.get().strip()
                actors = [actor.strip() for actor in actors_entry.get().strip().split(',') if actor.strip()]
                base_rating = float(base_rating_entry.get().strip()) if base_rating_entry.get().strip() else 0.0
                nominees = int(nominees_entry.get().strip()) if nominees_entry.get().strip() else 0
                awards = int(awards_entry.get().strip()) if awards_entry.get().strip() else 0
                industry = int(industry_entry.get().strip()) if industry_entry.get().strip() else 0

                new_movie = {
                    "title": new_movie_name,
                    "genre": genre,
                    "director": director,
                    "actors": actors,
                    "base_rating": base_rating,
                    "nominees": nominees,
                    "awards": awards,
                    "industry_influence": industry
                }

                self.recommender.user_movies.append(new_movie)
                self.recommender.save_movies_to_json('movies.json', self.recommender.user_movies)
                messagebox.showinfo("Success", f"Movie '{new_movie_name}' added successfully.")
                top.destroy()
                self.update_movies_list()
                self.update_recommendation()
                self.movie_entry.delete(0, tk.END)

            tk.Button(top, text="Add Movie", font=("Arial", 14), bg='#4CAF50', width=12, command=add_new_movie).grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        else:
            messagebox.showwarning("Input Error", "Please enter a movie name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()
