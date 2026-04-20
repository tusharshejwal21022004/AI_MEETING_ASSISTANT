from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()

options.binary_location = "/snap/bin/chromium"
options.add_argument("--user-data-dir=/home/azureuser/bot-profile")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--use-fake-device-for-media-stream")
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

def join_zoom_meeting():

    driver.get("https://us05web.zoom.us/j/88089653231?pwd=1NaD7u5d5CSQ37ccf0YU8y5SbqIBca.1")
    time.sleep(8)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        if "join from browser" in button.text.lower():
            button.click()
            break

    time.sleep(8)

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "webclient"))
    )

    driver.switch_to.frame(iframe)

    name_box = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
    )

    name_box.click()
    name_box.clear()

    for ch in "AI BOT":
        name_box.send_keys(ch)
        time.sleep(0.3)

    name_box.send_keys(Keys.TAB)
    time.sleep(1)
    name_box.send_keys(Keys.TAB)
    time.sleep(1)
    name_box.send_keys(Keys.ENTER)

    print("Zoom joined")

    time.sleep(15)

    driver.switch_to.default_content()
    time.sleep(3)

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "webclient"))
    )

    driver.switch_to.frame(iframe)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        txt = button.text.lower()

        if "mute" in txt:
            driver.execute_script("arguments[0].click();", button)
            print("Mic muted")

        if "stop video" in txt:
            driver.execute_script("arguments[0].click();", button)
            print("Video off")

    print("Meeting controls applied")


def mute_mic():
    driver.switch_to.default_content()

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "webclient"))
    )

    driver.switch_to.frame(iframe)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        if "mute" in button.text.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Mic muted")
            break


def stop_video():
    driver.switch_to.default_content()

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "webclient"))
    )

    driver.switch_to.frame(iframe)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        if "video" in button.text.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Video off")
            break


def unmute_mic():
    driver.switch_to.default_content()

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "webclient"))
    )

    driver.switch_to.frame(iframe)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        if "unmute" in button.text.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Mic on")
            break

if __name__ == "__main__":
    join_zoom_meeting()
    input("Press Enter to close...")