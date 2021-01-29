# Auto Attender

## Description

Python Automation Script to schedule logging into Google Meets as per schedule. Can be used to automate logging into daily meetings or school sessions. Initially built to automate logging into the author's Google Meet college sessions, now our Auto Attender can be used by professionals looking to save time on continuously quitting and logging into several meets simply by maintaining a csv schedule.

## Setting Up

### Web Driver

Script is built to run on Chrome browser. You must download the chrome web driver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Choose the version based on your chrome version in chrome at chrome://settings/help. Remember the location where you store the unzipped web driver executable.

#### Environment Setup

```bash
python setupenv.py
```

- Enter the directory to store your google profile information. All Information is stored locally so do not share the details within this directory with anybody.

- Next edit the .env and add the path to your chrome.exe file.

- Incase you cannot find path to your chrome binary (chrome.exe) try running without setting it. In some cases system automatically gets chrome.exe location.

- Next add path to your Chrome Web Driver you previously downloaded. Finally your .env file should look like this.

  ```bash
  CHROME_PROFILE=Path\to\chrome\user\profile
  CHROME_BINARY=Path\to\chrome.exe
  CHROME_WEB_DRIVER=Path\to\chromedriver
  # Interval to keep checking for current available session
  LAUNCH_INTERVAL=60
  # Re-builds schedule before attending sessions
  BUILD_SCHEDULE=True
  # Block Chrome access to Mic and Camera. If set user cannot manually give access to camera or mic
  BLOCK_CHROME_MIC_CAM=False
  # Mutes all audio from the Chrome window. If set user cannot manually un-mute
  MUTE_CHROME_AUDIO=False
  ```

You may find your chrome.exe under : `C:\Program Files (x86)\Google\Chrome\Application\`

#### Profile Setup

```bash
python setupprofile.py
```

- Used to setup the chrome profile used to log into sessions. Run above command and in the chrome window that opens, sign in using the google id used to join your meetings.

#### Building the Schedule

Follow our schedule.example.csv. Add details as specified and finally save the file as schedule.csv. Leave details empty if there is no session.

## Running the script

```bash
python run.py
```

This will run the main script which will keep checking if there is a meeting to attend. If yes it will join the meet else it will take you to a temporary page (in our case https://www.google.com) and will wait there till you have a meeting to attend. After the final meeting of the day the bot browser will close automatically.

### run.py Command Line Arguments

```bash
optional arguments:
  -h, --help            show this help message and exit
  -l [LAUNCH_INTERVAL], --launch-interval [LAUNCH_INTERVAL]
                        Interval to keep checking for current available session
  -sc [BUILD_SCHEDULE], --build_schedule [BUILD_SCHEDULE]
                        Re-builds schedule before attending sessions
  -mic [BLOCK_MIC_CAMERA], --block_mic_camera [BLOCK_MIC_CAMERA]
                        Block Chrome access to Mic and Camera. If set user cannot manually give access to camera or mic
  -mute [MUTE_CHROME_AUDIO], --mute_chrome_audio [MUTE_CHROME_AUDIO]
                        Mutes all audio from the Chrome window. If set user cannot manually un-mute
```

Default values for these arguments are taken from the .env file. So values there would take effect if no args are passed. However, keep in mind arguments passed over cli have precedence over .env default values.

## Quickly Attending Meetings

To instantly log into meets you can run:

```bash
python joinmeet.py -m MEET_CODE
```

## Windows Batch scripts

Can be run from cmd prompt or Run (Win + R) if set on path.

1. attendsession

   Used to begin attending meets according to schedule.

   Usage:

   ```bash
   attendsession
   ```

2. joinmeet

   Used to instantly join meet with specified meetcode.

   Usage:

   ```bash
   joinmeet MEETCODE
   ```
