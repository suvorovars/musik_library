import streamlit as st
from streamlit_option_menu import option_menu

from home import create_home_page, __click_disk
from edit_disk import create_edit_disk_page

with open('./style.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

__page = 'home'


if __name__ == '__main__':
    selected = option_menu('Music Library', ["Home", "Create Disk", "Edit Disks", "Search", 'Settings'],
                            icons=['house', 'plus-circle', "pencil-square", "search", 'gear'],
                            menu_icon="cast", default_index=0, orientation="horizontal")

    if selected == 'Edit Disk':
        create_edit_disk_page()
        print(selected)
    if selected == 'Home':
        create_home_page()
    if selected == 'Create Disk':
        pass