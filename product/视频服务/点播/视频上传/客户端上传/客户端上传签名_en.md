## Overview
Client needs to send a request for uploading signature to App server before it initiates the upload operation (see [How to Upload from Client](/document/product/266/9219)). If the App server allows the signature to be uploaded from client, a signature for upload should be generated for the client according to the generation rules described in this document. The client must carry this signature when performing the upload operation, so that Tencent Cloud VOD system can verify whether the upload operation has been authorized.

## Signature Parameters

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- | --- |
| secretId | Yes | String | SecretId in the cloud API key. For more information, please see [How to Upload from Client - Obtain Cloud API Key](/document/product/266/9219#.E8.8E.B7.E5.8F.96.E4.BA.91-api-.E7.A7.98.E9.92.A5). |
| currentTimeStamp | Yes | Integer | Current Unix timestamp |
| expireTime | Yes | Integer | Unix timestamp for signature expiration.<br/>```expireTime = currentTimeStamp + Signature validity```<br/>The maximum value for signature validity is 7776000 (90 days). |
| random | Yes | Integer | 32-digit unsigned random integer, a parameter used to construct plaintext signature string |
| classId | No | Integer | Video file category. Default is 0 | 
| procedure | No | String | For operations of follow-up video tasks, please see [Overview of Task Flow](/document/product/266/10263) | 
| sourceContext | No | String | The information added when uploading from client. In [Event Notification - Notification of Upload Completion](/document/product/266/7830), an upload behavior can be identified based on this field. For more information, please see [How to Upload from Client - Event Notification](/document/product/266/9219#.E4.BA.8B.E4.BB.B6.E9.80.9A.E7.9F.A5). |
| oneTimeValid | No | Integer | Whether the signature is for one-time use only. For more information, please see [How to Upload from Client - One-time Signature](/document/product/266/9219#.E5.8D.95.E6.AC.A1.E6.9C.89.E6.95.88.E7.AD.BE.E5.90.8D). 0 (default) means it is not enabled, and 1 means the signature is valid only once. The error code is provided in One-time Signature section below. | 


## Steps for Generating Signature

The signature to be uploaded from client is generated in the following three steps:
1. Obtain API key.
2. Concatenate plaintext string.
3. Convert plaintext string into final signature.

> **Note:**
> It is complicated to generate client signature code. VOD provides examples of code for generating signature in different languages. See the examples of generating signature in different languages.

### Step 1: Obtain API key
Obtain or create a SecretID and get its SecretKey by referring to [How to Upload from Client - Obtain Cloud API Key](/document/product/266/9219#.E8.8E.B7.E5.8F.96.E4.BA.91-api-.E7.A7.98.E9.92.A5).

### Step 2: Concatenate plaintext string
Generate plaintext signature string "Original" based on the format requirement of URL QueryString<sup>[Note 1](#.E6.B3.A8-1)</sup>. The format is as follows:
```
secretId=[secretId]&currentTimeStamp=[currentTimeStamp]&expireTime=[expireTime]&random=[random]
```

### Step 3: Convert plaintext string into final signature
After the plaintext signature string "Original" is generated, encrypt the string via [HMAC-SHA1](https://www.ietf.org/rfc/rfc2104.txt) algorithm using the SecretKey to obtain "SignatureTmp"<sup>[Note 2](#.E6.B3.A8-2)</sup>:
```
SignatureTmp = HMAC-SHA1(secretKey, Original) 
```
Place the ciphertext string "SignatureTmp" in front of the plaintext string "Original" and join them together, and then encode the string using [Base64](https://tools.ietf.org/html/rfc4648) to obtain the final signature "Signature":
```
Signature = Base64(append(SignatureTmp, Original)) 
```

## Notes
#### Note 1
The plaintext signature string "Original" must meet the following requirements:

* It must contain four required parameters: secretId, currentTimeStamp, expireTime and random. It may contain any number of the optional parameters.
* Parameter values ***must*** be URL encoded, or QueryString resolution may fail.

>***Suggestion:*** Generating "Original" by directly performing operations on the string can easily cause errors. Most programming languages provide relevant class libraries to help developers concatenate and encode QueryString. Therefore, it is recommended that developers use standard class libraries to construct "Oringinal" if possible.

#### Note 2
The output for the ciphertext signature string "SignatureTmp" is a 20-byte binary string.

## Examples for Generating Signature in Different Languages

Here, we provide examples of generating the signature on different language platforms. You can refer to a certain example for your App based on your preference:
- [PHP Example](/document/product/266/10638#php-.E7.AD.BE.E5.90.8D.E7.A4.BA.E4.BE.8B)
- [Node.js Example](/document/product/266/10638#node.js-.E7.AD.BE.E5.90.8D.E7.A4.BA.E4.BE.8B)
- [Java Example](/document/product/266/10638#java-.E7.AD.BE.E5.90.8D.E7.A4.BA.E4.BE.8B)
- [C# Example](/document/product/266/10638#c.23-.E7.AD.BE.E5.90.8D.E7.A4.BA.E4.BE.8B)

## Signature Generation and Verification Tools
The following tools are provided to help you verify whether the signature you generated is correct:
[Upload from VOD Client - Signature Generation Tool](https://video.qcloud.com/signature/ugcgenerate.html): Enter the parameters and key required for the signature to generate a valid signature.
[Upload from VOD Client - Signature Verification Tool](https://video.qcloud.com/signature/ugcdecode.html): Resolve a valid signature to obtain the parameters used to generate this signature.


## One-time Signature

- When an one-time signature is used, the signature server must assign different signatures to the user each time (for example, the "random" of signatures assigned at the same time point is different). Otherwise, it may lead to error of repeated signatures.
- If the upload fails due to a signature error, you need to retry and obtain a new signature. Otherwise, the repeated signature may cause a failed retry (the error code returned due to Android and Java SDK signature errors is 1001).

