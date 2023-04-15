################################################################################################
#                           Created with the assistance of Chat-GPT                            #
################################################################################################
import csv
from datetime import datetime

################################################################################################
#                                Taking in previous shot sheet data                            #
################################################################################################

with open('ShotMatrix.csv', 'r') as file:
    reader = csv.reader(file)
    previous_row = list(reader)[-1]

# Get the values for the new row from the user
ShotNumber = int(previous_row[0]) + 1
Date = datetime.now().strftime('%Y-%m-%d')
Time = datetime.now().strftime('%H:%M:%S')
Fuel = input("Enter Fuel (previous value: {}): ".format(previous_row[3]))
Oxidizer = input("Enter Oxidizer (previous value: {}): ".format(previous_row[4]))
P0f = input("Enter fuel bottle initial pressure (previous value: {} psi): ".format(previous_row[5]))
P0ox = input("Enter oxidizer bottle initial pressure (previous value: {} psi): ".format(previous_row[6]))
mdot_target = input("Enter target total mass flow rate (previous value: {} g/s): ".format(previous_row[7]))
FuelSet = input("Enter fuel needle valve setting (previous value: {}): ".format(previous_row[8]))
OxSet = input("Enter oxidizer needle valve setting (previous value: {}): ".format(previous_row[9]))
mdotf = input("Enter fuel mass flow rate, from calibrations (previous value: {} g/s): ".format(previous_row[10]))
mdoto = input("Enter oxidizer mass flow rate, from calibrations (previous value: {} g/s): ".format(previous_row[11]))
igniter = input("Enter igniter energy type (LE, HE, nonel) (previous value: {}): ".format(previous_row[13]))
engine = input("Enter engine type (MK1,MK2) (previous value: {}): ".format(previous_row[14]))
finj = input("Enter fuel injector geometry (for MK2, write MK2) (previous value: {}): ".format(previous_row[15]))
h = input("Enter annulus thickness (previous value: {}): ".format(previous_row[16]))
Outcome = input("Enter outcome of test (previous value: {}): ".format(previous_row[17]))
Comments = input("Enter any other comments about test (previous value: {}): ".format(previous_row[18]))

# Assign default values to empty inputs
Outcome = Outcome if Outcome != "" else "No information entered by user"
Comments = Comments if Comments != "" else "No information entered by user"

# Use the previous row as default values for empty inputs
default_values = [None if value == "" else value for value in previous_row]

# Assign default values to empty inputs
Fuel = Fuel if Fuel != "" else default_values[3]
Oxidizer = Oxidizer if Oxidizer != "" else default_values[4]
P0f = P0f if P0f != "" else default_values[5]
P0ox = P0ox if P0ox != "" else default_values[6]
mdot_target = mdot_target if mdot_target != "" else default_values[7]
FuelSet = FuelSet if FuelSet != "" else default_values[8]
OxSet = OxSet if OxSet != "" else default_values[9]
mdotf = mdotf if mdotf != "" else default_values[10]
mdoto = mdoto if mdoto != "" else default_values[11]
igniter = igniter if igniter != "" else default_values[13]
engine = engine if engine != "" else default_values[14]
finj = finj if finj != "" else default_values[15]
h = h if h != "" else default_values[16]

# Calculate mdott
mdott = float(mdotf or 0) + float(mdoto or 0)

# Create a list of the variables to write to CSV
data = [ShotNumber, Date, Time, Fuel, Oxidizer, P0f, P0ox, mdot_target, FuelSet, OxSet, mdotf, mdoto, mdott, igniter, engine, finj, h, Outcome, Comments]

# Open the existing CSV file in append mode
with open('ShotMatrix.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    # Write the new row to the CSV file
    writer.writerow(data)

print("Data added to ShotMatrix.csv.")


################################################################################################
#                             Taking in previous scope channel data                            #
################################################################################################


# Open the existing CSV file and read the last row
with open('ScopeChannels.csv', 'r') as file:
    reader = csv.reader(file)
    previous_row = list(reader)[-1]

# Get the values for the new row from the user
ShotNumber = int(previous_row[0]) + 1
Date = datetime.now().strftime('%Y-%m-%d')
Time = datetime.now().strftime('%H:%M:%S')

print('Entering channel details for Scope 1')

scp1ch1 = input("Channel 1 (previous value: {}): ".format(previous_row[3]))
scp1ch2 = input("Channel 2 (previous value: {}): ".format(previous_row[4]))
scp1ch3 = input("Channel 3 (previous value: {}): ".format(previous_row[5]))
scp1ch4 = input("Channel 4 (previous value: {}): ".format(previous_row[6]))

print('Entering channel details for Scope 2')

scp2ch1 = input("Channel 1 (previous value: {}): ".format(previous_row[7]))
scp2ch2 = input("Channel 2 (previous value: {}): ".format(previous_row[8]))
scp2ch3 = input("Channel 3 (previous value: {}): ".format(previous_row[9]))
scp2ch4 = input("Channel 4 (previous value: {}): ".format(previous_row[10]))

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

print("Data added to ScopeChannels.csv")


################################################################################################
#                         Taking in previous High speed camera data                            #
################################################################################################


# Open the existing CSV file and read the last row
with open('HSCameraSet.csv', 'r') as file:
    reader = csv.reader(file)
    previous_row = list(reader)[-1]

# Get the values for the new row from the user
ShotNumber = int(previous_row[0]) + 1
Date = datetime.now().strftime('%Y-%m-%d')
Time = datetime.now().strftime('%H:%M:%S')
FrameRate = input("Enter frame rate (previous value: {}): ".format(previous_row[3]))
Shutter = input("Enter shutter speed (previous value: {}): ".format(previous_row[4]))
fnumber = input("Enter f number (previous value: {}): ".format(previous_row[5]))

# Use the previous row as default values for empty inputs
default_values = [None if value == "" else value for value in previous_row]

# Assign default values to any missing inputs
FrameRate = FrameRate if FrameRate != "" else default_values[3]
Shutter = Shutter if Shutter != "" else default_values[4]
fnumber = fnumber if fnumber != "" else default_values[5]

# Create a list of the variables to write to CSV
data2 = [ShotNumber, Date, Time, FrameRate, Shutter, fnumber]

# Open the existing CSV file in append mode
with open('HSCameraSet.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    # Write the new row to the CSV file
    writer.writerow(data2)

print("Data added to HSCameraSet.csv.")

