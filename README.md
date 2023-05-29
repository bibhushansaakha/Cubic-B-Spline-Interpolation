# Cubic B-Spline Interpolation

This repository contains a Python implementation of cubic B-spline interpolation. The code allows you to generate a smooth curve that passes through a given set of control points.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)


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
git clone https://github.com/bibhushansaakha/cubic-bspline-interpolation.git

2. Change to the project directory:
cd cubic-bspline-interpolation


3. Install the required dependencies:
pip install -r requirements.txt


## Usage

To use the cubic B-spline interpolation code, follow these steps:

1. Import the necessary modules:

python
import numpy as np
import matplotlib.pyplot as plt

2. Define your control points as a 2D numpy array:

control_points = np.array([[0, 0], [1, 3], [2, -1], [3, 2], [4, 0]])

3. Generate the knot vector:

knot_vector = generate_knot_vector(len(control_points))

4. Define the data points at which you want to interpolate:

data_points = np.linspace(0, 4, 100)

5. Perform the interpolation:

interpolated_values_x, interpolated_values_y = interpolate_points(control_points, knot_vector, data_points)

6.Plot the interpolated curve:

plot_interpolated_curve(data_points, interpolated_values_x, interpolated_values_y)



