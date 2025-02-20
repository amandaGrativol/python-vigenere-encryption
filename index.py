# Function to perform the Vigenère cipher
def vigenere(message, key, direction=1):
    """
    Function to encrypt or decrypt a message using the Vigenère cipher.
    
    Args:
    message (str): The message to be encrypted/decrypted.
    key (str): The key for the Vigenère cipher.
    direction (int): The direction of the operation. 1 for encryption and -1 for decryption.
    
    Returns:
    str: The encrypted or decrypted message.
    """
    
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():  # Works with lowercase characters
        # Adds any non-alphabet character without changing it
        if not char.isalpha():
            final_message += char
        else:
            # Gets the corresponding key character
            key_char = key[key_index % len(key)]
            key_index += 1

            # Calculates the shift and the new letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

# Function to encrypt the message
def encrypt(message, key):
    """
    Function to encrypt the message using the Vigenère cipher.
    """
    return vigenere(message, key)

# Function to decrypt the message
def decrypt(message, key):
    """
    Function to decrypt the message using the Vigenère cipher.
    """
    return vigenere(message, key, -1)


# Testing the code
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# Displaying the results
print(f'Original text: {text}')
print(f'Key: {custom_key}')
encrypted_text = encrypt(text, custom_key)
print(f'Encrypted text: {encrypted_text}')
decrypted_text = decrypt(encrypted_text, custom_key)
print(f'Decrypted text: {decrypted_text}')
