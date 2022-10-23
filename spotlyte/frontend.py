
from cgi import test
from cgitb import small
from distutils.command.upload import upload
from imp import load_source
from json import load
#from termios import EXTA
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
from PIL import Image
import base64





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
    options = ["Home","Educational"],
    icons=["house","book","file-earmark-lock"],
    menu_icon="cast",
    default_index= 0,
    orientation = "horizontal",

    
    styles={
            "padding": "0px",
            "icon": {"color": "orange", "font-size": "30px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#6c744c"},
            "nav-link-selected": {"background-color": "#6c744c"},

        }
    
)

st.write("")
st.write("")

#Initializing the elements
pacmanEat = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_uhovpivr.json")
pacmanChar = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_ctiEUT.json")
#computer = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_mbrocy0r.json")
pacman = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_zBlJVT.json")
supportingComp = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_uhovpivr.json")
#When in the home page


if selected == "Home":
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st_lottie(pacman, height=120)
    with col2:
        st.image("testimage.png")
    with col3:
        st_lottie(pacmanChar, height=80)

    col, colz, colx = st.columns([1,3,1])
    with col:
        st.write("")
    with colz:
        st.image("statement.png", width=900)
    with colx:
        st.write("")

    st.write("")
    col1, col2, col3, col4 = st.columns([1,3,3,1])
    with col1:
        st.markdown("")
    with col2:
        st.markdown("<h1 style='text-align: center; font-size:30px; color: #18ccc4;'>Our function.</h>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size:20px; color: white;'> Spotlyte is a multipurpose audio, video, and text converter that that allows you to input a long and tedious file and returns the important outlined parts of it. It does this by utilizing APIs and machine learning algorithms to detect what is important in a long file. </p>", unsafe_allow_html=True)
    with col3:
         st.markdown("<h1 style='text-align: center; font-size:30px; color: #f83c1c;'>Our mission. </h>", unsafe_allow_html=True)
         st.markdown("<p style='text-align: center; font-size:20px; color: white;'>Spotlyte’s mission is to help level up students’ education. Students have busy schedules and efficiently studying for classes is essential to success in classes. Allowing for the compression of long recorded lectures into outlined PDF and audio files for quick reviewing and listening to while commuting throughout the day. This makes studying and reviewing easier and more convenient than ever.</p>", unsafe_allow_html=True)
    with col4:
        st.markdown("")

    col1, col2, col3= st.columns([1,3,1])
    with col1:
        st.markdown("")
    with col2:
        st.markdown("<h1 style='text-align: center; font-size:30px; color: #ffac1c;'>How to use our site....</h>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size:20px; color: white;'>First, head over to the “education tab”  on the top and import which file you want to ‘Spotlyte’. Then, click enter and In return, it will give you the important keywords and data from your long, tedious files into a form of downloadable data. This is the power up you need in academics. </p>", unsafe_allow_html=True)
    with col3:
        st.markdown("")





def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


#When in the educational page
if selected == "Educational":
    st.image("smalltest2.png")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    
    col1, col2, col3, col4 = st.columns([1,4,4,1])
    with col1:
        st.write("")
    with col2:
        st.image("pacsim.png", width=530)
        #st_lottie(computer, height=300, key = "coding3")
    with col3:
        st.markdown("<h1 style='text-align: center;font-size: 30px; color: white;'> Paste your educational URL below to spotlyte the important parts of the lesson (ex: Zoom or YouTube).</h1>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload your video", type=["mp4","mp3","docx","pdf"]) #THE DATA IS PASSED TO API
        userTextInput = st.text_input('or... paste in the text📁') #THIS IS PASSED TO API
        url = st.text_input("Paste the URL to cut through😁") #THIS IS PASSED TO API
        st.write("")


    
    #When there is a file (mp3) then this code runs
    if uploaded_file is not None:
        audio = uploaded_file.getvalue() #when mp3 uploaded, it is now the audio variable
        
        #st.audio(audio)
        #---CODE FOR API GOES HERE
        #---CODE FOR API GOES HERE
        #---CODE FOR API GOES HERE


        #with open(pdfFromAPI.name, "wb") as f:
            #f.write(uploaded_file.getbuffer())

        col1, col2, col3 = st.columns([1,3,1])
        with col1:
            st.write("")
        with col2:
            st.markdown("<h1 style='text-align: left;font-size: 30px; color: #ffc21c;'>All of that information is now spotlyted here...</h1>", unsafe_allow_html=True)
            st.markdown("") #PLUG IN THE TEXT VARIABLE HEREEEE
            #show_pdf(uploaded_file.name) 
        with col3:
            st.write("")




    #When the text box is not empty then this code runs
    if url != "":
        #-----------------API GOES HERE API GOES HERE API GOES HERE
        st.write("")#placeholder
        #audio download button




    #Setting the page background color
st.markdown(pagecolor, unsafe_allow_html=True)

