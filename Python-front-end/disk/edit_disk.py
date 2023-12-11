import streamlit as st
import requests

def create_edit_disk_page(disk=None):
    response = requests.get('http://localhost:8000/api/get/disks')
    list_disks = []
    list_strings = []
    for disk in response.json():
        list_disks.append(f"{disk['disk_id']}: {disk['disk_title']}, {disk['year']} год")
    disk_choice = st.selectbox('Выберете диск', list_disks)

    new_disk_title = st.text_input("Изменить название", value=None)
    new_year = st.text_input("Изменить год диска", value=None)
    
    disk_id = disk_choice.split(':')[0]
    strings = requests.get(f'http://localhost:8000/api/get/strs?disk_fk={disk_id}')

    for string in strings.json():
        list_strings.append(f"{string['id']}: Автор: {string['performer_name']}, Название трека: {string['track_title']}, Название жанра: {string['genre_title']}")

        
    string_choice = st.selectbox('Выберите строку', list_strings)

    string_id = 0
    if list_strings:
        string_id = int(string_choice.split(':')[0])
    
        new_performer_name = st.text_input("Изменить исполнителя", value=None)
        new_track_title = st.text_input("Изменить название произведения", value=None)
        new_genre_title = st.text_input("Изменить жанр", value=None)
        new_duration = st.text_input("Изменить длительность трека (вводить в секундах)", value=None)
    else:
        new_performer_name = None
        new_track_title = None
        new_genre_title = None
        new_duration = None
    st.button("Изменить", on_click=change, kwargs={'old_disk_id': int(disk_id), 
                                                   'new_disk_title': new_disk_title, 
                                                   'new_year': int(new_year) if new_year else None,
                                                   'id': string_id,
                                                   'new_performer_name': new_performer_name, 
                                                   'new_track_title':new_track_title, 
                                                   'new_genre_title': new_genre_title,
                                                   'new_duration': int(new_duration) if new_duration else None})

def change(**kwargs):
    change_disk = 'http://localhost:8000/api/edit/disks'
    change_string = 'http://localhost:8000/api/edit/strings'

    data = {'old_disk_id': kwargs['old_disk_id'],
            'new_disk_title': kwargs['new_disk_title'],
            'new_year': kwargs['new_year']}
    
    if kwargs['new_disk_title'] or kwargs['new_year']:
        response = requests.post(change_disk, json=data)

    new_performer_id, new_genre_id, new_track_id = None, None, None
    print(kwargs)
    if kwargs.get('new_performer_name'):
        new_performer_name = kwargs.get('new_performer_name')
        performer_id = requests.get(f'http://localhost:8000/api/get/performers?performer_name={new_performer_name}').json()
        if performer_id == []:
            st.warning("Такого исполнителя нет! Для начало его нужно добавить!")
        else:
            new_performer_id = performer_id[0]['performer_id']
    if kwargs.get('new_track_title'):
        new_track_title = kwargs.get('new_track_title')
        track_id = requests.get(f'http://localhost:8000/api/get/tracks?track_title={new_track_title}').json()
        if track_id == []:
            st.warning("Такого трека нет! Для начало его нужно добавить!")
        else:
            new_track_id = track_id[0]['track_id']
    if kwargs.get('new_genre_title'):
        new_genre_title = kwargs.get('new_genre_title')
        genre_id = requests.get(f'http://localhost:8000/api/get/genres?genre_title={new_genre_title}').json()
        if genre_id == []:
            st.warning("Такого жанра нет! Для начало его нужно добавить!")
        else:
            new_genre_id = genre_id[0]['genre_id']
                
    string_data = {
        'old_disk_fk': kwargs['old_disk_id'],
        'old_string_number': kwargs['id'],
        'new_performer_fk': new_performer_id,
        'new_track_fk': new_track_id,
        'new_genre_fk': new_genre_id,
        'new_duration': kwargs['new_duration'],
    }

    if kwargs['new_performer_name'] or kwargs.get('new_track_title') or kwargs.get('new_genre_title') or kwargs.get('new_duration'):
        response = requests.post(change_string, json=string_data)