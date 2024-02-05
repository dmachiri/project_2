#importing streamlit library

import streamlit as st

from PIL import Image



#opening the image

image = Image.open('imagefile')



#displaying the image on streamlit app

st.image(image, caption='Enter any caption here')


