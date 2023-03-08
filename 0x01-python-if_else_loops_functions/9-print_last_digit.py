def print_last_digit(number):
    """Print the last digit of a number and return it."""
    import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
  print(abs(number) % 10, end="")
