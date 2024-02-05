import streamlit 
import pandas 
 
streamlit.write("""
# My first app
Hello *world!*
""")
 
df = pandas.read_txt("my_data.txt")
streamlit.line_chart(df)
