import streamlit as st
import requests

def create_edit_track_page():
    response = requests.get('http://localhost:8000/api/get/tracks')
    list_tracks = []
    for track in response.json():
        list_tracks.append(f"{track['track_id']}: {track['track_title']}")
    choice = st.selectbox(label = "Выберите жанр", options=list_tracks)

    track_id = int(choice.split(":")[0])
    new_track_title = st.text_input("Введите новое название произведения", value=None)
    data = {
        'old_track_id': track_id,
        'new_track_title': new_track_title
    }
    st.button("Изменить", on_click=edit_track, kwargs=data)

def edit_track(**kwargs):
    url = 'http://localhost:8000/api/edit/tracks'
    
    response = requests.post(url, json=kwargs)