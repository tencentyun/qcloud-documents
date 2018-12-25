## Overview

Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document describes the authentication keys for all platforms to make it easy for developers to debug and integrate Game Multimedia Engine.

##  Key deployment
Tencent Cloud GME provides authentication keys for authentication of voice chat and voice message.

Plaintext, key and algorithm are used to generate a signature for authentication.

Plaintext is constructed using the following fields in the network byte order:

| Field Description | Type/Length | Value Definition/Note |
| ---------------- |-------------------|--------------|
| cVer				|unsigned char/1	|Version number. Value entered: 0 |
| wOpenIDLen		|unsigned short/2	|Length of third-party account	|
| dwOpenID			|wAccountLen		|Characters of third-party account	|
| dwSdkAppid		|unsigned short/4	|AppID of third-party account		|
| dwRoomID			|unsigned int/4		|For voice chat, enter the room ID; for voice message, enter 0. |
| dwExpTime		|unsigned int/4		|Expiration time (current time + validity period) (in sec). 300 seconds is recommended. |
| dwReserved1		|unsigned int/4		|Value entered: -1 or 0xFFFFFFFF |
| dwReserved2		|unsigned int/4		|Value entered: 0 |

### 1. Key
The permission key can be obtained on Tencent Cloud GME console.

![](https://main.qcloudimg.com/raw/bed3c36cdf3fcb421878c64cd5d775ba.png)

### 2. Algorithm
TEA symmetric encryption algorithm.
It is recommended to deploy authentication feature on the client at the early stage, and later deploy it at the game App backend.

| Solution       		| Advantage        		| Disadvantage																																|
| ------------- |-------------|-------------| 
| Backend deployment    		| High security	| Joint testing by backend developers is required |
| Client deployment      	| Quick integration	| Low security |

#### How to implement backend deployment
The encrypted string generated at backend is delivered to the client and used for the following scenario: when API EnterRoom is called for entering a room, the encrypted string is transferred to the field authBuffer in the parameters for entering room.




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



