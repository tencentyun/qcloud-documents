## Description
Get Bucket Lifecycle request is used to read life cycle management configurations. You will receive 404 Not Found if there is no configuration.

(Currently this is only supported for South China region)

## Request

### Request Syntax

```HTTP
GET /?lifecycle HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### Request Parameter

No particular request parameters

### Request Header

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

| Name                             | Description                                       | Type        |
| ------------------------------ | ---------------------------------------- | --------- |
| LifecycleConfiguration         | Describe all configuration information of this life cycle management. Supports up to 1000 rule entries.             | Container |
| Rule                           | Describe detailed information of a single rule entry, supports up to 1000 rule entries<Br/>Parent node: LifecycleConfiguration | Container |
| Prefix                         | Prefix matching policy (blank for root directory). Cannot specify the same prefix path for multiple Rules. Cannot specify a Rule for sub directories when the Rule of the same type has already been specified for the parent directory<Br/>Parent node: LifecycleConfiguration | String    |
| Status                         | Whether the policy is enabled. Enumerated values include Enabled, Disabled<Br/>Parent node: LifecycleConfiguration | String    |
| ID                             | Policy name<Br/>Parent node: LifecycleConfiguration    | String    |
| Transition                     | Configure the lifecycle management rules for files<Br/>Parent node: Rule                 | Container |
| Expiration                     | Configure periodic deletion rule for files. Expiration time must be longer than transition time<Br/>Parent node: Rule    | Container |
| Days                           | The action will be performed after this specified number of days have elapsed since the creation of the file. Please use a natural number for Transition action, and a positive integer for Expiration action. Different time formats may be used under different Rules, but not under the same Rule<Br/>Parent node: Transition, Expiration | Integer    |
| Date                           | The action will be performed at this specified time (time format is ISO 8601). You must specify UTC+8 to trigger 0 o'clock of the day. You may specify a historical time, such as 2016-10-31T00:00:00+08:00. The action will be performed when the current time is later than, or equal to Date (effect is long-term). Different time formats may be used under different Rules, but not under the same Rule<Br/>Parent node: Transition, Expiration | Intger    |
| StorageClass                   | Specify storage class, enumerated values include Standard, Standard_IA, Nearline<Br/>Parent node: Transition | String    |
| AbortIncompleteMultipartUpload | Configure periodic deletion rule for incomplete multipart upload operations<Br/>Parent node: Rule            | Container |
| DaysAfterInitiation            | Abort operation after this specified number of days have elapsed since the initialization part has been uploaded                  | Positive integer       |

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

