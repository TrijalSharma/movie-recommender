import pickle
import streamlit as st
import requests

st.header("Movie Recommendation System")

movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Which is your favourite movie?',
    movie_list
)


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x:x[1])
    recommended_movies_name = []
    #recommended_movies_poster = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        #recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)

    return recommended_movies_name #, recommended_movies_poster


if st.button('Show recommendation'):
    recommended_movies_name = recommend(selected_movie)

    for movie in recommended_movies_name:
        st.write(movie)