import os
import time
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()


class Attender:
    def __init__(self):
        options = webdriver.ChromeOptions() 
        options.add_argument(f'user-data-dir={os.environ["CHROME_PROFILE"]}')
        options.binary_location = os.environ['CHROME_BINARY']
        options.add_experimental_option(
            "prefs",
            {
                "profile.default_content_setting_values.media_stream_mic": 1,
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.default_content_setting_values.geolocation": 1,
                "profile.default_content_setting_values.notifications": 1
            }
        )
        self.driver = webdriver.Chrome(executable_path=os.environ['CHROME_WEB_DRIVER'],options=options)
        self.driver.get("https://meet.google.com")


    def join_meet(self,meetcode,camera_off=True,mic_off=True):
        # Click Enter Meeting Code
        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div').click()
        # Enter MeetCode
        meetcodefield = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')
        meetcodefield.click()
        meetcodefield.send_keys(meetcode)
        # Click Continue
        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span').click()

        time.sleep(5)

        # Camera OFF
        if camera_off:
            print("Click")
            self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div').click()
        # Mic OFF
        if mic_off:
            self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div').click()
        
        # Click Join Meet
        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span').click()


    def kill(self):
        self.driver.quit()
