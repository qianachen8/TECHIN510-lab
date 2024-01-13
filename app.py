import streamlit as st
from PIL import Image

st.title('This is Qiaaaaaaaa')

image = Image.open('./profile.png')

st.image(image)