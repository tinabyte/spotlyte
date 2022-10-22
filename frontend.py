from turtle import color
from urllib import request
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from streamlit_option_menu import option_menu
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re


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
loadingbar = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_DGRf6G.json")
pacman = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_zBlJVT.json")
spotlight = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_dt51mmkh.json")

#When in the home page
if selected == "Home":
    st.markdown("<h1 style='text-align: center; font-size: 100px; color: #f3eb0c;'> Welcome to spotlyte </h1>", unsafe_allow_html=True)    
    st.markdown("<h1 style='text-align: center; color: white;'> A magical filter to spotlyte the important parts of a long video.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:20px; color: white;'> Spotlyte enables you to highlight the important parts of a video so that you get straight to the point. Spotylte is a versitale application that utilizes _____, _____, and _______ to showcase the critical information in a user friendly way. In the age of the internet we have access through YouTube to millions of hours of content. We aim to use the internet to improve accessibility and access to information. With our software Spotly</p>", unsafe_allow_html=True)
    st_lottie(spotlight, height=250)
    

#When in the educational page
if selected == "Educational":
    st.markdown("<h1 style='text-align: left; font-size: 30px; color:#ffc21c ;'>spotlyte</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;font-size: 20px; color: white;'> Paste your educational URL below to spotlyte the important parts of the lesson (ex: Zoom or YouTube).</h1>", unsafe_allow_html=True)
    url = st.text_input("Paste the URL to cut through😁")
    if url != "":
        st.markdown("this is printing the url proving it's working: " + str(url))
        st_lottie(loadingbar, height=350, key = "coding3")


                

    #Setting the page background color
st.markdown(pagecolor, unsafe_allow_html=True)

