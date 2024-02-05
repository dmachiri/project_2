import streamlit 
import pandas 
 
streamlit.write("""
# My first app
Band structure*
""")
 
df = pandas.read_csv("bands.csv")
streamlit.line_chart(df)
