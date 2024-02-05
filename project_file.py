#importing streamlit library

import streamlit as st

#from PIL 
import Image



#opening the image

image = Image.open('MAPbBr_3.eps')



#displaying the image on streamlit app

st.image(image, caption='Band Structure and Density of states for Methyl ammonia lead bromide perovskite')


