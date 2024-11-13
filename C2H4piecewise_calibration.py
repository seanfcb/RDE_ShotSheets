import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def get_mass_flow_rate():
    try:
        return float(input("Enter the desired mass flow rate: "))
    except Exception:
        print("Input prompt not supported in this environment. Using a default mass flow rate of 5.0.")
        return 5.0

# Load the CSV file with headers
data = pd.read_csv('C2H4.csv')  # Replace with your file path

# Print column names for debugging
print("Columns in CSV file:", data.columns)

# Extract the data
x_data = data['Setting'].values  # First column as X (Setting)
mass_flow_rate = data['800 psi'].values  # Second column as Mass Flow Rate at 800 psi
pressure_columns = data.columns[2:]  # Single data points for 700, 600, 500, and 400 psi

# Define a linear model function
def linear_model(x, a, b):
    return a * x + b

# Fit the linear model to the mass flow rate data with an intercept allowing for negative settings
params, _ = curve_fit(linear_model, x_data, mass_flow_rate, bounds=([-np.inf, -10], [np.inf, np.inf]))

# Generate the main mass flow rate curve based on the linear fit
x_fit = np.linspace(-10, max(x_data), 1000)  # Extend x to -10 to allow for negative settings
y_fit = linear_model(x_fit, *params)

# Plot the main mass flow rate curve
plt.figure(figsize=(10, 6))
plt.plot(x_data, mass_flow_rate, 'bo', label='Mass Flow Rate Data at 800 psi')
plt.plot(x_fit, y_fit, 'b-', label='Fitted Linear Curve for Mass Flow Rate at 800 psi')

# Store extrapolated curves for each pressure
extrapolated_curves = {'800 psi': y_fit}
scaling_factors = {}

# Extrapolate for each pressure column using the single data points
for col in pressure_columns:
    # Extract the single data point for the current pressure
    pressure_value = int(data[col].name.split()[0])  # Extract pressure value (e.g., 700) from column name
    single_point = data[col].values[0]  # Single data point in the current column
    
    # Calculate scaling factor based on ratio of the single point to the fitted value at max setting for 800 psi
    scaling_factor = single_point / linear_model(x_data[-1], *params)
    scaling_factors[pressure_value] = scaling_factor
    extrapolated_y = linear_model(x_fit, *params) * scaling_factor  # Scale the entire curve by this factor
    extrapolated_curves[f"{pressure_value} psi"] = extrapolated_y

    # Plot the extrapolated curve
    plt.plot(x_fit, extrapolated_y, '--', label=f'Extrapolated Linear Curve at {pressure_value} PSI')

# Allow user to select a mass flow rate and find the corresponding setting, starting at the highest pressure
desired_mass_flow_rate = get_mass_flow_rate()
highest_pressure = 800
pressure_levels = sorted([highest_pressure] + [int(col.split()[0]) for col in pressure_columns], reverse=True)

setting_at_desired_flow = None
for pressure in pressure_levels:
    extrapolated_curve = extrapolated_curves[f"{pressure} psi"]
    if desired_mass_flow_rate >= min(extrapolated_curve) and desired_mass_flow_rate <= max(extrapolated_curve):
        # Find the setting for the desired mass flow rate at the current pressure level
        setting_at_desired_flow = x_fit[np.argmin(np.abs(extrapolated_curve - desired_mass_flow_rate))]
        print(f"Found setting at {pressure} PSI for desired mass flow rate: {setting_at_desired_flow:.2f}")
        break  # Stop searching once we find a valid setting
    else:
        print(f"Desired mass flow rate is out of range at {pressure} PSI. Trying next lower pressure...")

# Plot the calculated setting if within range
if setting_at_desired_flow is not None:
    plt.scatter(setting_at_desired_flow, desired_mass_flow_rate, color='green', s=100,
                label=f'Setting for {desired_mass_flow_rate} at {pressure} PSI: {setting_at_desired_flow:.2f}')
else:
    print(f"Desired mass flow rate of {desired_mass_flow_rate} is out of range for all pressures.")

# Configure plot limits and labels
plt.xlim(-10, max(x_fit))  # Allow x-axis to go down to -10
plt.ylim(0, max(y_fit) + 10)  # Start y-axis at 0
plt.xlabel('Setting')
plt.ylabel('Mass Flow Rate')
plt.legend()
plt.title('Mass Flow Rate vs Setting with Extrapolations for Various Pressures')
plt.grid(True)
plt.show()
