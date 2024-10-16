import streamlit as st
import pandas as pd
import json

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Wearable Technology',
    page_icon='https://utfs.io/f/alMZB5gCXzuS24GQqTWocmbORYtfUTyMF045CuwrBzZv9sjL',
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #f0f8ff;
    }
    .css-18e3th9 {
        padding: 2rem 1rem;
    }
    .css-1d391kg {
        padding: 2rem 1rem;
    }
    h1, h2 {
        color: #2c3e50;
        text-align: center;
    }
    .profile-info {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .profile-info p {
        margin-bottom: 10px;
        font-size: 16px;
    }
    .profile-info strong {
        color: #3498db;
    }
</style>
""", unsafe_allow_html=True)

def read_profiles_from_json(filename='user_profiles.json'):
    with open(filename, 'r') as json_file:
        profiles = json.load(json_file)
    return profiles

def display_user_profile(profile):
    """
    Displays the user profile based on the is_new status.

    Args:
        profile (dict): The user profile dictionary.
    """
    if profile['is_new']:
        # Display content for new users
        st.header("Welcome to Our Community!")
        with st.container():
            st.markdown('<div class="profile-info">', unsafe_allow_html=True)
            st.info(f"**Name:** {profile['name']}")
            st.info(f"**Age:** {profile['age']}")
            st.info(f"**Instagram Profile:** {profile['instagram_profile']}")
            st.info(f"**More Details:** {profile['description']}")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Display content for returning users
        st.header("Welcome Back!")
        st.subheader("We missed you!")
        with st.container():
            st.write(f"**Name:** {profile['name']}")
            st.write(f"**Age:** {profile['age']}")
            st.write(f"**Instagram Profile:** {profile['instagram_profile']}")
            st.write(f"**Description:** {profile['description']}")
            st.markdown('</div>', unsafe_allow_html=True)

# Get the user_id from the URL parameters
user_id = st.query_params.get("user_id", [None])[0]
user_id = "1000" + user_id

if user_id:
    user_profiles = read_profiles_from_json()
    profile = user_profiles.get(user_id)

    if profile:
        display_user_profile(profile)
    else:
        st.error(f"User ID {user_id} not found.")
else:
    st.error("No user ID provided.")