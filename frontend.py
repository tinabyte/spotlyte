from turtle import color
from urllib import request
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from streamlit_option_menu import option_menu
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
import time
import pandas as pd
from io import StringIO



st.set_page_config(page_title="SpotLyte webpage", page_icon=":)", layout="wide")

pagecolor = """
<style>
[data-testid = "stAppViewContainer"]{
background-color: #0f1017;
}
</style>
"""




#setting up the lottie url
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#linking into the css file 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

#part of the page navigation
selected = option_menu(
    menu_title=None,
    options = ["Home","Educational","Other compressions"],
    icons=["house","book","file-earmark-lock"],
    menu_icon="cast",
    default_index= 0,
    orientation = "horizontal",
    styles={
            "padding": "20px",
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#6c744c"},
            "nav-link-selected": {"background-color": "#6c744c"},
        }
    
)


#Initializing the elements
loadingbar = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_mbrocy0r.json")
pacman = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_zBlJVT.json")
spotlight = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_dt51mmkh.json")

#When in the home page
if selected == "Home":
    st.markdown("<h1 style='text-align: center; font-size: 100px; color: #f3eb0c;'> Welcome to spotlyte </h1>", unsafe_allow_html=True)    
    st.markdown("<h1 style='text-align: center; color: white;'> A magical filter to spotlyte the important parts of a long video.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:20px; color: white;'> Have you ever watched through a long lecture recording that reiterated the same information? Spotlyte filters that out for you. Utilizing our machine learning algorithm and parsing through long, tedious, lectures, it spotlytes the important parts of the video so you save time when reviewing for classes through lectures. This makes studying and reviewing easier and more convenient than ever.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:20px; color: white;'> Spotlyze can also be utilized for other long tedious videos like security videos. Allowing hours of review time to be reduced to mere minutes, allowing catching crime to be more efficient and effective for law enforcement. This enables for a safer community and happier life..</p>", unsafe_allow_html=True)
    st_lottie(spotlight, height=250)

    
#When in the educational page
if selected == "Educational":
    
    st.markdown("<h1 style='text-align: left; font-size: 30px; color:#ffc21c ;'>spotlyte</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;font-size: 20px; color: white;'> Paste your educational URL below to spotlyte the important parts of the lesson (ex: Zoom or YouTube).</h1>", unsafe_allow_html=True)
    st_lottie(loadingbar, height=400, key = "coding3")
    url = st.text_input("Paste the URL to cut through😁")#creates box to take in the URL
    uploaded_file = st.file_uploader("or... choose a MP3 file to upload 🎵")#creating box to upload file
    title = st.text_input('or... paste in the text📁')
    if uploaded_file is not None:
        audio = uploaded_file.getvalue()
        st.audio(audio)


    if url != "":
        selected = "Results"
        vid_id = 'Xh2TY0DMbas'
        data = yta.get_transcript(vid_id)
        transcript = ''
        for value in data:
            for key,val in value.items():
                if key == 'text':
                    transcript += val
                    
        l = transcript.splitlines()
        final_tran = " ".join(l)

        file = open("youtube.txt", 'w')
        file.write(final_tran)
        file.close()
        st.markdown("<h1 style='text-align: left; font-size: 30px; color:#ffc21c ;'>Now.. the important part</h1>", unsafe_allow_html=True)
        st.markdown(final_tran)

        #audio component of the code
        audio1 = open("audioTest.mp3", "rb")
        st.audio(audio1)
        st.download_button(
            label="Download audio data",
            data="mp3",
            file_name='audioTest.mp3',
            #mime='text/csv',
            )



    #Setting the page background color
st.markdown(pagecolor, unsafe_allow_html=True)

