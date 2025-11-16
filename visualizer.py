import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px

class Visualizer:
    def __init__(self, df):
        # Initialize with the cleaned DataFrame containing movie data
        self.df = df

    def plot_rating_distribution(self):
        # Plot a histogram showing the distribution of average movie ratings
        plt.figure(figsize=(8, 6))
        plt.hist(self.df['Average_rating'].dropna(), bins=20, edgecolor='black')
        plt.title("Distribution of Movie Ratings")
        plt.xlabel("Average Rating")
        plt.ylabel("Frequency")
        plt.show()

    def plot_runtime_vs_rating(self):
        # Scatter plot showing relationship between movie runtime and average rating
        plt.figure(figsize=(8, 6))
        plt.scatter(self.df['Runtime'], self.df['Average_rating'], alpha=0.5)
        plt.title("Movie Runtime vs Rating")
        plt.xlabel("Runtime (Minutes)")
        plt.ylabel("Average Rating")
        plt.show()

    def plot_films_per_genre_pie(self, genre_counts):
        # Pie chart showing proportion of films per top 6 genres
        if not isinstance(genre_counts, pd.Series):
            raise ValueError("Expected genre_counts to be a pandas Series.")

        top_genres = genre_counts.head(6)  # Select top 6 genres by film count

        plt.figure(figsize=(8, 8))
        plt.pie(top_genres.values, labels=top_genres.index, autopct='%1.1f%%', startangle=140)
        plt.title("Top 6 Genres by Number of Films")
        plt.axis('equal')  # Equal aspect ratio ensures pie is circular
        plt.tight_layout()
        plt.show()

    def plot_average_rating_per_genre(self):
        # Boxplot showing the distribution of ratings for each genre
        sns.set_style("whitegrid")
        plt.figure(figsize=(12, 8))
        sns.boxplot(
            data=self.df,
            x='Average_rating',
            y='Genres',
            hue='Genres',          # Color boxes by genre
            palette='pastel',      # Use pastel color palette
            dodge=False,           # Avoid separating boxes by hue
            legend=False           # Do not display legend (redundant here)
        )
        plt.title("Rating Distribution by Genre")
        plt.tight_layout()
        plt.show()

    def plot_top_directors(self):
        # Bubble chart for top 10 directors by average rating
        # Bubble size represents number of films directed
        director_stats = self.df.groupby('Director').agg({
            'Average_rating': 'mean',  # Average rating per director
            'Film_title': 'count'      # Count of films per director
        }).rename(columns={'Film_title': 'Film_Count'})

        # Sort directors by average rating and take top 10
        top_directors = director_stats.sort_values(by='Average_rating', ascending=False).head(10)

        plt.figure(figsize=(10, 6))
        plt.scatter(
            x=top_directors['Average_rating'],
            y=top_directors.index,
            s=top_directors['Film_Count'] * 50,  # Scale bubble size
            alpha=0.7,
            edgecolor='black'
        )
        plt.title("Top 10 Directors by Average Rating")
        plt.xlabel("Average Rating")
        plt.ylabel("Director")
        plt.tight_layout()
        plt.show()

    def plot_avg_rating_bar(self, avg_ratings):
        # Bar chart showing average rating per genre
        plt.figure(figsize=(12, 6))
        avg_ratings.sort_values().plot(kind='bar', color='skyblue')
        plt.title("Average Rating by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Average Rating")
        plt.tight_layout()
        plt.show()

    def interactive_scatter(self):
        # Interactive scatter plot of runtime vs average rating colored by genre using Plotly
        fig = px.scatter(
            self.df,
            x='Runtime',
            y='Average_rating',
            hover_data=['Film_title'],  # Show film title on hover
            color='Genres'
        )
        fig.update_layout(title="Interactive Scatter Plot: Runtime vs Rating")
        fig.show()

    def plot_genre_duration_heatmap(self, duration_col='Runtime', top_genres=15):
        # Heatmap showing distribution of movie durations across top genres

        # Select top genres by count
        top_genres_list = self.df['Genres'].value_counts().head(top_genres).index
        filtered_df = self.df[self.df['Genres'].isin(top_genres_list)].copy()

        # Bin runtime into duration categories
        filtered_df.loc[:, 'Duration_Bin'] = pd.cut(
            filtered_df[duration_col],
            bins=[0, 60, 90, 120, 150, 180, 240, 300],
            labels=['<1h', '1-1.5h', '1.5-2h', '2-2.5h', '2.5-3h', '3-4h', '4h+']
        )

        # Create cross-tabulation table normalized by genre
        heatmap_data = pd.crosstab(
            filtered_df['Genres'],
            filtered_df['Duration_Bin'],
            normalize='index'
        )

        plt.figure(figsize=(12, 8))
        sns.heatmap(heatmap_data * 100, annot=True, cmap='YlOrRd')
        plt.title(f"Movie Duration Distribution by Genre (Top {top_genres} Genres)")
        plt.tight_layout()
        plt.show()

    def plot_interactive_genre_bubble(self, top_genres=10):
        # Interactive bubble plot comparing average runtime and rating by genre
        # Bubble size represents number of films in genre
        genre_stats = (
            self.df.groupby('Genres')
            .agg(
                Avg_Rating=('Average_rating', 'mean'),
                Avg_Runtime=('Runtime', 'mean'),
                Movie_Count=('Film_title', 'count')
            )
            .sort_values('Movie_Count', ascending=False)
            .head(top_genres)
            .reset_index()
        )

        fig = px.scatter(
            genre_stats,
            x='Avg_Runtime',
            y='Avg_Rating',
            size='Movie_Count',
            color='Genres',
            hover_name='Genres',
            size_max=60
        )
        fig.update_layout(
            title="Genre Comparison: Runtime vs Rating",
            xaxis_title="Average Runtime",
            yaxis_title="Average Rating"
        )
        fig.show()
