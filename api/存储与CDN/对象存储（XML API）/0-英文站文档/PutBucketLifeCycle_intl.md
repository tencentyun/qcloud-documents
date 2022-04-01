## Description
COS allows users to manage the lifecycle of Objects in a Bucket. A lifecycle configuration contains one or more rule sets that will be applied to a set of object rules (where each rule defines an action for COS).
There are two types of operations:
- **Conversion** Defines when the object is converted to another storage class. For example, you can choose to convert an object to a low-frequency storage (STANDARD_IA for infrequent access) storage class 30 days after it is created. It also supports the sinking of data to archive storage (Archive, which is cheaper and currently only for Mainland China regions). For specific parameters, see the `Transition` item in the request example description.
- **Expiration:**Specifies the expiration time of the Object. COS will automatically delete expired Objects for the user.

### Notes

PUT Bucket lifecycle is used to create a new lifecycle configuration for Bucket. If the Bucket has been configured with a lifetime, using this interface to create a new configuration will overwrite the original configuration.

## Request

Grammar example:
```
PUT /?lifecycle HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Content-Length: length
Date: GMT Date
Authorization: Auth String
Content-MD5: MD5

Lifecycle configuration in the request body
```
> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)

### Request line

```
PUT /?lifecycle HTTP/1.1
```
The API interface accepts PUT requests.

### Request header

#### Public header
The implementation of this request operation uses the public request header. For details on the public request header, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728) section. <style rel="stylesheet"> table th:nth-of-type(1) { width: 180px; }</style>

#### Non-public header

**Required header**
The implementation of this request operation uses the following mandatory headers:

| Name | Description | Type | Required |
| ---------------- | ----------- | ------ | ---- |
| Content-MD5 | **Base64** encoded 128-bit content MD5 checksum as defined in RFC 1864. This header is used to check if the contents of the file have changed. | String | Yes |


### Request body

The specific node content of the request body requested by the API is:
```
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Filter>
      <Prefix></Prefix>
    </Filter>
    <Status></Status>
    <Transition>
      <Days></Days>
      <StorageClass></StorageClass>
    </Transition>
    <NoncurrentVersionExpiration>
      <NoncurrentDays></NoncurrentDays>
    </NoncurrentVersionExpiration>
  </Rule>
  <Rule>
    <ID></ID>
    <Filter>
      <Prefix></Prefix>
    </Filter>
    <Status></Status>
    <Transition>
      <Days></Days>
      <StorageClass></StorageClass>
    </Transition>
    <NoncurrentVersionTransition>
      <NoncurrentDays></NoncurrentDays>
      <StorageClass></StorageClass>
    </NoncurrentVersionTransition>
  </Rule>
  <Rule>
    <ID></ID>
    <Filter>
      <Prefix></Prefix>
    </Filter>
    <Status></Status>
    <Expiration>
      <ExpiredObjectDeleteMarker></ExpiredObjectDeleteMarker>
    </Expiration>
    <NoncurrentVersionExpiration>
      <NoncurrentDays></NoncurrentDays>
    </NoncurrentVersionExpiration>
  </Rule>
</LifecycleConfiguration>
```
The specific content is described as follows:


|Node Name (Keyword) | Parent Node | Description | Type | Required |
|---|---|---|---|---|
|LifecycleConfiguration |None |Lifecycle Configuration |Container |Yes|
|Rule| LifecycleConfiguration |Rules Description |Container| Yes |
|Filter |LifecycleConfiguration.Rule |Filter The Object collection that describes the impact of the rule |Container |Yes |
|Status |LifecycleConfiguration.Rule | Indicates if the rule is enabled, enumeration value: Enabled, Disabled |Container |Yes |
|ID |LifecycleConfiguration.Rule|Used to uniquely identify rules up to 255 characters in length |String |No|
|And |LifecycleConfiguration.Rule.Filter |Use to combine Prefix with Tag |Container |No|
|Prefix |LifecycleConfiguration.Rule.Filter<br> or LifecycleConfiguration.Rule.Filter.And |Specifies the prefix to which the rule applies. Objects that match the prefix are affected by this rule. Prefix can only have at most one |Container | No|
|Tag |LifecycleConfiguration.Rule.Filter<br> or LifecycleConfiguration.Rule.Filter.And |Label, Tag can have zero or more |Container |No|
|Key |LifecycleConfiguration.Rule.Filter.Tag<br> or LifecycleConfiguration.Rule.Filter.And.Tag |Tag Key, no more than 128 bytes. It cannot start with "cos:". It supports only letters, numbers, spaces, and symboles (+ - = . _ : /)|String |Yes|
|Value |LifecycleConfiguration.Rule.Filter.Tag<br> or LifecycleConfiguration.Rule.Filter.And.Tag |Tag Value, no more than 256 bytes in length, only supports letters, numbers, spaces, and +-=._:/ These symbols |String | is |
|Expiration |LifecycleConfiguration.Rule |Rules Expired Properties |Container |No|
|Transition |LifecycleConfiguration.Rule |Rules conversion properties, when objects are converted to Standard_IA or Archive |Container |No|
|Days |LifecycleConfiguration.Rule.Transition<br> or Expiration | Indicates how many days the action corresponding to the rule operates after the last modified date of the object. If it is Transition, the valid value of the field is a non-negative integer; if it is Expiration, the valid value of the field Is a positive integer | Integer | No |
|Date |LifecycleConfiguration.Rule.Transition<br> or Expiration | Indicates when the action corresponding to the rule is operating |String |No|
|ExpiredObjectDeleteMarker |LifecycleConfiguration.Rule.Expiration |Delete expired object delete tag, enum value true,false |String |No|
|AbortIncompleteMultipartUpload |LifecycleConfiguration.Rule |Set the maximum time allowed for shard uploads to keep running |Container |No|
|DaysAfterInitiation |LifecycleConfiguration.Rule<br>.AbortIncompleteMultipartUpload | Indicates how many days after the start of the shard upload must be completed |Integer |Yes |
|NoncurrentVersionExpiration |LifecycleConfiguration.Rule | Indicate when the non-current version object expires |Container |No|
|NoncurrentVersionTransition |LifecycleConfiguration.Rule | Indicates when a non-current version object is converted to STANDARD_IA or ARCHIVE |Container |No|
|NoncurrentDays |LifecycleConfiguration.Rule<br>.NoncurrentVersionExpiration<br> or NoncurrentVersionTransition|Specifies that the action corresponding to the rule is executed after the object becomes non-current version. If it is Transition, the valid value of the field is a non-negative integer; if it is Expiration, Field valid values ​​are positive integers | Integer | No |
|StorageClass |LifecycleConfiguration.Rule.Transition<br> or NoncurrentVersionTransition |Specifies the target storage type to which the Object is dumped, enumeration value: STANDARD_IA, ARCHIVE |String |Yes |


## Response
Response example:
```
HTTP/1.1 200 OK
Content-Type: application/xml
Date: Sat, 05 Aug 2017 07:13:50 GMT
Content-Length: 0
Server: tencent-cos
X-cos-request-id: NTk4NTcwMDNfMjQ4OGY3MGFfNDI0Y181
```

### Response header

#### Public response header
The response uses a common response header. See the [Public Response Header](https://cloud.tencent.com/document/product/436/7729) section for details on the public response header.
#### Unique response header
There is no special response header for this response.

### Response body
The response body returns empty.

### Error Codes
The following describes some of the common mistakes and the special circumstances of this request may occur:

|Error Code|HTTP Status Code|Description|
|--------|--------|----------|
|NoSuchBucket|404 Not Found|When accessing Bucket does not exist|
|MalformedXML|400 Bad Request| XML format is not legal, please compare it with restful api document |
|InvalidRequest|400 Bad Request|The request is invalid. If "Conflict lifecycle rule" is displayed in the error description, it means that there are conflicting parts in the rule in the xml data. |
|InvalidArgument|400 Bad Request|The request parameter is invalid. If "Rule ID must be unique. Found same ID for more than one rule" is displayed in the error description, it means that the id fields of multiple Rule are the same. |

Note: The specific cause of the error can be checked by referring to the returned message.
For more information on COS error codes, or a list of all product errors, please see the [Error Codes](https://cloud.tencent.com/document/product/436/7730) documentation.

## actual case

### request
```
PUT /?lifecycle HTTP/1.1
Host:lifecycletest-73196696.cos.ap-beijing.myqcloud.com
Date: Wed, 16 Aug 2017 11:59:33 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1502855771;1502935771&q-key-time=1502855771;1502935771&q-header-list=content-md5;host&q-url-param-list=lifecycle&q-signature= F3aa2c708cfd8d4d36d658de56973c9cf1c24654
Content-MD5: LcNUuow8OSZMrEDnvndw1Q==
Content-Length: 348
Content-Type: application/x-www-form-urlencoded

<LifecycleConfiguration>
  <Rule>
    <ID> id1 </ ID>
    <Filter>
       <Prefix>documents/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <Days>100</Days>
      <StorageClass>ARCHIVE</StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID>id2</ID>
    <Filter>
       <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Expiration>
      <Days>10</Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Wed, 16 Aug 2017 11:59:33 GMT
Server: tencent-cos
X-cos-request-id: NTk5NDMzYTRfMjQ4OGY3Xzc3NGRfMWY=
```