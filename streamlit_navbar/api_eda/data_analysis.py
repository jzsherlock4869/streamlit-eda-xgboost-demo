import streamlit as st
import pandas as pd
import os.path as osp
from glob import glob
import cv2
import os
import json
from functools import partial
import traceback
from copy import copy

def color_positive_highlight(pos, night, val):
    if night:
        pos_clr, neg_clr = 'yellow', 'white'
    else:
        pos_clr, neg_clr = 'red', 'black'
    color = pos_clr if val == pos else neg_clr
    return 'color: {}'.format(color)

def load_raw_data():
    root_dir = st.sidebar.text_input('dataset dir', value='../archive/german_credit', key=None)
    candidate_files = list(glob(osp.join(root_dir, '*.csv')))
    filepath = st.sidebar.selectbox('select file', candidate_files, index=0)
    try:
        # load raw data
        n_rows = st.sidebar.slider('num of rows to show', min_value=100, max_value=5000, value=200, step=100)
        df = pd.read_csv(filepath)
        st.sidebar.write('show row number '+ str(n_rows))
        df = df[:n_rows]
        st.title('Raw Data Table')
        st.write('Filename: {}'.format(osp.basename(filepath)))
        feature_names = list(df.keys())
        if 'Unnamed: 0' in feature_names:
            feature_names.remove('Unnamed: 0')
        sel_cols = st.sidebar.multiselect(label='select columns to be used', options=feature_names,\
            default=feature_names[:5])
        st.sidebar.write("Total {} cols selected for analysis".format(len(sel_cols)))

        # select target column and label to be predicted
        sel_target = st.sidebar.selectbox(
            'Select the target column',
            sel_cols,
            )
        pos_neg = list(df[sel_target].unique())
        pos_label = st.sidebar.selectbox(
            'Select positive label',
            pos_neg)
        st.sidebar.write("Training Target is : {}, with {} as positive".format(sel_target, pos_label))
        night = st.sidebar.checkbox('Black Background')
        st.dataframe(df[sel_cols].style.applymap( \
            partial(color_positive_highlight, pos_label, night)\
            ), 2000, 500)

        # save to storage as a new dataset
        dataset_name = st.text_input('dataset name: ', value='')
        if st.button('Save the dataset'):
            if dataset_name:
                save_csv_path = os.path.join('../streamlit_xgb_storage', 'datasets', dataset_name)
                os.makedirs(save_csv_path, exist_ok=True)
                df[sel_cols].to_csv(os.path.join(save_csv_path, 'data.csv'), index=False)
                feat_cols = copy(sel_cols)
                feat_cols.remove(sel_target)
                dataset_info = {
                                'raw_path': filepath, 
                                'target_col': sel_target,
                                'features_used': '|'.join(feat_cols),
                                'pos_label': str(pos_label)
                                }
                # print(dataset_info)
                with open(os.path.join(save_csv_path, 'info.json'), 'w') as f_json:
                    json.dump(dataset_info, f_json, indent=4)
                st.write('Dataset {} saved ~'.format(dataset_name))
            else:
                st.write('Please assign a dataset name !')
        
    except Exception as ex:
        traceback.print_exc()
        default_img_path = "./static/images/default.jpg"
        default_img = cv2.imread(default_img_path)
        st.title('Ooops... seems something wrong happened')
        st.image(default_img)
    
