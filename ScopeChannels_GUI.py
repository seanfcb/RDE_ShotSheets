import csv
from datetime import datetime
import tkinter as tk

# Open the existing CSV file and read the last row
with open('ScopeChannels.csv', 'r') as file:
    reader = csv.reader(file)
    previous_row = list(reader)[-1]

# Get the values for the new row from the user
ShotNumber = int(previous_row[0]) + 1
Date = datetime.now().strftime('%Y-%m-%d')
Time = datetime.now().strftime('%H:%M:%S')

# Create the Tkinter GUI
root = tk.Tk()
root.title("Enter Channel Details")
root.geometry("400x500")

# Add the ShotNumber label to the GUI
ShotNumber_label = tk.Label(root, text="Shot Number: {}".format(ShotNumber))
ShotNumber_label.pack()

# Add the Scope 1 channels to the GUI
scope1_label = tk.Label(root, text="Scope 1")
scope1_label.pack()

scp1ch1_label = tk.Label(root, text="Channel 1 (previous value: {}): ".format(previous_row[3]))
scp1ch1_entry = tk.Entry(root)
scp1ch1_label.pack()
scp1ch1_entry.pack()

scp1ch2_label = tk.Label(root, text="Channel 2 (previous value: {}): ".format(previous_row[4]))
scp1ch2_entry = tk.Entry(root)
scp1ch2_label.pack()
scp1ch2_entry.pack()

scp1ch3_label = tk.Label(root, text="Channel 3 (previous value: {}): ".format(previous_row[5]))
scp1ch3_entry = tk.Entry(root)
scp1ch3_label.pack()
scp1ch3_entry.pack()

scp1ch4_label = tk.Label(root, text="Channel 4 (previous value: {}): ".format(previous_row[6]))
scp1ch4_entry = tk.Entry(root)
scp1ch4_label.pack()
scp1ch4_entry.pack()

# Add the Scope 2 channels to the GUI
scope2_label = tk.Label(root, text="Scope 2")
scope2_label.pack()

scp2ch1_label = tk.Label(root, text="Channel 1 (previous value: {}): ".format(previous_row[7]))
scp2ch1_entry = tk.Entry(root)
scp2ch1_label.pack()
scp2ch1_entry.pack()

scp2ch2_label = tk.Label(root, text="Channel 2 (previous value: {}): ".format(previous_row[8]))
scp2ch2_entry = tk.Entry(root)
scp2ch2_label.pack()
scp2ch2_entry.pack()

scp2ch3_label = tk.Label(root, text="Channel 3 (previous value: {}): ".format(previous_row[9]))
scp2ch3_entry = tk.Entry(root)
scp2ch3_label.pack()
scp2ch3_entry.pack()

scp2ch4_label = tk.Label(root, text="Channel 4 (previous value: {}): ".format(previous_row[10]))
scp2ch4_entry = tk.Entry(root)
scp2ch4_label.pack()
scp2ch4_entry.pack()

def submit():
    # Get the values from the GUI
    scp1ch1 = scp1ch1_entry.get()
    scp1ch2 = scp1ch2_entry.get()
    scp1ch3 = scp1ch3_entry.get()
    scp1ch4 = scp1ch4_entry.get()
    scp2ch1 = scp2ch1_entry.get()
    scp2ch2 = scp2ch2_entry.get()
    scp2ch3 = scp2ch3_entry.get()
    scp2ch4 = scp2ch4_entry.get()

    # Use the previous row as default values for empty inputs
    default_values = [None if value == "" else value for value in previous_row]

    # Assign default values to any missing inputs
    scp1ch1 = scp1ch1 if scp1ch1 != "" else default_values[3]
    scp1ch2 = scp1ch2 if scp1ch2 != "" else default_values[4]
    scp1ch3 = scp1ch3 if scp1ch3 != "" else default_values[5]
    scp1ch4 = scp1ch4 if scp1ch4 != "" else default_values[6]
    scp2ch1 = scp2ch1 if scp2ch1 != "" else default_values[7]
    scp2ch2 = scp2ch2 if scp2ch2 != "" else default_values[8]
    scp2ch3 = scp2ch3 if scp2ch3 != "" else default_values[9]
    scp2ch4 = scp2ch4 if scp2ch4 != "" else default_values[10]

    # Create a list of the variables to write to CSV
    data1 = [ShotNumber, Date, Time, scp1ch1, scp1ch2, scp1ch3, scp1ch4, scp2ch1, scp2ch2, scp2ch3, scp2ch4]

    # Open the existing CSV file in append mode
    with open('ScopeChannels.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the new row to the CSV file
        writer.writerow(data1)

    # Destroy the GUI
    root.destroy()
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()
root.mainloop()

print("Data added to ScopeChannels.csv")