#importing streamlit library

import streamlit as st

from PIL import Image

image = Image.open('MAPbBr_3.eps')

st.image(image, caption='Band Structure and Density of states for Methyl ammonia lead bromide perovskite')


