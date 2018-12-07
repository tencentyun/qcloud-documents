## Customer Server Function

The following figure shows the role of a customer server in the process: it verifies whether the App has the permission to upload video files. If the App has such permission, the customer server calculates and sends the uploading signature to the App, and then the App uses the UGC SDK to upload video files.

![](//mc.qcloudimg.com/static/img/9c1893434805c80c44684207d47e4ab1/image.jpg)

Such process design ensures that your server controls whether to upload video files: On the one hand, you can determine on the server side which users can get uploading permissions; on the other hand, you can also effectively prevent attackers from using your cloud storage and CDN traffic, because the calculation key for uploading signatures is located on your server.


## Signature Generation and Calculation

For more information on signature calculation, please see [Signature Uploading](https://cloud.tencent.com/document/product/266/9221), which can be summarized as follows:

- **Step 1: Obtain SecretID and SecretKey**
You can obtain or create a SecretID in the management section of [Cloud API Key](https://console.cloud.tencent.com/capi), and acquire its corresponding SecretKey:
![](//mc.qcloudimg.com/static/img/23f95aaa97adf3eeae3bf90470fe5122/image.png)

- **Step 2: Combine the plaintext strings to be encrypted**
Combine the plaintext signature strings in the format of HTTP QueryString, as shown below:
```
Original = secretId=[SecretId]&currentTimeStamp=[currentTime]&expireTime=[expireTime]&random=[rand]
```

- **Step 3: Convert the plaintext string into a ciphertext signature**
Once the plaintext signature string "Original" is combined, use the acquired SecretKey to encrypt the string via [HMAC-SHA1](https://www.ietf.org/rfc/rfc2104.txt) to obtain "SignTmp":
```
SignTmp = HMAC-SHA1(SecretKey, Original) 
```

 Place the ciphertext string "SignTmp" in front of the plaintext string "Original", combine them, and then encode the string using [Base64](https://tools.ietf.org/html/rfc4648) to obtain the final signature "Sign":
```
Sign = Base64(append(SignTmp, Original)) 
```

-  **Sample Codes & Check Tools**
To avoid invisible characters and encoding problems in the process of string combining, you are highly recommended to use our sample codes for signature calculations instead of writing programs manually:
  + [PHP Sample](/document/product/266/7906)
  + [Node.js Sample](/document/product/266/7905)

 You can check the correctness of the generated signature using the following tools:
 + [UGC Upload - Signature Generation Tool](https://video.qcloud.com/signature/ugcgenerate.html): Enter the parameters and secret key required for the signature to generate a valid signature.
 + [UGC Upload - Signature Resolution Tool](https://video.qcloud.com/signature/ugcdecode.html): Resolve a valid signature to acquire the parameters used to generate this signature.

