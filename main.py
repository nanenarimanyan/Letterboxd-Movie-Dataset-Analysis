from data_handler import DataHandler
from visualizer import Visualizer

def main():
    handler = DataHandler("Movie_Data_File.csv")

    # Load data once
    df = handler.load_data()

    if df is not None:
        print("Initial Data Loaded.")
    else:
        print("Error: Data could not be loaded.")
        return

    # Flag to track data cleaning
    cleaned = False

    while True:
        step = input(
            "\nWhat would you like to do next?\n"
            "Options: clean, summary, analyze, visualize, all, exit\n"
            "Your choice: "
        ).strip().lower()

        if step == "exit":
            print("Goodbye!")
            break

        # Clean Data
        if step in ["clean", "all", "summary", "analyze", "visualize"]:
            if not cleaned:
                df = handler.clean_data(df)
                if df is not None:
                    cleaned = True
                    print("Data Cleaned.")
                else:
                    print("Data cleaning failed.")
                    continue

        # Summary
        if step in ["summary", "all"]:
            summary = handler.get_summary(df)
            if summary:
                print("\n--- Data Summary ---")
                for key, value in summary.items():
                    print(f"{key}:\n{value}\n")
            else:
                print("Summary generation failed.")

        # Analysis
        analysis = None
        if step in ["analyze", "all", "visualize"]:
            analysis = handler.analyze_data(df)
            if analysis:
                print("\n--- Analysis Results ---")
                print("Average Rating by Genre:\n", analysis['avg_rating_by_genre'].head())
                print("\nNumber of Films per Genre:\n", analysis['films_per_genre'].head())
                print("\nTop 10 Directors by Avg Rating:\n", analysis['top_directors'])
            else:
                print("Data analysis failed.")

        # Visualization
        if step in ["visualize", "all"]:
            visual = Visualizer(df)

            visual.plot_rating_distribution()
            visual.plot_runtime_vs_rating()
            visual.plot_films_per_genre_pie(analysis['films_per_genre'])
            visual.plot_top_directors()
            visual.plot_average_rating_per_genre()
            visual.plot_avg_rating_bar(analysis['avg_rating_by_genre'])

            # Optional visualizations (all methods must exist, even if empty)
            visual.interactive_scatter()
            visual.plot_genre_duration_heatmap()
            visual.plot_interactive_genre_bubble()

        # Handle invalid input
        if step not in ["clean", "summary", "analyze", "visualize", "all", "exit"]:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()