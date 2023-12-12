import streamlit as st
import requests

def create_track_page(api_url='http://localhost:8000'):
    st.title("Добавление нового Трека")

    track_title = st.text_input("Введите название нового трека")

    if track_title:
        if st.button("Подтвердить.", on_click=create_track, kwargs={'track_title': track_title}):
            st.success("Трек успешно добавлен!")
    else:
        st.warning('Введите трек!')

def create_track(url='http://localhost:8000/api/add/tracks', **kwargs):
    data = {
        'track': [kwargs['track_title']],
    }
    reponse = requests.post(url, json=data)