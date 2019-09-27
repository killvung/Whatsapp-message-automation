# Whatsapp-message-automation

Automate message sending in Whatsapp 

## Motiviation
My father often complain on my lacking visibility on WhatsApp, therefore I created a system to automate WhatsApp messaging just to keep him happy.

## Ingredient
- [Unofficial WhatsappAPI by mukulhase](https://github.com/mukulhase/WhatsAPI)
    - I clone its repo and extended upon it

## Make sure
- geckodriver has been located in PATH
- prepare own messages.txt for messages to be sent
- prepare phone numbers to be sent, now the phone number has defaulted to 911 (;-))

## Recommanded Step
- Clone this repo
- Prepare own virtualenv
- pip3 install all required modules from requirements.txt
- Assigned geckodriver on the path 
- Change the phone number to someone you want to send 
- Created `messages.txt` and assigned messages line by line
    - For instance: There are 5 messages had been recorded in this file
    ```
    Hi! This is a first message 
    Hi! This is a second message
    HI! This is a fourth message
    Oh wait, where is the third message? 
    Sorry, I can't count 3
   ```
- run run.py with Python3, (Make sure you run it with Pyton 3, it's almost 2020)

## Other
- Default messages are in misheard-Cantonese because my family speaks Cantonese.
