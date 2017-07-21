## 1. API Description
 
This API (DescribeBmVpcEx) is used to query BM VPC list.  
Domain name for API request: vpc.api.qcloud.com

When no parameter is passed for calling the API, the information of the first 20 VPCs in the default sort order will be returned.

 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeBmVpcEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | VPC ID assigned by the system. You can pass the value of vpcId field or unVpcId field returned by the list.  |
| vpnName | No | String | VPC name. Fuzzy search is supported.  |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of lines per page. Default is 20.  |
| orderField | No | String | Sort by a certain field. Currently, sorting by createTime (default) and vpcName is supported.  |
| orderDirection | No | String | Ascending (asc) or descending (desc). Default is asc.  |
| zoneIds | No | Array | Availability zone array, which can be searched according to availability zones. For more information, please see API <a href="https://www.qcloud.com/document/api/386/6634" title="DescribeRegions">DescribeRegions</a>. For example: 1000800001 |
| vpcStatus | No | Int | Current status of VPC. 0: Running; 1: Creation failed; 2: Creating; 3: Deleting.  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Total number of VPCs of the developer. |
| data.n | Array | VPC information array. |
| data.n.vpcId | String | vpcId assigned by the system, e.g. gz_vpc_266 |
| data.n.unVpcId | String | Unique VPC ID assigned by the system, e.g. vpc-8e0ypm3z |
| data.n.vpcName | String | VPC name. |
| data.n.cidrBlock | String | VPC IP address range, for example: 192.168.0.1/24. |
| data.n.subnetNum | Int | Number of subnets under the VPC. |
| data.n.productionStatus | Int | Current status of VPC. |
| data.n.zoneId | Int | Availability zone to which VPC belongs. |
| data.n.createTime | String | Creation time of the VPC. |

## 4. Error Codes
 
| Error Code | Error Message | Description |
|--------|---------|---------|
| -3047  | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct.  |

## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmVpcEx
	&<Common Request Parameters>
	&vpcId=vpc-2ari9m7h
	&offset=0
	&limit=1
	&orderDirection=desc
```

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
            "zoneId":0,
            "productionStatus":0,
            "createTime":"2015-08-24 15:05:16"
        }
   ]
}

```


