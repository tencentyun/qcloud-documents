## 1. API Description

This API (CreateNetworkInterface) is used to create ENIs.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

1) When creating an ENI, you can specify a private IP and a primary IP. The specified private IP must be in the subnet of the ENI, and cannot be occupied.
2) When creating an ENI, you can specify the number of private IP addresses that need to be requested. The system will randomly generate the private IP address(es).
3) You can bind an existing security group when creating an ENI.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/245/4772" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is CreateNetworkInterface.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID of ENI (new ID is recommended), for example: vpc-7t9nf3pu.   |
| subnetId | Yes | String | Subnet of ENI (new ID is recommended), for example: subnet-0ap8nwca.  |
| eniName| Yes| String | ENI name; should be within 60 characters.  |
| eniDescription| No | String | ENI description; should be within 60 characters.   |
| privateIpAddressSet.n | No | Array | Specified private IP address array.   |
| privateIpAddressSet.n.primary | Yes | Bool | Indicate whether it is a primary IP; can only set one primary IP.   |
| privateIpAddressSet.n.privateIpAddress | Yes | String | Specified private IP address.   |
| secondaryPrivateIpAddressCount | No | Int | The number of private IP addresses for new requests. |
| sgIds.n | No | Array | Specified Bound security group, for example: ['sg-1dd51d'].  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0:  succeeded, other values:  failed |
| message | String | Error message |
| taskId | Int | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |

## 4. Error Code Table
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | VPC does not exist. Please check the information you entered. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidSubnet.NotFound |  Subnet does not exist. Please check the information you entered. You can query the subnet via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a> API |
| InvalidNetworkInterfaceName | Invalid ENI name. The ENI name should be within 60 characters.  |
| NetworkInterfaceLimitExceeded | Number of ENIs exceeds the upper limit. Please contact customer service for more resources. For more information on VPC resources restrictions, refer to <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Service Limits">VPC Service Limits</a> |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateNetworkInterface
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-7t9nf3pu
&subnetId=subnet-0ap8nwca
&eniName=eni
&secondaryPrivateIpAddressCount=1
&sgIds.0=sg-1dd51d
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data":
        {
            "taskId": 16284
        }
}
```


