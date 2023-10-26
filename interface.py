import streamlit as st
import cv2
import tempfile
import numpy as np


def writeBYTESIO(filename, bytesio):
    with open(filename,"wb") as outfile:
        outfile.write(bytesio.getbuffer())

def generate(arr):
    ans = []
    for x in arr:
        if x == 0:
            ans.append("Red")
        elif x == 1:
            ans.append("Green")
    return ans



st.title("----------TempInterface----------")
st.header("------------------Upload here------------------")

uploaded_file = st.file_uploader("Upload a .mp4 file", ['mp4'])
temp_file_to_save = './temp_file_1.mp4'
temp_file_result = './temp_file_2.mp4'

if uploaded_file is not None:
    video_bytes = uploaded_file.read()
    st.video(video_bytes)
    # tfile = tempfile.NamedTemporaryFile(delete=False) 
    # tfile.write(uploaded_file.read())
    # video = cv2.VideoCapture(tfile.name)
    # duration = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # st.text(duration)
    # st.divider()
    writeBYTESIO(temp_file_to_save, uploaded_file)
    cap = cv2.VideoCapture(temp_file_to_save)
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = frames/fps
    st.text(int(duration))
    arr = np.random.randint(2,size=int(duration))
    st.divider()
    st.text(generate(arr))










