from webcam import webcam
import streamlit as st


source = st.sidebar.selectbox( "Image Source? ", ('Test Image', 'Upload', 'Webcam') )
if source == 'Webcam':
    captured_image = webcam()
    
if captured_image is None:
    st.write("Waiting for image...")
else:
    st.write("Got an image from the {}:".format(source.lower()))
