Permission key is optional. It is used to encrypt the protocol for audio/video permission when user joins an ILVB room.

## 1 Audio/Video Permission Key

Length: 16 characters
E.g.: 1234567890abcdef

## 2 Ciphertext Content

<table class="t">
<tbody><tr>
<th> <b>Field Description</b>
</th><th> <b>Type/Length</b>
</th><th> <b>Value Definition/Note</b>
</th></tr>
<tr>
<td> cVer
</td><td> unsigned char/1
</td><td> Version No. Please enter 0.
</td></tr>
<tr>
<td> wAccountLen
</td><td> unsigned short /2
</td><td> Length of third-party account
</td></tr>
<tr>
<td> buffAccount
</td><td> wAccountLen
</td><td> Characters of third-party account
</td></tr>
<tr>
<td> dwSdkAppid
</td><td> unsigned int/4
</td><td> sdkappid
</td></tr>
<tr>
<td> dwAuthId
</td><td> unsigned int/4
</td><td> Group ID
</td></tr>
<tr>
<td> dwExpTime
</td><td> unsigned int/4
</td><td> Expiration time (current time + validity period) (in sec). 300 seconds is recommended.
</td></tr>
<tr>
<td> dwPrivilegeMap
</td><td> unsigned int/4
</td><td> Permission bit
</td></tr>
<tr>
<td> dwAccountType
</td><td> unsigned int/4
</td><td> Third-party account type
</td></tr></tbody></table>

## 3 Encryption Method

1.1 Encryption algorithm: Tea

1.2 Encryption library and example: Appendix ["tea.zip"](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/tea.zip)

1.3 Encryption method:

(1) Convert numbers in ciphertext to network byte order (big endian);
(2) Construct the ciphertext into a string;
(3) Encrypt the string using Tea. The string output by symmetry_encrypt function is the encrypted permission string;

## 4 Use of ILVB SDK
A user who has joined the room through SDK can change specified permissions by calling the following methods of the API AVMultiRoom:

```
  /*
  @brief Modify user's permissions in the room.

  @details Dynamically modify upstream/downstream audio and video permissions during chat to achieve permission control and management by a third-party.

  @param [in] auth_buffer Encrypted permission string.

  @return Return the operation result.
  */
  virtual int32 ChangeAuthority(const std::string& auth_buffer) = 0;
```

auth_buffer is a generated encrypted permission string. SDK asynchronously returns the modification result through AVMultiRoom::Delegate.

```
/// For multi-member room delegation class, App needs to response to the change of room numbers by implementing member functions.
  struct Delegate : public AVRoom::Delegate {

    /**
    Callback function of @brief AVRoomMulti::ChangeAuthority().

    @details This function is used to asynchronously return the execution result of AVRoomMulti::ChangeAuthority().

    @param ret_code Error code:
     \n AV_OK Execution is successful;
     \n AV_ERR_FAILED Execution failed.
    */

    virtual void OnChangeAuthority(int32 ret_code) = 0;
  };
```


