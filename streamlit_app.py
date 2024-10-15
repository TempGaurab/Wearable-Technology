import streamlit as st
import pandas as pd
import json
# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Wearable Technology',
    page_icon='https://utfs.io/f/alMZB5gCXzuS24GQqTWocmbORYtfUTyMF045CuwrBzZv9sjL', # This is an emoji shortcode. Could be a URL too.
)

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
        st.write(f"**Name:** {profile['name']}")
        st.write(f"**Age:** {profile['age']}")
        st.write(f"**Instagram Profile:** {profile['instagram_profile']}")
        st.write(f"**More Details:** {profile['description']}")
    else:
        # Display content for returning users
        st.header("Welcome Back!")
        st.subheader("We missed you!")
        st.write(f"**Name:** {profile['name']}")
        st.write(f"**Age:** {profile['age']}")
        st.write(f"**Instagram Profile:** {profile['instagram_profile']}")
        st.write(f"**Description:** {profile['description']}")


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