import streamlit as st
import requests

def delete_strings(disk_id):
    response = requests.post('http://localhost:8000/api/delete/strings', json={"disk_fk": disk_id})
    return response.json()["success"]


def delete_disk(disk):
    id = int(disk.split(":")[0])
    response = requests.post("http://localhost:8000/api/delete/disks",
                             json={"disk_id": id})
    return response.json()["success"]



def create_delete_disk_page(disk=None):
    response = requests.get('http://localhost:8000/api/get/disks')
    list_disks = []
    response_json = response.json()
    for disk in response_json:
        list_disks.append(f"{disk['disk_id']}: {disk['disk_title']}, {disk['year']} год")
    disk_choice = st.selectbox('Выберете диск', list_disks)
    if disk_choice:
        st.warning('Внимание! При удалении диска, удалятся все записи, связанные с хранящимися на нём данными')
        st.warning(f"Вы уверены, что хотите удалить диск {disk_choice}?")
        if st.button(f"Удалить {disk_choice}"):
            r = delete_disk(disk_choice)
            if r:
                st.success('Диск успешно удалён')