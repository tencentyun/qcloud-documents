## 1. API Description
 
This API (DescribeOs) is used to acquire the operating systems that are supported by the specified device.

Domain for API request: bm.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| deviceClass | Yes | String | Device class. You can acquire device class information by using the [Query Device Class (DescribeDeviceClass)](/doc/api/456/6636) API |



## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Array | Array. The array element is the information of operating system |

Operating system information in the data array

| Parameter Name | Type | Description |
|---------|---------|---------|
| osTypeId | Int | Operating system type ID |
| osName | String | Operating system code |
| osNameDisplay | String | Operating system frontend display |
| osClass | String | Operating system class, such as CentOs, Debian |


## 4. Module Error Codes

| code | codeDesc | Description |
|------|------|------|
| 9001 | InternalError.DbError | An error occurred when operating the database |


## 5. Example
 
Input

<pre>
	https://domain/v2/index.php?Action=DescribeOs
    &deviceClass=M10
	&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output

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
