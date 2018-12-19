## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ModifyHostsAttribute) is used to modify the attributes of a CDH instance, such as instance name and renewal flag. Either the parameter HostName or RenewFlag must be set, but not both.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyHostsAttribute |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| HostIds.N | Yes | Array of String | ID(s) of one or more CDH instances you are working with. |
| HostName | No | String | Displayed name of a CDH instance. It is limited to 60 characters. |
| RenewFlag | No | String | Auto renewal flag. Value range:<br><li>NOTIFY_AND_AUTO_RENEW: notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify expiry nor renew automatically<br><br>If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis when the account balance is sufficient. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidHost.NotSupported | This host instance is not supported for performing the specified operation. |
| InvalidHostId.Malformed | Invalid [CDH](https://cloud.tencent.com/document/product/416) `ID`. The specified [CDH](https://cloud.tencent.com/document/product/416) `ID` is in an incorrect format. For example, `host-1122` has an invalid `ID` length. |
| InvalidHostId.NotFound | The specified HostId does not exist, or does not belong to the request account. |

## 5. Example

### Example 1 Modify the attributes of a CDH instance

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ModifyHostsAttribute
&HostIds.0=host-ey16rkyg
&HostName=web server
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```


