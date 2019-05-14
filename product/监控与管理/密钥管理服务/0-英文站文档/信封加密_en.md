## Overview
Envelope Encryption, also known as digital envelope technology, is an encryption solution that combines symmetric and asymmetric encryption technologies aiming to take advantage of **the high performance of symmetric encryption** and **the manageability of asymmetric encryption**. In Envelope Encryption, large amount of business data is encrypted using **Data Encryption Key (DEK)** in the process of storage or communication by means of **symmetric encryption**. DEK is encrypted using **Customer Master Key (CMK )** by means of **asymmetric encryption**. During decryption in the communication scenario, for example, the sender sends both data ciphertext and DEK ciphertext, and the receiver decrypts DEK plaintext first, and then decrypts data plaintext using DEK.

### Figure

![](https://mc.qcloudimg.com/static/img/7c76f4c06331142c09008735cfbaaf3b/ee_1.png)

In Step 3 Encrypt Data of "Encryption" and Step 4 Decrypt Data of "Decryption", business data is encrypted and decrypted using DEK by means of **symmetric encryption** for the **local service** on CVM.

### How to Create Plaintext DEK?

1. Create an AES 256 data key using the KMS Cloud API. For more information, please see [Generate Data Key](/document/product/573/8895).
2. The key is created using third-party tools or development libraries (such as OpenSSL).

### How to Create and Store Ciphertext DEK?

1. The ciphertext DEK can be generated from the plaintext encrypted via the KMS Cloud API, or by using online tools. For more information, please see [Encryption and Decryption](/document/product/573/8877).
2. Ciphertext DEK is stored by users. In common implementation solutions, the ciphertext DEK is stored together with ciphertext business data, for example, in a storage container or that similar to an access path in storage scenarios. In communicating scenarios, ciphertext DEK and ciphertext business data together form a message.

## Advantages

### High Efficiency
All business data is encrypted using highly efficient local symmetric encryption, which has little impact on the business access experience. For the costs of DEK creation and encryption/decryption, except in extreme cases, you need to use "one key at a time" solution. In most scenarios, the plaintext and ciphertext of one DEK can be reused for a certain period of time, so the cost is generally small.

### Secure and Easy-to-use
The security of Envelope Encryption is similar to a common public key system. Since DEK protects business data, and Tencent Cloud KMS protects DEK and provides increased availability, your CMK is never disclosed. Only the object authorized to access with key can operate on CMK.

## When to use Envelope Encryption on the cloud?

1. **Larger volume**: Currently, KMS API supports the encryption and decryption of data under 4 KB in size.
2. **Massive data and low latency**: Most users want to encrypt business data, but care more about access delay. Although Tencent Cloud KMS backstage is of extremely high performance, it only supports remote call and uses asymmetric encryption. However, high-performance local symmetric encryption is used for most operations of Envelope Encryption solution.

### Comparison of Common Solutions
| | Sensitive Information Encryption | Envelope Encryption
|-|:-:|:-:|
| Related key | CMK | CMK, DEK |
| Performance | Asymmetric encryption, remote call | Remote asymmetric encryption for small amount of data, and local symmetric encryption for massive data |
| Key scenarios | Keys, certificates, small-sized data | Massive large-sized data |
