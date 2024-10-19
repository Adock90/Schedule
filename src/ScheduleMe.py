import alertMe
import findTime
import launcher
import keyboard
import time
import os
import tkinter.messagebox
import webbrowser

def main():
    while True:
        TimeNow = findTime.findTime()
        if keyboard.is_pressed("esc") != None and keyboard.is_pressed("n") != None:
            time.sleep(1.5)
            if keyboard.is_pressed("esc") and keyboard.is_pressed("n") != None:
                alertMe.notification("Finishing", "bye", None)
                os._exit(os.EX_OK)
        if TimeNow == "10:20:00":
            tkinter.messagebox.showerror("Do work", "Opening Google Classroom")
            alertMe.notification("Adam do Work or Revision", "Adam", None)
            webbrowser.open("https://classroom.google.com/u/1/")
        elif TimeNow == "10:50:00":
            alertMe.notification("Stop Working", "Adam", None)
        elif TimeNow == "15:20:00":
            tkinter.messagebox.showerror("Do work", "Opening Google Classroom")
            alertMe.notification("Adam do Work or Revision", "Adam", None)
            webbrowser.open("https://classroom.google.com/u/1/")
        elif TimeNow == "16:20:00":
            alertMe.notification("Stop Working", "Adam", None)
        elif TimeNow == "18:00:00":
            alertMe.notification("Revise for half an hour", "Adam", "https://classroom.google.com/u/1/")
        elif TimeNow == "18:30:00":
            alertMe.notification("Do some coding", "Adam", None)
            launcher.launchApp(r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            launcher.launchApp(r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe")

main()