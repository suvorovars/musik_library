import streamlit as st
import requests

def delete_strings(id):
    response = requests.post('http://localhost:8000/api/delete/strings', json={"performer_fk": id})
    return response.json()["success"]

def delete_performer(track):
    id = int(track.split(":")[0])
    delete_strings(id)
    response = requests.post("http://localhost:8000/api/delete/performers",
                             json={"performer_id": id})
    return response.json()["success"]

def create_delete_performer_page(api_url="http://localhost:8000"):
    st.title("Удаление Исполнителей")
    response = requests.get(f'{api_url}/api/get/performers').json()
    performers = sorted([f"{performer['performer_id']}:{performer['performer_name']}" for performer in response])
    choise = st.selectbox("Выберите исполнителя для удаления", performers)
    if choise:
        st.warning("При удалении исполнителя удалятся все его упоминания на дисках")
        if st.button(f"Удалить {choise}"):
            if delete_performer(choise):
                st.success("Испонитель удален")
