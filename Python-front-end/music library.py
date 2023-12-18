import streamlit as st
from streamlit_option_menu import option_menu

from home import create_home_page

from disk.edit_disk import create_edit_disk_page
from disk.create_disk import create_disk_page
from disk.add_string import create_add_string_page
from disk.delete_disk import create_delete_disk_page

from genre.create_genre import create_genre_page
from genre.edit_genre import create_edit_genre_page
from genre.delete_genre import create_delete_genre_page

from performer.create import create_performer_page
from performer.edit import create_edit_performer_page
from performer.delete import create_delete_performer_page

from track.create import create_track_page
from track.edit import create_edit_track_page
from track.delete import create_delete_track_page

with open('./style.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

selected = option_menu('Music Library', ["Home", "Disk", "Track", "Performer", 'Genre'],
                           icons=['house', 'vinyl-fill', "music-note-list", "person-fill", 'music-player-fill'],
                           menu_icon="cast", default_index=0, orientation="horizontal", key='menu')


if selected == 'Disk':
    selected_disk_page = st.selectbox("Add, Edit or Delete", ['Add Disk', 'Delete', 'Edit', 'Add Track'])
    if selected_disk_page == "Add Disk":
        create_disk_page()
    elif selected_disk_page == "Add Track":
        create_add_string_page()
    elif selected_disk_page == "Delete":
        create_delete_disk_page()
    elif selected_disk_page == "Edit":
        create_edit_disk_page()
elif selected == 'Home':
    create_home_page()
elif selected == 'Track':
    selected_track_page = st.selectbox("Add, Edit or Delete", ['Add', 'Delete', 'Edit'])
    if selected_track_page == "Add":
        create_track_page()
    elif selected_track_page == "Delete":
        create_delete_track_page()
    elif selected_track_page == "Edit":
        create_edit_track_page()
elif selected == 'Performer':
    selected_performer_page = st.selectbox("Add, Edit or Delete", ['Add', 'Delete', 'Edit'])
    if selected_performer_page == "Add":
        create_performer_page()
    elif selected_performer_page == "Delete":
        create_delete_performer_page()
    elif selected_performer_page == "Edit":
        create_edit_performer_page()
elif selected == 'Genre':
    selected_genre_page = st.selectbox("Add, Edit or Delete", ['Add', 'Delete', 'Edit'])
    if selected_genre_page == "Add":
        create_genre_page()
    elif selected_genre_page == "Delete":
        create_delete_genre_page()
    elif selected_genre_page == "Edit":
        create_edit_genre_page()


