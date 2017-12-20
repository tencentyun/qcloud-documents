### 1. Overview
ILVB provides audio/video key for the encryption and authentication of relevant features. For now, the key is mainly used for the encryption of upstream/downstream permission and the cross-room joint broadcasting.
- Key: APPID corresponds to the MD5 value of audio/video key, with a length of 16 bytes.
- Encryption algorithm: TEA
- Encryption library and example: Appendix [tea.zip](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/tea.zip)

Obtain the key in the following location at Tencent Cloud backend. 
![4](//mc.qcloudimg.com/static/img/71dc27273a362ae8a7b0875855f2d269/image.png)

The key takes effect within 15 minutes to 1 hour once modified. Frequent modification is not recommended.

### 2. Encrypt Permission for Joining Room
#### 2.1. Ciphertext Content
<table class="t">
<tbody><tr>
<th>  Field Description
</th><th>  Type/Length
</th><th>  Value Definition/Note
</th></tr>
<tr>
<td> cVer
</td><td> unsigned char/1
</td><td> Version No. Please enter 0.
</td></tr>
<tr>
<td>  wAccountLen
</td><td>  unsigned short /2
</td><td>  Length of third-party account
</td></tr>
<tr>
<td>  buffAccount
</td><td>  wAccountLen
</td><td>  Characters of third-party account
</td></td>
<tr>
<td>  dwSdkAppid
</td><td>  unsigned int/4
</td><td>  sdkappid
</td></tr>
<tr>
<td>  dwAuthId
</td><td>  unsigned int/4
</td><td>  Group ID, i.e. roomID
</td></tr>
<tr>
<td>  dwExpTime
</td><td>  unsigned int/4
</td><td>  Expiration Time  
(current time + validity period) (in sec). 300 seconds is recommended.
</td></tr>
<tr>
<td>  dwPrivilegeMap
</td><td>  unsigned int/4
</td><td>  Permission bit. Recommendations:<br>
Audio-only scenario:<br>
If you need to join broadcasting, configure: AUTH_BITS_CREATE_ROOM | AUTH_BITS_JOIN_ROOM |
AUTH_BITS_SEND_AUDIO | AUTH_BITS_RECV_AUDIO<br>
If you don't need to join broadcasting, configure: AUTH_BITS_CREATE_ROOM | AUTH_BITS_JOIN_ROOM |
AUTH_BITS_RECV_AUDIO<br>
Video scenario:<br>
If you need to join broadcasting, configure: AUTH_BITS_CREATE_ROOM | AUTH_BITS_JOIN_ROOM |
AUTH_BITS_SEND_AUDIO | AUTH_BITS_RECV_AUDIO|
AUTH_BITS_SEND_CAMERA_VIDEO | AUTH_BITS_RECV_CAMERA_VIDEO |
AUTH_BITS_SEND_SCREEN_VIDEO | AUTH_BITS_RECV_SCREEN_VIDEO<br>
If you don't need to join broadcasting, configure: AUTH_BITS_CREATE_ROOM | AUTH_BITS_JOIN_ROOM |
AUTH_BITS_RECV_AUDIO | AUTH_BITS_RECV_CAMERA_VIDEO |
AUTH_BITS_RECV_SCREEN_VIDEO

<a href="https://cloud.tencent.com/document/product/268/3227 ">For more information, please click here</a>
</td></tr>
<tr>
<td>  dwAccountType
</td><td>  unsigned int/4
</td><td>  Third-party account type <a href="https://console.cloud.tencent.com/ilvb ">can be found here</a>
</td></tr></tbody></table>

#### 2.2. Encryption Method	
1. Use [google protobuf](//github.com/google/protobuf) for serialization, and a binary string is output.
2. Convert numbers in ciphertext to network byte order (big endian), and convert the encrypted string into a hexadecimal string in a case-insensitive manner.
3. Encrypt the binary string using TEA. The string output by symmetry_encrypt function is the encrypted string (authBuf).

#### 2.3. Tips on Usage
1. The encrypted string (authBuf) generated at the backend is sent to the client.
2. authBuf is passed when client calls JoinRoom function while joining a room.
