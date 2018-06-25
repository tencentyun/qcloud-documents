
## Key Management Service

### Encryption/Decryption APIs
| Feature | Action ID | Description
|---------|---------|---------|
| [Encryption](https://cloud.tencent.com/document/product/573/8889) | Encrypt | It is used to encrypt data under 4 KB in size, such as RSA keys, database keys, or sensitive customer information. |
| [Decryption](https://cloud.tencent.com/document/product/573/8890) | Decrypt | It is used to decrypt ciphertext data to get plaintext data. |



### Key Management APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| [Create CMK](https://cloud.tencent.com/document/product/573/8893) | CreateKey | Create a custom master key (CMK) used to manage data keys. |
| [Obtain CMK List](https://cloud.tencent.com/document/product/573/8897) | ListKey | It is used to obtain all the KeyIds of a user. |
| [Obtain CMK Attributes](https://cloud.tencent.com/document/product/573/8898) | GetKeyAttributes | It is used to obtain the attribute information of a specified keyId. |
| [Disable CMK](https://cloud.tencent.com/document/product/573/8896) | DisableKey | It is used to disable a specified keyId. |
| [Enable CMK](https://cloud.tencent.com/document/product/573/8894) | EnableKey | It is used to enable a specified keyId. |
| [Generate Data Key](https://cloud.tencent.com/document/product/573/8895) | GenerateDataKey | It is used to generate a key that a user can use to encrypt the local data. |
| [Modify CMK Attributes](https://cloud.tencent.com/document/product/573/8892) | SetKeyAttributes | It is used to modify the attribute information of a specified keyId. |



