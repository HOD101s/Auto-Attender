from selenium import webdriver
import os


class Attender:
    def __init__(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("user-data-dir=D:\\ChromeProfiles\\sfit")
        options.binary_location = r"D:\ProgramFiles\Google\Chrome\Application\chrome.exe"
        self.driver = webdriver.Chrome(executable_path=os.environ['CHROME_WEB_DRIVER'],options=options)
        self.driver.get("https://meet.google.com")


    def kill(self):
        self.driver.quit()
