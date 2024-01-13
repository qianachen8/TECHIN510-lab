import streamlit as st
from PIL import Image

st.title('This is Qianaaaaaaaaa')

image = Image.open('./profile.png')

st.image(image)