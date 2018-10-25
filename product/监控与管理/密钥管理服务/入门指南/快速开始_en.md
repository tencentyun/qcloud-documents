## Overview
The document takes simple certificate encryption and decryption as an example to illustrate a typical KMS application scenario. The procedure of this example includes directly encrypting the certificates, keys and profiles on the host hard disk for protection.

## 1. Activate service
	
Go to [Application Page](https://cloud.tencent.com/act/apply/kmsreq), enter the information, and submit the application for approval.

## 2. Create a Key

When you get the internal trial qualification, go to the [Console](https://console.cloud.tencent.com/kms). Here we recommend to select Guangzhou as the region to conform to the follow-up demo codes.

Click the "New" button on the top, enter the key name, and click "OK" (the "Purpose" can be left empty).

After the page is switched back to "Key List", you can see the new key at the top of the list. You can also find it by the key name.

![](https://mc.qcloudimg.com/static/img/85f55b345a84f0f75c3bde5b46b65ea6/quickstart_1.png)

## 3. Encrypt an SSL certificate using tools on the Console

On the "Key List" page, click the "Key ID/Key Name" column of the created key to go to the "Details" page. Then, scroll to the "Online Tools" and select "Encrypt".

Tencent Cloud provides a [Demo Certificate (plaintext)>>](http://jkmsdemo-1252462967.cosgz.myqcloud.com/demo_cert.pem) for testing.

Open the certificate as text, copy the contents to the plaintext input box at the left side, and then click "Execute".

![](https://mc.qcloudimg.com/static/img/4c7135fc386cff8af1e2b5290a3084be/kms_start_3_4.png)

The ciphertext is generated into the result box at the right side. Save the ciphertext simply by clicking "Download" for further use in the decrypting process.

![](https://mc.qcloudimg.com/static/img/f070c3b96652d94a044b62a84e653526/kms_start_3_3.png)

## 4. Decrypt Certificate Ciphertext using KMS SDK

### Checking Python Environment
Python environment is required to run demo codes. Run the following command to see whether Python is installed in your server.
```
$ Python -V
Python 2.7.10
```
If the version information is returned, it means that Python is installed. Otherwise, please see [How to Install Python>>](https://cloud.tencent.com/document/product/440/6181)

### Running Demo
The followings are the core demo codes. To download the complete demo, please see [Get Started with Demo>>](http://jkmsdemo-1252462967.cosgz.myqcloud.com/kms_start_demo.zip).
```
#!/usr/bin/env python
# coding=utf8

from kms.kms_account import KMSAccount
from kms.kms_exception import *

# 1. Initialize KMS SDK
# Enter the cloud API key
secretId = "your secret id"
secretKey = "your secret key"

# Enter the appropriate endpoint URL based on the region where the key is created
endpoint = "https://kms-gz.api.qcloud.com"
kms_account = KMSAccount(endpoint, secretId, secretKey)

# 2. Call the decryption API
CiphertextBlob = "your ciphertextblob";
Plaintest = kms_account.decrypt(CiphertextBlob)
print "the decrypted data is :\n%s\n" % Plaintest
```

* secreteId and secretKey need to use the cloud API key of the account under which you create the key. Here you can find the [Cloud API Key](https://console.cloud.tencent.com/capi).
* The endpoint needs to correspond to the region selected when the key is created. The demo uses the URL corresponding to the Guangzhou region. For details, see [Region Description](https://cloud.tencent.com/document/product/573/8922).
* The CiphertextBlob is the certificate ciphertext generated using the tools in the console in previous step. You can also click [Demo Certificate (Ciphertext)>>](http://jkmsdemo-1252462967.cosgz.myqcloud.com/demo_ciphertextblob.txt) to download and copy the corresponding text into the code. The kms_start_demo.py file in the Demo package already includes this text.


Here are the demo command and the running result. The plaintext certificate is decrypted as a string in the memory of the demo program.
```
$ python kms_start_demo.py

the decrypted data is :
-----BEGIN CERTIFICATE-----
MIICgjCCAeugAwIBAgIJAJqEq8+4pyq/MA0GCSqGSIb3DQEBCwUAMHoxCzAJBgNV
BAYTAlVTMQswCQYDVQQIDAJDQTELMAkGA1UEBwwCU0YxDzANBgNVBAoMBkpveWVu
dDEQMA4GA1UECwwHTm9kZS5qczEMMAoGA1UEAwwDY2ExMSAwHgYJKoZIhvcNAQkB
FhFyeUB0aW55Y2xvdWRzLm9yZzAeFw0xNTA0MTgxMzI4NDFaFw00MjA5MDIxMzI4
NDFaMHoxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJDQTELMAkGA1UEBwwCU0YxDzAN
BgNVBAoMBkpveWVudDEQMA4GA1UECwwHTm9kZS5qczEMMAoGA1UEAwwDY2EzMSAw
HgYJKoZIhvcNAQkBFhFyeUB0aW55Y2xvdWRzLm9yZzCBnzANBgkqhkiG9w0BAQEF
AAOBjQAwgYkCgYEAqs4MKn9saUIu/9EfHQPouC3kL9Mo5sd1WR6RBeSd8cqeFxXW
EWEq/P0hUeAH1sY0u8RFOccJmSJg8KTyRGc+VZzWimopz17mTuQY4hPW4bFzqmQm
7STfJz5eHzynBTU8jk5omi8hjbnRA38jOm4D7rN/vqtB+RG+vEhxONnq4DMCAwEA
AaMQMA4wDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOBgQBo8rX1uZWHvKHG
gWw+LXrY24Pkg8NdDRmfqEVyuaR4GoGGOXCqlVaFa6x+4/eqOUzHoC9uGfPtjrvW
BYQ1o/l0JZWW4KZYuXoVuMUSj+sel82mf9zLDeq5WYTPECgJDMfgVpXOmhHfyezn
SkUTX7XJUohjET+X5BqTFlqRT/RfIw==
-----END CERTIFICATE-----
```


You can incorporate similar codes into your applications. The small extra workload can result in significant security enhancement.

## 5. In the above example, how well the certificate security is enhanced?

* ``Static storage security``: Hackers used to identify a certificate file by directly viewing the file in text mode or even by the suffix. But now, ``there is no plaintext certificate file`` on the host, which is replaced with a ``unrecognizable ciphertext``.

* ``Process Security``: For large development companies, certificate management personnel generate the ciphertext certificates. Developers develop programs to decrypt and use such certificates. OPS personnel deploy the ciphertext certificates. Both ``developers and OPS personnel`` ``cannot get plaintext certificates independently``. For individual developers, there is no security risk even if the encrypted certificates are "accidentally" uploaded to Git along with codes.

## 6. What to Do Next?
1. Create more keys via the console, and then you can enable or disable them, or modify their aliases or purpose descriptions.
	
	1) [New Key](/document/product/573/8875)
	
	2) [Key Management](/document/product/573/8876)
	
2. Try to use KMS for file encryptions and decryptions frequently, so that you are fully prepared to use KMS in actual business scenarios.

	1) [Encryption and Decryption](/document/product/573/8877)
	
	2) [Sensitive Information Encryption](/document/product/573/8790)

3. If you need to perform massive static data encryption or communication encryption, learn and try the KMS-based envelope encryption.

	1) [Envelope Encryption](/document/product/573/8791)
