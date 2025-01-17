# Python Math Package

This project provides a Python package named `mymath` with a `geometry` module containing functions for basic geometric calculations.

## Features

*   **`geometry` Module:**
    *   `area_of_rectangle(length, breadth)`: Calculates and returns the area of a rectangle given its length and breadth.
    *   `area_of_circle(radius)`: Calculates and returns the area of a circle given its radius.

## Project Structure

*   `mymath/`: The package directory
    *   `__init__.py`: Defines `mymath` as a Python package and makes `geometry` module accessible.
    *   `geometry.py`: Module containing the `area_of_rectangle` and `area_of_circle` functions.
*   `README.md`: Project documentation.

## How to Use

Follow these steps to use the geometry functions in your projects.

### Prerequisites

*   [Python](https://www.python.org/) (version 3.6 or higher) installed on your system.

### Usage

1.  **Clone the repository:** (if you want the project structure)
    ```bash
    git clone https://github.com/JayJay247in/Mymath.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Mymath
    ```

3. **Import and test:** Open the python terminal with the command `python`. Then, import and test the function using following commands in python terminal:
        ```python
        from mymath.geometry import area_of_circle
        print(area_of_circle(5))
        print(area_of_circle(2.5))
        ```
        Expected output will be something similar to this:
        ```bash
        78.53981633974483
        19.634954084936208
       ```

      You can also test the function `area_of_rectangle` using the following in python terminal after doing `from mymath.geometry import area_of_rectangle` command:
      ```python
      print(area_of_rectangle(5, 10))
      print(area_of_rectangle(10.5, 2))
      ```
      Expected output will be something similar to this:
      ```bash
       50
       21.0
       ```

**Explanation**

*  To use the functions, first, the package `mymath` and the module `geometry` must be imported correctly, and then the functions from the geometry modules can be used.
* The `__init__.py` in the `mymath` folder makes the `mymath` folder as a python package, and makes the modules inside the package like `geometry` accessible.

## Project Structure

*   `mymath/`: package directory
    *   `__init__.py`: package definition.
    *   `geometry.py`: contains the python code for the functions.
*   `README.md`: Project documentation.

## Author

[Your Name]

Feel free to customize this `README.md` with more information specific to your development process or other functions in your package.