from utils.attender import Attender


print("Now Login into required google profile")
attend = Attender()
attend.driver.get('https://accounts.google.com/login')