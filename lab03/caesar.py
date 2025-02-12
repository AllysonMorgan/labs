class Caesar:
    def __init__(self):
        self._key=None

    def get_key(self):
        return self._key

    def set_key(self,key):
        self._key=key

    def encrypt(self,plaintext):
        plaintext=plaintext.lower()
        new_string=""
        for char in plaintext:
            if char.isalpha():
                new_letter=((ord(char)-97+self._key)%26)+97
                new_string+=chr(new_letter)
            elif ord(char) == 32:
                new_string+=char
            else:
                new_letter=(ord(char)+self._key)%256
                new_string+=chr(new_letter)
        return(new_string)
    def decrypt(self,ciphertext):
        ciphertext=ciphertext.lower()
        new_string=""
        for char in ciphertext:
            if char.isalpha():
                new_letter=((ord(char)-97-self._key)%26)+97
                new_string+=chr(new_letter)
            elif ord(char) == 32:
                new_string+=char
            else:
                new_letter=(ord(char)-self._key)%256
                new_string+=chr(new_letter)
        return(new_string)
def main():
    cipher=Caesar()

    cipher.set_key(3)
    print(cipher.encrypt("hell0 WORLD!"))
    print(cipher.decrypt("KHOOR zruog$"))

    cipher.set_key(6)
    print(cipher.encrypt("zzz"))
    print(cipher.decrypt("FFF"))

    cipher.set_key(-6)
    print(cipher.encrypt("FFF"))

    message=input("Enter your own message to be encrypted: ")
    key=int(input("Enter the key: "))
    cipher.set_key(key)
    encrypted_message=cipher.encrypt(message)
    print("Your encrypted message is: ", encrypted_message)

    message=input("Enter your own message to be decrypted: ")
    key=int(input("Enter the key: "))
    cipher.set_key(key)
    decrypted_message=cipher.decrypt(message)
    print("Your decrypted message is: ", decrypted_message)
main()
