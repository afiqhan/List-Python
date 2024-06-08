# Importing the random module to select quotes randomly
import random

# List of quotes
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy"
]

# Function to print a random quote
def print_random_quote():
    print(random.choice(quotes))

# Calling the function to print a random quote
print_random_quote()
