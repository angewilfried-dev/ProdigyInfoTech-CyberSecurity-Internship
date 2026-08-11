def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


print("=================================")
print("       CAESAR CIPHER TOOL")
print("=================================")
print("1. Encrypt")
print("2. Decrypt")
print("3. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_cipher(message, shift)
    print("\nEncrypted message:", encrypted)

elif choice == "2":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    decrypted = caesar_cipher(message, -shift)
    print("\nDecrypted message:", decrypted)

elif choice == "3":
    print("Goodbye!")

else:
    print("Invalid choice.")
