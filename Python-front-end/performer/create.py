import streamlit as st
import requests

def create_performer_page(api_url='http://localhost:8000'):
    st.title("Добавление нового Исполнителя")

    performer_name = st.text_input("Введите имя производителя")

    if performer_name:
        if st.button("Подтвердить.", on_click=create_performer, kwargs={'performer_name': performer_name}):
            st.success("Исполнитель успешно добавлен!")
    else:
        st.warning('Введите исполнителя!')

def create_performer(url='http://localhost:8000/api/add/performers', **kwargs):
    data = {
        'performer': [kwargs['performer_name']],
    }
    reponse = requests.post(url, json=data)