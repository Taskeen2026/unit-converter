""" Unit Converter with GUI (Tkinter) - Length, Weight, Volume, Temperature"""

import tkinter as tk
from tkinter import ttk, messagebox

# Base units: length=meter, weight=kg, volume=liter
UNITS = {
    "Length": {
        "Millimeter": 0.001, "Centimeter": 0.01, "Meter": 1, "Kilometer": 1000,
        "Inch": 0.0254, "Foot": 0.3048, "Yard": 0.9144, "Mile": 1609.344,
    },
    "Weight": {
        "Milligram": 0.000001, "Gram": 0.001, "Kilogram": 1, "Ton": 1000,
        "Ounce": 0.0283495, "Pound": 0.453592,
    },
    "Volume": {
        "Milliliter": 0.001, "Liter": 1, "Gallon": 3.78541,
        "Cup": 0.24, "Tablespoon": 0.0147868,
    },
    "Temperature": {"Celsius": None, "Fahrenheit": None, "Kelvin": None},
}

PLACEHOLDER = "Result yahan dikhega"


def convert_temperature(value, from_u, to_u):
    if from_u == "Celsius":
        c = value
    elif from_u == "Fahrenheit":
        c = (value - 32) * 5 / 9
    else:
        c = value - 273.15

    if to_u == "Celsius":
        return c
    if to_u == "Fahrenheit":
        return c * 9 / 5 + 32
    return c + 273.15


def convert(category, value, from_u, to_u):
    if category == "Temperature":
        return convert_temperature(value, from_u, to_u)
    table = UNITS[category]
    return value * table[from_u] / table[to_u]


class UnitConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        self.geometry("420x380")
        self.resizable(False, False)
        self.configure(bg="#f0f4f8")

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TLabel", background="#f0f4f8", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)
        style.configure("TCombobox", padding=4)

        tk.Label(self, text="Unit Converter", font=("Segoe UI", 20, "bold"),
                 bg="#f0f4f8", fg="#1f3a5f").pack(pady=(15, 10))

        frame = tk.Frame(self, bg="#f0f4f8")
        frame.pack(padx=25, fill="x")
        frame.columnconfigure(1, weight=1)

        # Category
        ttk.Label(frame, text="Category:").grid(row=0, column=0, sticky="w", pady=8)
        self.category = ttk.Combobox(frame, values=list(UNITS), state="readonly")
        self.category.grid(row=0, column=1, sticky="ew", padx=(10, 0))
        self.category.bind("<<ComboboxSelected>>", self.update_units)

        # Value
        ttk.Label(frame, text="Value:").grid(row=1, column=0, sticky="w", pady=8)
        self.value_entry = ttk.Entry(frame, font=("Segoe UI", 11))
        self.value_entry.grid(row=1, column=1, sticky="ew", padx=(10, 0))
        self.value_entry.bind("<Return>", lambda e: self.do_convert())

        # From
        ttk.Label(frame, text="From:").grid(row=2, column=0, sticky="w", pady=8)
        self.from_unit = ttk.Combobox(frame, state="readonly")
        self.from_unit.grid(row=2, column=1, sticky="ew", padx=(10, 0))

        # To
        ttk.Label(frame, text="To:").grid(row=3, column=0, sticky="w", pady=8)
        self.to_unit = ttk.Combobox(frame, state="readonly")
        self.to_unit.grid(row=3, column=1, sticky="ew", padx=(10, 0))

        # Buttons
        btns = tk.Frame(self, bg="#f0f4f8")
        btns.pack(pady=12)
        ttk.Button(btns, text="Convert", command=self.do_convert).grid(row=0, column=0, padx=5)
        ttk.Button(btns, text="Swap", command=self.swap).grid(row=0, column=1, padx=5)
        ttk.Button(btns, text="Clear", command=self.clear).grid(row=0, column=2, padx=5)

        # Result box
        self.result_var = tk.StringVar(value=PLACEHOLDER)
        tk.Label(self, textvariable=self.result_var, font=("Segoe UI", 13, "bold"),
                 bg="white", fg="#0b6e4f", relief="groove", bd=2,
                 wraplength=360, height=3).pack(padx=25, fill="x", pady=5)

        # Shuru mein sab khali rahega (category, from, to)

    def update_units(self, event=None):
        """Category select karne par From/To list bharo."""
        names = list(UNITS[self.category.get()])
        self.from_unit["values"] = names
        self.to_unit["values"] = names
        self.from_unit.current(0)
        self.to_unit.current(1)
        self.result_var.set(PLACEHOLDER)

    def do_convert(self):
        cat, f, t = self.category.get(), self.from_unit.get(), self.to_unit.get()
        if not cat or not f or not t:
            messagebox.showwarning("Warning", "Pehle Category, From aur To select karo!")
            return
        try:
            value = float(self.value_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Sirf number enter karo!")
            return
        result = convert(cat, value, f, t)
        self.result_var.set(f"{value:g} {f} =\n{result:,.4f} {t}")

    def swap(self):
        f, t = self.from_unit.get(), self.to_unit.get()
        if not f or not t:
            return
        self.from_unit.set(t)
        self.to_unit.set(f)
        if self.value_entry.get():
            self.do_convert()

    def clear(self):
        """Sab kuch khali kar do: value, category, from, to aur result."""
        self.value_entry.delete(0, tk.END)
        self.category.set("")
        self.from_unit.set("")
        self.to_unit. set (" ")set("")
        self.from_unit["values"] = []
        self.to_unit["values"] = []
        self.result_var.set(PLACEHOLDER)
        self.value_entry.focus()


if __name__ == "__main__":
    UnitConverterApp().mainloop()
