Key Management Service (KMS) is a security-related management service. With KMS, you can manage key-based sensitive information more safely and conveniently, and Tencent Cloud can guarantee their usability and security. KMS also allows you to implement efficient encryption-based protection solutions for massive data or files.

Applicable developers

| Developer ID | Protected Data | Purpose | Solution |
|-|:-:|:-:|:-:|
| Website or application development | Certificates, keys | Websites and applications use HTTPS certificates to secure communications protocols and also use keys to sign documents with their own corporate signatures. However, these common security solutions rely heavily on the security of certificates and keys | KMS file encryption |
| Background service development | Passwords, login keys, configurations | Database passwords, login keys, configuration information of background service may be used by hackers as stepping information to control the entire system. It is very dangerous to store plaintext on the disk | KMS file encryption |
| Contents, social network websites or applications | User-generated contents, valuable intellectual properties | The core UGC contents or unique intellectual properties relied on by enterprises to establish competitive advantage in the industry must not be "dragged" | KMS Envelope Encryption |
| Governments, financial institutions | Protocol communication contents, important files and data | The communication and storage data of governments and financial institutions are highly valuable and confidential, whose compliance and security must be ensured when business systems are established | KMS Envelope Encryption |
