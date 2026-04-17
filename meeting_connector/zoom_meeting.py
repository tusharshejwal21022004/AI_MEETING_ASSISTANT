from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument(r"--user-data-dir=C:\bot-profile")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--use-fake-device-for-media-stream")

driver = webdriver.Chrome(options=options)

def open_meeting(meeting_link):

    driver.get(meeting_link)
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

def raise_hand():
    driver.switch_to.default_content()

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "webclient"))
    )

    driver.switch_to.frame(iframe)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")

        if label and "reaction" in label.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Reactions opened")
            time.sleep(2)
            break

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        txt = button.text.lower()

        if "raise hand" in txt:
            driver.execute_script("arguments[0].click();", button)
            print("Hand raised")
            break


def lower_hand():
    driver.switch_to.default_content()

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "webclient"))
    )

    driver.switch_to.frame(iframe)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")

        if label and "reaction" in label.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Reactions opened")
            time.sleep(2)
            break

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        if "lower hand" in button.text.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Hand lowered")
            break

def leave_meeting():
    driver.switch_to.default_content()

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "webclient"))
    )

    driver.switch_to.frame(iframe)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        label = button.get_attribute("aria-label")

        if label and "leave" in label.lower():
            driver.execute_script("arguments[0].click();", button)
            print("Meeting left")
            break

if __name__ == "__main__":
    join_zoom_meeting()
    input("Press Enter to close...")