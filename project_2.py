import streamlit 
import pandas 
 
streamlit.write("""
# My first app
Band structure*
""")
 
df = pandas.read_csv("al.csv")
streamlit.line_chart(df)
sstreamlit_echarts(
    options=option, height="10px",
)
