print()
print("***CAESAR CIPHER PROGRAM***")
print()

print("do you want to encrypt or decrypt?")
user_input = input("e/d:").lower()
print()

if user_input == "e":
    print("ENCRYPTION MODE SELECTED")
    print()
    def caesar_cipher(text, shift, direction):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + shift * direction) % 26 + ascii_offset)
            else:
                result += char
        return result

    def encrypt(text, shift):
        return caesar_cipher(text, shift, 1)

    message = input("Enter a message: ")
    shift = int(input("Enter a shift value: "))

    encrypted = encrypt(message, shift)
    print(f"Encrypted: {encrypted}")
elif user_input == "d":
    print("DECRYPTION MODE SELECTED")
    print()
    def caesar_cipher(text, shift, direction):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + shift * direction) % 26 + ascii_offset)
            else:
                result += char
        return result

    def decrypt(text, shift):
        return caesar_cipher(text, shift, -1)

    message = input("Enter a message: ")
    shift = int(input("Enter a shift value: "))

    decrypted = decrypt(message, shift)
    print(f"Decrypted: {decrypted}")
else:
    print("Invalid input. Please enter 'e' for encryption or 'd' for decryption.")