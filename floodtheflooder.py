#!/bin/bash
#
###################################### ############# ########## ## # # ## ### ###
#   _______  ___      _______  _______  ______
#  |       ||   |    |       ||       ||      |
#  |    ___||   |    |   _   ||   _   ||  _    |
#  |   |___ |   |    |  | |  ||  | |  || | |   |
#  |    ___||   |___ |  |_|  ||  |_|  || |_|   |
#  |   |    |       ||       ||       ||       |
#  |___|    |_______||_______||_______||______|
#   _______  __   __  _______
#  |       ||  | |  ||       |
#  |_     _||  |_|  ||    ___|
#    |   |  |       ||   |___
#    |   |  |       ||    ___|
#    |   |  |   _   ||   |___
#    |___|  |__| |__||_______|          Coder: Guilherme(@anplasec)
#   _______  ___      _______  _______  ______   _______  ______
#  |       ||   |    |       ||       ||      | |       ||    _ |
#  |    ___||   |    |   _   ||   _   ||  _    ||    ___||   | ||
#  |   |___ |   |    |  | |  ||  | |  || | |   ||   |___ |   |_||_
#  |    ___||   |___ |  |_|  ||  |_|  || |_|   ||    ___||    __  |
#  |   |    |       ||       ||       ||       ||   |___ |   |  | |
#  |___|    |_______||_______||_______||______| |_______||___|  |_|
#
#  Flood the Flooder, Whatsapp/Telegram Flood against telemarketing!
#
################### ####### #### #### ## # #
#
# This app is just a joke against unwanted telemarketing. We are not responsible for malicious use of this tool!
#
## ⚠️ Important Warning & Disclaimer
##       Risk of Account Ban
#        ^^^^^^^^^^^^^^^^^^^
# Using this script violates the **WhatsApp and Telegram Terms of Service** regarding automated messaging, spam, and flooding.
# WhatsApp uses automated detection systems to spot bot-like behavior.
# Using this tool can result in your phone number being **permanently banned** from WhatsApp or any other message app.
#
### Disclaimer
#
# This project is created strictly for **educational and personal testing purposes** as a coding joke.
# - The author is **not responsible** for any misuse, suspended accounts, banned phone numbers, or damages caused by this script.
# - You choose to run this code entirely at your **own risk**.
#
################################
###
## Requirements
#- **Python 3** installed.
#- Required external libraries:
#  - `pyautogui`
#  - `keyboard`
#---
#
## How to Use 🛠️
#
#1. **Open WhatsApp:** Make sure WhatsApp Web or the WhatsApp desktop app is open to the specific chat you want to target.
#2. **Run the Script:** You will have exactly **10 seconds** to switch to the WhatsApp window after starting the code.
#3. **Stay in the Chat:** Do not switch to another chat while the script is running, or it will flood that conversation instead!
#
#---
#
## How to Stop 🛑
#
#The script runs in an infinite loop. To stop the application at any time, press **`CTRL + C`** in your terminal or press ESC.
#
#---
#
## Customization ✍️
#
#You can easily change or add more messages. Open the script file, find the `msgs` variable, and modify the text as you like.
#
#---
#
#*Remember: This is just a joke! Don't overdo it.* 😉

import time
import pyautogui
###import keyboard

# WELCOME TO FLOOD THE FLOODER

fthef = """
###################################### ############# ########## ## # # ## ### ###
#   _______  ___      _______  _______  ______
#  |       ||   |    |       ||       ||      |
#  |    ___||   |    |   _   ||   _   ||  _    |
#  |   |___ |   |    |  | |  ||  | |  || | |   |
#  |    ___||   |___ |  |_|  ||  |_|  || |_|   |
#  |   |    |       ||       ||       ||       |
#  |___|    |_______||_______||_______||______|
#   _______  __   __  _______
#  |       ||  | |  ||       |
#  |_     _||  |_|  ||    ___|
#    |   |  |       ||   |___
#    |   |  |       ||    ___|
#    |   |  |   _   ||   |___
#    |___|  |__| |__||_______|           coder: Guilherme(@anplasec)
#   _______  ___      _______  _______  ______   _______  ______
#  |       ||   |    |       ||       ||      | |       ||    _ |
#  |    ___||   |    |   _   ||   _   ||  _    ||    ___||   | ||
#  |   |___ |   |    |  | |  ||  | |  || | |   ||   |___ |   |_||_
#  |    ___||   |___ |  |_|  ||  |_|  || |_|   ||    ___||    __  |
#  |   |    |       ||       ||       ||       ||   |___ |   |  | |
#  |___|    |_______||_______||_______||______| |_______||___|  |_|
#
#  Flood the Flooder, Whatsapp/Telegram Flood against telemarketing!
#
#
#  YES IT KEEPS LOOPING!
#
#  Press CTRL+C to KILL!
#
################### ####### #### #### ## # #
"""

print(fthef)

print("You have 10 seconds to go to the desired conversation! Remember The application will always flood the active conversation!")
time.sleep(5)
print("GO! FAST! FAST!")

# This is the time the application wait till start: ex: You have 10 Seconds to put on the desired conversation.

time.sleep(10)

# messages (YOUR DICTIONARY HERE!)

msgs = ["You're making unwanted telemarketing", "I didnt accepted any marketing or even asked for this product!", "You're a spammer! Now you are on my blacklist", "I declare that whoever sent me that spam is the guilty!", "Now i am gonna show you why telemarking is so so hated.", "Telemarketing is often perceived as annoying for several reasons:", "Intrusiveness: Telemarketing calls can interrupt your daily activities, such as work, meals, or family time, making them feel intrusive.", "Unsolicited Calls: Many telemarketing calls are unsolicited, meaning they come from unknown numbers and individuals who are trying to sell you something you may not be interested in.", "Frequency: Some individuals receive multiple telemarketing calls daily, which can be overwhelming and frustrating.", "Persistence: Telemarketers often use persistent tactics to try to make a sale, even after you've declined their offer. This can be seen as pushy and annoying.", "Time-Wasting: Long telemarketing calls can be time-consuming, especially if they are not relevant to your needs or interests.", "Privacy Concerns: People may feel that telemarketers are invading their privacy by calling them without permission or obtaining their personal information.", "Scams: Some telemarketing calls are scams aimed at defrauding individuals, making people wary of answering unknown calls.", "Please stop messaging me!", "I dont want to recive your messages!", "PLEASE! I DONT WANT ANY TELEMARKETING ON MY PHONE!", "RESPECT-ME", "Now to make sure you understand, I will repeat it again and again until you understand.", "(Flood the Flooder) Whatsapp/Telegram Flood against telemarketing!", "My  personal life needs to be respected!"]

index = 0 #start point index

# EXIT Shortcut: ESC
#                ^^^

def exit_app(e):
    print("Flood the Flooder: The chat have been flooded!")
    exit()
keyboard.add_hotkey('esc', exit_app)

# SOURCE

while True:
    message = msgs[index]

# Flooding your "friend"

    pyautogui.typewrite(message)
    pyautogui.press("enter")

# Verifying if all messages are sended then it will restart

    index += 1
    if index == len(msgs):
        index = 0

# TIME BETWEEN THE MESSAGES: ex: 1 second till next line.
    time.sleep(1)

# THIS THE END! MY ONLY FRIEND... THE END!

print("Flood the Flooder: The chat have been flooded!")









