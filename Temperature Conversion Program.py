"""
Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales. The program should prompt the user to input a temperature value and the original unit of measurement. It should then convert the temperature to the other two units and display the converted values to the user. For example, if the user enters a temperature of 25 degrees Celsius, the program should convert it to Fahrenheit and Kelvin, and present the converted values as outputs.
"""

import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as ms

options = ["Celsius", "Fahrenheit", "Kelvin"]

def toCelsius(prev_unit, temp):
    if prev_unit == options[1]:  #from fahrrenheit
        # Formula °C = (°F - 32) × 5/9
        return (temp-32)*(5/9)
    else:   #from Kelvin
        # Formula 0K = -273C
        return temp-273.15

def toKelvin(prev_unit, temp):
    if prev_unit == options[1]:  #from fahrrenheit
        # Formula K = (F − 32) × 5 ⁄ 9 + 273.15
        return ((temp- 32) * (5 / 9))+ 273.15
    else:   #from Celcius
        # Formula 0K = -273C
        return temp+273.15

def toFahr(prev_unit, temp):
    if prev_unit == options[2]:  #from Kelvin
        # Formula F = (K × (9/5)) - 459.67
        return (temp * (9/5)) - 459.67
    else:   #from Celcius
        # Formula °F = (9/5) °C+32.
        return ((9/5)*temp) +32
    

def convert():
    booly = choose.get()
    temp = myentry.get()

    if booly == options[0]: # From Celcius
        conv1.config(text=f"{toKelvin(booly, int(temp))}°K")
        conv2.config(text=f"{toFahr(booly, int(temp))}°F")
    if booly == options[1]: #From Fahr
        conv1.config(text=f"{toCelsius(booly, int(temp))}°C")
        conv2.config(text=f"{toKelvin(booly, int(temp))}°K")
    if booly == options[2]: # From Kelvin
        conv1.config(text=f"{toCelsius(booly, int(temp))}°C")
        conv2.config(text=f"{toFahr(booly, int(temp))}°F")



root = tk.Tk()
root.geometry("600x300")
root.title("Temperature Conversion Program")

#Frames
main = tk.Frame(root)
second_frame = tk.Frame(root)
main.pack()
second_frame.pack()

# Main Frame
value = tk.Label(main, text="Enter the value")
choose = ctk.CTkOptionMenu(main, values=options)
myentry = ctk.CTkEntry(main)
select = tk.Label(main, text="Select original unit")
butt = ctk.CTkButton(main, text="Convert", command=convert)



value.grid(row=1, column=1)
choose.grid(row=2, column=2)
myentry.grid(row=2, column=1)
select.grid(row=1, column=2)
butt.grid(row=2, column=3)

#Second Frame
conv1 = tk.Label(second_frame, text="")
conv2 = tk.Label(second_frame, text="")

conv1.pack()
conv2.pack()


root.mainloop()