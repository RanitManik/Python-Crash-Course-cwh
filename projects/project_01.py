# This is project 1

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# To stop the program press 'q'

print("Enter the word you want to speak it out by computer: ")
while 1:
    s = input()
    if s == 'q':
        print("exiting...")
        speaker.Speak("exiting")
        break
    else:
        speaker.Speak(s)
