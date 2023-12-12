import streamlit as st
import requests

def create_edit_performer_page():
    response = requests.get('http://localhost:8000/api/get/performers')
    list_performers = []
    for performer in response.json():
        list_performers.append(f"{performer['performer_id']}: {performer['performer_name']}")
    choice = st.selectbox(label = "Выберите исполнителя", options=list_performers)

    performer_id = int(choice.split(":")[0])
    new_performer_name = st.text_input("Введите новое имя исполнителя", value=None)
    if new_performer_name:
        data = {
            'old_performer_id': performer_id,
            'new_performer_name': new_performer_name
        }
        st.button("Изменить", on_click=edit_performer, kwargs=data)
    else:
        st.warning('Введите новое имя исполнителя!')
def edit_performer(**kwargs):
    url = 'http://localhost:8000/api/edit/performers'
    
    response = requests.post(url, json=kwargs)