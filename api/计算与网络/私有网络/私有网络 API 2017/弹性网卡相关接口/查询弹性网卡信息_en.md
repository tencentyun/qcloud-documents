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
| data.totalNum | Int | Total number of ENIs |
| data.data| Array | ENI information array |
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
| data.n.macAddress| String | ENI mac address, for example: 02: 81: 60: cb: 27: 37 | 
| data.n.privateIpAddressesSet | Array | IP information bound to ENI | 
| data.n.instanceSet | Object | CVM information bound to ENI | 
| data.n.groupSet | Array | Security group information bound to ENI | 

**privateIpAddressesSet information array:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| privateIpAddress | String | IP address |
| Primary | Bool | Indicate whether it is a primary IP. true: yes; false: no |
| wanIp | String | Public IP |
| description |String | ENI description |
| isWanIpBlocked | Bool | Indicate whether public ip has been blocked. true: yes; false: no |
| EipId | String | EIP ID |

**instanceSet information:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceId | String | Tencent CVM instance ID, for example: ins-xx44545f | 
| attachTime | String | binding time, for example: 2016-02-15 19:20:54 | 

**groupSet information array:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| sgId | String | Security group ID, for example: sg-dfg1df54 | 
| sgName | String | Security group name | 
| projectId | Int | Security group name |

## 4. Error Codes
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidNetworkInterface.NotFound | Invalid ENI, ENI resource does not exist. Please verify that the resource information you entered is correct. You can query the ENI via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%bc%b9%e6%80%a7%e7%bd%91%e5%8d%a1%e4%bf%a1%e6%81%af?viewType=preview" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> API |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeNetworkInterfaces
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-fyc4pilj
</pre>
Output
```
{
    "code": 0,
        "message": "",
        "codeDesc": "Success",
        "data": {
            "totalNum": 3,
            "data": [
            {
                "vpcId": "vpc-fyc4pilk",
                "vpcName": "test",
                "subnetId": "subnet-pq7ptksb",
                "zoneId": 100002,
                "eniName": "大",
                "eniDescription": "",
                "networkInterfaceId": "eni-d6m4m0iy",
                "primary": false,
                "macAddress": "20:90:6F:59:8D:79",
                "createTime": "2017-08-31 11:33:59",
                "flowLogsSet": [],
                "privateIpAddressesSet": [
                {
                    "privateIpAddress": "10.53.54.19",
                    "primary": true,
                    "wanIp": "119.29.158.39",
                    "description": "asdfasdfasdf",
                    "isWanIpBlocked": false,
                    "eipId": "eip-07vqn979"
                }
                ],
                    "instanceSet": {
                        "instanceId": "ins-7s7zjjcz",
                        "attachTime": "2017-12-12 11:55:07"
                    },
                    "groupSet": [
                    {
                        "sgId": "sg-lb62wxwb",
                        "sgName": "asdfsadf",
                        "projectId": 1079263
                    },
                    {
                        "sgId": "sg-ikmc8kcy",
                        "sgName": "全drop",
                        "projectId": 0
                    }
                    ]
            },
            {
                "vpcId": "vpc-fyc4pilk",
                "vpcName": "test",
                "subnetId": "subnet-pq7ptksb",
                "zoneId": 100002,
                "eniName": "手动",
                "eniDescription": "",
                "networkInterfaceId": "eni-ay1ac9c7",
                "primary": false,
                "macAddress": "20:90:6F:94:86:77",
                "createTime": "2017-07-28 20:09:34",
                "flowLogsSet": [],
                "privateIpAddressesSet": [
                {
                    "privateIpAddress": "10.53.54.230",
                    "primary": true,
                    "wanIp": "",
                    "description": "",
                    "isWanIpBlocked": false,
                    "eipId": ""
                },
                {
                    "privateIpAddress": "10.53.54.231",
                    "primary": false,
                    "wanIp": "",
                    "description": "",
                    "isWanIpBlocked": false,
                    "eipId": ""
                }
                ],
                    "instanceSet": {
                        "instanceId": "",
                        "attachTime": ""
                    },
                    "groupSet": [
                    {
                        "sgId": "sg-lb62wxw9",
                        "sgName": "asdfsadf",
                        "projectId": 1079263
                    },
                    {
                        "sgId": "sg-37tmkdiz",
                        "sgName": "Windows 放通3389端口-20170928143645736",
                        "projectId": 0
                    }
                    ]
            },
            {
                "vpcId": "vpc-fyc4pilk",
                "vpcName": "test",
                "subnetId": "subnet-pq7ptksb",
                "zoneId": 100002,
                "eniName": "新建弹性网卡手动",
                "eniDescription": "",
                "networkInterfaceId": "eni-a7hx9qae",
                "primary": false,
                "macAddress": "20:90:6F:31:88:B4",
                "createTime": "2017-07-28 17:39:39",
                "flowLogsSet": [],
                "privateIpAddressesSet": [
                {
                    "privateIpAddress": "10.53.54.200",
                    "primary": true,
                    "wanIp": "",
                    "description": "",
                    "isWanIpBlocked": false,
                    "eipId": ""
                }
                ],
                    "instanceSet": {
                        "instanceId": "",
                        "attachTime": ""
                    },
                    "groupSet": [
                    {
                        "sgId": "sg-lb62wxwe",
                        "sgName": "asdfsadf",
                        "projectId": 1079263
                    },
                    {
                        "sgId": "sg-5y2tai6e",
                        "sgName": "createPolicy_repair_test",
                        "projectId": 0
                    },
                    {
                        "sgId": "sg-q7bvssoa",
                        "sgName": "del usg test",
                        "projectId": 0
                    },
                    {
                        "sgId": "sg-0cgr10ie",
                        "sgName": "bilibili no icmp",
                        "projectId": 0
                    },
                    {
                        "sgId": "sg-ei2rr0qf",
                        "sgName": "广州",
                        "projectId": 0
                    },
                    {
                        "sgId": "sg-oodf2fc6",
                        "sgName": "offset",
                        "projectId": 0
                    }
                ]
            }
        }
}
```


