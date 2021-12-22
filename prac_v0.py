import streamlit as st
from PIL import Image

#----
st.title("--Image Visualize--")
ip_image=st.file_uploader("--please upload an image--", type="jpg")
st.write("-your imput image-")
st.image(ip_image,caption="--your input image--")
#-----
