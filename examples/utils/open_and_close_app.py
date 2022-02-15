# open and close app with some time interval

import os
import time

app = 'notepad'
# creating while loop to run forever
while True:
    # opening app
    os.system("start "+app)
    # waiting for 5 * 60 seconds
    time.sleep(5 * 60)
    # closing app
    os.system("TASKKILL /F /IM "+app+".exe")
    # waiting for 15 seconds
    time.sleep(15)

    # interrupting screen sleep mode if it is on
    # os.system("powercfg /hibernate off")