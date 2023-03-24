# akoencrypt

Simple Python script that recursively encrypts files in a folder.

This program takes a key and a directory path, and recursively encrypts all files in the directory and its subdirectories.

To use the program, 

# For Encryption

1. Replace the key variable with your own encryption key
2. Replace the path variable with the path to the directory you want to encrypt. 
3. Then, call the encrypt_directory function with these arguments to encrypt all files in the directory and its subdirectories.

# Example usage
key = b'this is a key123' # Replace with your own key
path = '/path/to/directory' # Replace with the path to the directory you want to encrypt
encrypt_directory(key, path)

#For Decryption, see the akodecrypt version of this program

