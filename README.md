# Monte Carlo Algorithm for PI Approximation

## Project Description

This project implements a Monte Carlo simulation to approximate the value of PI. The algorithm generates random points within a square and determines the proportion of those points that fall inside a circle inscribed within the square. This proportion is then used to approximate the value of PI.

## Key Functions

### `monte_carlo_pi(num_samples)`

Performs the Monte Carlo simulation to approximate PI.

- **Parameters**:
  - `num_samples` (int): The number of random points to generate.

- **Returns**:
  - (float): The approximated value of PI.

- **Logic**:
  1. Generates random points within a square of side 2 (from -1 to 1 in both x and y coordinates).
  2. Counts the points that fall inside the unit circle centered at the origin (x^2 + y^2 <= 1).
  3. Approximates PI using the proportion of points inside the circle to the total number of points, multiplied by 4.

- **Visualization**:
  - Plots the distribution of the generated points, highlighting those inside the circle in green and those outside in red.
