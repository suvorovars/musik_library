import streamlit as st
import requests
import pandas as pd

from time import gmtime, strftime

from generate_img import generate_image

__click_disk = None


def create_home_page():
    click_disk = None
    response = requests.get('http://localhost:8000/api/get/strings')

    for disk in response.json():
        col1, col2 = st.columns([1, 2])

        if disk['strings']:
            df = pd.DataFrame.from_dict(disk['strings'], orient='columns')
            df = df.sort_values(by='number')[['number', 'track_title', 'performer_name', 'genre_title', 'duration']]
        with col1:
            img = generate_image(f"""{disk['disk_title']}
                        {disk['year']}
                        """)
            st.image(img)
            _, button_col = col1.columns(2)
            with button_col:
                if disk['strings']:
                    st.text(f"listening time is {strftime('%M:%S', gmtime(df['duration'].sum()))}")
                st.button(f'Edit {disk["disk_title"]}', on_click=click_button, args=(disk['disk_title'], ))

        with col2:
            if disk['strings']:
                st.table(df)
            else:
                st.text("Пока нет ни одной песни")


def click_button(args):
    global __click_disk
    __click_disk = args
    print(args)