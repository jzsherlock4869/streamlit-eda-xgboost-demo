import streamlit as st
import cv2
import os
import pandas as pd
import os.path as osp
import json
from datetime import datetime

from api_manage.dataset_manager import dataset_update


storage_root = '../streamlit_xgb_storage'

def load_dataset(dataset_name):
    data_path = osp.join(storage_root, 'datasets', dataset_name, 'data.csv')
    info_path = osp.join(storage_root, 'datasets', dataset_name, 'info.json')
    df = pd.read_csv(data_path)
    with open(info_path) as f_json:
        info = json.load(f_json)
    return df, info

def cal_ks(factor, target):
    # continous factor
    return # pd.Series


def cal_woe(factor, target):
    # bins / categorical factor
    return # pd.Series


def get_hist(factor):
    # continous or categorical
    return

def cut_bins(factor, target):
    # continous
    return

def feature_main():
    st.title('Feature Analysis & Engineering')
    dataset_names = dataset_update()
    dataset_name = st.sidebar.selectbox('Select dataset', options=dataset_names)
    if st.sidebar.button('Load'):
        df, df_info = load_dataset(dataset_name)
        st.sidebar.write('Load success')
        st.write(df_info)
        feat_names = list(df.keys())
        st.write('Feature names : ', feat_names)
        target_col = df_info["target_col"]
        feat_name = st.sidebar.selectbox('Select a single factor', options=feat_names)
        target, sel_feat = df[target_col], df[feat_name]
        



