from selenium import webdriver
import os


class Attender:
    def __init__(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("user-data-dir=D:\\ChromeProfiles\\sfit")
        options.binary_location = r"D:\ProgramFiles\Google\Chrome\Application\chrome.exe"
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


    def kill(self):
        self.driver.quit()
