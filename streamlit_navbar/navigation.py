import streamlit as st
import cv2
import sys

from api_home.welcome import welcome
from api_home.server_status import show_server_status
from api_eda.data_analysis import load_raw_data
from api_manage.dataset_manager import dataset_main
from api_feature.feature_engine import feature_main

def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path

if navigation() == "home":
    welcome()
    show_server_status()

elif navigation() == "manage":
    # TODO: task management
    dataset_main()

elif navigation() == "eda":
    load_raw_data()

elif navigation() == "feature":
    feature_main()
    for item in range(5):
        st.write(f'TO BE CONT\'D {item}')

elif navigation() == "eval":
    st.title('Examples Menu')
    st.write('Select an example.')

elif navigation() == "eval":
    st.title('Examples Menu')
    st.write('Select an example.')

# elif navigation() == "logs":
#     st.title('View all of the logs')
#     st.write('Here you may view all of the logs.')


# elif navigation() == "verify":
#     st.title('Data verification is started...')
#     st.write('Please stand by....')


# elif navigation() == "config":
#     st.title('Configuration of the app.')
#     st.write('Here you can configure the application')
