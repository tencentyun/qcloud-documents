## 1. API Description
 
This API (CreateBmInterface) is used to add an CPM to the subnet whose VLANID is not 5.  
Domain name for API request: vpc.api.qcloud.com

1) You cannot add a CPM to a subnet whose VLANID is 5.  
2) Each CPM can be added to at most 30 subnets.  
3) A maximum of 10 CPMs are allowed to be passed each time the API is called.

 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is CreateBmInterface.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | ID of VPC to which the subnet belongs. It can be vpcId or unVpcId. unVpcId is recommended. For example, vpc-kd7d06of. You can query this through API DescribeBmVpcEx.  |
| subnetId | Yes | String | ID of the subnet to be deleted. Both subnetId and unSubnetId are supported. unSubnetId is recommended. For example: subnet-k20jbhp0. You can query this through API DescribeBmSubnetEx.  |
| instanceIds | Yes | Array | Unique ID of CPM. For example: cpm-k20jbhp0. You can query this through API DescribeDeviceClass. A maximum of 10 CPMs are allowed to be added to the subnet at a time |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned operation task ID. |


## 4. Error Codes
 
| Error Code | Error Message | Description |
|--------|---------|---------|
| -3047  | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct.  |
| 17001  | BmVpc.InvalidSubnet | Invalid subnet. Subnet resource does not exist. Please verify whether the resource information entered is correct.  |
| 17003  | BmVpc.InvalidVlanId | Invalid subnet VLAN ID.  |
| 17002  | BmVpc.InterfaceLimitExceeded | The number of CPMs added to the subnet has reached the limit.  |
| 11041  | BmVpc.InvalidInstanceId | Invalid CPM. The CPM does not exist.  |

## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=CreateBmInterface
	&<Common Request Parameters>
	&vpcId=vpc-34cxlz7z
    &subnetId=subnet-pohv7d8w
    &instanceIds.0=tcpm-rewhxuo7
```

Output
```

{
	"code": 0,
	"message": "",
	"data": {
		"taskId": 9641,
		"resourceIds": ["tcpm-rewhxuo7"]
	}
}

```


