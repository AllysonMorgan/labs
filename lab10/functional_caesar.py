def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    new_string = ""
    for char in plaintext:
        if char.isalpha():
            new_letter = ((ord(char) - 97 + key) % 26) + 97
            new_string += chr(new_letter)
        elif ord(char) == 32:
            new_string += char
        else:
            new_letter = (ord(char) + key) % 256
            new_string += chr(new_letter)
    return new_string

def decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    new_string = ""
    for char in ciphertext:
        if char.isalpha():
            new_letter = ((ord(char) - 97 - key) % 26) + 97
            new_string += chr(new_letter)
        elif ord(char) == 32:
            new_string += char
        else:
            new_letter = (ord(char) - key) % 256
            new_string += chr(new_letter)
    return new_string

def main():
    print(encrypt("hell0 WORLD!", 3))
    print(decrypt("KHOOR zruog$", 3))
    print(encrypt("zzz", 6))
    print(decrypt("FFF", 6))
    print(encrypt("FFF", -6))

    message = input("Enter your own message to be encrypted: ")
    key = int(input("Enter the key: "))
    encrypted_message = encrypt(message, key)
    print("Your encrypted message is: ", encrypted_message)

    message = input("Enter your own message to be decrypted: ")
    key = int(input("Enter the key: "))
    decrypted_message = decrypt(message, key)
    print("Your decrypted message is: ", decrypted_message)

if __name__ == "__main__":
    main()
