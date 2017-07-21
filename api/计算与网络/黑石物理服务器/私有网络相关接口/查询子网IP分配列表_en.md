## 1. API Description
 
This API (DescribeBmSubnetIps) is used to query BM VPC subnet IP assignment list.  
Domain name for API request: vpc.api.qcloud.com


## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeBmSubnetIps.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | ID of VPC to which the subnet belongs. It can be vpcId or unVpcId. unVpcId is recommended. For example, vpc-kd7d06of. You can query this through API DescribeBmVpcEx.  |
| subnetId | Yes | String | ID of the subnet to be deleted. Both subnetId and unSubnetId are supported. unSubnetId is recommended. For example: subnet-k20jbhp0. You can query this through API DescribeBmSubnetEx.  |
 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| data.cpmSet | Array | CPM type IP information. |
| data.vmSet | Array | VM type IP information. |
| data.tgSet | Array | Hosting machine IP information. |

## 4. Error Codes
 
| Error Code | Error Message | Description |
|--------|---------|---------|
| -3047  | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct. You can query the VPC through API DescribeBmVpcEx.  |
| -3001  | InvalidInputParams | The format of the input parameter is incorrect.  |
| -3051  | BmVpc.SubnetNotExist | Invalid subnet. Subnet resource does not exist. Please verify whether the resource information entered is correct. You can query the subnet through API DescribeBmSubnetEx.  |


## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmSubnetIps
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
    "data": {
        "cpmSet": [
            "10.10.1.2"
        ],
        "vmSet": [
            "10.10.1.5"
        ],
        "tgSet": [
			"10.10.1.10"
		]
    }
}

```


