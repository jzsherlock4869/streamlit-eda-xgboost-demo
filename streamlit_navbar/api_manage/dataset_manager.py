import streamlit as st
import os
import json
import os.path as osp
import shutil as su
import traceback
import cv2
import sys

storage_root = '../streamlit_xgb_storage'

def dataset_update():
    dataset_path = osp.join(storage_root, 'datasets')
    dataset_names = os.listdir(dataset_path)
    return dataset_names

def dataset_delete(dataset_name):
    try:
        toberm = osp.join(storage_root, 'datasets', dataset_name)
        su.rmtree(toberm)
        return True
    except FileNotFoundError as ex:
        print('Error in dataset deletion', ex)
        return False

def dataset_show(dataset_name):
    info_path = osp.join(storage_root, 'datasets', dataset_name, 'info.json')
    with open(info_path) as f_json:
        info = json.load(f_json)
    return info

def dataset_main():
    st.title('Dataset Management')
    try:
        dataset_names = dataset_update()
        if st.button('Update'):
            dataset_names = dataset_update()
        st.header("Current dataset list")
        if len(dataset_names) > 0:
            for dataset_id, dataset_name in enumerate(dataset_names):
                st.subheader("Dataset [{}]: {}".format(dataset_id, dataset_name))
                info = dataset_show(dataset_name)
                st.write(" -- Total {} features, target is {}, created at {}\n"\
                    .format(len(info["features_used"].split("|")),\
                            info["target_col"],\
                            info["created_time"]))
            tobe_deleted = st.sidebar.selectbox('Delete dataset', options=dataset_names)
            if st.sidebar.button('Delete Now'):
                del_flag = dataset_delete(tobe_deleted)
                del_message = "Delete success" if del_flag else "Delete failed, check if dataset exist"
                st.sidebar.write(del_message)
                dataset_names = dataset_update()
                # dataset_names.remove(tobe_deleted)
            tobe_shown = st.sidebar.selectbox('Show info of dataset', options=dataset_names)
            st.header("Detailed info of selected dataset")
            show_info = dataset_show(tobe_shown)
            st.write(show_info)
        else:
            st.write("No datasets created now")
    
    except Exception as ex:
        traceback.print_exc()
        default_img_path = "./static/images/default.jpg"
        default_img = cv2.imread(default_img_path)
        st.title('Ooops... seems something wrong happened')
        st.image(default_img)




