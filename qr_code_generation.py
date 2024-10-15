import qrcode
from PIL import Image
import requests
import json
import os


#this is to create qrcodes
def read_profiles_from_json(filename='user_profiles.json'):
    """
    Reads user profiles from a JSON file.

    Args:
        filename (str): The name of the JSON file to read. Default is 'user_profiles.json'.

    Returns:
        dict: The user profiles loaded from the JSON file.
    """
    with open(filename, 'r') as json_file:
        profiles = json.load(json_file)
    return profiles

def get_user_profile(user_profiles, user_id):
    profile = user_profiles.get(user_id)
    if profile:
        return profile
    else:
        return f"User ID {user_id} not found."

def generate_qr_code(user_id):
    # Generate a QR code encoding the user profile URL
    url = f"http://localhost:8501/?user_id={user_id}"
    qr_img = qrcode.make(url)
    return qr_img


user_profiles = read_profiles_from_json()
# Ensure the output directory exists
output_directory = "qr_codes"
os.makedirs(output_directory, exist_ok=True)

# Generate QR codes for all user profiles
for user_id in user_profiles.keys():
    qr_img = generate_qr_code(user_id)
    qr_img.save(os.path.join(output_directory, f"qr_code_{user_id}.png"))

print("QR codes generated for all user profiles.")
