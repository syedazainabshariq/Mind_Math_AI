{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOR7LuvwNpZ+JHTKTfeIyug",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/syedazainabshariq/Mind_Math_AI/blob/main/Generatve_Math_AI.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# First, install streamlit in your environment if you haven't already\n",
        "# !pip install streamlit\n",
        "\n",
        "import streamlit as st\n",
        "\n",
        "# Calculator functions\n",
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "def divide(x, y):\n",
        "    if y == 0:\n",
        "        return \"Error! Division by zero.\"\n",
        "    return x / y\n",
        "\n",
        "# Streamlit app\n",
        "def calculator():\n",
        "    st.title(\"Simple Calculator\")\n",
        "\n",
        "    # User inputs for the two numbers\n",
        "    num1 = st.number_input(\"Enter first number\", format=\"%.2f\")\n",
        "    num2 = st.number_input(\"Enter second number\", format=\"%.2f\")\n",
        "\n",
        "    # Radio buttons to choose the operation\n",
        "    operation = st.radio(\"Choose operation:\", ('Add', 'Subtract', 'Multiply', 'Divide'))\n",
        "\n",
        "    # Button to calculate the result\n",
        "    if st.button(\"Calculate\"):\n",
        "        if operation == 'Add':\n",
        "            result = add(num1, num2)\n",
        "        elif operation == 'Subtract':\n",
        "            result = subtract(num1, num2)\n",
        "        elif operation == 'Multiply':\n",
        "            result = multiply(num1, num2)\n",
        "        elif operation == 'Divide':\n",
        "            result = divide(num1, num2)\n",
        "\n",
        "        st.write(f\"The result is: {result}\")\n",
        "\n",
        "# Run the app\n",
        "if __name__ == \"__main__\":\n",
        "    calculator()\n"
      ],
      "metadata": {
        "id": "418Ax_nIScff"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}