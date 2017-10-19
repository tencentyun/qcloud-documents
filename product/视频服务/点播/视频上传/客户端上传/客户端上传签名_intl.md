## Overview

Client needs to request for upload signature from App server before it initiates the upload operation (refer to [Client Upload Overview](/document/product/266/9219)). If the App server allows the client to upload files, it should generate an upload signature for the client according to the generation rules described in this document. The client must carry this signature when performing the upload operation in order for Tencent Cloud VOD system to verity whether the upload operation has been authorized.

## Parameter Description

### Signature Parameters

The App server needs to determine 4 required parameters (and any number of optional parameters) to generate signature. The user-constructed plaintext signature string contains the following parameters:

#### Required Parameters

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- | --- |
| secretId | Yes | String | Secret ID of the [Cloud API Secret Key](https://console.cloud.tencent.com/capi), a parameter used to construct plaintext signature string. |  |
| currentTimeStamp | Yes | Integer | Current UNIX time, a parameter used to construct plaintext signature string.  |
| expireTime | Yes | Integer| Signature expiration time (UNIX), a parameter used to construct plaintext signature string. <br/>```expireTime = currentTimeStamp + Signature validity```<br/>The maximum value for signature validity is 7776000 (90 days).  |
| random | Yes | Integer | 32-digit unsigned random integer, a parameter used to construct plaintext signature string.  |

#### Optional Parameters

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- | --- |
| classId | No | Integer | Video file category. Default is 0.  | 
| isTranscode | No | Integer | Whether to transcode the video, default is 0 (do not transcode). 1 means to transcode video.  | 
| isScreenshot  | No | Integer | Whether to take screenshot for video, default is 0 (do not take screenshot), 1 means to take screenshot.  |
| isWatermark | No | Integer | Whether to apply watermark for video, default is 0 (do not apply watermark), 1 means to apply watermark.  |

## Steps to Generate Signature

The following steps are required for App server to generate an upload signature.

### Step 1: Acquire API Secret Key

Obtain or create a SecretID in the management section of [Cloud API Key](https://console.cloud.tencent.com/capi), and acquire its corresponding SecretKey.

![](//mc.qcloudimg.com/static/img/23f95aaa97adf3eeae3bf90470fe5122/image.png)

### Step 2: Concatenate Plaintext String

Generate plaintext signature string "Original" based on the format requirements of URL QueryString <sup>[Note 1](#.E6.B3.A8-1)</sup>. The format is as follows:

```
secretId=[secretId]&currentTimeStamp=[currentTimeStamp]&expireTime=[expireTime]&random=[random]
```

### Step 3: Convert Plaintext String into Final Signature

Once the plaintext signature string "Original" is generated, use the acquired secretKey to encrypt the string via [HMAC-SHA1](https://www.ietf.org/rfc/rfc2104.txt) algorithm to obtain "SignatureTmp" <sup>[Note 2](#.E6.B3.A8-2)</sup>:

```
SignatureTmp = HMAC-SHA1(secretKey, Original) 
```

Place the ciphertext string "SignatureTmp" in front of plaintext string "Original" and concatenate them, then encode the string using [Base64](https://tools.ietf.org/html/rfc4648) to obtain the final signature "Signature":

```
Signature = Base64(append(SignatureTmp, Original)) 
```

## Note
### Note 1

The plaintext signature string "Original" must meet the following requirements:

* It must contain four required parameters: secretId, currentTimeStamp, expireTime and random. It may contain any number of the optional parameters.
* Parameter values ***must*** be encoded with URL, or Query String resolution may fail.

***Suggestion:*** Generating "Original" by directly manipulating the strings can easily cause errors. Most programming languages provide relevant libraries to help developers concatenate and encode QueryString. Thus, it is recommended that developers use standard class libraries to construct "Oringinal" if possible.

### Note 2

The output for the ciphertext signature string "SignatureTmp" is a 20-byte binary string.

## Signature Examples in Different Languages

Here, we provide examples of generating signatures on different language platforms. You can refer to a certain example for your App based on your preference:

[PHP Example](/document/product/266/9493)

[Node.js Example](/document/product/266/9243)

[Java Example](/document/product/266/9609)

[c# Example](/document/product/266/9762)

## Signature Generation and Verification Tools

Here, we provide tools to help users verify whether their generated signatures are correct:

[VOD Client Upload-Signature Generation Tool](https://video.qcloud.com/signature/ugcgenerate.html): Enter the parameters and secret key required for the signature to generate a valid signature.

[VOD Client Upload-Signature Verification Tool](https://video.qcloud.com/signature/ugcdecode.html): Resolve a valid signature to acquire the parameters used to generate this signature.

