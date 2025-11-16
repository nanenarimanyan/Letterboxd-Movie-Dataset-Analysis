# 🎬 **Letterboxd Movie Dataset Analysis**

*A full exploratory analysis of movie trends, genres, ratings, directors, and viewing patterns.*

**Contributors:** Zara Matevosyan, Mane Muradyan, Nare Davtyan, Nane Narimanyan
Dataset Source: [https://letterboxd.com](https://letterboxd.com)
Report Reference: 

---

## 📚 **1. Project Overview**

This project analyzes a movie dataset from Letterboxd with the goal of uncovering meaningful insights about:

* Viewer ratings
* Movie runtime patterns
* Genre performance and distribution
* Top-rated directors
* Audience preferences and trends

The project includes **data cleaning**, **statistical summaries**, **advanced analysis**, and both **static** and **interactive** visualizations.

This work is valuable for:

* Film industry analysts
* Streaming platforms
* Recommendation system designers
* Anyone exploring movie data trends

---

## 🗂 **2. Dataset Description**

The dataset (`Movie_Data_File.csv`) includes the following key fields:

* **Average_rating** — Numeric viewer rating
* **Runtime** — Length of each movie (minutes)
* **Genres** — One or more genre tags
* **Director** — Film director
* **Film_title** — Movie title

Before analysis, extensive cleaning was required due to missing values and inconsistencies.

---

## 🧹 **3. Data Cleaning Steps**

* Removed rows missing essential fields (rating, runtime, genre, director, title)
* Imputed missing runtimes using the **mean runtime**
* Standardized genre values by extracting the **primary genre**
* Ensured structural consistency before further processing

This produced a reliable dataset for accurate insights.

---

## 📊 **4. Summary Statistics**

Computed descriptive statistics for:

* Movie ratings
* Runtimes
* Genre frequency counts

This helped capture the distribution of the dataset and identify common movie patterns.

---

## 🔍 **5. Advanced Analysis**

### **⭐ Average Ratings by Genre**

Identified which genres tend to receive higher viewer ratings.

### **🎭 Film Counts per Genre**

Determined which genres are most common in the dataset.

### **🎬 Top Directors by Average Rating**

Extracted and ranked the top **10 directors** with consistently high ratings.

---

## 🖼 **6. Visualizations**

The project includes both **static** and **interactive** plots.

### **Static (Matplotlib / Seaborn):**

* Rating histogram
* Runtime vs. rating scatter plot
* Genre distribution pie chart
* Rating boxplots
* Director ratings bubble chart
* Average rating bar charts

### **Interactive (Plotly Express):**

* Scatter: Runtime vs. Rating
* Heatmap: Genre vs average runtime
* Bubble chart: Genre comparisons

These visualizations enhance interpretability and allow users to explore the dataset more intuitively.

---

## 🧠 **7. Code Structure**

The project is organized into **three main modules**:

### **`main.py` — Workflow Controller**

* Loads the dataset using `DataHandler`
* Provides CLI menu for user choices
* Runs cleaning, statistical analysis, visualizations

### **`data_handler.py` — Data Loading & Analysis**

* Reads and validates the CSV
* Cleans missing or inconsistent data
* Computes summary statistics
* Performs grouped and comparative analysis

### **`visualizer.py` — Visualization Engine**

* Generates all visualizations
* Works with cleaned data and analysis results
* Produces both static and interactive charts

---

## ▶️ **8. Program Flow**

1. Script starts in **main.py**
2. User selects actions:

   * Clean data
   * View summary stats
   * Run analysis
   * Generate visualizations
3. Results print to console and/or display graphically
4. Users may repeat tasks or exit

---

## ✔️ **9. Conclusion**

This project successfully demonstrates how to:

* Clean and preprocess real-world data
* Extract meaningful insights using grouped analysis
* Visualize trends with multiple plotting libraries
* Structure Python code in modular, reusable components

The findings offer valuable perspectives for movie industry analysis and provide a strong foundation for future recommendation or prediction models.

---

## 💻 **10. Technologies Used**

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly Express


