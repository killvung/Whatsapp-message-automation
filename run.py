import schedule
import time
from messageFactory import *
from webwhatsapi import WhatsAPIDriver

def init():
    global driver
    global sent_message
    driver = WhatsAPIDriver()
    driver.view_unread()
    schedule.every(20).seconds.do(job)
    sent_message = construct_message()

def job():
    sent_message = construct_message(*(open("messages.txt","r")))
    result = driver.send_to_phone_number(911, sent_message)
    print("OK, sent" if result else "Not ok, not sent :-(")

init()
while True:
    schedule.run_pending()
    time.sleep(1)