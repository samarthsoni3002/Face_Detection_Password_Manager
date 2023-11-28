def prepare_input(input_str):
    return ''.join(e for e in input_str if e.isalnum()).upper()

def generate_table(key):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = prepare_input(key)
    
    # Remove 'J' from key
    key = key.replace('J', '')
    
    if len(set(key)) != len(key):
        raise ValueError('Key must not contain duplicate characters')
    
    table = key + alphabet
    table = [c for c in table if c not in key]
    
    return table

def find_char_positions(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encode(plaintext, key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""

    i = 0
    while i < len(plaintext) - 1:
        char1, char2 = plaintext[i], plaintext[i + 1]

        row1, col1 = find_char_positions(table, char1)
        row2, col2 = find_char_positions(table, char2)

        if row1 == row2:
            ciphertext += table[row1][(col1 + 1) % 5]
            ciphertext += table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[(row1 + 1) % 5][col1]
            ciphertext += table[(row2 + 1) % 5][col2]
        else:
            ciphertext += table[row1][col2]
            ciphertext += table[row2][col1]

        i += 2

    if i < len(plaintext):
        ciphertext += plaintext[i]

    return ciphertext

def decode(ciphertext, key):
    table = generate_table(key)
    ciphertext = prepare_input(ciphertext)
    plaintext = ""

    i = 0
    while i < len(ciphertext) - 1:
        char1, char2 = ciphertext[i], ciphertext[i + 1]

        row1, col1 = find_char_positions(table, char1)
        row2, col2 = find_char_positions(table, char2)

        if row1 == row2:
            plaintext += table[row1][(col1 - 1) % 5]
            plaintext += table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[(row1 - 1) % 5][col1]
            plaintext += table[(row2 - 1) % 5][col2]
        else:
            plaintext += table[row1][col2]
            plaintext += table[row2][col1]

        i += 2

    if i < len(ciphertext):
        plaintext += ciphertext[i]

    return plaintext

# Example usage:
plain_text = "INSTRUMENTS"
key = "MONARCHY"

cipher_text = encode(plain_text, key)
print("Encrypted:", cipher_text)

decoded_text = decode(cipher_text, key)
print("Decrypted:", decoded_text)
