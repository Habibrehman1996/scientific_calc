# Install required packages for Gradio
!pip install gradio

import gradio as gr
import math

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error: Negative value for square root"
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    if x <= 0:
        return "Error: Logarithm undefined for non-positive values"
    return math.log10(x)

def ln(x):
    if x <= 0:
        return "Error: Natural logarithm undefined for non-positive values"
    return math.log(x)

# Create a function that selects the right calculation
def calculate(operation, x, y=None):
    if operation == "Add":
        return add(x, y)
    elif operation == "Subtract":
        return subtract(x, y)
    elif operation == "Multiply":
        return multiply(x, y)
    elif operation == "Divide":
        return divide(x, y)
    elif operation == "Power":
        return power(x, y)
    elif operation == "Square Root":
        return sqrt(x)
    elif operation == "Sine":
        return sin(x)
    elif operation == "Cosine":
        return cos(x)
    elif operation == "Tangent":
        return tan(x)
    elif operation == "Logarithm":
        return log(x)
    elif operation == "Natural Logarithm":
        return ln(x)
    else:
        return "Invalid operation"

# Gradio interface
def calculator_interface(operation, x, y=None):
    if y is None and operation not in ["Square Root", "Sine", "Cosine", "Tangent", "Logarithm", "Natural Logarithm"]:
        return "Error: This operation requires two inputs"
    
    return calculate(operation, x, y)

# Setting up Gradio UI
with gr.Blocks() as calculator_app:
    gr.Markdown("# Scientific Calculator")

    # Operation dropdown
    operation = gr.Dropdown(
        label="Select Operation",
        choices=["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root",
                 "Sine", "Cosine", "Tangent", "Logarithm", "Natural Logarithm"],
        value="Add"
    )
    
    # Inputs for numbers
    x = gr.Number(label="Input X")
    y = gr.Number(label="Input Y (optional for some operations)")

    # Output text
    output = gr.Textbox(label="Result")

    # Submit button
    calculate_btn = gr.Button("Calculate")

    # When the button is clicked, perform the calculation
    calculate_btn.click(fn=calculator_interface, inputs=[operation, x, y], outputs=output)

# Launch the calculator app
calculator_app.launch()
