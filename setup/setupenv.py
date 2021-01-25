import os


try:
    profile_path = input('Enter Folder to store Chrome user profile in: ')
    profile_path = os.path.join(os.getcwd(), profile_path)
    os.mkdir(profile_path)
    backslash = "\\"
    with open('.env.ex', 'w') as f:
        f.write(f'CHROME_PROFILE={profile_path.replace(backslash, backslash+backslash)}\n')
        f.write(f'CHROME_BINARY=')
    print("Now add path to chrome.exe in .env file under and continue with setupprofile.py")
except Exception as e:
    print(e)

