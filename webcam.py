# import cv2
# import streamlit as st

# st.title("Webcam Application")
# run = st.checkbox('Run')
# FRAME_WINDOW = st.image([])
# cam = cv2.VideoCapture(0)
# st.write("---captured images---", cam)
# while run:
#     ret, frame = cam.read()
#     st.write("---read images---", type(ret), type(frame), ret)
# #     FRAME_WINDOW.image(frame)
#     st.write("---showed images---")
    
    
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     FRAME_WINDOW.image(frame)
# else:
#     st.write('Stopped')

import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

faceCascade = cv2.CascadeClassifier(cv2.haarcascades+'haarcascade_frontalface_default.xml')


class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.i = 0

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        i =self.i+1
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (95, 207, 30), 3)
            cv2.rectangle(img, (x, y - 40), (x + w, y), (95, 207, 30), -1)
            cv2.putText(img, 'F-' + str(i), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

        return img

webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
