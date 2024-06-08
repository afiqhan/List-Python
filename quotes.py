# Importing the random module to select quotes randomly
import random

# List of quotes
quotes = [
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "May you live all the days of your life. - Jonathan Swift",
    "Life itself is the most wonderful fairy tale. - Hans Christian Andersen",
    "Do not take life too seriously. You will never get out of it alive. - Elbert Hubbard"
]

# Function to print a random quote
def print_random_quote():
    # Select and print a random quote from the list
    print(random.choice(quotes))

# Calling the function to print a random quote
print_random_quote()
