# Unit Converter – Python Tkinter GUI

A simple, user-friendly, and interactive **Unit Converter Application** built using Python and Tkinter. This application allows users to convert different types of measurements, including Length, Weight, Volume, and Temperature, through a clean graphical user interface.

The project is designed to make unit conversions quick, easy, and accurate. It provides multiple conversion options along with useful features such as Swap, Clear, and instant result display.

## Features

- **Length Conversion:** Convert between Millimeter, Centimeter, Meter, Kilometer, Inch, Foot, Yard, and Mile.
- **Weight Conversion:** Convert between Milligram, Gram, Kilogram, Ton, Ounce, and Pound.
- **Volume Conversion:** Convert between Milliliter, Liter, Gallon, Cup, and Tablespoon.
- **Temperature Conversion:** Convert between Celsius, Fahrenheit, and Kelvin.
- **Convert Button:** Quickly calculate and display the converted value.
- **Swap Button:** Easily exchange the From and To units.
- **Clear Button:** Reset all fields, categories, selected units, and results.
- **Input Validation:** Displays error messages when invalid or incorrect values are entered.
- **User-Friendly GUI:** Simple and clean interface built with Tkinter.
- **Keyboard Support:** Press Enter to perform conversions.

## Technologies Used

- **Python:** Main programming language.
- **Tkinter:** Used to create the graphical user interface.
- **ttk:** Provides styled widgets such as buttons, labels, and dropdown menus.
- **Messagebox:** Displays warning and error messages.

## Project Structure

```text
Unit-Converter/
│
├── unit_converter.py
│
└── README.md
```

## Installation and Setup

Follow these steps to run the project on your computer.

### 1. Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

### 2. Clone the Repository

Open your terminal or VS Code terminal and run:

```bash
git clone YOUR_REPOSITORY_URL
```

### 3. Navigate to the Project Folder

```bash
cd Unit-Converter
```

### 4. Run the Application

```bash
python unit_converter.py
```

**Note:** Tkinter is included with most standard Python installations. On some Linux systems, it may need to be installed separately.

## How to Use

1. Run the Python program.
2. Select a conversion category (Length, Weight, Volume, or Temperature).
3. Enter the numeric value you want to convert.
4. Select the original unit from the **From** dropdown menu.
5. Select the target unit from the **To** dropdown menu.
6. Click the **Convert** button to see the result.
7. Use the **Swap** button to exchange the selected units.
8. Click **Clear** to reset the application and start a new conversion.

## Example Conversions

| Category | From | To |
|---|---|---|
| Length | Kilometer | Meter |
| Length | Meter | Centimeter |
| Weight | Kilogram | Gram |
| Weight | Pound | Kilogram |
| Volume | Liter | Milliliter |
| Volume | Gallon | Liter |
| Temperature | Celsius | Fahrenheit |
| Temperature | Kelvin | Celsius |

## Error Handling

The application includes basic input validation to improve the user experience.

- Displays a warning if the required category or units are not selected.
- Displays an error message if the entered value is not a valid number.
- Prevents invalid input from being processed.

## Learning Objectives

This project helped practice and understand:

- Python programming fundamentals.
- Functions and conditional statements.
- Dictionaries and data structures.
- Object-Oriented Programming (OOP).
- Tkinter GUI development.
- Event handling and button commands.
- Exception handling using try-except.
- Working with mathematical conversion formulas.

## Future Improvements

- Add more measurement categories.
- Improve the GUI design with additional themes.
- Add conversion history.
- Add a copy-result option.
- Support more measurement units.

## Author

**Taskeen Fatima**

Python Developer | Web Developer

## License

This project is open-source and available for educational and learning purposes.
