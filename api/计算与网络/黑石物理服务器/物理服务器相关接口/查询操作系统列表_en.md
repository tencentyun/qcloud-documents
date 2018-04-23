## Description

This API (DescribeOs) is used to acquire the operating systems that are supported by the specified model.

Domain name for API access: bm.api.qcloud.com

## Request

### Request Example

```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeOs
	&<Common request parameters>
    &deviceClassCode=<Device class>	
```

### Request Parameter

The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For other parameters, please see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is DescribeOs.

| Parameter Name | Required | Type | Description |
| ----------- | ---- | ------ | ---------------------------------------- |
| deviceClassCode | Yes | String | Device class. The device class information can be obtained via the API [Query Device Class (DescribeDeviceClass)](/doc/api/456/6636). |

## Response

### Response Example

```
{
  "code": 0,
  "message": "OK",
  "data": [
    {
      "osTypeId": "1",
      "osName": "BM-centos6.5",
      "osNameDisplay": "centos 6.5 64 bit",
      "osClass": "CentOS"
    },
    {
      "osTypeId": "3",
      "osName": "BM-debian7.8",
      "osNameDisplay": "debian 7.8 64 bit",
      "osClass": "Debian"
    },
    {
      "osTypeId": "4",
      "osName": "BM-rhel7.1",
      "osNameDisplay": "redhat 7.1 64 bit",
      "osClass": "Redhat"
    }
  ]
}

```

## Response Parameters
The response parameter section contains two layers of structure. The outer layer shows the response result of the API, and the inner layer shows the specific API contents, including the operating systems.

| Parameter Name | Type | Description |
| ------- | ------ | ---------------------------------------- |
| code | Int | Error code. 0: Successful; other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725). |
| message | String | Error Message |
| data | Array (Object) | An array of objects. Array element is the information on operating system. See details below. |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
| ------------- | ------ | ------------------------ |
| osTypeId | Int | Operating system type ID |
| osName | String | Operating system code |
| osNameDisplay | String | Operating system frontend display |
| osClass | String | Operating system class, such as CentOs, Debian |


## Error Code

| Error Code | Error Message | Error Description |
| ---- | --------------------- | ------- |
| 9001 | InternalError.DbError | An error occurred while operating the database |


## Practical Case

### Input

```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeOs
	&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC
	&Nonce=48476
	&Timestamp=1476436689
	&Region=bj
	&Signature=afRlJQ0disdT97B7uIfVB4v2KWo%3D
    &deviceClassCode=PS100v1
```

### Output

```
{
  "code": 0,
  "message": "OK",
  "data": [
    {
      "osTypeId": "1",
      "osName": "BM-centos6.5",
      "osNameDisplay": "centos 6.5 64 bit",
      "osClass": "CentOS"
    },
    {
      "osTypeId": "3",
      "osName": "BM-debian7.8",
      "osNameDisplay": "debian 7.8 64 bit",
      "osClass": "Debian"
    },
    {
      "osTypeId": "4",
      "osName": "BM-rhel7.1",
      "osNameDisplay": "redhat 7.1 64 bit",
      "osClass": "Redhat"
    }
  ]
}
```

