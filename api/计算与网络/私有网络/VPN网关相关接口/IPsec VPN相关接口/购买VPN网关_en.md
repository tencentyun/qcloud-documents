## 1. API Description

This API (CreateVpn) is used to purchase VPN gateway.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>


## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is CreateVpn.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| name | Yes | string | IPsec VPN gateway name. You can use any content as long as it does not exceed 60 characters. The IPsec VPN gateway name must be unique under the same VPC.  |
| vpcId | Yes | string | VPC ID or unified ID (unified ID is recommened). Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| period | Yes | Int | Length of purchase to be queried (in months). The maximum is 36 months.  |
| bandwidth | Yes | Int | Bandwidth, supported values: 5, 10, 20, 50, 100 (in Mb).  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |
| dealIds | Array |  The generated order number. You can call the API of <a href="https://www.qcloud.com/doc/api/245/5108" title="Query VPN Gateway List">Query VPN Gateway List</a> via the order number to query VPN details |

## 4. Error Code Table
 The API does not have a business error code. For common error codes, see <a href="https://www.qcloud.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes for details</a>.

## 5. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=CreateVpn
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=gz_vpc_1111
	&period=1
	&name=test
	&bandwidth=5
</pre>

Output
```
{
    "code" : 0,
    "message" : "ok",
    "data":
    ｛
       "dealIds":[
          121
       ]
     ｝
}
```


