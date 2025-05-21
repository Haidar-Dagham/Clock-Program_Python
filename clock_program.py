from time import *  # Import all functions from the time module to access current time, date, and day
from tkinter import *  # Import all tkinter functions and classes for GUI creation

def update():  # Define a function to update the time, day, and date every second
    time_string = strftime("%H:%M:%S")  # Get current time in Hours:Minutes:Seconds format
    time_label.config(text=time_string)  # Display current time on the time label

    day_string = strftime("%A")  # Get the full name of the current day (e.g., Monday)
    day_label.config(text=day_string)  # Display the current day on the day label

    date_string = strftime("%Y/%m/%d")  # Get current date in Year/Month/Day format
    date_label.config(text=date_string)  # Display the current date on the date label

    window.after(1000, update)  # Re-run the update() function after 1000 milliseconds (1 second)

window = Tk()  # Create the main window for the GUI application
window.config(bg="black")  # Set the background color of the main window to black
window.title("Haidar Dagham's O'Clock")  # Set the window title to "Haidar O'Clock"

frame = Frame(window, bg="black")  # Create a container (frame) with a black background
frame.pack()  # Add the frame to the main window

time_label = Label(frame, font=("Arial", 80), fg="#FF0000", bg="black")  # Create a large red label for the time
time_label.pack(side=TOP)  # Place the time label at the top of the frame

date_label = Label(frame, font=("Arial", 30, "bold"), fg="#FF0000", bg="black")  # Create a bold red label for the date
date_label.pack(side=LEFT)  # Place the date label on the left side of the frame

day_label = Label(frame, font=("Arial", 30, "bold"), fg="#FF0000", bg="black")  # Create a bold red label for the day
day_label.pack(side=LEFT)  # Place the day label next to the date label, also on the left side

update()  # Call the update function once to initialize the labels with the current time, date, and day

window.mainloop()  # Run the tkinter event loop (keeps the window open and responsive)
