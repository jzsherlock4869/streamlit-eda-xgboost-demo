import streamlit as st
import cv2
from api_home.welcome import welcome
from api_eda.data_analysis import load_raw_data

def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path


if navigation() == "home":
    welcome()

elif navigation() == "eda":
    load_raw_data()

elif navigation() == "modeling":
    st.title('Results List')
    for item in range(5):
        st.write(f'Results {item}')

elif navigation() == "eval":
    st.title('Examples Menu')
    st.write('Select an example.')


elif navigation() == "logs":
    st.title('View all of the logs')
    st.write('Here you may view all of the logs.')


elif navigation() == "verify":
    st.title('Data verification is started...')
    st.write('Please stand by....')


elif navigation() == "config":
    st.title('Configuration of the app.')
    st.write('Here you can configure the application')
