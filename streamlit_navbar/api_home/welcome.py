import streamlit as st
import cv2
import os

def welcome():
    st.title('Home')
    st.write('Welcome to Auto Modeling Platform')
    st.write('Created by @jzsherlock4869')
    try:
        default_img = cv2.imread('static/images/default.jpg')
        st.image(default_img)
    except:
        pass
    os.makedirs('../streamlit_xgb_storage', exist_ok=True)
