## 1. API Description

This API (ModifyHostsAttribute) is used to modify the attributes of CDH instance, such as instance name and renewal flag. Either the parameter HostName or RenewFlag must be set, but not both.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: ModifyHostsAttribute |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| HostIds.N | Yes | Array of String | ID(s) of one or more CDH instance to be operated. |
| HostName | No | String | Displayed name of CDH instance. You can specify any name you like, but its length should be limited to 60 characters.
| RenewFlag | No | String | Auto renewal flag. Value range: <li>NOTIFY_AND_AUTO_RENEW: notify expiry and renew automatically</li><li>NOTIFY_AND_MANUAL_RENEW: notify expiry but not renew automatically</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify expiry nor renew automatically</li>If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis when the account balance is sufficient. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidHost.NotSupported | This host instance is not supported for performing the specified operation. |
| InvalidHostId.Malformed | Invalid [CDH](https://cloud.tencent.com/document/product/416) `ID`. The specified [CDH](https://cloud.tencent.com/document/product/416) `ID`format is incorrect. For example, `ID` length error `host-1122`. |
| InvalidHostId.NotFound | The specified HostId does not exist, or does not belong to the request account. |

## 5. Example

## Example 1 Modify the Attributes of CDH Instances

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ModifyHostsAttribute
&HostIds.1=host-ey16rkyg
&HostName=web server
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```

