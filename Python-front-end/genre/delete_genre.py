import streamlit as st
import requests

def delete_strings(id):
    response = requests.post('http://localhost:8000/api/delete/strings', json={"genre_fk": id})
    return response.json()["success"]

def delete_genre(track):
    id = int(track.split(":")[0])
    delete_strings(id)
    response = requests.post("http://localhost:8000/api/delete/genres",
                             json={"genre_id": id})
    return response.json()["success"]

def create_delete_genre_page(api_url="http://localhost:8000"):
    st.title("Удаление Жанров")
    response = requests.get(f'{api_url}/api/get/genres').json()
    tracks = sorted([f"{genre['genre_id']}:{genre['genre_title']}" for genre in response])
    choise = st.selectbox("Выберите трек для удаления", tracks)
    if choise:
        st.warning("При удалении жанра удалятся все его упоминания на дисках")
        if st.button(f"Удалить {choise}"):
            if delete_genre(choise):
                st.success("Жанр удален")
