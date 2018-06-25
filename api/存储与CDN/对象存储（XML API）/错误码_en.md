## Overview

This document describes the error codes and corresponding error messages returned when a request encounters an error.

## Format of Returned Error Message

### Response Header

Content-Type: application/xml

Corresponding HTTP status code: 3XX, 4XX, 5XX

### Response Content

**Syntax Format**

```XML
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>[Error code]</Code>
  <Message>[Error message]</Message>
  <Resource>[Resource Address]</Resource>
  <RequestId>[Request ID]</RequestId>
  <TraceId>[Error ID]</TraceId>
</Error>
```
<style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

**Element Description**

| Element Name      | Description                               | Type        |
| --------- | ---------------------------------------- | --------- |
| Error     | Contain all error information.                               | Container |
| Code      | Error codes are used to locate a unique error condition and determine scenario of the error. Error codes are described in detail below.         | String    |
| Message   | Contain detailed error information.                               | String    |
| Resource  | Resource address: Bucket address or Object address.                  | String    |
| RequestId | The server will automatically generate a unique ID for the request when the request is sent. When a problem occurs, request-id can help COS locate the problem faster. | String    |
| TraceId   | When a request encounters an error, the server will automatically generate a unique ID for the error. When a problem occurs, trace-id can help COS locate the problem faster. When a request encounters an error, one trace-id corresponds to one request-id. | String    |

## Error Codes

**3XX Errors**

| Error Code               | Description                                       | HTTP Status Code               |
| ----------------- | ---------------------------------------- | --------------------- |
| PermanentRedirect | This resource has been moved to another location permanently, please use HTTP Location to redirect to the new location | 301 Moved Permanently |
| TemporaryRedirect | This resource has been moved to another location temporarily, please use HTTP Location to redirect to the new location | 302 Moved Temporarily |
| Redirect          | Temporary redirection                                    | 307 Moved Temporarily |
| TemporaryRedirect | You will be redirected temporarily during DNS update process                        | 307 Moved Temporarily |

**4XX Errors**

| Error Code                                 | Description                                | HTTP Status Code                             |
| ----------------------------------- | --------------------------------- | ----------------------------------- |
| BadDigest                           | The provided x-cos-SHA-1 value is different from the SHA-1 value of the file received by the server end | 400 Bad Request                     |
| EntityTooSmall                      | The size of the file to be uploaded is smaller than the required minimum size, which is common for multipart upload          | 400 Bad Request                     |
| EntityTooLarge                      | The size of the file to be uploaded is larger than the required maximum size                   | 400 Bad Request                     |
| ImcompleteBody                      | The actual content length of the request is inconsistent with the specified Conent-Length             | 400 Bad Request                     |
| IncorrectNumberOfFilesInPostRequest | Only one file is allowed to be uploaded at a time for a Post request                 | 400 Bad Request                     |
| InlineDataTooLarge                  | The size of inline data is larger than the required maximum size                    | 400 Bad Request                     |
| InvalidArgument                     | URI is invalid                   | 400 Bad Request                     |
| InvalidBucketName                   | Bucket name is invalid                       | 400 Bad Request                     |
| InvalidDigest                       | x-cos-SHA-1 value is invalid                   | 400 Bad Request                     |
| InvalidPart                         | Part is missing or SectionID is invalid                 | 400 Bad Request                     |
| InvalidPolicyDocunment              | Policy configuration file is invalid                         | 400 Bad Request                     |
| InvalidURI                          | URI is invalid                            | 400 Bad Request                     |
| KeyTooLong                          | File path is too long                            | 400 Bad Request                     |
| MalformedACLError                   | Described ACL policy does not comply with XML syntax                  | 400 Bad Request                     |
| MalformedPOSTRequest                | The Body content of the POST request is invalid         | 400 Bad Request                     |
| MalformedXML                        | "body" in XML format does not comply with XML syntax                 | 400 Bad Request                     |
| MaxMessageLengthExceeded            | Request is too long                              | 400 Bad Request                     |
| MaxPostPreDataLengthExceededError   | The data prefix of the POST request is too long, this usually happens for multipart upload operations            | 400 Bad Request                     |
| MatadataTooLarge                  | The size of metadata is larger than the required maximum size                    | 400 Bad Request                     |
| MissingRequestBodyError             | Request Body is missing                          | 400 Bad Request                     |
| MissingSecurityHeader               | Required Header is missing                        | 400 Bad Request                     |
| MissingContentMD5             | Content-MD5 is missing in request header                         | 400 Bad Request                     |
| MissingAppid                  |   Appid is missing in request header  | 400 Bad Request                     |
| MissingHost                   |  Host is missing in request header    | 400 Bad Request                     |
| RequestIsNotMultiPartContent        | The Content-Type of the POST request is invalid            | 400 Bad Request                     |
| RequestTimeOut                      | Read timeout. Check whether the network is too slow or number of concurrent file uploads is too large                                | 400 Bad Request                     |
| TooManyBucket                       | The number of Buckets exceeded the limit (200)                       | 400 Bad Request                     |
| UnexpectedContent                   | Relevant content is not supported for the request                         | 400 Bad Request                     |
| UnresolvableGrantByUID              | The provided UID does not exist                         | 400 Bad Request                     |
| UserKeyMustBeSpecified              | The path must be specified for the POST operation performed against a Bucket           | 400 Bad Request                     |
| AccessDenied                        | Access denied due to invalid signature or permission                           | 403 Forbidden                       |
| AccountProblem                     | This operation has been denied by your account                       | 403 Forbidden                       |
| InvaildAccessKeyId                  | AccessKey does not exist                      | 403 Forbidden                       |
| InvalidObjectState                  | Request content is in conflict with Object attribute                  | 403 Forbidden                       |
| InvalidSecurity                     | Signature string is invalid                            | 403 Forbidden                       |
| RequestTimeTooSkewed                | Request time is beyond the valid period of permission                      | 403 Forbidden                       |
| SignatureDoesNotMatch               | Incorrect signature                  | 403 Forbidden                       |
| NoSuchBucket                        | Specified Bucket does not exist                      | 404 Not Found                       |
| NoSuchUpload                        | Specified multipart upload does not exist                        | 404 Not Found                       |
| NoSuchBucket                        | Specified Bucket policy does not exist                    | 404 Not Found                       |
| MethodNotAllowed                    | The HTTP method is not supported by this resource                     | 405 Method Not Allowed              |
| BucketAlreadyExists                 | BucketName specified by CreateBucket is already in use. Select another BucketName               | 409 Conflict                        |
| BucketNotEmpty                      | Delete files and unfinished multipart upload tasks before performing DeleteBucket operation                    | 409 Conflict                        |
| InvalidBucketState                  | Bucket status conflicts with operation request, for example, multi-version management conflicts with cross-region duplication                   | 409 Conflict                        |
| actionAborted                    | This operation is not supported by specified resource                       | 409 Conflict                        |
| MissingContentLength                | Header Content-Length is missing           | 411 Length Required                 |
| PreconditionFailed                  | Precondition matching failed                          | 412 Precondition                    |
| InvalidRange                        | Requested file range is invalid                        | 416 Requested Range Not Satisfiable |
| InvalidSHA1Digest                        | sha1 of the request content is invalid                        | 400 Bad Request  |
| NoSuchUpload |	"uploadid" specified when performing multipart upload operation does not exist  | 400 Bad Request  |
| InvalidPart | Part is missing  | 400 Bad Request  |
| InvalidPartOrder | The numbers of uploaded parts are discontinuous  | 400 Bad Request  |
| ObjectNotAppendable | Specified file is not appendable  | 400 Bad Request  |
| AppendPositionErr | Append: file length is inconsistent with position  | 400 Bad Request  |
| NoSuchVersion | Specified version does not exist  | 400 Bad Request  |
| NoLifecycle | Lifecycle does not exist  | 400 Bad Request  |
| PreconditionFailed | Precondition matching failed  | 400 Bad Request  |
| UnexpectedContent | Relevant content is not supported for the request  | 400 Bad Request  |
| MultiBucketNotSupport | Only one bucket is configured for cross-region duplication  | 400 Bad Request  |
| NotSupportedStorageClass | Specified storage type is invalid  | 400 Bad Request  |
| InvalidAccessKeyId | AccessKey does not exist |  403 Forbidden                       |
| ExpiredToken | Signature string expired | 403 Forbidden                       |


**5XX Errors**

| Error code                | Description               | HTTP status code                 |
| ------------------ | ---------------- | ----------------------- |
| InternalError     | Internal error occurred on the server end          | 500 Internal Server     |
| NotImplemented     | A method in the Header cannot be implemented | 501 Not Implemented     |
| ServiceUnavailable | Internal error on the server. Try again   | 503 Service Unavailable |
| SlowDown           | Please reduce access frequency          | 503 Slow Down           |

**Other Errors**

| Error code                     | Description         | HTTP status code |
| ----------------------- | ---------- | ------- |
| InvaildAddressingHeader | Anonymous access is required | N/A     |


