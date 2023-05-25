import csv
from datetime import datetime
import tkinter as tk

# Define global variables
ShotNumber = None
Date = None
Time = None
previous_row = None
window = None

# Define a function to initialize the GUI
def initialize_gui():
    global ShotNumber, Date, Time, previous_row, window
    
    # Take in previous shot sheet data
    with open('ShotMatrix.csv', 'r') as file:
        reader = csv.reader(file)
        previous_row = list(reader)[-1]
    
    # Get the shot number from the previous row
    ShotNumber = int(previous_row[0]) + 1
    
    # Get the current date and time
    Date = datetime.now().strftime('%Y-%m-%d')
    Time = datetime.now().strftime('%H:%M:%S')
    
    # Create the main window
    window = tk.Tk()
    window.title("Shot Data")
    
    # Create the input widgets
    global TambEntry
    TambEntry = tk.Entry(window)
    TambEntry.grid(row=1, column=1)
    tk.Label(window, text="Ambient temperature (previous value: {}):".format(previous_row[3])).grid(row=1, column=0)

    global FuelEntry
    FuelEntry = tk.Entry(window)
    FuelEntry.grid(row=2, column=1)
    tk.Label(window, text="Fuel (previous value: {}):".format(previous_row[4])).grid(row=2, column=0)

    global OxidizerEntry
    OxidizerEntry = tk.Entry(window)
    OxidizerEntry.grid(row=3, column=1)
    tk.Label(window, text="Oxidizer (previous value: {}):".format(previous_row[5])).grid(row=3, column=0)

    global P0fEntry
    P0fEntry = tk.Entry(window)
    P0fEntry.grid(row=4, column=1)
    tk.Label(window, text="Fuel bottle initial pressure (previous value: {} psi):".format(previous_row[6])).grid(row=4, column=0)

    global P0oxEntry
    P0oxEntry = tk.Entry(window)
    P0oxEntry.grid(row=5, column=1)
    tk.Label(window, text="Oxidizer bottle initial pressure (previous value: {} psi):".format(previous_row[7])).grid(row=5, column=0)

    global mdot_targetEntry
    mdot_targetEntry = tk.Entry(window)
    mdot_targetEntry.grid(row=6, column=1)
    tk.Label(window, text="Target total mass flow rate (previous value: {} g/s):".format(previous_row[8])).grid(row=6, column=0)

    global FuelSetEntry
    FuelSetEntry = tk.Entry(window)
    FuelSetEntry.grid(row=7, column=1)
    tk.Label(window, text="Fuel needle valve setting (previous value: {}):".format(previous_row[9])).grid(row=7, column=0)

    global OxSetEntry
    OxSetEntry = tk.Entry(window)
    OxSetEntry.grid(row=8, column=1)
    tk.Label(window, text="Oxidizer needle valve setting (previous value: {}):".format(previous_row[10])).grid(row=8, column=0)

    global mdotfEntry
    mdotfEntry = tk.Entry(window)
    mdotfEntry.grid(row=9, column=1)
    tk.Label(window, text="Fuel mass flow rate, from calibrations (previous value: {} g/s):".format(previous_row[11])).grid(row=9, column=0)

    global mdotoEntry
    mdotoEntry = tk.Entry(window)
    mdotoEntry.grid(row=10, column=1)
    tk.Label(window, text="Oxidizer mass flow rate, from calibrations (previous value: {} g/s):".format(previous_row[12])).grid(row=10, column=0)

    global igniterEntry
    igniterEntry = tk.Entry(window)
    igniterEntry.grid(row=11,column=1)
    tk.Label(window, text="Igniter energy type (LE, HE, nonel) (previous value: {}):".format(previous_row[14])).grid(row=11, column=0)

    global engineEntry
    engineEntry = tk.Entry(window)
    engineEntry.grid(row=12, column=1)
    tk.Label(window, text="Engine type (MK1,MK2) (previous value: {}):".format(previous_row[15])).grid(row=12, column=0)

    global finjEntry
    finjEntry = tk.Entry(window)
    finjEntry.grid(row=13, column=1)
    tk.Label(window, text="Fuel injector geometry (for MK2, write MK2) (previous value: {}):".format(previous_row[16])).grid(row=13, column=0)

    global hEntry
    hEntry = tk.Entry(window)
    hEntry.grid(row=14, column=1)
    tk.Label(window, text="Annulus thickness (previous value: {}):".format(previous_row[17])).grid(row=14, column=0)

    global OutcomeEntry
    OutcomeEntry = tk.Entry(window)
    OutcomeEntry.grid(row=15, column=1)
    tk.Label(window, text="Outcome of test (previous value: {}):".format(previous_row[18])).grid(row=15, column=0)

    global CommentsEntry
    CommentsEntry = tk.Entry(window)
    CommentsEntry.grid(row=16, column=1)
    tk.Label(window, text="Any other comments about test (previous value: {}):".format(previous_row[19])).grid(row=16, column=0)
    
    # Create the button
    tk.Button(window, text="Submit", command=write_data).grid(row=17, column=0, columnspan=2)
    
    # Create the ShotNumber label
    global ShotNumberLabel
    ShotNumberLabel = tk.Label(window, text="Shot Number:")
    ShotNumberLabel.grid(row=0, column=0)
    tk.Label(window, text=ShotNumber).grid(row=0, column=1)
    
    # Run the main event loop
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

# Define a function to write data to the CSV file
def write_data():
    global ShotNumber, window
    # Get the values from the GUI
    Tamb = TambEntry.get()
    Fuel = FuelEntry.get()
    Oxidizer = OxidizerEntry.get()
    P0f = P0fEntry.get()
    P0ox = P0oxEntry.get()
    mdot_target = mdot_targetEntry.get()
    FuelSet = FuelSetEntry.get()
    OxSet = OxSetEntry.get()
    mdotf = mdotfEntry.get()
    mdoto = mdotoEntry.get()
    igniter = igniterEntry.get()
    engine = engineEntry.get()
    finj = finjEntry.get()
    h = hEntry.get()
    Outcome = OutcomeEntry.get()
    Comments = CommentsEntry.get()
    
    # Assign default values to empty inputs
    Outcome = Outcome if Outcome != "" else "No information entered by user"
    Comments = Comments if Comments != "" else "No information entered by user"
    
    # Use the previous row as default values for empty inputs
    default_values = [None if value == "" else value for value in previous_row]
    Tamb = Tamb if Tamb != "" else default_values[3]
    Fuel = Fuel if Fuel != "" else default_values[4]
    Oxidizer = Oxidizer if Oxidizer != "" else default_values[5]
    P0f = P0f if P0f != "" else default_values[6]
    P0ox = P0ox if P0ox != "" else default_values[7]
    mdot_target = mdot_target if mdot_target != "" else default_values[8]
    FuelSet = FuelSet if FuelSet != "" else default_values[9]
    OxSet = OxSet if OxSet != "" else default_values[10]
    mdotf = mdotf if mdotf != "" else default_values[11]
    mdoto = mdoto if mdoto != "" else default_values[12]
    igniter = igniter if igniter != "" else default_values[14]
    engine = engine if engine != "" else default_values[15]
    finj = finj if finj != "" else default_values[16]
    h = h if h != "" else default_values[17]
    
    # Calculate mdott
    mdott = float(mdotf or 0) + float(mdoto or 0)
    
    # Create a list of the variables to write to CSV
    data = [ShotNumber, Date, Time, Tamb, Fuel, Oxidizer, P0f, P0ox, mdot_target, FuelSet, OxSet, mdotf, mdoto, mdott, igniter, engine, finj, h, Outcome, Comments]
    
    # Open the existing CSV file in append mode
    with open('ShotMatrix.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the new row to the CSV file
        writer.writerow(data)
    
    # Increment the ShotNumber and update the GUI
    ShotNumber += 1
    ShotNumberLabel.config(text=ShotNumber)
    
    # Clear the input fields
    TambEntry.delete(0, tk.END)
    FuelEntry.delete(0, tk.END)
    OxidizerEntry.delete(0, tk.END)
    P0fEntry.delete(0, tk.END)
    P0oxEntry.delete(0, tk.END)
    mdot_targetEntry.delete(0, tk.END)
    FuelSetEntry.delete(0, tk.END)
    OxSetEntry.delete(0, tk.END)
    mdotfEntry.delete(0, tk.END)
    mdotoEntry.delete(0, tk.END)
    igniterEntry.delete(0, tk.END)
    engineEntry.delete(0, tk.END)
    finjEntry.delete(0, tk.END)
    hEntry.delete(0, tk.END)
    OutcomeEntry.delete(0, tk.END)
    CommentsEntry.delete(0, tk.END)
    
    # Close the window after writing data
    window.destroy()
    print("Data added to ShotMatrix.csv.")




def on_closing():
    window.destroy()


initialize_gui()