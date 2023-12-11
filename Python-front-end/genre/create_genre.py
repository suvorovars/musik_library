import streamlit as st
import requests

def create_genre_page(api_url='http://localhost:8000'):
    st.title("Добавление нового Жанра")

    genre_title = st.text_input("Введите название нового жанра")

    if genre_title:
        if st.button("Подтвердить.", on_click=create_genre, kwargs={'genre': genre_title}):
            st.success("Жанр успешно добавлен!")
    else:
        st.warning('Введите жанр!')

def create_genre(url='http://localhost:8000/api/add/genres', **kwargs):
    data = {
        'genre': [kwargs['genre']],
    }
    reponse = requests.post(url, json=data)
    
