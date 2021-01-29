import os
import shutil


try:
    profile_path = input('Enter Folder to store Chrome user profile in: ')
    profile_path = os.path.join(os.getcwd(), profile_path)
    if os.path.exists(profile_path):
        shutil.rmtree(profile_path)
    os.makedirs(profile_path)
    backslash = "\\"
    with open('.env', 'w') as f:
        f.write(
            f'CHROME_PROFILE={profile_path.replace(backslash, backslash+backslash)}\n')
        f.write(f'CHROME_BINARY=\n')
        f.write(f'CHROME_WEB_DRIVER=\n')
        f.write(f'LAUNCH_INTERVAL=60\n')
        f.write(f'BUILD_SCHEDULE=True\n')
        f.write(f'BLOCK_CHROME_MIC_CAM=False\n')
        f.write(f'MUTE_CHROME_AUDIO=False\n')
    print("Now add path to chrome.exe as CHROME_BINARY and path to chrome web driver as CHROME_WEB_DRIVER in .env file and continue with setupprofile.py")
except Exception as e:
    print(e)
