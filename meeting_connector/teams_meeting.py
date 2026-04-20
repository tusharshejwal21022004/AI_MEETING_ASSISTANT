from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time

options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--user-data-dir=/home/azureuser/bot-profile")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--use-fake-device-for-media-stream")
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

service = Service("/usr/bin/chromedriver")

print("Launching Chrome...")
driver = webdriver.Chrome(service=service, options=options)
print("Chrome launched")


def open_meeting(meeting_link):

    driver.get(meeting_link)
    time.sleep(8)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        txt = button.text.lower()

        if "continue on this browser" in txt:
            driver.execute_script("arguments[0].click();", button)
            print("Browser selected")
            break

    time.sleep(8)

    name_box = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.TAG_NAME, "input"))
    )

    name_box.click()
    name_box.clear()
    name_box.send_keys("AI BOT")

    print("Name entered")

    time.sleep(2)

    mute_mic()
    time.sleep(1)

    stop_video()
    time.sleep(1)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        txt = button.text.lower()

        if "join now" in txt:
            driver.execute_script("arguments[0].click();", button)
            print("Joined Teams")
            break


def mute_mic():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")

        if label and "mute" in label.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Mic muted")
            break


def unmute_mic():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")

        if label and "unmute" in label.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Mic on")
            break


def stop_video():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")

        if label and "camera" in label.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Camera off")
            break


def raise_hand():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        text = button.text.lower()
        label = button.get_attribute("aria-label")

        if "raise" in text:
            driver.execute_script("arguments[0].click();", button)
            print("Hand raised")
            break

        if label and "raise" in label.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Hand raised")
            break


def lower_hand():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        text = button.text.lower()

        if "raise" in text:
            driver.execute_script("arguments[0].click();", button)
            print("Hand lowered")
            break


def leave_meeting():
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")

        if label and "leave" in label.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Meeting left")
            break


if __name__ == "__main__":
    meeting_link = input("Enter Teams link: ")
    open_meeting(meeting_link)
    input("Press Enter to close...")