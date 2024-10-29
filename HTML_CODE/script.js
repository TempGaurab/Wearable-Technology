function readProfilesFromSessionStorage(key = 'user_profiles') {
    try {
      const sessionData = sessionStorage.getItem(key);
      return sessionData ? JSON.parse(sessionData) : {};
    } catch (error) {
      console.error('Error reading profiles from session storage:', error);
      return {};
    }
  }
  
  function saveProfileToSessionStorage(profile, key = 'user_profiles') {
    const userProfiles = readProfilesFromSessionStorage(key);
    userProfiles[profile.userId] = profile;
    sessionStorage.setItem(key, JSON.stringify(userProfiles));
  }
  
  function displayUserProfile(profile) {
    const profileContent = document.getElementById('profile-content');
    profileContent.innerHTML = '';
  
    if (profile.isNew) {
      // Display new user form
      profileContent.innerHTML = `
        <h3>Welcome, New User!</h3>
        <p>Please provide your details:</p>
        <input type="text" id="name" placeholder="Name" />
        <input type="number" id="age" placeholder="Age" />
        <input type="text" id="instagram" placeholder="Instagram Profile" />
        <textarea id="description" placeholder="Description"></textarea>
        <button onclick="saveNewProfile()">Submit</button>
      `;
    } else {
      // Display existing user profile
      profileContent.innerHTML = `
        <p><strong>Name:</strong> ${profile.name}</p>
        <p><strong>Age:</strong> ${profile.age}</p>
        <p><strong>Instagram Profile:</strong> ${profile.instagram}</p>
        <p><strong>Description:</strong> ${profile.description}</p>
      `;
    }
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
  
    saveProfileToJson(profile);
    displayUserProfile(profile);
    alert('Your profile has been created!');
  }
  
  // Retrieve user ID from the URL
  const urlParams = new URLSearchParams(window.location.search);
  const userId = urlParams.get('user_id');
  
  if (userId) {
    const userProfiles = readProfilesFromJson();
    const profile = userProfiles[userId];
  
    if (profile) {
      profile.userId = userId;
      displayUserProfile(profile);
    } else {
      alert(`User ID ${userId} not found.`);
    }
  } else {
    alert('No user ID provided in the URL.');
  }