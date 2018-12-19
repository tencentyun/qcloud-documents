Des encryption feature can protect plaintext HTTP requests against malicious tampering. You need to apply for enterprise edition before using encryption feature. The following shows how to use this feature:

### 1. Activate enterprise edition
The encryption feature is supported for HttpDNS enterprise edition only. You will receive the authorization ID and key which must be kept properly to avoid leakage.

### 2. Basic steps

Step 1: Check the authorization ID and its key in the email.
Step 2: Encrypt the domain name to be queried with the authorization ID and key by way of ECB of Des. The filling method is PKCS5Padding.
Step 3: Send request for encryption.
Step 4: Receive encrypted response.
Step 5: Decrypt the result to acquire the resolution result corresponding to the queried domain name.

Take Android system for example:

### 3. Example for Android
#### 3.1 Encrypt request to be sent

First, encrypt the domain name to be queried with the key corresponding to the ID in the email you received by way of ECB of Des. The filling method is PKCS5Padding.
```
try {
//Initialize the key
SecretKeySpec keySpec = new SecretKeySpec(encKey.getBytes("utf-8"), "DES");
//Use DES as algorithm, ECB as encryption method, and PKCS5Padding as filling method
Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
//Initialize
cipher.init(Cipher.ENCRYPT_MODE, keySpec);
//Acquire encrypted string
encryptedString = bytesToHex(cipher.doFinal(hostName.getBytes("utf-8")));
} catch (Exception e) {
e.printStackTrace();
}

```

#### 3.2 Send request
After the domain name is encrypted, send request to HttpDNS server:
```
//dn parameter corresponds to the encrypted string, and id is your key ID
http://119.29.29.29/d?dn=ac7875d400dacdf09954edd788887719&id=1&ttl=1
```

#### 3.3 Receive encrypted response
After the encrypted request is sent to HttpDNS, the client will receive an encrypted string:
`60a111ecb44008ac1b32d1fdfb42aa8a96bade20444421dcf83362072c84cf2ad8f870dfb0a1e448`

#### 3.4 Decrypt the result
```
try {
//Initialize the key
SecretKeySpec keySpec = new SecretKeySpec(encKey.getBytes("utf-8"), "DES");
//Use DES as algorithm, ECB as encryption method, and PKCS5Padding as filling method
Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
//Initialize
cipher.init(Cipher.DECRYPT_MODE, keySpec);
//Acquire decrypted string
decryptedString = cipher.doFinal(hexToBytes(s));
} catch (Exception e) {
e.printStackTrace();
}
```
Now, you have obtained the decrypted resolution result of domain name.

### 4. Encryption/Decryption test
To perform a test, you can use the following encryption and decryption test features:
Encryption: http://119.29.29.29/en?v=www.google.com&k=weijianliao
![Encryption Test](//mccdn.qcloud.com/static/img/0b2c48b03efef60980b937c85d035921/image.png)
Decryption: http://119.29.29.29/de?v=cd52888ecabcac455a14ddbac7f03d97&k=weijianliao
![Decryption Test](//mccdn.qcloud.com/static/img/100404ddcd725edd7933d6b7af7b7139/image.png)

