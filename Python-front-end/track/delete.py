import streamlit as st
import requests

def delete_strings(id):
    response = requests.post('http://localhost:8000/api/delete/strings', json={"track_fk": id})
    return response.json()["success"]

def delete_track(track):
    id = int(track.split(":")[0])
    delete_strings(id)
    response = requests.post("http://localhost:8000/api/delete/tracks",
                             json={"track_id": id})
    return response.json()["success"]

def create_delete_track_page(api_url="http://localhost:8000"):
    st.title("Удаление Песен")
    response = requests.get(f'{api_url}/api/get/tracks').json()
    tracks = sorted([f"{track['track_id']}:{track['track_title']}" for track in response])
    choise = st.selectbox("Выберите трек для удаления", tracks)
    if choise:
        st.warning("При удалении трека удалятся все его упоминания на дисках")
        if st.button(f"Удалить {choise}"):
            if delete_track(choise):
                st.success("Песня удалена")
