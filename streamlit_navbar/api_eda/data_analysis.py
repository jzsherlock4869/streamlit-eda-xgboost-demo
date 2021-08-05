from os import write
import streamlit as st
import pandas as pd
import os.path as osp
from glob import glob
import cv2
from functools import partial

def color_positive_red(pos, val):
    color = 'red' if val == pos else 'white'
    return 'color: {}'.format(color)

def load_raw_data():
    root_dir = st.sidebar.text_input('dataset dir', value='../archive/german_credit', key=None)
    candidate_files = list(glob(osp.join(root_dir, '*.csv')))
    filepath = st.sidebar.selectbox('select file', candidate_files, index=0)
    try:
        n_rows = st.sidebar.slider('num of rows to show', min_value=100, max_value=5000, value=200, step=100)
        df = pd.read_csv(filepath)
        st.sidebar.write('show row number '+ str(n_rows))
        df = df[:n_rows]
        st.title('Raw data table')
        st.write('Filename: {}'.format(osp.basename(filepath)))
        feature_names = list(df.keys())
        if 'Unnamed: 0' in feature_names:
            feature_names.remove('Unnamed: 0')
        sel_cols = st.sidebar.multiselect(label='select columns to be used', options=feature_names, default=feature_names[0])
        st.sidebar.write("Total {} cols selected for analysis".format(len(sel_cols)))
        sel_target = st.sidebar.selectbox(
            'Select the target column',
            sel_cols,
            )
        pos_neg = list(df[sel_target].unique())
        pos_label = st.sidebar.selectbox(
            'Select positive label',
            pos_neg)
        st.sidebar.write("Training Target is : {}, with {} as positive".format(sel_target, pos_label))
        st.dataframe(df[sel_cols].style.applymap(partial(color_positive_red, pos_label)), 2000, 500)
    except:
        default_img_path = "./static/images/default.jpg"
        default_img = cv2.imread(default_img_path)
        st.title('Ooops... raw data seems failed to be loaded')
        st.image(default_img)
        print('[error] not valid file path for csv file')
    
