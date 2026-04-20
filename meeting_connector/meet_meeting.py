
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--user-data-dir=/home/azureuser/bot-profile")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--use-fake-device-for-media-stream")
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

print("Launching Chrome...")
driver = webdriver.Chrome(options=options)
print("Chrome launched")

def open_meeting(meeting_link):
    driver.get(meeting_link)
    time.sleep(8)

    mute_mic()
    time.sleep(1)

    join_meeting()

def unmute_mic():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")

        if label and "Turn on microphone" in label:
            driver.execute_script("arguments[0].click();", button)
            print("Mic unmuted")
            break

def join_meeting():
    buttons = ["Join now", "Ask to join", "Switch here"]

    for text in buttons:
        try:
            btn = driver.find_element(By.XPATH, f"//*[text()='{text}']")
            driver.execute_script("arguments[0].click();", btn)
            print(f"{text} clicked")
            break
        except:
            continue

def mute_mic():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")
        if label and "Turn off microphone" in label:
            driver.execute_script("arguments[0].click();", button)
            print("Mic muted")
            break

def raise_hand():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")
        if label and "Raise hand" in label:
            driver.execute_script("arguments[0].click();", button)
            print("Hand raised")
            break

def lower_hand():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")

        if label and "Lower hand" in label:
            driver.execute_script("arguments[0].click();", button)
            print("Hand lowered")
            break

def leave_meeting():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")
        if label and "Leave call" in label:
            driver.execute_script("arguments[0].click();", button)
            print("Meeting left")
            break