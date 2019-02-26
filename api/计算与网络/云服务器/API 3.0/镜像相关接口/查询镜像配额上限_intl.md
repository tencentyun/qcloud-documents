
## 1. API Description

This API (DescribeImageQuota) is used to query the image quota under the user account.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DescribeImageQuota |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| ImageNumQuota | Integer | The image quota under an account |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



## 5. Example

## Example 1: Query image quota

### Scenario description

The user needs to know how many images his/her account can hold.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeImageQuota
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "ImageNumQuota": 20,
    "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
  }
}
```


        
