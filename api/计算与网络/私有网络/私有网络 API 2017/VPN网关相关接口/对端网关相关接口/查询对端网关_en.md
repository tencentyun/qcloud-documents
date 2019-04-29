## 1. API Description
This API (DescribeUserGw) is used to query customer gateway.
Domain for API request: <font style='color:red'>vpc.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DescribeUserGw.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| userGwId | No | String | Customer gateway ID or unified ID (unified ID is recommended). For example: cgw-1tb1k34n.  |
| userGwName | No | String | Customer gateway name. |
| offset | No | Int | Offset of initial line. Default is 0. |
| limit | No | Int | Number of rows per page. Default is 20. Supports up to 50. |
| orderField | No | String | Sort by a certain field. Currently you can sort by userGwName or createTime (default). |
| orderDirection | No | String | Ascending (asc) or descending (desc). Default is desc. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| totalCount | Int | The total number of customer gateways returned. |
| data.n | Array | Returned array. |
| data.userGwName | String | Customer gateway name. | 
| data.userGwId | Int | Customer gateway ID assigned by the system. For example: 400. | 
| data.unUserGwId | String | New customer gateway ID assigned by the system (it is recommended to use this ID). For example: cgw-1tb1k34n. | 
| data.userGwAddr | String | Public IP of the customer gateway. | 
| data.vpnConnNum | Int | Number of connected channels. | 
| data.createTime | String | Creation time: 2016-06-23 11:11:49. | 


## 4. Error Codes
 The following list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error code | Description |
|---------|---------|
| InvalidUserGw.NotFound | Customer gateway does not exist. Please  check the information you entered. You can query customer gateway by using the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%af%b9%e7%ab%af%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeUserGw">DescribeUserGw</a> API.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeUserGw
 &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "totalCount":"20",
    "data":[
        {
            "userGwName":"183.60.249.12",
            "userGwId":"404",
            "unUserGwId":"cgw-1tb1k34n",
            "userGwAddr":"183.60.249.12",
            "vpnConnNum":"1",
            "createTime":"2016-06-23 11:11:49"
        },
        {
            "userGwName":"183.60.249.138",
            "userGwId":"403",
            "unUserGwId":"cgw-mzmzjzf9",
            "userGwAddr":"183.60.249.138",
            "vpnConnNum":"1",
            "createTime":"2016-06-22 21:20:54"
        },
        {
            "userGwName":"SH",
            "userGwId":"402",
            "unUserGwId":"cgw-2530cjg1",
            "userGwAddr":"222.92.194.28",
            "vpnConnNum":"1",
            "createTime":"2016-04-28 14:15:41"
        },
        {
            "userGwName":"183.60.249.126",
            "userGwId":"401",
            "unUserGwId":"cgw-j8pcwzu9",
            "userGwAddr":"183.60.249.126",
            "vpnConnNum":"1",
            "createTime":"2016-04-22 12:18:05"
        },
        {
            "userGwName":"183.60.249.129",
            "userGwId":"400",
            "unUserGwId":"cgw-blr1nrwb",
            "userGwAddr":"183.60.249.129",
            "vpnConnNum":"1",
            "createTime":"2016-04-21 20:47:47"
        },
        {
            "userGwName":"183.60.249.121",
            "userGwId":"399",
            "unUserGwId":"cgw-ov9j6csd",
            "userGwAddr":"183.60.249.121",
            "vpnConnNum":"0",
            "createTime":"2016-04-21 20:47:14"
        },
        {
            "userGwName":"183.60.249.95",
            "userGwId":"397",
            "unUserGwId":"cgw-g013kis9",
            "userGwAddr":"183.60.249.95",
            "vpnConnNum":"0",
            "createTime":"2016-01-23 13:41:35"
        },
        {
            "userGwName":"183.60.249.33",
            "userGwId":"396",
            "unUserGwId":"cgw-c5p3f6fr",
            "userGwAddr":"183.60.249.33",
            "vpnConnNum":"0",
            "createTime":"2016-01-18 17:08:09"
        },
        {
            "userGwName":"115.159.143.150",
            "userGwId":"344",
            "unUserGwId":"cgw-oe7vq0uz",
            "userGwAddr":"115.159.143.150",
            "vpnConnNum":"0",
            "createTime":"2015-11-26 02:30:02"
        },
        {
            "userGwName":"9101",
            "userGwId":"315",
            "unUserGwId":"cgw-e098slul",
            "userGwAddr":"183.60.249.39",
            "vpnConnNum":"0",
            "createTime":"2015-11-06 11:18:53"
        }
    ],
    "codeDesc":"Success"
}
```


