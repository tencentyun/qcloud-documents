## 1. API Description

This API (DescribeNetworkInterfaces) is used to query the information of ENI.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeNetworkInterfaces.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | Virtual private cloud ID of ENI, for example: vpc-7t9nf3pu |
| networkInterfaceId | No | String | ENI ID assigned by the system, for example: eni-m6dyj72l |
| eniName | No | String | ENI name, support fuzzy search |
| eniDescription | No | String | ENI description, support fuzzy search |
| instanceId | No | String | CVM instance ID, for example: ins-xx44545f |
| offset | No | Int | Offset of initial line. Default is 0 |
| limit | No | Int | Number of lines per page. Default is 20. Maximum is 50.  |
| orderField | No | String | Sort by a certain field, <br>which can be: eniName, createTime. Default is createTime |
| orderDirection | No | String | Ascending (asc) or descending (desc). Default is desc |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed
| message | String | Error message |
| totalCount | Int | Total number of ENIs |
| data.n | Array | ENI information array |
**data array:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.n.vpcId | String | Virtual private cloud ID of ENI, for example: vpc-8e0ypm3z | 
| data.n.subnetId | String | Subnet ID of ENI,  for example: subnet-0ap8nwca | 
| data.n.zoneId | int | Availability zone ID of the subnet of ENI, for example: 200001 | 
| data.n.eniName | String | ENI name, support fuzzy search | 
| data.n.eniDescription| String | ENI description | 
| data.n.networkInterfaceId | String | ENI ID, for example: eni-m6dyj72l | 
| data.n.primary | Bool | Indicate whether it is a primary ENI. true: primary ENI; false: secondary ENI | 
| data.n.macAddress| String | ENI mac address | for example: 02: 81: 60: cb: 27: 37 | 
| data.n.privateIpAddressesSet | Array | IP information bound to ENI | 
| data.n.instanceSet | Array | CVM information bound to ENI | 
| data.n.groupSet | Array | Security group information bound to ENI | 

**privateIpAddressesSet information array:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| privateIpAddress | String | IP address |
| Primary | Bool | Indicate whether it is a primary IP. true: yes; false: no |
| wanIp | String | Public IP |
| EipId | String | EIP ID |

**instanceSet information array:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceId | String | Tencent CVM instance ID, for example: ins-xx44545f | 
| attachTime | String | binding time, for example: 2016-02-15 19:20:54 | 

**groupSet information array:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| sgId | String | Security group ID, for example: sg-dfg1df54 | 
| sgName | String | Security group name | 

## 4. Error Codes
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidNetworkInterface.NotFound | Invalid ENI, ENI resource does not exist. Please verify that the resource information you entered is correct. You can query the ENI via the <a href="https://www.qcloud.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%bc%b9%e6%80%a7%e7%bd%91%e5%8d%a1%e4%bf%a1%e6%81%af?viewType=preview" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> API |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeNetworkInterfaces
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-7t9nf3pu
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "totalCount":1,
    "data":[
        {
            "vpcId":"vpc-7t9nf3pu",
            "subnetId":"subnet-0ap8nwca",
	    "zoneId":200001,
            "eniName":"eni",
            "eniDescription":"eni example",
            "networkInterfaceId":"eni-m6dyj72l",
            "primary":false,
            "macAddress":"02:81:60:cb:27:37",
            "privateIpAddressesSet":[
                 {
                     "privateIpAddress":"10.0.0.2",
                     "primary":true,
                     "wanIp":"183.23.0.2",
                     "eipId":"eip-dgd545ef"
                  }
	           ],
             "instanceSet":[
                  {
                       "instanceId":"ins-xx44545f",
                       "attachTime":"2016-02-15 19:20:54"
                  }
            ],
            "groupSet":[
                 {
                      "sgId":"sg-dfg1df54",
                      "sgName":"Security group 1"
                  }
            ]
        }
    ]
}
```


