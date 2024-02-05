import streamlit 
import pandas 
 
streamlit.write("""
# My first app
Density of states*
""")

streamlit.image("dos", caption="Density of states for FCC Aluminium metal", output_format="auto" )


df = pandas.read_csv("al.csv")
streamlit.line_chart(df)
