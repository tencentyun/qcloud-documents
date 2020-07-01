To ensure the security and reliability of instances, Tencent Cloud allows users to log in to instances with: [password](/doc/product/213/6093) and SSH key pair. This document describes how to make configurations for login with SSH key pair. Users of instances with different operating systems can choose an encryption method by referring to the settings section in [Custom Configuration of Windows CVMs](/doc/product/213/10516#.E8.AE.BE.E7.BD.AE.E4.BF.A1.E6.81.AF) and [Custom Configuration of Linux CVMs](/doc/product/213/10517#.E8.AE.BE.E7.BD.AE.E4.BF.A1.E6.81.AF).

## SSH Key Overview
Tencent Cloud allows encryption and decryption of the information for logging into Linux instances with public key cryptography. The public key cryptography uses a public key to encrypt data (such as a password), and then recipients can decrypt the data using a private key. The combination of a public key and a private key is also known as key pair. An SSH key can be used to connect to instances in a safe way, making it a more secured login method than normal passwords.

Tencent Cloud only stores the public key, and you must retain the private key. Anyone who has your private key can decrypt your login information. So be sure to keep your private key in a secure location.


## Features and Advantages
Compare to the traditional verification method involving user name and password, SSH key has the following advantages:

- Login verification with SSH key offers a higher security to prevent brute force attacks.
- Login with SSH key makes it more convenient for you to log in to your instance by making simple configurations on the console and local client, without the need to enter the password again in case of re-login.

## Use Limits
- Only supported for Linux instances.
- Tencent Cloud will not retain your private key information. You need to click **Download** to obtain the private key within 10 minutes after you have created an SSH key, and keep it properly.
- A Linux instance can only bound with an SSH key. A key that has been bound to your instance will be replaced with the new key.
- To ensure data security, you need to shut the instance down before the key can be loaded.


## Operation Instructions

For more information, please [SSH Key](https://cloud.tencent.com/document/product/213/16691).

