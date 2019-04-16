## 1 Signature Definition

Tencent mobile service makes use of the signature to verify the legitimacy of the request. Developers allow the client to upload, download, and manage the specified resources by authorizing the signature to the client.

## 2 Signature Types

The signature consists of **multiple-time signature** and **one-time signature**:

- Multiple-time signature: The signature does not bind the fileid of the file, and you need to set a validity period later than the current time. This signature can be used multiple times within the validity period, and the maximum validity period can be set for three months.


- One-time signature: The signature will bind the fileid of the file. The valid period must be set to 0. This signature can only be used once, and can only be applied to the bound file.


