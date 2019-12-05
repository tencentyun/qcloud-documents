This document describes the architecture that is compatible with Tencent Cloud COS and how to apply Tencent Cloud COS to such architecture. To ensure service quality and data security, this document also provides suggestions on design and encoding of server architecture. It is recommended that you build the architecture in accordance with the following references.

![](//mccdn.qcloud.com/static/img/7acb464a731cd8a47480566ab443e2d9/image.png)

When you use Tencent Cloud COS to build a business scenario, the following parts are necessary:
- Tencent Cloud COS,  providing reliable and high-speed object storage service with high success rate;
- Developer's business server, 
  which can be used to:
- Generate signature. **The signature cannot be generated on the terminal APP. Otherwise it will cause a great security risk**;
- Manage user information and file resources in the database;
- Respond to the terminal's business request; the developer server can directly manage operations via Tencent Cloud COS.
- Terminal, which supports both uploading and downloading an object. It typically gets a signature from the developer's server before requesting Tencent Cloud COS to upload the object, and gets the object information such as object URL from the developer's server before downloading the object.

The terminal gets a signature from the developer's server before requesting Tencent Cloud COS to upload the object. COS will upload the signature for verification. If the signature is invalid, information such as "signature verification failed" will be returned.

- The terminal accesses the developer's server and gets a signature (Note: the signature cannot be created on the terminal APP; otherwise it may lead to user information leakage and other security risks);
- The terminal uploads the object, and COS verifies the permission, stores the object, generates file ID, URL and other information and returns them to the terminal;
- The terminal reports the object information and user information to the developer's service server.

![](//mccdn.qcloud.com/static/img/7acb464a731cd8a47480566ab443e2d9/image.png)



