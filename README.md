# 🎬 Movies Recommendation System

A content-based movie recommender system built with Python and Streamlit. This application suggests the top 5 most similar movies based on a user's selection using natural language processing and cosine similarity.

## ✨ Features
* **Interactive UI:** Clean, web-based interface built entirely in Python using Streamlit.
* **Content-Based Filtering:** Recommends movies by analyzing metadata (genres, keywords, cast, crew, and overview) rather than user search history.
* **Pre-trained Models:** Utilizes serialized `.pkl` files for instant recommendations without recalculating machine learning algorithms on the fly.

## 📸 Interface Snapshot
<img width="1353" height="656" alt="image" src="https://github.com/user-attachments/assets/21b5e528-760d-41cf-814f-4a0884adb64b" />
<img width="1178" height="596" alt="image" src="https://github.com/user-attachments/assets/f66e5d6d-de0f-437c-9303-9bdc367e8e7d" />


* **Main Screen:** Dropdown menu to select from thousands of movie titles.
* **Recommendations:** Displays a clean list of the top 5 closest matches instantly upon clicking the recommendation button.

## 🛠️ Tech Stack
* **Frontend/Web Framework:** [Streamlit](https://streamlit.io/)
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning & NLP (Training Phase):** Scikit-learn (`CountVectorizer`, `cosine_similarity`), NLTK (`PorterStemmer`)
* **Serialization:** Pickle

## 🧠 How It Works
1. **Data Preprocessing:** The system processes the TMDB 5000 movies dataset, extracting and merging key tags (overview, genres, cast, crew).
2. **Text Vectorization:** The merged text tags are stemmed using NLTK and converted into numerical vectors using Scikit-Learn's `CountVectorizer`.
3. **Distance Calculation:** The mathematical distance between every movie vector is calculated using **Cosine Similarity**, determining how closely related any two movies are.
4. **Deployment:** The final data and similarity matrices are exported as Pickle (`.pkl`) files and loaded into a lightweight Streamlit server for user interaction.

## 📂 Project Structure
```text
Movie Recommender/
│
├── artifacts/
│   ├── movie_list.pkl       # Saved Pandas DataFrame containing movie titles and IDs
│   └── similarity.pkl       # Saved NumPy array containing cosine similarity distances
│
├── app.py                   # Main Streamlit web application script
├── recommender.ipynb        # Jupyter Notebook with raw ML training and data cleaning code
├── requirements.txt         # Production dependencies (streamlit, pandas, numpy)
└── .gitignore               # Excludes virtual environments and cache from Git tracking
