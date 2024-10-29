import streamlit as st
import json

# Set the title and favicon
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
    .profile-info {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    h1, h2 {
        color: #2c3e50;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def read_profiles_from_json(filename='user_profiles.json'):
    with open(filename, 'r') as json_file:
        profiles = json.load(json_file)
    return profiles

def display_user_profile(profile):
    st.header("User Profile")
    st.info(f"**Name:** {profile['name']}")
    st.info(f"**Age:** {profile['age']}")
    st.info(f"**Instagram Profile:** {profile['instagram_profile']}")
    st.info(f"**Description:** {profile['description']}")

# Extract user_id from query params
query_params = st.experimental_get_query_params()
user_id = query_params.get("user_id", [None])[0]

# Display profile if user_id is provided
if user_id:
    user_profiles = read_profiles_from_json()
    profile = user_profiles.get(user_id)

    if profile:
        display_user_profile(profile)
    else:
        st.error(f"User ID {user_id} not found.")
else:
    st.info("No user ID provided in the URL.")
