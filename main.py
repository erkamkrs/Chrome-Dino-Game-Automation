from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from PIL import ImageGrab

# Setup Selenium WebDriver

chrome_driver_path = "YOUR CHROME DRIVER PATH"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://dino-chrome.com/en")
driver.fullscreen_window()

# Actions
def jump():
    actions = ActionChains(driver)
    actions.send_keys(Keys.SPACE)
    actions.perform()

def duck_down():
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()

time.sleep(5)

# Start the Game
jump()
duck_down()




def Collide(data):
   # Cactus Barriers
    for i in range(190, 238):
        for j in range(395, 460):
            if data[i, j] < 100:
                jump()
                return
    # Birds
    for i in range(170, 210):
        for j in range(270, 395):
            if  data[i, j] < 100:
                duck_down()
                return
    return

while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    Collide(data)