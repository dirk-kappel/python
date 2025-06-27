
import random


def generate_random_numbers():
    # Set the range for random numbers
    lower_limit = 1.15
    upper_limit = 7.36

    # Generate a list of 23 random numbers
    random_numbers = [round(random.uniform(lower_limit, upper_limit), 2) for _ in range(23)]

    return random_numbers

# Print the generated list of random numbers
print(generate_random_numbers())
