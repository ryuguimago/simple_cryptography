def get_key():
    """Prompts the user to enter an encryption key and ensures it is an integer."""
    while True:
        try:
            key = int(input("Input key (number): "))
            return key
        except ValueError:
            print("Please enter a whole number (int) as key")

def get_filename():
    """Prompts the user to enter the name or the path of the file."""
    filename = input("Please enter the name of or the path to the file: ")
    filename = filename.replace("\\", "\\\\") # replaces \ with \\
    return filename

def encrypt_file(filename, key):
    """Encrypts the content of the file with the given key."""
    try:
        with open(filename, 'r') as file:
            # Store all encrypted lines here
            encrypted_lines = []  
            for line in file:
                original = line.strip()
                # Split the original string into words
                original_list = original.split(' ')  
                encrypted_list = []
                for word in original_list:
                     # Split word into characters
                    split_word = list(word) 
                    # Encrypt each character in the word
                    encrypted_word = ''.join(
                        [chr(((ord(char) - 33 + key) % 94) + 33) 
                        for char in split_word]
                    )
                    encrypted_list.append(encrypted_word)
                    # Join the words into a string for the line
                encrypted_line = ' '.join(encrypted_list)  
                 # Append the lines to a list of lines
                encrypted_lines.append(encrypted_line) 
        # Join the list of lines
        encrypted_file_content = "\n".join(encrypted_lines)  

        with open(f"{filename}_encrypted", "w") as file:
            file.write(encrypted_file_content)
            print("Your file has been successfully encrypted.")
            return
    except FileNotFoundError:
        print("Could not find a file with this name")
        return
    

def decrypt_file(filename, key):
    """Decrypts the content of the file with the given key."""
    try:
        with open(filename, "r") as file:
            decrypted_lines = []  # Store decrypted lines here
            for line in file:
                encrypted = line.strip()
                encrypted_list = encrypted.split(" ")  # Split string into words
                decrypted_list = []
                for word in encrypted_list:
                    split_word = list(word)  # Split word into characters
                    # Decrypt each character then join back to word
                    decrypted_word = ''.join(
                        [chr(((ord(char) - 33 - key) % 94) + 33) 
                        for char in split_word]
                    )
                    decrypted_list.append(decrypted_word)
                decrypted_line = ' '.join(decrypted_list)  # Join the single words to string for line
                decrypted_lines.append(decrypted_line)  # Append line to list of lines

        decrypted_file_content = "\n".join(decrypted_lines)  # Create complete file structure

        with open(f"{filename}_decrypted", "w") as file:  # Creates new file
            file.write(decrypted_file_content)
            print("Your file has been successfully decrypted.")
            return
    except FileNotFoundError:
        print("Could not find a file with this name")
        return

def main():
    """Main function to drive the encryption/decryption tool."""
    print("Secret Encryption Tool")
    while True:  # Loop to handle file not found
        choice = input("Do you want to decrypt (d) or encrypt (e) "
                       "your file? Or enter (0) to exit: "
        ).strip().lower()
        if choice == "d":
            key = get_key()
            filename = get_filename()
            decrypt_file(filename, key)
        elif choice == "e":
            key = get_key()
            filename = get_filename()
            encrypt_file(filename, key)
        elif choice == '0':
            exit()
        else:
            print("Please enter 'd' or 'e' to indicate your choice.")

if __name__ == "__main__":
    main()
