import timeit
import socket
import datetime
import speech_recognition as sr

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
    print(timeDesc)

if __name__ == '__main__':
    main()