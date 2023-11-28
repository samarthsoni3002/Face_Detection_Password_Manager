import random
import string

def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Generate a random word with a length of 8
random_word = generate_random_word(8)
print(random_word)
