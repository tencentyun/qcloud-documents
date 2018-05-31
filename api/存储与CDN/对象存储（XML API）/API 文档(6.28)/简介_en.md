The XML APIs of Tencent Cloud Object Storage (COS) service are a kind of lightweight interfaces without connection state. You can call these APIs to send requests and receive responses directly via http/https, in order to interact with the backend of Tencent Cloud Object Storage. The contents of both requests and responses for these APIs are in XML format.
>**Note:**
>Currently, the available Regions of COS have different values for XML APIs and JSON APIs, and the corresponding region fields are required when using different APIs and their SDKs. For more information, see the document [Available Regions](https://cloud.tencent.com/document/product/436/6224). 
>In order to use the XML APIs of Tencent Cloud Object Storage service more efficiently, please read [Request Signature](https://cloud.tencent.com/document/product/436/7778) carefully before reviewing other API documents.

## Terminology Information
Some main concepts and terms appear in the text:
<style rel="stylesheet">
table th:nth-of-type(1) {
width: 150px;	
}
table th:nth-of-type(2) {
width:550px;	
}
</style>

|Name|	Description|
|---|---|
| APPID	| A unique resource ID in user dimension owned by a developer when accessing COS services, which is used to indicate resources |
| SecretId | The project identity ID owned by a developer, which is used for identity authentication |
| SecretKey	| The project identity key owned by a developer |
| Bucket|	 The container used to store data in COS |
| Object |	 The specific file stored in COS, which is the basic entity that is stored |
| Region|	The region information in domain name. For enumerated values, please see the document [Available Regions](https://cloud.tencent.com/document/product/436/6224), such as: ap-beijing, ap-hongkong, eu-frankfurt, etc. |
| ACL |	Access Control List, which refers to the access control information list of specified Buckets or Objects |
| CORS | Cross-Origin Resource Sharing, <br>which refers to the HTTP request for resources from a different domain |
| Multipart Uploads | Refers to a multipart upload mode provided by Tencent Cloud COS service for uploading files |
## Quick Start

To use the Tencent Cloud object storage APIs, you need to follow these steps first:

1. Purchase the Tencent Cloud Object Storage (COS) service
2. Create a Bucket in Tencent Cloud [Object Storage Console](https://console.cloud.tencent.com/cos4/index) 
2. Obtain APPID, SecretId, and SecretKey on the console [Personal API Key](https://console.cloud.tencent.com/capi) page
2. Write an algorithm program for requesting signature (or use any of server-side SDKs)
3. Calculate the signature and call API to perform operation

## APIs of Other Versions

### JSON APIs

[JSON API](https://cloud.tencent.com/document/product/436/6052) is the API provided by Tencent Cloud COS service for users to access COS before launching the XML API, and the upload domain name is [Region].file.myqcloud.com. JSON APIs and standard XML APIs have the same underlying infrastructure, and thus data interoperability is possible and they can be cross-used. However, they're not compatible with each other and have different domains.
After the XML API service of Tencent Cloud COS is launched, it is recommended that you use the XML API interface. JSON APIs will be kept in a state of maintenance, and they will be available for use but no new features will be added.

