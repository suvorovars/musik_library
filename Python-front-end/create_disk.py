import pandas as pd
import streamlit as st
import requests
from datetime import datetime
import json

def get_data(api_url='http://localhost:8000'):
    try:
        tracks = [track["track_title"] for track in requests.get(f'{api_url}/api/get/tracks').json()]
        performers = [performer["performer_name"] for performer in requests.get(f'{api_url}/api/get/performers').json()]
        genres = [genre["genre_title"] for genre in requests.get(f'{api_url}/api/get/genres').json()]
        return tracks, performers, genres
    except requests.exceptions.RequestException as e:
        st.error(f"Ошибка при запросе к API: {e}")
        return [], [], []


def add_disk(disk_title, disk_year, strings):
    data = {'disk_title': [str(disk_title)], 'disk_year': [str(disk_year)]}
    st.write(data)
    response = requests.post('http://localhost:8000/api/add/disks', json=data)
    # if not response.json()['success']:
    #     st.exception('Could not create')
    #     return None
    if not strings:
        return None
    response = requests.get('http://localhost:8000/api/get/disks')
    disk_id = None
    for i in response.json():
        if str(i['year']) == str(disk_year) and str(i['disk_title']) == str(disk_title):
            disk_id = i['disk_id']
            break
    tracks = {track["track_title"]: track["track_id"] for track in requests.get(f'http://localhost:8000/api/get/tracks').json()}
    performers = {performer["performer_name"]: performer["performer_id"] for performer in requests.get(f'http://localhost:8000/api/get/performers').json()}
    genres = {genre["genre_title"]: genre["genre_id"] for genre in requests.get(f'http://localhost:8000/api/get/genres').json()}
    json_strings = {
        "disk_fk": [],
        "track_fk": [],
        "genre_fk": [],
        "performer_fk": [],
        "duration": []
    }
    for i in strings:
        if not i:
            continue
        json_strings["disk_fk"].append(disk_id)
        json_strings["track_fk"].append(tracks[i[0]])
        json_strings["performer_fk"].append(performers[i[1]])
        json_strings["genre_fk"].append(genres[i[2]])
        t = i[3].split(':')
        t = int(t[0]) * 60 + int(t[1])
        json_strings["duration"].append(t)

    st.write(json_strings)
    response = requests.post("http://localhost:8000/api/add/strings", json=json_strings)


def create_create_disk_page(api_url='http://localhost:8000'):
    st.title("Добавление нового Диска")

    # Используем st.session_state для хранения переменной между вызовами
    if 'strings' not in st.session_state:
        st.session_state.strings = [[]]

    title = st.text_input("Введите название нового Диска")
    year = st.text_input("Введите год выхода Диска")

    if title and year:
        st.header(f"Добавление песен для альбома '{title}' ({year})")

        tracks, performers, genres = get_data(api_url)

        # Логика выбора для Названия, Исполнителя и Жанра
        song_title = st.selectbox("Выберите песню", tracks)
        selected_performer = st.selectbox("Выберите Исполнителя", performers)
        selected_genre = st.selectbox("Выберите Жанр", genres)
        time = st.text_input("Введите время записи")

        # Предоставление возможности добавить еще песню
        if st.button("Добавить еще песню"):
            if song_title and selected_performer and selected_genre and time:
                st.session_state.strings.append([song_title, selected_performer, selected_genre, time])

        # Вывод всех введенных данных о песнях после нажатия кнопки
        st.header("Информация о добавленных песнях:")
        if st.session_state.strings[1:]:
            st.table(pd.DataFrame(st.session_state.strings[1:], columns=["Название", "Исполнитель", "Жанр", "Время записи"]))

        # Кнопка для сохранения диска
        if st.button("Сохранить Диск"):
            add_disk(title, year, st.session_state.strings)
            st.session_state.strings = [[]]
            # Вставьте ваш запрос сюда
            # например, requests.post('ваш_адрес_сервера', json={'title': title, 'year': year, 'songs': st.session_state.strings[1:]})
            st.success("Диск успешно сохранен!")

