import streamlit 
import pandas 
 
streamlit.write("""
# My first app
Density of states*
""")

streamlitt.image('dos.jpg', caption='Density of states for FCC Aluminium metal')


df = pandas.read_csv("al.csv")
streamlit.line_chart(df)
