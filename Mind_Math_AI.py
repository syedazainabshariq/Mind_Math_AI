# First, install streamlit in your environment if you haven't already
# !pip install streamlit

import streamlit as st

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Streamlit app
def calculator():
    st.title("Simple Calculator")
    
    # User inputs for the two numbers
    num1 = st.number_input("Enter first number", format="%.2f")
    num2 = st.number_input("Enter second number", format="%.2f")

    # Radio buttons to choose the operation
    operation = st.radio("Choose operation:", ('Add', 'Subtract', 'Multiply', 'Divide'))
    
    # Button to calculate the result
    if st.button("Calculate"):
        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)
        
        st.write(f"The result is: {result}")

# Run the app
if __name__ == "__main__":
    calculator()
