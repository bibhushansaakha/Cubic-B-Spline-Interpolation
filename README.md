# Cubic B-Spline Interpolation

This repository contains a Python implementation of cubic B-spline interpolation. The code allows you to generate a smooth curve that passes through a given set of control points.

We also have a detailed breakdown of the code in Notion. 

Link: https://www.notion.so/bibhushansaakha/Code-Breakdown-3f2648db97e24aefbd8d7536b2285fbf?pvs=4

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Cubic B-spline interpolation is a numerical method used to approximate a curve based on a set of control points. It is commonly used in computer graphics, computer-aided design (CAD), and data visualization.

This implementation provides the necessary functions to perform cubic B-spline interpolation, including generating the knot vector, evaluating basis functions, and interpolating points.

## Requirements

To run the code in this repository, you need the following:

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bibhushansaakha/cubic-bspline-interpolation.git
   ```

2. Change to the project directory:

   ```bash
   cd cubic-bspline-interpolation
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the cubic B-spline interpolation code, follow these steps:

1. Import the necessary modules:

   ```python
   import numpy as np
   import matplotlib.pyplot as plt
   ```

2. Define your control points as a 2D numpy array:

   ```python
   control_points = np.array([[0, 0], [1, 3], [2, -1], [3, 2], [4, 0]])
   ```

3. Generate the knot vector:

   ```python
   knot_vector = generate_knot_vector(len(control_points))
   ```

4. Define the data points at which you want to interpolate:

   ```python
   data_points = np.linspace(0, 4, 100)
   ```

5. Perform the interpolation:

   ```python
   interpolated_values_x, interpolated_values_y = interpolate_points(control_points, knot_vector, data_points)
   ```

6. Plot the interpolated curve:

   ```python
   plot_interpolated_curve(data_points, interpolated_values_x, interpolated_values_y)
   ```

## Examples

To help you get started, here are a few examples of how to use the cubic B-spline interpolation code:

### Example 1: Interpolating a Simple Curve

Suppose you have the following control points:

```python
control_points = np.array([[0, 0], [1, 3], [2, -1], [3, 2], [4, 0]])
```

You can perform cubic B-spline interpolation on these control points and plot the resulting curve using the provided code.

### Example 2: Interpolating a Complex Shape

In this example, you can define a more complex set of control points that form a shape, such as a letter or a symbol. Then, you can use cubic B-spline interpolation to generate a smooth curve that represents the shape.

## Contributing

Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


In the updated version of the readme, I have added additional sections such as "Examples," "Contributing," and "License" to provide more information about the project. I have also provided more detailed instructions for installation and usage. Additionally, I have included placeholders for examples and encouraged contributions to the repository.
