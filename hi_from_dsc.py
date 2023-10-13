import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

message = "HI! FROM DATA SCIENCE COMMUNITY"

print("\033[1;31;40m" + "Message receiveing..." + "\033[0m")

for i in range(len(message)+1):
    # print in green color
    print("\033[1;32;40m" + message[:i] + '.'*3 + "\033[0m", end="\r")
    time.sleep(0.2)
time.sleep(.5)
print("\n")

print("\033[1;31;40m" + "Message received!" + "\033[0m")
time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')    


print("\033[1;34;40m" + '>' + "\033[0m", end="")
print("\033[1;34;40m" + ("=======> "+message+" <=======").center(100) + "\033[0m")
0