import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()


class Attender:
    def __init__(self,block_mic_cam=False, mute_audio=False):
        self.currentLecture = None
        self.block_mic_cam = block_mic_cam
        options = webdriver.ChromeOptions() 
        options.add_argument(f'user-data-dir={os.environ["CHROME_PROFILE"]}')
        if mute_audio:
            options.add_argument("--mute-audio")
        options.binary_location = os.environ['CHROME_BINARY']

        if block_mic_cam:
            exptoption = 2
        else:
            exptoption = 1

        options.add_experimental_option(
            "prefs",
            {
                "profile.default_content_setting_values.media_stream_mic": exptoption,
                "profile.default_content_setting_values.media_stream_camera": exptoption,
                "profile.default_content_setting_values.geolocation": exptoption,
                "profile.default_content_setting_values.notifications": exptoption
            }
        )
        self.driver = webdriver.Chrome(executable_path=os.environ['CHROME_WEB_DRIVER'],options=options)


    def join_meet(self,meetcode,camera_off=True,mic_off=True):
        self.driver.get("https://meet.google.com")
        try:
            # Wait till button loads
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div')))
            # Click Enter Meeting Code
            self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div').click()
            # Wait till input appears
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')))
            # Enter MeetCode
            meetcodefield = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')
            meetcodefield.click()
            meetcodefield.send_keys(meetcode)
            # Click Continue
            self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span').click()

            if self.block_mic_cam:
                WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span')))
                # Click Dismis blocked mic and cam
                self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span').click()
            else:
                # Wait till Join Now Button appears
                WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')))
                # Camera OFF
                if camera_off:
                    self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div').click()
                # Mic OFF
                if mic_off:
                    self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div').click()
            
            # Wait to Click Join Meet
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')))
            # Click Join Meet
            self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span').click()

            # set flag
            self.currentLecture = meetcode

        except TimeoutException:
                print("Page took too long to load")

    def kill(self):
        self.driver.quit()
