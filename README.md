# Introduction to Python 🐍

Welcome to this repository! This collection of Python programming exercises has been converted into **interactive Jupyter Notebooks (`.ipynb`)** to provide a hands-on, interactive learning experience for beginners learning the fundamentals of Python.

## 📂 Project Structure

This repository contains various notebooks covering basic concepts, file handling, object-oriented programming, and more.

| Notebook | Description |
| :--- | :--- |
| [`01.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/01.ipynb) | **Student Details & Senior Citizen Check**: Consists of: <br> • **Part A**: Takes student inputs and calculates percentage. <br> • **Part B**: Calculates age to determine senior citizen status. |
| [`02.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/02.ipynb) | **Fibonacci & Binomial Coefficient**: Consists of: <br> • **Part A**: Generates Fibonacci sequence. <br> • **Part B**: Calculates binomial coefficient (nCr). |
| [`03.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/03.ipynb) | **Statistics Calculator**: Calculates Mean, Variance, and Standard Deviation for a list of numbers. |
| [`04.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/04.ipynb) | **Digit Frequency**: Counts the frequency of each digit in a given multi-digit number. |
| [`05.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/05.ipynb) | **Word Frequency**: Reads a file (e.g., `sample.txt`) and counts the frequency of each word. |
| [`06.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/06.ipynb) | **File Sorter**: Reads lines from an input file, sorts them alphabetically, and writes them to an output file. |
| [`07.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/07.ipynb) | **Zip Directory**: Zips the contents of a specified directory into a zip file. |
| [`08.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/08.ipynb) | **Exception Handling**: Demonstrates error handling (assertions) during division operations. |
| [`09.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/09.ipynb) | **Complex Numbers**: A Class-based approach to add two complex numbers. |
| [`10.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/10.ipynb) | **Student Class**: A Class-based approach to manage student details and marks. |

## 🛠️ Setup & Requirements

These notebooks rely on the **Python Standard Library** (e.g., `math`, `datetime`, `os`, `sys`, `zipfile`). To run these notebooks interactively, you will need **Jupyter Notebook**, **JupyterLab**, or a compatible editor like **VS Code**.

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/toxicbishop/Introduction-To-Python.git
    cd Introduction-To-Python
    ```

2. **Install Jupyter dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 How to Run

You have multiple options for running these interactive notebooks:

### Option 1: In VS Code (Recommended)
1. Install the **Python** and **Jupyter** extensions in VS Code.
2. Open the cloned folder.
3. Click on any `.ipynb` file and press **Run All** or execute cells individually.

### Option 2: Jupyter Notebook / JupyterLab
1. Run the following command in your terminal:
    ```bash
    jupyter notebook
    ```
2. A browser tab will open. Navigate to any notebook (e.g., `01.ipynb`) and run the cells!

### Option 3: Google Colab
1. Go to [Google Colab](https://colab.research.google.com/).
2. Select **Upload** and upload any `.ipynb` file from this repository to start running it instantly in the cloud!

## 📝 Concepts Covered

- **Input/Output**: `input()`, `print()`
- **Control Structures**: `if`, `elif`, `else`, `while`, `for` loops
- **Data Structures**: Lists, Dictionaries, Tuples
- **File Handling**: Reading and Writing text files (use the provided `sample.txt` as a test file!)
- **Functions**: Definition, arguments, recursion
- **OOP**: Classes, Objects, Constructors (`__init__`)
- **Exception Handling**: `try`, `except`, `assert`
- **Modules**: `datetime`, `math`, `os`, `zipfile`, `sys`
