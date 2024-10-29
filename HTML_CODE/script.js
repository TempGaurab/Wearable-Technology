function saveProfileToSessionStorage(profile, key = 'user_profiles') {
    const userProfiles = readProfilesFromSessionStorage(key);
    userProfiles[profile.userId] = profile;
    sessionStorage.setItem(key, JSON.stringify(userProfiles));
  }
  
  function saveNewProfile() {
    const nameInput = document.getElementById('name');
    const ageInput = document.getElementById('age');
    const instagramInput = document.getElementById('instagram');
    const descriptionInput = document.getElementById('description');
  
    const profile = {
      userId: Date.now().toString(), // Generate a unique user ID
      name: nameInput.value,
      age: parseInt(ageInput.value),
      instagram: instagramInput.value,
      description: descriptionInput.value,
      isNew: false
    };
  
    saveProfileToSessionStorage(profile);
    displayUserProfile(profile);
    alert('Your profile has been created!');
  }