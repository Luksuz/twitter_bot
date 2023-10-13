import os
import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By

# the code is fragile because xpath were used for all the elements.
# needs to be done using css selectors where possible

def start_script():
    os.environ["PATH"] += ";C:/SeleniumDriver"
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/")

    accept_cookies = driver.find_element(By.CSS_SELECTOR,
                                         '#layers > div > div:nth-child(1) > div > div > div > div > div > div > div > div:nth-child(1) > a > div > span > span').click()
    time.sleep(4)

    fill_username = driver.find_element(By.NAME, "text").send_keys(username_input.get())
    next_button = driver.find_element(By.XPATH, "//div[@role='button'][contains(.,'Next')]").click()
    time.sleep(4)

    fill_password = driver.find_element(By.NAME, "password").send_keys(password_input.get())
    login = driver.find_element(By.XPATH, "//div[@role='button'][contains(.,'Log in')]").click()
    time.sleep(5)

    driver.get(f"https://twitter.com/{username_target.get()}")
    time.sleep(3)

    DM_button = driver.find_element(By.XPATH, '//*[@data-testid="sendDMFromProfile"]').click()
    time.sleep(3)

    Message_text = driver.find_element(By.XPATH, '//*[@data-testid="dmComposerTextInput"]')
    Send_button = driver.find_element(By.XPATH, '//*[@data-testid="dmComposerSendButton"]')

    repeat = int(repeat_input.get())
    delay = float(delay_input.get())
    message = message_input.get()

    for i in range(repeat):
        Message_text.send_keys(message)
        time.sleep(delay)
        Send_button.click()
        time.sleep(delay)

    print("done")
    time.sleep(4)
    driver.quit()


root = tk.Tk()
root.geometry("500x300")
root.title("Twitter Automation")

frame = tk.Frame(root)
frame.pack()

username_label = tk.Label(frame, text="Username:")
username_label.pack()
username_input = tk.Entry(frame)
username_input.pack()

password_label = tk.Label(frame, text="Password:")
password_label.pack()
password_input = tk.Entry(frame, show="*")
password_input.pack()

username_target_label = tk.Label(frame, text="Username to DM:")
username_target_label.pack()
username_target = tk.Entry(frame)
username_target.pack()

message_label = tk.Label(frame, text="Message to send:")
message_label.pack()
message_input = tk.Entry(frame)
message_input.pack()

times_label = tk.Label(frame, text="Number of times to send:")
times_label.pack()
repeat_input = tk.Entry(frame)
repeat_input.pack()

delay_label = tk.Label(frame, text="Delay between sends (seconds):")
delay_label.pack()
delay_input = tk.Entry(frame)
delay_input.pack()

start_button = tk.Button(frame, text="Start", command=start_script)
start_button.pack()

root.mainloop()