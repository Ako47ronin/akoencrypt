# Banner and ASCII art logo
banner = """

⠀⠀⠀⠀⠀⠀⢠⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⢹⠀⠀⠀⠀⢠⣺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣼⡀⠀⣀⣤⣶⡴⠒⠒⠒⠒⠒⠠⣤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣃⣗⣿⠇⣿⣧⡃⠀⠀⠀⠀⠀⠀⠀⠹⣾⠱⠤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡰⠋⢸⢾⣿⢣⣿⣿⠷⣄⡒⢤⣀⣀⠀⢐⢀⠀⠦⠀⠉⢕⢄⠀⠀⠀⠀
⠀⠀⠀⡠⣎⣃⠀⠀⢟⣽⢸⣿⣿⡀⠱⣷⡾⣡⣦⣝⡀⠉⠘⠃⠠⠄⠀⢈⣧⡀⠀⠀
⠀⠀⠰⠁⢸⡟⠲⠀⢘⣜⣿⣿⡟⣉⣣⣼⣷⣻⣯⣙⣿⣿⣶⣶⣦⣴⣶⡿⠋⠱⡀⠀
⠀⠀⡸⠀⡀⠀⠀⠀⠠⡽⢟⣵⣾⣿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠱⠀
⠀⡇⡃⠀⢁⡀⠀⠀⠠⠷⢟⣿⣵⣶⣶⣇⣿⣿⣿⣟⣛⣛⠻⣯⠀⠀⠀⠀⠀⠀⠀⡇
⠀⢿⡃⠀⠈⠈⠀⠀⠀⠀⠃⢌⣿⣿⣿⣾⣿⣎⣋⣴⣶⣯⣿⣿⡆⠀⠀⠀⠀⠀⢠⢰
⢠⠸⢋⡀⡀⢀⣴⣮⠀⢀⡀⠀⣴⡿⠻⠘⠛⡟⡿⡬⢧⢊⡩⢿⣷⡀⠀⠀⠀⠀⠫⡞
⠘⣇⣇⢟⢶⠟⡉⠀⠀⠀⠁⣰⠊⢀⡀⣄⡰⣱⡷⡗⣭⢄⣐⠙⢿⡂⠠⠿⠇⠀⢀⡇
⠀⢟⡵⠈⣵⠀⠀⠀⠀⠀⠀⣷⢜⠊⣭⡴⢁⣽⡷⡖⣪⠴⢆⣉⣿⡇⠀⠀⠀⠘⡺⠀
⠀⠘⡜⣧⠘⠃⠀⠀⡐⠀⡼⡝⣮⣩⢴⣈⣿⣽⡇⡇⢼⠒⠬⣘⣿⡇⠀⠀⠀⣰⡅⠀
⠀⠀⠘⢌⢷⡔⠦⢀⣈⢠⡓⣭⣰⡴⣽⡽⢿⠍⡿⠏⠇⠒⠡⣽⣟⡅⠀⠀⣼⡟⠀⠀
⠀⠀⠀⠈⠢⣸⣾⣿⠟⣹⣭⣾⠷⣛⢭⣻⣿⣿⣷⣶⣴⣦⣬⣼⣿⣆⠈⡠⠊⠀⠀⠀
⠀⠀⠀⠀⣀⣈⣫⡼⡿⣟⢬⡢⣝⣮⣵⣿⣿⣿⣿⣿⣿⣿⣷⡉⠻⡧⠊⠁⠀⠀⠀⠀
⠀⠀⢠⢖⢧⣛⣛⣛⣾⣾⣷⡿⣟⣋⣽⣿⣿⣿⣿⣿⣯⣿⠼⠓⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⠿⢼⣸⡽⠿⠿⢯⣯⣻⣘⣯⡟⢿⣿⢿⣿⣿⣷⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⡭⣿⣿⣿⣿⣿⣿⣯⣾⣟⡋⡓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡌⢀⣀⠘⠳⠙⣽⣿⣿⣿⣧⣋⣙⢾⡷⠦⡄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠉⠈⠃⠿⠟⠉⢹⠟⠛⠻⡞⠿⠏⠀⠘⠄⠀⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        

Ako Encryptor v1.0
Author: Ako
Email : ako47ron at gmail.com
"""

import os
import sys
from Crypto.Cipher import AES
import argparse

# Define the encryption function
def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'

    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create a new AES cipher with the given key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Open the input and output files
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            # Write the IV to the output file
            outfile.write(iv)

            # Encrypt the file one chunk at a time
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    # Pad the last chunk with spaces if needed
                    chunk += b' ' * (16 - len(chunk) % 16)

                # Encrypt the chunk and write it to the output file
                outfile.write(cipher.encrypt(chunk))

# Define the recursive encryption function
def encrypt_directory(key, path, extension):
    for root, dirs, files in os.walk(path):
        for file in files:
            in_filename = os.path.join(root, file)
            if in_filename.endswith(extension):
                encrypt_file(key, in_filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt files in a directory recursively.')
    parser.add_argument('path', metavar='PATH', type=str, help='the path to the directory')
    parser.add_argument('key', metavar='KEY', type=str, help='the encryption key')
    parser.add_argument('-e', '--extension', metavar='EXT', type=str, default='.txt', help='the file extension to encrypt (default: .txt)')
    args = parser.parse_args()

    path = args.path
    key = args.key.encode('utf-8')
    extension = args.extension
    
    print(banner)
    encrypt_directory(key, path, extension)

