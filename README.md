# Installing dependencies
This repository uses Tkinter to generate GUI windows.
## To install Tkinter:
```
sudo apt-get install python3-tk
```

# Using this repository
Before every shot, run the script GUI_ShotData.py.
- First, this script calls ShotMatrix_GUI in the first window, so that the user may add initial flow details.
- Second, this script calls ScopeChannels_GUI which allows the user to input which channels correspond to what pressure sensor
- Third, this script calls HSCameraSet_GUI which allows the user to input the high-speed camera settings.

In all cases:
- The number of the current shot is generated automatically (previous plus 1)
- The script takes the user inputed data in every window, and saves it in an appropriately named CSV file contained in the same directory. This occurs as soon as the user presses submit.
- With the exception of data ranges Outcome and Comments, an leaving a text box empty will repeat the previous value.
