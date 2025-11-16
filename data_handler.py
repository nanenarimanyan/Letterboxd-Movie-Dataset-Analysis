import pandas as pd
import numpy as np

class DataHandler:
    # This class helps with loading, cleaning, summarizing, and analyzing a movie dataset.

    def __init__(self, file_path):
        # Saves the path to the CSV file.
        self.file_path = file_path

    def load_data(self):
        # Loads the CSV file and returns it as a DataFrame.
        try:
            df = pd.read_csv(self.file_path)
            # Check for essential columns
            required_columns = ['Average_rating', 'Runtime', 'Genres', 'Director', 'Film_title']
            for col in required_columns:
                if col not in df.columns:
                    print(f"Warning: '{col}' column is missing.")
            return df
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error while loading data: {e}")
            return None

    def clean_data(self, df):
        #Cleans the data:
        #Removes rows with missing rating, runtime, genre, director, or film title.
        #Fills missing runtime values with the mean runtime.
        #Simplifies the genre column to the first genre.
        if df is None:
            print("Data is None. Cannot proceed with cleaning.")
            return None

        # Drop rows with missing essential data
        df = df.dropna(subset=['Average_rating', 'Runtime', 'Genres', 'Director', 'Film_title']).copy()

        # Fill missing runtime values with mean
        mean_runtime = df['Runtime'].mean()
        df['Runtime'] = df['Runtime'].fillna(mean_runtime)

        # Simplify the 'Genres' column to the first genre
        df['Genres'] = (
            df['Genres']
            .astype(str)  # Ensure strings for genre column
            .str.split(',').str[0].str.strip()
        )

        return df

    def get_summary(self, df):
        #Returns summary statistics:
        #Column data types
        #Rating statistics
        #Runtime statistics
        #Genre distribution
        if df is None:
            print("Data is None. Cannot generate summary.")
            return None

        return {
            "Column Info": df.dtypes,
            "Rating Stats": df['Average_rating'].describe(),
            "Runtime Stats": df['Runtime'].describe(),
            "Genre Distribution": df['Genres'].value_counts()
        }

    def analyze_data(self, df):
        #Performs deeper analysis:
        #Average rating for each genre
        #Number of films per genre
        #Top 10 directors by average rating
        if df is None:
            print("Data is None. Cannot perform analysis.")
            return None

        # Ensure that essential columns exist
        required_columns = ['Genres', 'Average_rating', 'Director', 'Film_title']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Missing columns for analysis: {missing_columns}")
            return None

        # Analysis
        avg_rating_by_genre = (
            df.groupby('Genres')['Average_rating']
            .mean()
            .sort_values(ascending=False)
        )

        films_per_genre = df['Genres'].value_counts()

        top_directors = (
            df.groupby('Director')['Average_rating']
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

        return {
            "avg_rating_by_genre": avg_rating_by_genre,
            "films_per_genre": films_per_genre,
            "top_directors": top_directors
        }
