import streamlit as st
from streamlit_option_menu import option_menu

from generate_img import generate_image
from home import create_home_page

with open('./style.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

page = 'home'


if __name__ == '__main__':
    selected = option_menu(None, ["Home", "Create Disk", "Edit Disks", "Search", 'Settings'],
                            icons=['house', 'plus-circle', "pencil-square", "search", 'gear'],
                            menu_icon="cast", default_index=0, orientation="horizontal")
    if selected == 'Home':
        create_home_page()
    elif selected == 'Create Disk':
        pass