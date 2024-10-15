import json
#only run this if we want to get more user profiles, this is to create initial user list.
def generate_empty_user_profiles(num_profiles=10):
    """
    Generates a specified number of user profiles with empty placeholders.

    Args:
        num_profiles (int): Number of user profiles to generate. Default is 10.

    Returns:
        dict: A dictionary containing user profiles with empty fields.
    """
    users = {}

    for i in range(num_profiles):
        user_id = str(10000 + i)  # Generate unique user IDs starting from 10000
        users[user_id] = {
            "name": "",                # Placeholder for name
            "age": None,               # Placeholder for age
            "instagram_profile": "",   # Placeholder for Instagram profile
            "description": "",          # Placeholder for description
            "is_new": True
        }
    
    return users

def save_profiles_to_json(profiles, filename='user_profiles.json'):
    """
    Saves the user profiles to a JSON file.

    Args:
        profiles (dict): The user profiles to save.
        filename (str): The name of the JSON file. Default is 'user_profiles.json'.
    """
    with open(filename, 'w') as json_file:
        json.dump(profiles, json_file, indent=4)
    print(f"User profiles saved to {filename}")

# Generate user profiles
user_profiles = generate_empty_user_profiles(10)

# Save the generated profiles to a JSON file
save_profiles_to_json(user_profiles)