import streamlit as st
from PIL import Image

st.title('This is Qi``anaaaaaa``aaa')

image = Image.open('./profile.png')

st.image(image)