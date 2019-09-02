## 1. API Description
 
This API (DescribeVpcClassicLink) is used to query the Classiclink between VPC and CVM.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>


 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeVpcClassicLink.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | The Virtual Private Cloud ID assigned by the system. Both the vpcId before upgrading and the upgraded unVpcId are supported. For example: vpc-dgd5454.  |
| classicLinkId | No | String | Classiclink ID between VPC and CVM, for example: vcx-opgnzgo9.  |
| lanIp | No | String | CVM private IP.  |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of lines per page. Default is 20 (maximum is 50).  |
| orderField | No | String | Sort by a certain field. No sorting by default. Available field: createTime.  |
| orderDirection | No | String | Ascending order (asc) or descending order (desc). Default is desc.  |
 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a>. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Returned total number of links. |
| data.n | Array | Returned details. |
| data.n.lanIp | String | Private IP address of Tencent CVM. |
| data.n.unVpcId | String | Unified ID for VPC assigned by the system, which is upgraded from vpcId. The system supports both IDs for compatibility purpose, but the unified ID is recommended. For example: vpc-2ari9m7h. |
| data.n.vpcId | String | Virtual private cloud ID assigned by the system, for example: gz_vpc_15. |
| data.n.classicLinkId | String | Link ID assigned by the system. For example: vcx-opgnzgo9. |
| data.n.createTime | String | Creation time, for example: 2016-01-21 14:59:37. |
| data.n.instanceId | String | Unified ID of CVM, for example: ins-xxd51df. |
| data.n.instanceName | String | CVM name. |

## 4. Error Codes
 The following error code list only provides error codes for this API. For common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidLanIp.NotFound | The CVM does not exist. Please verify that the lanIP you entered is correct. To query the CVMs under the VPC, please see <a href="https://cloud.tencent.com/doc/api/229/831" title="Query CVM Instance List">Query CVM Instance List</a>.  |
| InvalidVpc.NotFound | The VPC does not exist. Please check the information you entered.  |

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpcClassicLink
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
	&vpcId=vpc-2ari9m7h
	&classicLinkId=vcx-df454d
</pre>

Output
```

{
    "code": 0,
    "message": "",
		"totalCount":"1",
		"data":[
        {
            "lanIp":"10.232.18.145",
            "uniqVpcId":"vpc-8e0ypm3z",
            "vpcId":"gz_vpc_245",
            "classicLinkId":"vcx-opgnzgo9",
            "createTime":"2016-01-21 14:59:37",
            "instanceId":"ins-d1o128ru",
            "instanceName":"Unnamed"
        }
    ]
}

```


