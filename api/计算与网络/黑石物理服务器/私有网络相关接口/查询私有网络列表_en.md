## 1. API Description
 
This API (DescribeBmVpcEx) is used to query the BM VPC list.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

When no parameter is passed for the API, the first 20 VPCs in the default sort order will be returned.

 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DescribeBmVpcEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | VPC ID assigned by the system. Support both vpcId before the upgrade and unVpcId after the upgrade.  |
| vpnName | No | String | VPC name. Fuzzy search is supported.  |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of lines per page. Default is 20.  |
| orderField | No | String | Sort by a certain field. Currently, sorting by createTime (default) and vpcName is supported.  |
| orderDirection | No | String | Ascending order (asc) or descending order (desc). Default is asc.  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Total number of VPCs of the developer. |
| data.n | Array | VPC information array. |
| data.n.vpcId | String | vpcId assigned by the system, for example: gz_vpc_266 |
| data.n.vpcName | String | VPC name. |
| data.n.cidrBlock | String | VPC network segment, for example: 192.168.0.1/24. |
| data.n.subnetNum | Int | Number of subnets under the VPC. |
| data.n.createTime | String | Creation time of the VPC. |

  ## 4. Error Codes
 
| Error Code | Error Message | Description |
|--------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. The VPC resource does not exist. Please verify that you have entered resource information correctly.  |

## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmVpcEx
	&<Common request parameters>
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
            "createTime":"2015-08-24 15:05:16"
        }
   ]
}

```


