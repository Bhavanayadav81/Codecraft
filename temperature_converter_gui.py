import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Main conversion logic
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get().lower()

        if unit == "celsius":
            f = celsius_to_fahrenheit(temp)
            k = celsius_to_kelvin(temp)
            result.set(f"Fahrenheit: {f:.2f}°F\nKelvin: {k:.2f}K")
        elif unit == "fahrenheit":
            c = fahrenheit_to_celsius(temp)
            k = fahrenheit_to_kelvin(temp)
            result.set(f"Celsius: {c:.2f}°C\nKelvin: {k:.2f}K")
        elif unit == "kelvin":
            c = kelvin_to_celsius(temp)
            f = kelvin_to_fahrenheit(temp)
            result.set(f"Celsius: {c:.2f}°C\nFahrenheit: {f:.2f}°F")
        else:
            messagebox.showerror("Invalid Unit", "Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)

# Temperature entry
tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack(pady=10)
entry_temp = tk.Entry(root, font=("Arial", 12))
entry_temp.pack()

# Unit selection
tk.Label(root, text="Select Unit:", font=("Arial", 12)).pack(pady=10)
combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12), state="readonly")
combo_unit.current(0)
combo_unit.pack()

# Convert button
tk.Button(root, text="Convert", font=("Arial", 12), command=convert_temperature).pack(pady=10)

# Result display
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), fg="blue").pack(pady=10)

# Run the GUI
root.mainloop()
