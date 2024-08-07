def get_key():
    key = int(input("input key (number): "))
    return key

def get_filename():
    filename = input("please enter the path to the file you want to encrypt: ")
    return filename
def encrypt_file(filename,key):
    try:
        with open(filename, 'r') as file:
            encrypted_lines = [] #store all encrypted lines here
            for line in file:
                original = line.strip()
                # split the original string into words
                original_list = original.split(' ')
                encrypted_list =[]
                for word in original_list:
                    # split word into characters
                    split_word = list(word)
                    # Encrypt each character in the word
                    encrypted_word = ''.join([chr(ord(char) + key) for char in split_word])
                    #appends the encrypted words to a list
                    encrypted_list.append(encrypted_word)
                encrypted_line = ' '.join(encrypted_list)   # joins the words into a strign for the line
                encrypted_lines.append(encrypted_line)         # appends the lines to a list of lines
        encrypted_file_content ="\n".join(encrypted_lines) # joins the list of lines '\n' for original file structure
       
        with open(f"{filename}_encrypted", "w") as file:
                file.write(encrypted_file_content)     
    except FileNotFoundError:
        print("Could not find a file with this name")

def main():
    key = get_key()
    filename = get_filename()
    encrypt_file(filename, key)
    



if __name__ == "__main__":
    main()

# add decrypt function 
# add de/encrypt menu 
# handle errors and exceptions 
# add message if successfull 