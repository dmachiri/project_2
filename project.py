import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def read_csv_file('al.csv'):
    df = pd.read_csv('al.csv')
    return df


def plot_counters(df, enter_col, exit_col):
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df[enter_col], label='Enter')
    ax.plot(df[exit_col], label='Exit')
    ax.set_xlabel('Time')
    ax.set_ylabel('Count')
    ax.legend()
    st.pyplot(fig)



