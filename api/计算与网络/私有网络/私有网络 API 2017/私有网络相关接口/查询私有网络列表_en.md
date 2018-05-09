## 1. API Description
 
This API (DescribeVpcEx) is used to query VPC list.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

When no parameter is passed, the first 20 VPCs in the default sort order will be returned.

 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, pleases see <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeVpcEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | VPC ID assigned by the system. Support both vpcId before the upgrade and unVpcId after the upgrade.  |
| vpnName | No | String | VPC name. Fuzzy search is supported.  |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of lines per page. Default is 20.  |
| orderField | No | String | Sort by a certain field. Currently, sorting by createTime (default) and vpcName is supported.  |
| orderDirection | No | String | Ascending (asc) or descending (desc). Default is desc.  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Total number of VPCs under the developer account. |
| data.n | Array | VPC information array. |
| data.n.vpcId | String | vpcId assigned by the system, e.g. gz_vpc_266. |
| data.n.unVpcId | String | The new vpcID assigned by the system, which is upgraded from the subnet ID. It is recommended to use the new vpcId, for example: vpc-5gu2jxf4. |
| data.n.vpcName | String | VPC name. |
| data.n.cidrBlock | String | VPC network segment, for example: 192.168.0.1/24. |
| data.n.subnetNum | Int | Number of subnets under the VPC. |
| data.n.routeTableNum | Int | Number of routing tables under the VPC. |
| data.n.vpnGwNum | Int | Number of VPN gateways under the VPC. |
| data.n.vpcPeerNum | Int | Number of peering connections under the VPC. |
| data.n.vpcDeviceNum | Int | Number of CVMs under the VPC. |
| data.n.classicLinkNum | Int | Number of basic network devices that are linked to the VPC. |
| data.n.vpgNum | Int | Number of Direct Connect gateways under the VPC. |
| data.n.natNum | Int | Number of NAT gateways under the VPC. |
| data.n.createTime | String | Creation time of the VPC. |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
 | Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | The VPC does not exist. Please check the information you entered.  |

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpcEx
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
	&vpcId=vpc-2ari9m7h
	&offset=0
	&limit=1
	&orderDirection=desc
</pre>

Output
```

{
    "code": 0,
    "message": "",
		"totalCount":10,
		"data":[
        {
            "vpcId":"gz_vpc_245",
            "unVpcId":"vpc-8e0ypm3z",
            "vpcName":"alblack.bbb",
            "cidrBlock":"10.0.0.0/24",
            "subnetNum":0,
            "routeTableNum":5,
            "vpnGwNum":3,
            "vpcPeerNum":5,
            "vpcDeviceNum":0,
            "classicLinkNum":1,
            "vpgNum":0,
            "natNum":0,
            "createTime":"2015-08-24 15:05:16"
        }
   ]
}

```


