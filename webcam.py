import cv2
import streamlit as st

st.title("Webcam Application")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)
st.write("---captured images---")
while run:
    ret, frame = cam.read()
    st.write("---read images---")
    FRAME_WINDOW.image(frame)
    st.write("---showed images---")
    
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
