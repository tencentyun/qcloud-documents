## Description

XML APIs of object storage are lightweight and unconnected. You can call these APIs to send requests and receive responses directly via http/https, in order to interact with the backend of Tencent Cloud Object Storage (COS). The contents of both requests and responses for these APIs are in XML format.

Please refer to Signature Authentication for details before reading other API documents.

## Basic Information

This section provides major concepts and terms required to use COS effectively.

| Name          | Description                                       |
| ----------- | ---------------------------------------- |
| UID (AppID) | UID, a unique resource ID in user dimension owned by a developer when accessing COS services, used to indicate resources.        |
| SecretID    | SecretID is the project identity ID owned by a developer, used for identity authentication         |
| SecretKey   | SecretKey is the project identity key owned by a developer.                  |
| Bucket      | Bucket is a container used to store data in COS, and the first-level directory stored under Appid by a user. Each object is stored in a Bucket.  |
| Object      | Object is a specific file stored in COS. It is the basic entity that is stored.                |
| Region      | Region information of a domain. Enumerated values: cn-east (East China), cn-north (North China), cn-south (South China), sg (Singapore) |

## Quick Start

To use object storage APIs, you need to follow these steps first:

1. Obtain Appid, SecretID, SecretKey
2. Write an algorithm program for signature authentication (or use any server SDK)
3. Calculate the signature and call API to perform operation

## APIs of Other Versions

### JSON APIs

JSON APIs refer to the APIs used by users when connecting to COS after Oct. 2016. The upload domain is [Region].file.myqcloud.com. JSON APIs will be kept in a state of maintenance. They will be available for use but will not develop new features. The infrastructure of these APIs is the same as that of the APIs for standard XML, with data interoperability and can be cross-used. However, they're not compatible with each other and have different domains. [Document Link](/document/product/436/6053)

### Historical APIs

Historical APIs refer to the APIs used by users when connecting to COS before Oct. 2016. The upload domain is web.file.myqcloud.com. For users who use these APIs, COS will help them migrate data slowly, and forward requests. Users do not need to change APIs if they don't need to use any new features. The infrastructure of these APIs is different with that of the API for standard XML, without data interoperability, and both APIs are not compatible with each other. [Document Link](/document/product/430/6012)
