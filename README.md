# Ransomware-Example

## Disclaimer:

This repository is intended solely for educational purposes. It includes very basic code developed in Python to illustrate how ransomware operates and provides a sample decryption file. This code is not intended for any practical use beyond understanding the fundamental mechanisms of ransomware.

The functions within this repository are rudimentary and designed to offer insight into the functionality of such malware for study purposes only.

**Important**: Any other use of this code, or any issues arising from its misuse, is not my responsibility. Please use this code with caution and ensure it is only employed in controlled, ethical, and legal environments.

# Simple Ransomware Example Manual

This guide will walk you through the steps to create and test a simple ransomware script using Python's Cryptography library with Fernet.

## Prerequisites

- A computer running a Unix-like OS (Linux or macOS) or Windows with Python 3 installed.

## Steps

### 1. Install Python 3

First, ensure Python 3 is installed on your system. You can check this by running:

```bash
python3 --version
```
If Python 3 is not installed, you can download and install it from the official [Python website](https://www.python.org/downloads/).

### 2. Install pip3
After confirming Python 3 is installed, you'll need to install pip3, the package installer for Python:

```bash
sudo apt-get install python3-pip  # For Ubuntu/Debian
brew install python3  # For macOS
```

For Windows, pip3 is typically included with Python installation. Otherwise, run:

```bash
python -m ensurepip --upgrade
```

### 3. Install the Cryptography Library
Once pip3 is installed, you can install the Cryptography library, which includes the Fernet module, by running:

```bash
pip3 install cryptography
```

### 4. Create a Project Folder
Now, create a directory where you'll store your scripts:

```bash
mkdir ransomware_example
cd ransomware_example
```

### 5. Create Sample Files
Inside your project directory, create some text files to test the ransomware script. You can create as many as you like:

```bash
touch example1.txt example2.txt example3.txt
```

Add any content you like to these files. They will be encrypted by the ransomware script.

### Next Steps
After setting up, proceed to create the ransomware.py and decrypt.py scripts, which will handle encryption and decryption of your sample files.