import streamlit as st
import requests

def create_edit_disk_page(disk=None):
    response = requests.get('http://localhost:8000/api/get/disks')
    list_disks = []
    for disk in response.json():
        list_disks.append(f"{disk['disk_id']}: {disk['disk_title']}, {disk['year']}")
    choise = st.selectbox('Выберете диск', list_disks)
    st.write(choise)