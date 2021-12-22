import streamlit as st
from PIL import Image

#----
st.title("--Image Visualize--")
ip_image=st.file_uploader("--please upload an image--", type="jpg")
if ip_image not None:
  image = Image.open(ip_image)

  st.write("-your imput image-")
  st.image(image,caption="--your input image--")
#-----
