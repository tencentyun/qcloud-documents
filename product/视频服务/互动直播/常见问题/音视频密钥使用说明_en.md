
## Audio & Video Key Instructions
### Key and encryption algorithm
#### Key: AppId corresponds to the audio/video key with a length of 16 bytes, which can be found in the official website:
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/audiosig_0.png)

#### Encryption algorithm: Tea;
####  Encryption library and example: Appendix "tea.zip";

### Usage Scenario 1: Encrypted permission string for creating a room

#### Ciphertext content

Field Description | Type/Length | Value Definition/Note
:--:|:--:|:--
cVer | unsigned char/1 | Version Number. Enter 0
wAccountLen | unsigned short/2 | Length of third-party account 
buffAccount | wAccountLen | Characters of third-party account 
dwSdkAppid | unsigned int/4 | sdkappid
dwAuthId | unsigned int/4 | Group ID
dwExpTime | unsigned int/4 | Expiration time (current time + validity period) (in sec). 300 seconds is recommended.
dwPrivilegeMap | unsigned int/4 | Permission bit
dwAccountType | unsigned int/4 | Third-party account type

#### Encrytion method
1. Convert numbers in ciphertext to network byte order (big endian);
2. Construct the ciphertext into a string;
3. Encrypt the string using Tea. The string output by symmetry_encrypt function is the encrypted permission string (Note: Do not convert the binary strings into hexadecimal ones).

#### Ciphertext verification
Use the tool test_tea_decode (packaged with lib) to initially verify whether the ciphertext can be decrypted.
1. Convert the ciphertext into a readable hexadecimal string.
2. Tool verification:
The scenario that the ciphertext can be decrypted correctly:
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/audiosig_1.png)
The scenario that the ciphertext cannot be decrypted correctly:
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/audiosig_2.png)

### Usage Scenario 2: Cross-room joint broadcasting encrypted string
#### Ciphertext content
Attachment: "conn_room_sig.proto".

```
package tencent.im.groupvideo.conn_room;

message ConnRoomSig
{
    optional uint32         uint32_groupcode            = 1; //Initiator's group number
    optional string         str_third_account           = 2; //Initiator's third-party account

    optional uint32         uint32_conned_groupcode     = 3; //Joined party's group number
    optional string         str_conned_third_account    = 4; //Joined party's third-party account

    optional uint32         uint32_create_time          = 5; //Signature creation time
    optional uint32         uint32_expire_time          = 6; //Signature expiration time
}
```
Field Description | Required or Not | Value Definition/Note
:--:|:--:|:--:
uint32_groupcode | Yes | Initiator's group number/group ID
str_third_account | Yes | Initiator's account
uint32_conned_groupcode | Yes | Group number/group ID of joined party
str_conned_third_account | Yes | Joined party account
uint32_create_time | Yes | Signature creation time
uint32_expire_time | Yes | Signature expiration time. It is recommended to set it as the creation time +300 seconds

#### Encryption method
1. Use google protobuf to serialize the ConnRoomSig object, then output the binary string;
2. Encrypt the binary string using TEA. The string output by symmetry_encrypt function is the encrypted string;
3. Convert the encrypted string into a hexadecimal string in a case-insensitive manner, for example:
```
bytes_conn_room_sig: 
"00A47C7E5FD0471A6D90CBE6FAAC2D862A114EFC6337D8F0BD1161BB53250F4EE46DB0244E8515D58BA7DAED23190484"
```
The official website of google protobuf: [https://github.com/google/protobuf](https://github.com/google/protobuf).
[Download Encrypted Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/tea_3.zip).

