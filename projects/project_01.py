# This is project 1

import win32com.client

# credits ==>
print("Welcome to RoboSpeaker v1.1 created by Ranit Kumar Manik.")

# speaker API ==>
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# entering a conditional infinite loop of inputs ==>
print("Enter the word you want to speak it out by computer: ")
while 1:
    s = input()
    # To stop the program press 'q' ==>
    if s == 'q':
        print("exiting...")
        speaker.Speak("exiting")
        break
    else:
        speaker.Speak(s)
