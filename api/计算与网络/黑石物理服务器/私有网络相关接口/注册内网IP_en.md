## 1. API Description
 
The API (RegisterBatchIp) is used to add a specified private IP to the CPM NAT gateway after the subnet to which the private IP belongs has been added to CPM NAT gateway. Otherwise, the IP will not be added to the gateway.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>



 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is RegisterBatchIp.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system. Support both vpcId before the upgrade and unVpcId after the upgrade.  |
| subnetId | Yes | String | VPC subnet ID assigned by the system. Support both subnetId before the upgrade and unSubnetId after the upgrade.  |
| ipList | Yes | Array | Requested IP array. The range for the number of arrays is 1-20.  |


 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| count | Int | Number of IPs registered successfully. |
| extramsg | String | Message returned by the API. |
| data.n | Array | The array of IPs registered successfully. |


## 4. Error Codes

 | Error Code | Error message | Description |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. The VPC resource does not exist. Please verify that you have entered resource information correctly.  |
| -3030 | InvalidBmSubnet.NotFound | Invalid subnet. The subnet resource does not exist. Please verify that you have entered resource information correctly.  |
| -3031 | AvailableIpUseUp | No IP available for assignment.  |
| -3001| InvalidInputParams | Invalid parameter

## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=RegisterBatchIp
	&<Common request parameters>
	&vpcId=vpc-2ari9m7h
	&subnetId=subnet-keqt3oty
	&ipList.0=10.1.1.2&ipList.1=10.1.1.300
```

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        "10.6.100.40"
    ],
    "extramsg":"10.1.1.300 is invalid ip."
    "count": 1
}

```


