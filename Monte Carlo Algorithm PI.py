import random
import matplotlib.pyplot as plt

def monte_carlo_pi(num_samples):
    inside_circle = 0

    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_approximation = (inside_circle / num_samples) * 4

    # Plotting the points
    plt.figure(figsize=(6,6))
    plt.scatter(x_inside, y_inside, color='green', s=1)
    plt.scatter(x_outside, y_outside, color='red', s=1)
    plt.title(f'Monte Carlo Approximation of PI with {num_samples} samples')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

    return pi_approximation

# Example usage
num_samples = 10000
pi_estimate = monte_carlo_pi(num_samples)
print(f'Approximation of PI with {num_samples} samples: {pi_estimate}')
