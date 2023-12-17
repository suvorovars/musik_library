import streamlit as st
import requests

def create_add_string_page():
    response = requests.get('http://localhost:8000/api/get/disks')

    list_disks = []
    list_tracks = []
    list_genres = []
    list_performers = []

    for disk in response.json():
        list_disks.append(f"{disk['disk_id']}: {disk['disk_title']}, {disk['year']} год")
    disk_choice = st.selectbox('Выберете диск', list_disks)

    for track in requests.get('http://localhost:8000/api/get/tracks').json():
        list_tracks.append(f"{track['track_id']}: {track['track_title']}")
    
    for genre in requests.get('http://localhost:8000/api/get/genres').json():
        list_genres.append(f"{genre['genre_id']}: {genre['genre_title']}")

    for performer in requests.get('http://localhost:8000/api/get/performers').json():
        list_performers.append(f"{performer['performer_id']}: {performer['performer_name']}")

    track_choice = st.selectbox('Выберите трек', list_tracks)
    genre_choice = st.selectbox('Выберите жанр', list_genres)
    performer_choice = st.selectbox('Выберите исполнителя', list_performers)
    duration = st.text_input("Введите длительность трека", value=None)

    if (duration) is None:
        st.warning("Введите длительность!")
    else:
        duration = int(duration)
    
    disk_fk = int(disk_choice.split(':')[0])
    track_fk = int(track_choice.split(':')[0])
    genre_fk = int(genre_choice.split(':')[0])
    performer_fk = int(performer_choice.split(':')[0])

    st.button('Добавить', on_click=add_string, kwargs={'disk_fk': [disk_fk], 
                                                     'track_fk': [track_fk], 
                                                     'genre_fk': [genre_fk], 
                                                     'performer_fk': [performer_fk], 
                                                     'duration': [duration]})

def add_string(**kwargs):
    req = requests.post('http://localhost:8000/api/add/strings', json=kwargs)

    st.success("Трек успешно добавлен!")




  
    