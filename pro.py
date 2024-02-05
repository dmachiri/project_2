import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
 
## Load the data
data = pd.read_csv('al.csv')
 
## Create two columns
#col1, col2 = st.columns(2)
 
## Display the data table in the first column
#col1.dataframe(data)
 
## Create and display the bar chart in the second column
fig, ax = plt.subplots()
data.groupby('model')['sales'].sum().plot(kind='line', ax=ax)
#col2.pyplot(fig)
