## Overview

Thank you for using Tencent Cloud Game Multimedia Engine SDK. To make it easier for developers to debug and integrate GME products, this document describes the authentication keys for all platforms.

## Voice Chat Key
Tencent Cloud GME provides authentication keys for the encryption and authentication of related features. Generating a signature used for authentication involves plaintext, key and algorithm.

Plaintext is constructed using the following fields in the network order:

| Field Description | Type/Length | Value Definition/Note |
| ---------------- |-------------------|--------------|
| cVer				|unsigned char/1	|Version number. Value entered: 0 |
| wAccountLen		|unsigned short/2	|Length of third-party account	|
| buffAccount		|wAccountLen		|Characters of third-party account	|
| dwSdkAppid		|unsigned short/4	|AppID of third-party account		|
| dwAuthid			|unsigned int/4		|Group ID				|
| dwExpTime		|unsigned int/4		|Expiration time (current time + validity period) (in sec). 300 seconds is recommended. |
| dwPriviegeMap	|unsigned int/4		|ITMG_AUTH_BITS_DEFAULT indicates full access |
| dwReserved		|unsigned int/4		|Value entered: 0 |

### 1. Key
The permission key can be obtained on Tencent Cloud GME console.

![](https://main.qcloudimg.com/raw/bed3c36cdf3fcb421878c64cd5d775ba.png)

### 2. Algorithm
TEA symmetric encryption algorithm.
It is recommended to deploy the algorithm on the client in the early stage of integration, and deploy it at the game application backend later.

| Solution       		| Advantage        		| Disadvantage																																|
| ------------- |-------------|-------------| 
| Backend deployment    		| High security	| Joint testing by backend developers is required |
| Client deployment      	| Quick integration	| Low security |

#### How to implement backend deployment
The encrypted string generated at backend is delivered to the client and used for the following scenario: when API enterRoom is called for entering a room, the encrypted string is transferred to the field authBuffer in the parameters for entering room.




### 3. Algorithm encryption details
- Key: APPID corresponds to the MD5 value of the authentication key, with a length of 16 bytes.
- Encryption algorithm: TEA
- Encryption library and example: Appendix [authbuffer.zip](https://main.qcloudimg.com/raw/eac8e36ca4a24edf9414dfe7f58a764a.zip)

>**Note:**
> The modified key takes effect within 15 minutes to 1 hour. Frequent modification is not recommended.


#### Encryption method	
- Convert numbers in ciphertext to network byte order (big endian).
- Construct the ciphertext into a string.
- Encrypt the string using Tea. The string output by symmetry_encrypt function is the encrypted permission string.

>**Note:**
>Do not convert the binary strings into hexadecimal ones.



## Offline Voice Key
Overview: Offline voice messages are uploaded and downloaded through the COS platform of Tencent Cloud, which requires separate authentication. Generating a signature used for authentication involves plaintext, key and algorithm.
### 1. Plaintext
The plaintext is constructed based on appid and openid.

### 2. Obtain the key
Click **Download Public and Private Keys** in the Authentication Information module on the application setting page to download the public and private keys for the application.
![](https://main.qcloudimg.com/raw/bed3c36cdf3fcb421878c64cd5d775ba.png)

Decompress the downloaded zip package and you can find two files as below:

| File Name       | Role    |
| :-----------: | ------------- |
|public_key |Public key |
|private_key |Private key |

Open a file in Notepad as required, copy the key in it, and enter the key to corresponding function as a parameter.

>**Note:**
>The public and private key pair obtained each time can be used after 1 hour upon download.

### 3. Deploy the algorithm
It is recommended to deploy the algorithm on the client in the early stage of integration, and deploy it at the application backend later.

| Solution       | Disadvantage        | Details |
| ------------- |:-------------:| ------------- 
| Backend deployment   		| Heavy workload				| [TLS Backend API User Guide](https://cloud.tencent.com/document/product/269/1510#1-.E6.A6.82.E8.BF.B0)					|
| Client deployment      	| Large installer package and low security 		| Two library files libqav_tlssig.so (Android) and QAVSDKTlsSig.framework (iOS), as well as QAVSig.cs are introduced to the project. 	|  

For more information, please see platform documents.

