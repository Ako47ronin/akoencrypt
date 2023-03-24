# akoencrypt

Simple Python script that recursively encrypts files in a folder.

This program takes a key and a directory path, and recursively encrypts all files in the directory and its subdirectories.

To use the program, 

# For Encryption

1. Replace the key variable with your own encryption key
2. Replace the path variable with the path to the directory you want to encrypt. 
3. Then, call the encrypt_directory function with these arguments to encrypt all files in the directory and its subdirectories.

# Example usage
python akoencrypt.py /path/to/directory encryption_key

Here, replace /path/to/directory with the path to the directory you want to encrypt, encryption_key with your own encryption key.


#For Decryption, see the akodecrypt version of this program

# Example usage
python akodecrypt.py /path/to/directory decryption_key -e .enc

Here, replace /path/to/directory with the path to the directory you want to decrypt, decryption_key with your own decryption key, and .enc with the file extension you want to decrypt (e.g., .doc.enc, .pdf.enc, etc.).

You can also omit the -e switch to use the default extension of .enc.
