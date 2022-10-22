from urllib import request
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="SpotLyte webpage", page_icon=":)", layout="wide")

pagecolor = """
<style>
[data-testid = "stAppViewContainer"]{
background-color: black;
}
</style>
"""

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_DGRf6G.json")
lottie_coding2 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_n7kzkgjp.json")

st.markdown("<h1 style='text-align: center; font-size: 70px; color: #ffc21c;'> spotlyte. </h1>", unsafe_allow_html=True)    
st.markdown("<h1 style='text-align: center; color: white;'> Deskscription blah blah blah </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'> more information about our website and stuff </p>", unsafe_allow_html=True)



with st.container():
    leftCol, rightCol = st.columns(2)
    with leftCol:
        st_lottie(lottie_coding2, height=300)


    with rightCol:
        #TEXT INPUT HERE 
        
        url = st.text_input("Paste the URL to cut through😁")




if url != "":
    st.markdown("this is printing the url proving it's working: " + str(url))
    st_lottie(lottie_coding, height=300, key = "coding3")
    
st.markdown(pagecolor, unsafe_allow_html=True)