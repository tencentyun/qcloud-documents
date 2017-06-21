## 1. API Description
 
This API (DescribeBmSubnetByCpmId) is used to query the list of subnets to which CPMs are added.  
Domain name for API request: vpc.api.qcloud.com


## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeBmSubnetByCpmId.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | Unique ID of CPM resource, for example: cpm-kd7d06of. You can query this through API DescribeDevice.  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| subnetSet.n | Array | Subnet information. |
| subnetSet.n.unVpcId | String | Unique ID of VPC to which the subnet belongs. |
| subnetSet.n.vpcId | String | Integer ID of VPC to which the subnet belongs. |
| subnetSet.n.cidr | String | Subnet CIDR. |

## 4. Error Codes
 
| Error Code | Error Message | Description |
|--------|---------|---------|
| -3244  | BmVpc.InvalidInstanceId | Invalid CPM resource ID. You can query the CPM resource ID through API DescribeDevice.  |


## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmSubnetByCpmId
	&<Common Request Parameters>
	&vpcId=vpc-kd7d06of
    &subnetId=subnet-1so5ae8m
```

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "subnetSet": [
        {
            "unVpcId": "vpc-muinpf9p",
            "vpcId": 4100,
            "subnet": "10.1.0.0",
            "cidr": "10.1.0.0/24"
        }
    ]
}

```


