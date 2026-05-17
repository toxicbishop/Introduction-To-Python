# Introduction to Python 🐍

Welcome to this repository! This collection of Python programming exercises has been converted into **interactive Jupyter Notebooks (`.ipynb`)** to provide a hands-on, interactive learning experience for beginners learning the fundamentals of Python.

## 📂 Project Structure

This repository contains various notebooks covering basic concepts, file handling, object-oriented programming, and more.

| Notebook | Description |
| :--- | :--- |
| [`01a.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/01a.ipynb) | **Student Details**: Takes student inputs (Name, USN, Marks) and calculates the percentage. |
| [`01b.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/01b.ipynb) | **Senior Citizen Check**: Calculates age from date of birth to determine if a person is a senior citizen. |
| [`02a.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/02a.ipynb) | **Fibonacci Sequence**: Generates the Fibonacci sequence up to a given number `N`. |
| [`02b.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/02b.ipynb) | **Binomial Coefficient**: Calculates the binomial coefficient (nCr) using a recursive factorial function. |
| [`3.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/3.ipynb) | **Statistics Calculator**: Calculates Mean, Variance, and Standard Deviation for a list of numbers. |
| [`4.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/4.ipynb) | **Digit Frequency**: Counts the frequency of each digit in a given multi-digit number. |
| [`5.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/5.ipynb) | **Word Frequency**: Reads a file (e.g. `sample.txt`) and counts the frequency of each word, displaying the top 11. |
| [`6.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/6.ipynb) | **File Sorter**: Reads lines from an input file, sorts them alphabetically, and writes them to an output file. |
| [`7.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/7.ipynb) | **Zip Directory**: Zips the contents of a specified directory into a zip file. |
| [`8.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/8.ipynb) | **Exception Handling**: Demonstrates error handling (Assertions) during division operations. |
| [`9.ipynb`](file:///d:/Code/Repo/Introduction-To-Python/9.ipynb) | **Complex Numbers**: A Class-based approach to add two complex numbers. |
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
2. A browser tab will open. Navigate to any notebook (e.g., `01a.ipynb`) and run the cells!

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
