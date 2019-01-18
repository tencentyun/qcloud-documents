Welcome to Key Management Service (KMS).
For more information on KMS products, please see [Product Overview](https://cloud.tencent.com/document/product/573/8780).


For more information on supported operations, please see [API Overview Page](https://cloud.tencent.com/document/product/573/8899).


**Note: Currently, collaborator account is not allowed to perform KMS operations.**

## Cryptography Glossary
The key terms involved in the document are as follows:

| Term | Full Name | Description | Note |
|--|--|--|--|
| DataKey | Data Key | The key is actually used to encrypt business data |
| CMK | Customer Master Key | It is a key created by a user to encrypt packet data (a maximum of 4 KB) or DataKey |
| KeyId | Key Id | It is a global unique identifier returned to the user by CMK. Note: This is an index, but not CMK itself. |
| CiphertextBlob | Ciphertext Structure | The structure returned via the API Encrypt or GenerateDataKey called by the user, which contains plaintext KeyId and ciphertext DataKey or encrypted data |
| Root Key | | The key used to encrypt CMKs |

## KMS Terms

| Term | Full Name | Description |
|--|--|--|
| KMS | Key Management Service | PAAS layer key service, which provides key security management and packet data encryption and decryption service |
| HSA | Harden Security Appliance | A security module implemented by a software or a hardware, which is the core component to implement key management, encryption and decryption for KMS. |
| qps throttling | QPS Throttling | qps limit |




## Definitions of input and response parameters
- limit and offset

	> These parameters are used to control paging. For the results in a list format, if the number of entries exceeds the "limit" value, the number of returned values is limited to the "limit" value. You can use the parameters "limit" and "offset" to control paging. "limit" indicates the maximum number of entries returned at a time, and "offset" is the offset value.
	For example, if offset=0&limit=20, the 0th to the 20th entries are returned; if offset=20&limit=20, the 20th to the 40th entries are returned; if offset=40&limit=20, the 40th to the 60th entries are returned, and so on.
	
- id.n

	> Format for inputting multiple parameters at a time. Multiple parameters in such a format can be input at the same time. For example:
	
	> id.0="10.12.243.21"&id.1="10.12.243.21"&id.2="10.12.243.21"&id.3="10.12.243.21"...
	
	> And so on (starting with the subscript 0).


## API Quick Start

You can use KMS services through [KMS SDK](https://cloud.tencent.com/document/product/573/8908) (recommended. It is available in multiple languages) or by directly calling cloud APIs (this method is very inconvenient and is suitable for the users using a language other than SDK language):


Select a region and private/public network. The request domain names for the KMS APIs, unlike those of APIs of other cloud products, vary with the regions, and need to be selected based on the regions. Each request domain name has a composition such as `kms-region.api.cloud.tencent.com/v2/index.php`, where the "region" field needs to be replaced with the specific region: gz (Guangzhou), sh (Shanghai), bj (Beijing). If you are using a Tencent CVM, private network domain name is preferred, otherwise a public network domain name.

| Feature | API | Description
|---------|---------|---------|
| [Encryption](https://cloud.tencent.com/document/product/573/8889) | Encrypt | It is used to encrypt data under 4 KB in size, such as RSA keys, database keys, or sensitive customer information. |
| [Decryption](https://cloud.tencent.com/document/product/573/8890) | Decrypt | It is used to decrypt ciphertext data to get plaintext data. |
| [Create CMK](https://cloud.tencent.com/document/product/573/8893) | CreateKey | Create a custom master key (CMK) used to manage data keys. |
| [Obtain CMK List](https://cloud.tencent.com/document/product/573/8897) | ListKey | It is used to obtain all the KeyIds of a user. |
| [Obtain CMK Attributes](https://cloud.tencent.com/document/product/573/8898) | GetKeyAttributes | It is used to obtain the attribute information of a specified keyId. |
| [Disable CMK](https://cloud.tencent.com/document/product/573/8896) | DisableKey | It is used to disable a specified keyId. |
| [Enable CMK](https://cloud.tencent.com/document/product/573/8894) | EnableKey | It is used to enable a specified keyId. |
| [Generate Data Key](https://cloud.tencent.com/document/product/573/8895) | GenerateDataKey | It is used to generate a key that a user can use to encrypt the local data. |
| [Modify CMK Attributes](https://cloud.tencent.com/document/product/573/8892) | SetKeyAttributes | It is used to modify the attribute information of a specified keyId. |








