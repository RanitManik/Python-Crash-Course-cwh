# This is project 1

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# To stop the program press 'q'

while 1:
    print("Enter the word you want to speak it out by computer")
    s = input()
    speaker.Speak(s)
    if s == 'q':
        print("exiting...")
        break
