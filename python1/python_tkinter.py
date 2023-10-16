import tkinter as tk


def update_units(*args):
    from_unit_menu['menu'].delete(0, 'end')
    to_unit_menu['menu'].delete(0, 'end')

    from_units = units[conversion_type_var.get()]
    to_units = units[conversion_type_var.get()]

    from_unit.set(from_units[0])
    to_unit.set(to_units[1])

    for unit in from_units:
        from_unit_menu['menu'].add_command(
            label=unit, command=lambda value=unit: from_unit.set(value))

    for unit in to_units:
        to_unit_menu['menu'].add_command(
            label=unit, command=lambda value=unit: to_unit.set(value))


def convert():
    from_unit = from_unit.get()
    to_unit = to_unit.get()
    value = float(entry.get())

    result = 0  

    if conversion_type_var.get() == "Length":
        if from_unit == "Centimeter" and to_unit == "Meter":
            result = value / 100
        elif from_unit == "Meter" and to_unit == "Centimeter":
            result = value * 100
        elif from_unit == "Centimeter" and to_unit == "Feets":
            result = value / 30.48
        elif from_unit == "Feets" and to_unit == "Inches":
            result = value * 12
        elif from_unit == "Sqft" and to_unit == "Sqmtrs":
            result = value / 10.764
        elif from_unit == "Sqft" and to_unit == "Hectares":
            result = value / 107600

    elif conversion_type_var.get() == "Mass":
        if from_unit == "Gram" and to_unit == "Kilogram":
            result = value / 1000
        elif from_unit == "Kilogram" and to_unit == "Gram":
            result = value * 1000

    elif conversion_type_var.get() == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9 / 5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5 / 9

    result_label.config(text=f"Result: {result} {to_unit}")


root = tk.Tk()
root.title("Unit Converter")
root.configure(bg="blue")



conversion_types = [
    "Length", "Mass", "Temperature"
]
conversion_type_var = tk.StringVar(value=conversion_types[0])
conversion_type_var.trace("w", update_units)

conversion_type_dropdown = tk.OptionMenu(
    root, conversion_type_var, *conversion_types)
conversion_type_dropdown.grid(row=0, column=0, columnspan=2)

from_unit_label = tk.Label(root, text="From:",bg="red",fg="white")
from_unit_label.grid(row=1, column=0)

to_unit_label = tk.Label(root, text="To:",bg="red",fg="white")
to_unit_label.grid(row=2, column=0)

value_label = tk.Label(root, text="Value:",bg="red",fg="white")
value_label.grid(row=3, column=0)

result_label = tk.Label(root, text="",bg="red",fg="white")
result_label.grid(row=6, column=0, columnspan=2)

entry = tk.Entry(root)
entry.grid(row=3, column=1)

units = {
    "Length": ["Centimeter", "Meter", "Feets", "Inches", "Hectares", "Sqft", "Sqmtrs"],
    "Mass": ["Gram", "Kilogram"],
    "Temperature": ["Celsius", "Fahrenheit"]
    
}

from_unit = tk.StringVar()
to_unit = tk.StringVar()

from_unit_menu = tk.OptionMenu(
    root, from_unit, *units[conversion_type_var.get()])
from_unit_menu.grid(row=1, column=1)

to_unit_menu = tk.OptionMenu(
    root, to_unit, *units[conversion_type_var.get()])
to_unit_menu.grid(row=2, column=1)

convert_button = tk.Button(root, text="Convert", command=convert,bg="black",fg="white")
convert_button.grid(row=4, column=0, columnspan=2)

root.mainloop()