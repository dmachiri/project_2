import streamlit 
import pandas 
 
streamlit.write("""
# My first app
Band structure*
""")
 
df = pandas.read_csv("my_data.csv")
streamlit.line_chart(df)
