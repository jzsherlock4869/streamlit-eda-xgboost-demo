import os
import streamlit as st
import psutil
import pandas as pd
import matplotlib.pyplot as plt

def plot_pie_chart(names, values, explode, figsize, title):
    # fig1, ax1 = plt.subplots(1, 5, figsize=figsize)
    fig1 = plt.figure(figsize=figsize)
    ax1 = plt.axes()
    ax1.pie(values, explode=explode, labels=names, autopct='%1.1f%%',
            shadow=True, startangle=90, textprops={'fontsize': 14})
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('off')
    ax1.set_title(title, fontdict={'fontsize': 24, 'fontweight': 'medium'})
    st.pyplot(fig1)

def get_memory_status():
    mem = psutil.virtual_memory()
    names = ['used', 'avail']
    values = [mem.used / (1024 ** 3), mem.available / (1024 ** 3)]
    explode = [0.1, 0]
    # print(values)
    plot_pie_chart(names, values, explode, figsize=(4, 4), title='CURRENT MEMORY USE')

def get_cpu_status():
    cputime = psutil.cpu_times()
    names = ['user', 'sys', 'idle']
    values = [cputime.user, cputime.system, cputime.idle]
    explode = [0.1, 0, 0]
    # print(values)
    plot_pie_chart(names, values, explode, figsize=(4, 4), title='CURRENT CPU STATUS')

def get_current_procs():
    df = pd.DataFrame(columns=['pid', 'process_name'])
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            df = df.append({'pid': processID, 'process_name': processName}, ignore_index=True)
            if len(df) >= 5:
                break
            # print(processName , ' ::: ', processID)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # print('process exception occurs')
            pass
    # print(df)
    st.dataframe(df)

def show_server_status():
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.header("MEMORY")
        get_memory_status()
    with col2:
        st.header("CPU")
        get_cpu_status()
    with col3:
        st.header("CURRENT PROCS")
        get_current_procs()