## 1. API Description

This API (CreateVpn) is used to purchase VPN gateway.
Domain for API request: vpc.api.qcloud.com 


## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| name | Yes | string | IPsec VPN gateway name. Up to 60 characters.  |
| vpcId | Yes | string | VPC ID or unified ID (unified ID is recommened). It can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| period | Yes | Int | Number of month you want to purchase (up to 36)|
| bandwidth | Yes | Int | Bandwidth, supported values: 5, 10, 20, 50, 100 (in Mb).  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |
| dealIds | Array |  The generated order number. You can call <a href="https://cloud.tencent.com/doc/api/245/5108" title="DescribeVpnGw">DescribeVpnGw</a> API to query VPN details |

## 4. Error Code Table
 The API does not have a business error code. For common error codes, see <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes for details</a>.

## 5. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=CreateVpn
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
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


