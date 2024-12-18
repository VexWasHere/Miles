import socket
import datetime
import speech_recognition as sr
from win10toast import ToastNotifier
import time

# Day 1. Made a function to test code and another function to run it. -Charles
# Day 2 Cant be bothered. But I did remove the test mode for the main() function. Me running it is testing it already. -Charles
# Also made my first function: Calling the time. Weather is gonna be delayed :( -Charles
# Kinda forgot to do days ngl so that's done ig
# I noticed the issue with the requirements.txt (I would add and remove packages) and I am working to fix it.

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

recognizer = sr.Recognizer()

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%a-%d-%m-%y")

def get_day():
    return datetime.datetime.now().strftime("%A")

def get_day_number():
    day = datetime.datetime.now().strftime("%d")
    day = str(int(day))
    if day.endswith("1") and day != "11":
        day += "st"
    elif day.endswith("2") and day != "12":
        day += "nd"
    elif day.endswith("3") and day != "13":
        day += "rd"
    else:
        day += "th"
    return day

def get_time_description():
    return f"Today is {get_day()} the {get_day_number()}"

def display_time():
    toaster = ToastNotifier()
    toaster.show_toast(f"Hello {hostname}",
                       get_time_description(),
                       icon_path="computerIcon.ico",  # Ensure this path is correct
                       duration=10,
                       threaded=False)
    while toaster.notification_active():
        time.sleep(0.1)

def main():
    display_time()

if __name__ == '__main__':
    main()