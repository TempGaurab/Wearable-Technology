import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import json
import requests

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Wearable Technology',
    page_icon='https://utfs.io/f/alMZB5gCXzuS24GQqTWocmbORYtfUTyMF045CuwrBzZv9sjL',
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-weight: bold;
    color: #1E88E5;
}
.info-box {
    background-color: #E3F2FD;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}
.profile-header {
    text-align: center;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def read_profiles_from_json(filename='user_profiles.json'):
    with open(filename, 'r') as json_file:
        profiles = json.load(json_file)
    return profiles

def display_new_user_profile(profile):
    st.markdown('<div class="profile-header"><h1 class="big-font">Welcome to Our Community!</h1></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("Profile Information")
        st.write(f"**Name:** {profile['name']}")
        st.write(f"**Age:** {profile['age']}")
        st.write(f"**Instagram Profile:** [{profile['instagram_profile']}](https://instagram.com/{profile['instagram_profile']})")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("More About Me")
        st.write(profile['description'])
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        lottie_url = "https://assets5.lottiefiles.com/packages/lf20_ncpnijkz.json"
        lottie_welcome = load_lottieurl(lottie_url)
        st_lottie(lottie_welcome, key="welcome", height=300)

        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("Quick Tips")
        st.write("• Complete your profile")
        st.write("• Connect with others")
        st.write("• Explore our features")
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Start Exploring!", key="explore_button"):
        st.balloons()
        st.success("Welcome aboard! Let's begin your journey with us.")

def display_returning_user_profile(profile):
    st.markdown('<div class="profile-header"><h1 class="big-font">Welcome Back!</h1></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("Your Profile")
        st.write(f"**Name:** {profile['name']}")
        st.write(f"**Age:** {profile['age']}")
        st.write(f"**Instagram Profile:** [{profile['instagram_profile']}](https://instagram.com/{profile['instagram_profile']})")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("Your Bio")
        st.write(profile['description'])
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        lottie_url = "https://assets3.lottiefiles.com/packages/lf20_khzniaya.json"
        lottie_welcome_back = load_lottieurl(lottie_url)
        st_lottie(lottie_welcome_back, key="welcome_back", height=300)

        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("What's New")
        st.write("• Check out our latest features")
        st.write("• Update your profile")
        st.write("• Connect with new members")
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Explore New Features", key="explore_new_features"):
        st.success("Exciting! Let's see what's new for you.")

def display_user_profile(profile):
    if profile['is_new']:
        display_new_user_profile(profile)
    else:
        display_returning_user_profile(profile)

# Main execution
user_id = st.query_params.get("user_id", [None])[0]
if user_id:
    user_id = "1000" + user_id
    user_profiles = read_profiles_from_json()
    profile = user_profiles.get(user_id)

    if profile:
        display_user_profile(profile)
    else:
        st.error(f"User ID {user_id} not found.")
else:
    st.error("No user ID provided.")