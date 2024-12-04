import timeit
import socket
import datetime
import speech_recognition as sr
from win10toast import ToastNotifier
import win11toast as w11t

#Day 1. Made a function to test code and another function to run it. -Charles
#Day 2 Cant be bothered. But I did remove the test mode for the main() function. Me running it is testing it already. -Charles
#Also made my first function: Calling the time. Weather is gonna be delayed :( -Charles

global start_time

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

recognizer = sr.Recognizer()


dateObj = datetime.datetime.now()
timeNow = dateObj.strftime("%a-%d-%m-%y %T:%M%p")
weekdy = dateObj.strftime("%A")
day = dateObj.strftime("%d")
day = str(int(day))

if day.endswith("1") and day != "11":
   day += "st"
elif day.endswith("2") and day != "12":
   day += "nd"
elif day.endswith("3") and day != "13":
   day += "rd"
else:
   day += "th"

timeDesc = (f"Today is {weekdy} the {day}")


class Stopwatch:
   def __init__(self):
         self.start_time = None
         self.end_time = None


   def start(self):
    self.start_time = timeit.default_timer()


   def stop(self):
    self.end_time = timeit.default_timer()
    elapsed_time = self.end_time - self.start_time
    print(f"Execution time: {elapsed_time:.6f} seconds")
    return elapsed_time

def test_function(function):
       stopwatch = Stopwatch()
       stopwatch.start()
       try:
           function()
           print("Function executed successfully!")
       except Exception as e:
           print(f"Err: {e}")
       finally:
           stopwatch.stop()
           
def main():
   toaster = ToastNotifier()
   toaster.show_toast(f"Hello {hostname}",
   timeDesc,
   icon_path="computerIcon.ico",
   duration=10,
   threaded = False)import timeit
import socket
import datetime
import speech_recognition as sr
from win10toast import ToastNotifier
import win11toast as w11t

# Day 1. Made a function to test code and another function to run it. -Charles
# Day 2 Cant be bothered. But I did remove the test mode for the main() function. Me running it is testing it already. -Charles
# Also made my first function: Calling the time. Weather is gonna be delayed :( -Charles

global start_time

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

recognizer = sr.Recognizer()

dateObj = datetime.datetime.now()
timeNow = dateObj.strftime("%a-%d-%m-%y %T:%M%p")
weekdy = dateObj.strftime("%A")
day = dateObj.strftime("%d")
day = str(int(day))

if day.endswith("1") and day != "11":
   day += "st"
elif day.endswith("2") and day != "12":
   day += "nd"
elif day.endswith("3") and day != "13":
   day += "rd"
else:
   day += "th"

timeDesc = (f"Today is {weekdy} the {day}")

class Stopwatch:
   def __init__(self):
         self.start_time = None
         self.end_time = None

   def start(self):
    self.start_time = timeit.default_timer()

   def stop(self):
    self.end_time = timeit.default_timer()
    elapsed_time = self.end_time - self.start_time
    print(f"Execution time: {elapsed_time:.6f} seconds")
    return elapsed_time

def test_function(function):
       stopwatch = Stopwatch()
       stopwatch.start()
       try:
           function()
           print("Function executed successfully!")
       except Exception as e:
           print(f"Err: {e}")
       finally:
           stopwatch.stop()

def main():
   toaster = ToastNotifier()
   toaster.show_toast(f"Hello {hostname}",
   timeDesc,
   icon_path="computerIcon.ico",
   duration=10,
   threaded = False)
   while toaster.notification_active(): time.sleep(0.1)

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
   icon_path="computerIcon.ico",
   duration=10,
   threaded = False)
    while toaster.notification_active(): time.sleep(0.1)

if __name__ == '__main__':
o
   while toaster.notification_active(): time.sleep(0.1)

if __name__ == '__main__':
   main()
