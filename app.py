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

col = st.columns(1)
with col:
    st.markdown("![Header](https://camo.githubusercontent.com/b0e39c2427d5a41b55b5fe556d317fa402905af871de2f188647a35c8d5a795f/68747470733a2f2f696d616765732d7769786d702d6564333061383662386334636138383737373335393463322e7769786d702e636f6d2f662f35323938626163302d623862662d346338302d616636372d3732356331323732646262302f6465626f386a652d31646332376339302d633162372d346438382d626132652d6635653036646162326362352e6a70672f76312f66696c6c2f775f313139322c685f3637302c715f37302c737472702f323032315f6d6f7669655f706f73746572735f62795f7468656b696e67626c616465723939355f6465626f386a652d7072652e6a70673f746f6b656e3d65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a7a645749694f694a31636d3436595842774f6a646c4d4751784f4467354f4449794e6a517a4e7a4e684e5759775a4451784e5756684d4751794e6d55774969776961584e7a496a6f6964584a754f6d467763446f335a54426b4d5467344f5467794d6a59304d7a637a5954566d4d4751304d54566c5954426b4d6a5a6c4d434973496d39696169493657317437496d686c6157646f64434936496a77394d5441344d434973496e4268644767694f694a634c325a634c7a55794f54686959574d774c574934596d59744e474d344d4331685a6a59334c5463794e574d784d6a63795a474a694d4677765a475669627a68715a5330785a474d794e324d354d43316a4d5749334c54526b4f446774596d45795a53316d4e5755774e6d5268596a4a6a596a5575616e426e4969776964326c6b644767694f694938505445354d6a4169665631644c434a68645751694f6c736964584a754f6e4e6c636e5a7059325536615731685a3255756233426c636d46306157397563794a6466512e4976727931307030686a4349574e4d7663564d5172702d6e43774e67327071487a6a714c48534541415377)") 

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



