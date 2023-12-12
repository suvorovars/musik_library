import streamlit as st
import requests

def create_edit_genre_page():
    response = requests.get('http://localhost:8000/api/get/genres')
    list_genres = []
    for genre in response.json():
        list_genres.append(f"{genre['genre_id']}: {genre['genre_title']}")
    choice = st.selectbox(label = "Выберите жанр", options=list_genres)

    genre_id = int(choice.split(":")[0])
    new_genre_title = st.text_input("Введите новое название жанра", value=None)
    data = {
        'old_genre_id': genre_id,
        'new_genre_title': new_genre_title
    }
    st.button("Изменить", on_click=edit_genre, kwargs=data)

def edit_genre(**kwargs):
    url = 'http://localhost:8000/api/edit/genres'
    
    response = requests.post(url, json=kwargs)