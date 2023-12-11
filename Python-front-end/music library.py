import streamlit as st
from streamlit_option_menu import option_menu

from home import create_home_page, __click_disk
from disk.edit_disk import create_edit_disk_page
from disk.create_disk import create_create_disk_page, get_data

with open('./style.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

__page = 'home'


selected = option_menu('Music Library', ["Home", "Disk", "Track", "Performer", 'Genre'],
                           icons=['house', 'vinyl-fill', "music-note-list", "person-fill", 'music-player-fill'],
                           menu_icon="cast", default_index=0, orientation="horizontal", key='menu')


if selected == 'Disk':
    selected_disk_page = st.selectbox("Add, Edit or Delete", ['Add', 'Delete', 'Edit'])
    if selected_disk_page == "Add":
        create_create_disk_page()
    elif selected_disk_page == "Delete":
        pass
    elif selected_disk_page == "Edit":
        create_edit_disk_page()
elif selected == 'Home':
    create_home_page()
elif selected == 'Track':
    selected_track_page = st.selectbox("Add, Edit or Delete", ['Add', 'Delete', 'Edit'])
    if selected_track_page == "Add":
        pass
    elif selected_track_page == "Delete":
        pass
    elif selected_track_page == "Edit":
        pass
elif selected == 'Performer':
    selected_performer_page = st.selectbox("Add, Edit or Delete", ['Add', 'Delete', 'Edit'])
    if selected_performer_page == "Add":
        pass
    elif selected_performer_page == "Delete":
        pass
    elif selected_performer_page == "Edit":
        pass
elif selected == 'Genre':
    selected_genre_page = st.selectbox("Add, Edit or Delete", ['Add', 'Delete', 'Edit'])
    if selected_genre_page == "Add":
        pass
    elif selected_genre_page == "Delete":
        pass
    elif selected_genre_page == "Edit":
        pass


