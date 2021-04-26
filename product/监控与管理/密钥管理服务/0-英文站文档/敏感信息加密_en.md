## Overview
Data encryption is the core capability of key management service. In practice, data encryption is mainly used to protect sensitive information on the server disk, such as keys, certificates, and configuration files.

## Example of Sensitive Information

| | Key, certificate | Backend configuration file |
|-|:-:|:-:|
| Usage | Encrypt business data, communication channels, and digital signatures | Store system architecture and other business information, such as database IP, password |
| Risk of data loss | Confidential information is stolen; encrypted tunnels are intercepted; signatures are faked | Business data is dragged as a stepping stone to attack other systems | 

## Plan Ahead for Security
Sensitive information is the key to accessing company's higher secrets and secure tunnels. The security should be planned during the development of company businesses in view of its great importance. One of the most basic protection methods is not to **explicitly place sensitive information** on CVM disks, but to encrypt it through key management service before storage. Then, you can decrypt the information to memory to **avoid writing plaintext to disk**.
The benefit is that even if the CVM was accessed by unidentified individuals due to personal negligence, sensitive plaintext information cannot be accessed directly. Attackers need to speculate the use of the ciphertext file, obtain the decryption access permission and write the decryption program after they obtain the ciphertext information, which greatly increase the difficulty of obtaining the plaintext information and the possibility of being discovered.

## Why does Tencent not directly store sensitive information?
An important measure to enhance security is separation of permissions. For example, to separate the ownership of information and the encryption permission of information, the ownership belongs to you, and Tencent Cloud is responsible for encryption-related operations and permissions control. This is a simple but effective way to enhance security.

## Example: Protect Backend Application Configuration File

The steps are as follows:

1. Preparations
	* A CVM
	* A familiar backend service framework, such as Python. Deploy it to the CVM.
	* Backend application configuration file used by businesses, such as a file configured with a database IP and a password.
	* Create a KMS CMK through the console or Cloud API, keep it enabled, and pay attention to the region where it resides in.

2. Generate a ciphertext configuration file

	Method 1: Use online tools

	Method 2: Use KMS SDK

	Place the generated ciphertext configuration file in a location to which your backend application can access.

3. Decrypt the file in the application and use it

Write code in your backend application, read the ciphertext configuration file and decrypt it with KMS SDK before using. For more information about sample codes, please see [SDK Sample Code](/document/product/573/8909).
