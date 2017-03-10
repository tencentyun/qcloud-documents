## Description
Put Bucket Lifecycle request is used to configure life cycle management. You can use this request to implement lifecycle management and periodic deletion for data. This operation will overwrite previous configuration files with newly uploaded files. Life cycle management is effective to both files and folders.

(Currently this is only supported for South China region)

## Request

### Request Syntax

```HTTP
PUT /?lifecycle HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Content-Type:application/xml
Content-MD5:MD5
Authorization: Auth
```

### Request Parameter

No particular request parameters

### Request Header

#### Required Headers

| Name          | Description                               | Type     | Required   |
| ----------- | -------------------------------- | ------ | ---- |
| Content-MD5 | 128-bit content MD5 algorithm check value defined in RFC 1864.  | String | Yes |

### Request Content

| Name                             | Description                                       | Type        | Required             |
| ------------------------------ | ---------------------------------------- | --------- | -------------- |
| LifecycleConfiguration         | Describe all configuration information of this life cycle management. Supports up to 1000 rule entries.             | Container | Yes              |
| Rule                           | Describe detailed information of a single rule entry, supports up to 1000 rule entries<Br/>Parent node: LifecycleConfiguration | Container | Yes              |
| Prefix                         | Prefix matching policy (blank for root directory). Cannot specify the same prefix path for multiple Rules. Cannot specify a Rule for sub directories when the Rule of the same type has already been specified for the parent directory<Br/>Parent node: LifecycleConfiguration | String    | Yes              |
| Status                         | Whether the policy is enabled. Enumerated values include Enabled, Disabled<Br/>Parent node: LifecycleConfiguration | String    | Yes              |
| ID                             | Policy name<Br/>Parent node: LifecycleConfiguration    | String    | No              |
| Transition                     | Configure the lifecycle management rules for files<Br/>Parent node: Rule                 | Container | Yes              |
| Expiration                     | Configure periodic deletion rule for files. Expiration time must be longer than transition time<Br/>Parent node: Rule    | Container | Yes              |
| Days                           | The action will be performed after this specified number of days have elapsed since the creation of the file. Please use a natural number for Transition action, and a positive integer for Expiration action. Different time formats may be used under different Rules, but not under the same Rule<Br/>Parent node: Transition, Expiration | Integer    | Choose one (Days or Date)   |
| Date                           | The action will be performed at this specified time (time format is ISO 8601). You must specify UTC+8 to trigger 0 o'clock of the day. You may specify a historical time, such as 2016-10-31T00:00:00+08:00. The action will be performed when the current time is later than, or equal to Date (effect is long-term). Different time formats may be used under different Rules, but not under the same Rule<Br/>Parent node: Transition, Expiration | Integer    | Choose one (Days or Date)   |
| StorageClass                   | Specify storage class, enumerated values include Standard, Standard_IA, Nearline. <Br/>Parent node: Transition | String    | Must be included in Transition |
| AbortIncompleteMultipartUpload | Configure periodic deletion rule for incomplete multipart upload operations<Br/>Parent node: Rule            | Container | Yes              |
| DaysAfterInitiation            | Abort operation after this specified number of days have elapsed since the initialization part has been uploaded                  | Positive integer       | Yes              |

Configuring the lifecycle management rules for files

```XML
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Transition>
      <Date></Date>
      <StorageClass></StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Transition>
      <Days></Days>
      <StorageClass></StorageClass>
    </Transition>
  </Rule>
</LifecycleConfiguration>
```

Configuring periodic deletion rule for files

```XML
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Expiration>
      <Date></Date>
    </Expiration>
  </Rule>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Expiration>
      <Days></Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
```

Configuring periodic deletion rule for incomplete multipart upload operations

```XML
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <AbortIncompleteMultipartUpload>
      <DaysAfterInititation></DaysAfterInititation>
    </AbortIncompleteMultipartUpload>
  </Rule>
</LifecycleConfiguration>
```

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

No response content
