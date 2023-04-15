import csv
from datetime import datetime
import tkinter as tk

# Open the existing CSV file and read the last row
with open('HSCameraSet.csv', 'r') as file:
    reader = csv.reader(file)
    previous_row = list(reader)[-1]

# Get the values for the new row from the user
ShotNumber = int(previous_row[0]) + 1
Date = datetime.now().strftime('%Y-%m-%d')
Time = datetime.now().strftime('%H:%M:%S')

# Create a GUI to get the user input
root = tk.Tk()
root.title("HS Camera Set")

frame_rate_label = tk.Label(root, text="Frame rate (previous value: {}): ".format(previous_row[3]))
frame_rate_label.pack()
frame_rate_entry = tk.Entry(root)
frame_rate_entry.pack()

shutter_label = tk.Label(root, text="Shutter speed (previous value: {}): ".format(previous_row[4]))
shutter_label.pack()
shutter_entry = tk.Entry(root)
shutter_entry.pack()

fnumber_label = tk.Label(root, text="f number (previous value: {}): ".format(previous_row[5]))
fnumber_label.pack()
fnumber_entry = tk.Entry(root)
fnumber_entry.pack()

def submit():
    # Use the previous row as default values for empty inputs
    default_values = [None if value == "" else value for value in previous_row]

    # Assign default values to any missing inputs
    frame_rate = frame_rate_entry.get() if frame_rate_entry.get() != "" else default_values[3]
    shutter = shutter_entry.get() if shutter_entry.get() != "" else default_values[4]
    fnumber = fnumber_entry.get() if fnumber_entry.get() != "" else default_values[5]

    # Create a list of the variables to write to CSV
    data2 = [ShotNumber, Date, Time, frame_rate, shutter, fnumber]

    # Open the existing CSV file in append mode
    with open('HSCameraSet.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the new row to the CSV file
        writer.writerow(data2)

    print("Data added to HSCameraSet.csv.")
    root.destroy()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()
