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

Ako Decryptor v1.0
Author: Ako
Email : ako47ron at gmail.com
"""

import os
import sys
from Crypto.Cipher import AES
import argparse

# Define the decryption function
def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    # Open the input and output files
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            # Read the IV from the input file
            iv = infile.read(16)

            # Create a new AES cipher with the given key and IV
            cipher = AES.new(key, AES.MODE_CBC, iv)

            # Decrypt the file one chunk at a time
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(cipher.decrypt(chunk))

# Define the recursive decryption function
def decrypt_directory(key, path, extension):
    for root, dirs, files in os.walk(path):
        for file in files:
            in_filename = os.path.join(root, file)
            if in_filename.endswith(extension):
                decrypt_file(key, in_filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decrypt files in a directory recursively.')
    parser.add_argument('path', metavar='PATH', type=str, help='the path to the directory')
    parser.add_argument('key', metavar='KEY', type=str, help='the decryption key')
    parser.add_argument('-e', '--extension', metavar='EXT', type=str, default='.enc', help='the file extension to decrypt (default: .enc)')
    args = parser.parse_args()

    path = args.path
    key = args.key.encode('utf-8')
    extension = args.extension

    print(banner)
    decrypt_directory(key, path, extension)
