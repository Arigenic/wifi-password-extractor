import subprocess
import re

# Function to get all saved Wi-Fi profiles
def get_profiles():
    # Run the 'netsh wlan show profiles' command to get profiles list
    result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
    
    # Use regex to find the profile names in the command output
    profiles = re.findall(r"All User Profile\s*:\s*(.*)", result.stdout)
    
    # Return a list of profile names (trim any leading/trailing spaces)
    return [p.strip() for p in profiles]

# Function to get the password for a specific profile
def get_password(profile):
    # Run the 'netsh wlan show profile' command to get detailed information for each profile
    result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True)
    
    # Look for the 'Key Content' field in the command output to extract the password
     = re.search(r"Key Content\s*:\s*(.*)", result.stdout)
    
    # Return the password if found, otherwise return None
    return match.group(1).strip() if match else None

# Main function to execute the logic
def main():
    # Get all saved Wi-Fi profiles
    profiles = get_profiles()

    # Print the header for the output
    print(f"{'Wi-Fi Name':<30} | {'Password'}")
    print("-" * 50)

    # Loop through each profile and print the name and password
    for profile in profiles:
        password = get_password(profile)
        print(f"{profile:<30} | {password if password else 'N/A'}")

# Entry point to run the script
if __name__ == "__main__":
    main()