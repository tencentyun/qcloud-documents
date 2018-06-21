### 1. Overview
Game Multimedia Engine (GME) provides audio/video keys for authentication for joining voice chat room and encryption of permissions for sending upstream and downstream data.
- Key: APPID corresponds to the MD5 value of audio/video key, with a length of 16 bytes.
- Encryption algorithm: TEA
- Encryption library and example: Attachment [tea.zip](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/tea.zip)

Obtain the key in the following location at Tencent Cloud backend. 
![4](https://main.qcloudimg.com/raw/3484d992b06830c504fa3267009aaef8.png)

The modified key takes effect within 15 minutes to 1 hour. Frequent modification is not recommended.

### 2. Encryption of Permission for Joining Room
#### 2.1. Ciphertext content
<table class="t">
<tbody><tr>
<th> Field Description
</th><th> Type/Length
</th><th> Description
</th></tr>
<tr>
<td> cVer
</td><td> unsigned char/1
</td><td> Version No. Enter 0.
</td></tr>
<tr>
<td> wAccountLen
</td><td> unsigned short/2
</td><td> Length of third-party account
</td></tr>
<tr>
<td> buffAccount
</td><td> wAccountLen
</td><td> Characters of third-party account
</td></td>
<tr>
<td> dwSdkAppid
</td><td> unsigned int/4
</td><td> sdkappid
</td></tr>
<tr>
<td> dwAuthId
</td><td> unsigned int/4
</td><td> Group ID (roomID)
</td></tr>
<tr>
<td> dwExpTime
</td><td> unsigned int/4
</td><td> Expiration time  
(current time + validity period) (in sec). 300 seconds is recommended.
</td></tr>
<tr>
<td> dwPrivilegeMap
</td><td> unsigned int/4
</td><td> Permission bit. <br>
Audio-only scenario:<br>
If joining broadcasting is needed, set it to: AUTH_BITS_CREATE_ROOM | AUTH_BITS_JOIN_ROOM |
AUTH_BITS_SEND_AUDIO | AUTH_BITS_RECV_AUDIO<br>
If joining broadcasting is not needed, set it to: AUTH_BITS_CREATE_ROOM | AUTH_BITS_JOIN_ROOM | 
AUTH_BITS_RECV_AUDIO<br>
Video scenario:<br>
If joining broadcasting is needed, set it to: AUTH_BITS_CREATE_ROOM | AUTH_BITS_JOIN_ROOM |
AUTH_BITS_SEND_AUDIO | AUTH_BITS_RECV_AUDIO |
AUTH_BITS_SEND_CAMERA_VIDEO | AUTH_BITS_RECV_CAMERA_VIDEO |
AUTH_BITS_SEND_SCREEN_VIDEO | AUTH_BITS_RECV_SCREEN_VIDEO<br>
If joining broadcasting is not needed, set it to: AUTH_BITS_CREATE_ROOM | AUTH_BITS_JOIN_ROOM |
AUTH_BITS_RECV_AUDIO | AUTH_BITS_RECV_CAMERA_VIDEO |
AUTH_BITS_RECV_SCREEN_VIDEO

<a href="https://cloud.tencent.com/document/product/268/3227 ">For more information, click here</a>
</td></tr>
<tr>
<td> dwAccountType
</td><td> unsigned int/4
</td><td> Third-party account type,<a href="https://console.cloud.tencent.com/ilvb "> which can be found here</a>
</td></tr></tbody></table>

#### 2.2. Encryption method	
1. Convert numbers in ciphertext to network byte order (big endian);
2. Construct the ciphertext into a string;
3. Encrypt the string with TEA algorithm. The string output by function symmetry_encrypt is the encrypted permission string (Note: Do not convert the binary strings into hexadecimal ones)

#### 2.3. Tips on usage
The encrypted string generated at backend is delivered to the client and used for the following two scenarios:
1. When API enterRoom is called for joining a room, the encrypted string is transferred to the field authBuffer in the parameters for joining room.
2. When API ChangeRole is called to modify a role, the encrypted string is transferred to the parameter authBuffer or buff.
