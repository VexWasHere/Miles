import timeit
import socket

#Day 1. Made a function to test code and another function to run it. -Charles
#Day 2 I'm planning on starting a data set

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

engine = pyttsx3.init()


global start_time

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


def main(testMode):
    if testMode == 1:
        pass



    elif testMode == 0:
        pass
        
    else:
        testMode = 0 

if __name__ == '__main__':
    main(1)