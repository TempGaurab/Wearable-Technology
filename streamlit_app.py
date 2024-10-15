import streamlit as st
import pandas as pd
from qr_code_generation import read_profiles_from_json
from creation_of_code import save_profiles_to_json

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Wearable Technology',
    page_icon='https://utfs.io/f/alMZB5gCXzuS24GQqTWocmbORYtfUTyMF045CuwrBzZv9sjL', # This is an emoji shortcode. Could be a URL too.
)

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

if user_id:
    user_profiles = read_profiles_from_json()
    profile = user_profiles.get(user_id)

    if profile:
        display_user_profile(profile)
    else:
        st.error(f"User ID {user_id} not found.")
else:
    st.error("No user ID provided.")