# Calculator Application

This is a simple calculator application built using the `wxPython` library. The calculator performs basic arithmetic operations, such as addition, subtraction, multiplication, and division. The graphical user interface (GUI) features a 4x4 grid layout with buttons representing numbers and operators.

## Features
- **Basic Arithmetic:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Interactive GUI:** Built with `wxPython`, using a grid layout for buttons and a display for input/output.
- **Error Handling:** Displays an "Error" message if invalid expressions are entered.

## Requirements
- Python 3.x
- `wxPython` library

You can install the required dependencies using:
```bash
pip install wxPython
```
## How to Run
1. Clone the repository or copy the code.
2. Ensure that the required dependencies are installed.
3. Run the following command:
   ```bash
    python calculator.py
   ```
## Code Overview
- CalculatorFrame: The main class that creates the window, display area, and buttons.
- The on_button_click method handles the button click events.
- CalculatorApp: This class initializes the calculator frame and runs the application loop.

## Screenshot
<img src="https://github.com/chuadharysagar/calculator-python/blob/main/calculator.jpeg" alt="Calculator image" width="300"/>

