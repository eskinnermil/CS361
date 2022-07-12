# Name: Emilio Skinner
# Email: skinneem@oregonstate.edu
# Course: CS361
# Assignment: Assignment 1.6 - Milestone #1
# Date: 07/11/2022
# Description: An alarm clock that plays a sound when the alarm goes off.

from tkinter import *
import tkinter.messagebox
import datetime
from pygame import mixer

running = True
am = False
pm = False


def alarm_clock():
    """Tracks the time and plays a sound when the alarm goes off."""
    global running
    global alarm
    global am
    global pm
    # Validation of hour/min/sec fields
    if running:
        if hour.get() == '' or min.get() == '' or sec.get() == '':
            tkinter.messagebox.showinfo("Error", "Please enter the time in 24-hour format.")
        if int(float(hour.get())) >= 24 or int(float(hour.get())) < 0:
            tkinter.messagebox.showinfo("Error", "Please enter hours between 0 and 24.")
        if int(float(min.get())) >= 60 or int(float(min.get())) < 0:
            tkinter.messagebox.showinfo("Error", "Please enter minutes between 0 and 60.")
        if int(float(sec.get())) >= 60 or int(float(sec.get())) < 0:
            tkinter.messagebox.showinfo("Error", "Please enter seconds between 0 and 60.")

    # Set the alarm
        if 0 <= int(float(hour.get())) < 24 and 0 <= int(float(min.get())) < 60 and 0 <= int(float(sec.get())) < 60:
            app.after(1000, alarm_clock)
            current = datetime.datetime.now()
            meridiemTimeNow = current.strftime("%#I:%M:%S %p")
            militaryTimeNow = current.strftime("%#H:%M:%S %p")

            if meridiemTimeNow == alarm or militaryTimeNow == alarm:
                print("The current alarm has ended...")
                mixer.init()
                mixer.music.load(r'C:\Users\vlyse\Music\tedingerIG.mp3')
                mixer.music.play()
                running = False
                am = False
                pm = False
            print(meridiemTimeNow)


def set_alarm():
    """Sets the timer."""
    global running
    global alarm
    global am
    global pm
    running = True
    if am:
        alarm = f"{hour.get()}:{min.get()}:{sec.get()} AM"
    elif pm:
        alarm = f"{hour.get()}:{min.get()}:{sec.get()} PM"
    alarm_clock()


def cancel_alarm():
    """Cancels the timer."""
    global running
    running = False
    print("The current alarm has been canceled...")


def print_am():
    """Prints AM time."""
    global am
    global pm
    am = True
    pm = False


def print_pm():
    """Prints PM time."""
    global am
    global pm
    am = False
    pm = True


def show_time():
    """Shows the current time."""
    global am
    global pm
    current = datetime.datetime.now()
    now = current.strftime('%#I:%M:%S %p')
    showTime.config(text=now)
    showTime.after(1000, show_time)


if __name__ == '__main__':

    app = Tk()
    app.title("Emilio Skinner's Alarm Clock")
    app.geometry("600x300")
    hour, min, sec = StringVar(), StringVar(), StringVar()
    hrTime = Entry(app, textvariable=hour, bg="white", width=15).place(x=150, y=100)
    minTime = Entry(app, textvariable=min, bg="white", width=15).place(x=250, y=100)
    secTime = Entry(app, textvariable=sec, bg="white", width=15).place(x=350, y=100)
    showTime = Label(app, font=15, width=25, fg="white", bg="black")
    showTime.place(x=180, y=50)
    Label(app, text="Current Time", font=50, width=25, fg="white", bg="black").place(x=180, y=15)
    Label(app, text="Hour", font=50).place(x=175, y=120)
    Label(app, text="Minute", font=25).place(x=275, y=120)
    Label(app, text="Second", font=25).place(x=375, y=120)
    Label(app, text="Set the alarm using 12-hour format", fg="white", bg="black").place(x=200, y=160)
    # Label(app, text)

    Button(app, text="AM", width=5, command=print_am).place(x=425, y=225)
    Button(app, text="PM", width=5, command=print_pm).place(x=470, y=225)
    Button(app, text="Cancel", width=25, command=cancel_alarm).place(x=200, y=250)
    Button(app, text="Set Alarm", width=25, command=set_alarm).place(x=200, y=200)

    show_time()
    app.mainloop()
