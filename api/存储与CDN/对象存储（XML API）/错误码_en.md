## Overview

This document describes the error codes and corresponding error messages returned when a request encounters error.

## Format of Returned Error Message

### Response Header

Content-Type：application/xml

Corresponding HTTP status code: 3XX, 4XX, 5XX

### Response Content

**Syntax Format**

```XML
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>[Error Code]</Code>
  <Message>[Error Message]</Message>
  <Resource>[Resource Address]</Resource>
  <RequestId>[Request ID]</RequestId>
  <TraceId>[Error ID]</TraceId>
</Error>
```

**Element Description**

| Element Name      | Description                               | Type        |
| --------- | ---------------------------------------- | --------- |
| Error     | Contain all error information.                                | Container |
| Code      | Error codes are used to locate a unique error condition and determine scenario of the error. Error codes are described in detail below.         | String    |
| Message   | Contain detailed error information.                                | String    |
| Resource  | Resource address: Bucket address or Object address.                  | String    |
| RequestId | The server will automatically generate a unique ID for the request when the request is sent. When a problem occurs, request-id can help COS locate the problem faster.  | String    |
| TraceId   | When a request encounters an error, the server will automatically generate a unique ID for the error. When a problem occurs, trace-id can help COS locate the problem faster. When a request encounters an error, one trace-id will correspond to one request-id.  | String    |

## List of Error Codes

**3XX Errors**

| Error code               | Description                                       | HTTP status code               |
| ----------------- | ---------------------------------------- | --------------------- |
| PermanentRedirect | This resource has been moved to another location permanently, please use HTTP Location to redirect to the new location | 301 Moved Permanently |
| Redirect          | Temporary redirection                                    | 307 Moved Temporarily |
| TemporaryRedirect | You will be redirected temporarily during DNS update process                        | 307 Moved Temporarily |

**4XX Errors**

| Error code                                 | Description                                | HTTP status code                             |
| ----------------------------------- | --------------------------------- | ----------------------------------- |
| BadDigest                           | The provided x-cos-SHA-1 value is different from the SHA-1 value of the file received by the server end | 400 Bad Request                     |
| EntityTooSmall                      | The size of the file to be uploaded is smaller than the required minimum size. This usually happens for multipart upload operations          | 400 Bad Request                     |
| EntityTooLarge                      | The size of the file to be uploaded is larger than the required maximum size                   | 400 Bad Request                     |
| ImcompleteBoady                     | The size of the file is inconsistent with Content-Length            | 400 Bad Request                     |
| IncorrectNumberOfFilesInPsotRequest | Only one file is allowed to be uploaded at a time for a Post request                 | 400 Bad Request                     |
| InlineDataTooLarge                  | The size of inline data is larger than the required maximum size                    | 400 Bad Request                     |
| InvalidArgument                     | The configuration declaration is invalid, this usually happens when configuring notifications                   | 400 Bad Request                     |
| InvalidBucketName                   | Bucket name is invalid                       | 400 Bad Request                     |
| InvalidDigest                       | x-cos-SHA-1 value is invalid                   | 400 Bad Request                     |
| InvalidPart                         | Part is missing or SectionID is invalid                 | 400 Bad Request                     |
| InvalidPolicyDocunment              | Policy configuration file is invalid                         | 400 Bad Request                     |
| InvalidURI                          | URI is invalid                            | 400 Bad Request                     |
| KeyTooLong                          | key is too long                             | 400 Bad Request                     |
| MalformedACLError                   | Described ACL policy does not comply with XML syntax                  | 400 Bad Request                     |
| MalformedPOSTRequest                | The Body content of the POST request is invalid, this usually happens for multipart upload operations         | 400 Bad Request                     |
| MalformedXML                        | Uploaded XML file does not comply with XML syntax                  | 400 Bad Request                     |
| MaxMessageLengthExceeded            | Request is too long                              | 400 Bad Request                     |
| MaxPostPreDataLengthExceededError   | The data prefix of the POST request is too long, this usually happens for multipart upload operations            | 400 Bad Request                     |
| MatadataTooLarge                  | The size of metadata is larger than the required maximum size                    | 400 Bad Request                     |
| MissingRequestBodyError             | Request Body is missing                          | 400 Bad Request                     |
| MissingSecurityHeader               | Required Header is missing                        | 400 Bad Request                     |
| RequestIsNotMultiPartContent        | The Content-Type of the POST request is invalid            | 400 Bad Request                     |
| RequestTimeOut                      | Request timed out                              | 400 Bad Request                     |
| TooManyBucket                       | The number of Buckets exceeded the limit                        | 400 Bad Request                     |
| UnexpectedContent                   | Relevant content is not supported for the request                         | 400 Bad Request                     |
| UnresolvableGrantByUID              | The provided UID does not exist                         | 400 Bad Request                     |
| UserKeyMustBeSpecified              | The path must be specified for the POST operation performed against a Bucket           | 400 Bad Request                     |
| AccessDenied                        | Access has been denied by the server end                           | 403 Forbidden                       |
| AccoountProblem                     | This operation has been denied by your account                       | 403 Forbidden                       |
| InvaildAccessKeyId                  | AccessKey does not exist                      | 403 Forbidden                       |
| InvalidObjectState                  | Request content is in conflict with Object attribute                  | 403 Forbidden                       |
| InvalidSecurity                     | Signature string is invalid                            | 403 Forbidden                       |
| RequestTimeTooSkewed                | Request time is beyond the valid period of permission                      | 403 Forbidden                       |
| SignatureDoesNotMatch               | Mismatched Authorization                  | 403 Forbidden                       |
| NoSuchBucket                        | Specified Bucket does not exist                      | 404 Not Found                       |
| NoSuchUpload                        | Specified multipart upload does not exist                        | 404 Not Found                       |
| NoSuchBucket                        | Specified Bucket policy does not exist                    | 404 Not Found                       |
| MethodNotAllowed                    | The HTTP method is not supported by this resource                     | 405 Method Not Allowed              |
| BucketAlreadyExists                 | The provided Bucket name already exists or is not available               | 409 Conflict                        |
| BucketNotEmpty                      | The Bucket to be deleted is not empty                    | 409 Conflict                        |
| InvalidBucketState                  | Request content is in conflict with Bucket attribute                  | 409 Conflict                        |
| actionAborted                    | This operation is not supported by specified resource                       | 409 Conflict                        |
| MissingContentLength                | Header Content-Length is missing           | 411 Length Required                 |
| PreconditionFailed                  | Precondition matching failed                          | 412 Precondition                    |
| InvalidRange                        | Requested file range is invalid                        | 416 Requested Range Not Satisfiable |

**5XX Errors**

| Error code                | Description               | HTTP status code                 |
| ------------------ | ---------------- | ----------------------- |
| InternalError     | Internal error occurred on the server end          | 500 Internal Server     |
| NotImplemented     | A method in the Header cannot be implemented | 501 Not Implemented     |
| ServiceUnavailable | The service is unavailable, please reduce access frequency    | 503 Service Unavailable |
| SlowDown           | Please reduce access frequency          | 503 Slow Down           |

**Other Errors**

| Error code                     | Description         | HTTP status code |
| ----------------------- | ---------- | ------- |
| InvaildAddressingHeader | Anonymous access is required | N/A     |


