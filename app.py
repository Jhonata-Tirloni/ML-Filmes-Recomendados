import pandas as pd
import streamlit as st
import requests
import joblib

def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=5b23ce0eeb95b91e1fae905d65606841&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = 'https://image.tmdb.org/t/p/w500/'+poster_path
    return full_path

def recommendation(movie):
    index = filmes[filmes['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []

    for i in distances[1:9]:
        movie_id = filmes.iloc[i[0]].id
        recommended_movies_poster.append(get_poster(movie_id))
        recommended_movies_name.append(filmes.iloc[i[0]].title)
    
    return recommended_movies_name, recommended_movies_poster

dict_filmes = joblib.load('lista_filmes.pkl')
similarity = joblib.load('similarity.pkl')
filmes = pd.DataFrame(dict_filmes)
movie_list = filmes['title'].values

st.header('Recomendação de filmes - via ML')
select_movies = st.selectbox('Selecione um filme!', movie_list)

if st.button("Me recomende!"):
    recommended_movies_name, recommended_movies_poster = recommendation(select_movies)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])
    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])
    with col6:
        st.text(recommended_movies_name[5])
        st.image(recommended_movies_poster[5])
    with col7:
        st.text(recommended_movies_name[6])
        st.image(recommended_movies_poster[6])
    with col8:
        st.text(recommended_movies_name[7])
        st.image(recommended_movies_poster[7])



