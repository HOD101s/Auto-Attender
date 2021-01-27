# Auto Attender

## Description

Python Script to schedule logging into Google Meets as per schedule. Can be used to automate logging into daily meetings or school sessions. Initially built to automate logging into the author's Google Meet college sessions, our Auto Attender can be used by professionals looking to save time on continuously quitting and logging into several meets simply by maintaining a csv schedule.

## Setting Up

#### Environment Setup

```python
python setupenv.py
```

- Enter the directory to store your google profile information. All Information is stored locally so do not share the details within this directory with anybody.

- Next edit the .env and add the path to your chrome.exe file. Finally your .env file should look like this.

  ```bash
  CHROME_PROFILE=Path\to\chrome\user\profile
  CHROME_BINARY=Path\to\chrome.exe
  ```

You may find your chrome.exe under : ```C:\Program Files (x86)\Google\Chrome\Application\```

#### Profile Setup

```python
python setupprofile.py
```

- Used to setup the chrome profile used to log into sessions. Run above command and in the chrome window that opens, sign in using the google id used to join your meetings. 

#### Building the Schedule

Follow our schedule.example.csv. Add details as specified and finally save the file as schedule.csv. Leave details empty if there is no session.

## Running the script

```python
python run.py
```

This will run the main script which will keep checking if there is a meeting to attend. If yes it will join the meet else it will take you to a temporary page (in our case https://www.google.com) and will wait there till you have a meeting to attend. After the final meeting of the day the bot browser will close automatically.