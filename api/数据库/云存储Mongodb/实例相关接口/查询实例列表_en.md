## 1. API Description
 
This API (DescribeMongoDBInstances) is used to query the list of replica set instances.
Domain for API request: <font style='color:red'>mongodb.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is DescribeMongoDBInstances.

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| limit | Yes | Int | Length of a page. Maximum is 100 |
| offset | Yes | Int | Current page number. Default is 0.  For query APIs, a maximum number of returned records is generally set for a single query by default. To traverse all the resources, you need to use "limit" and "offset" for a paged query; For example, to query the 40 records between 110 and 149, you can set offset = 110 and limit = 40.  |
| instanceIds | No | Array | One or more instance IDs (n represents array subscript starting with 0). |
| projectIds | No | Array | One or more project IDs (n represents array subscript starting with 0).  |
| vips | No | Array | One or more virtual IPs (n represents array subscript starting with 0).  |
| status | No | Array | One or more statuses (n represents array subscript starting with 0). Current status of instance. 0: To be initialized; 1: In process; 2: Running; -2: Isolated |
| instanceNames | No | Array | One or more instance names (n represents array subscript starting with 0).  |
| vpcId | No | Int | This parameter is retained for historical reasons. It is recommended to use the following parameter unVpcId (VPC ID) .
| subnetId | No | Int | This parameter is retained for historical reasons. It is recommended to use the following parameter unSubnetId (Subnet ID under VPC).  |
| unVpcId | No | String | VPC ID. If it is left empty, the default is basic network. This value is subject to the unVpcId returned by API [Query VPC List](https://cloud.tencent.com/doc/api/245/1372), such as: vpc-kd7d06of |
| unSubnetId | No | String | Subnet ID. Under VPC, the value is subject to the unSubnetId returned by the API [Query Subnet List](https://cloud.tencent.com/document/product/215/1371), such as subnet-3lzrkspo |

## 3. Output Parameters

| Parameter Name | Type | Description |
|:---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| totalCount | Int | Total number of instances |
| data | Object | Details of instance list |


Parameter data indicates the details of instance list, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| data.mongodbSet | Array | An array of instance details |

Parameter mongodbSet indicates an array of instance details, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| zoneId| Int| Availability zone ID |
| instanceId | String | Instance ID |
| instanceName | String | Instance name |
| projectId | Int | ID of project to which the instance belongs |
| vpcId | Int | VPC ID (not recommended) |
| unVpcId | String | VPC ID (recommended) |
| subnetId | Int | Subnet ID under VPC (not recommended) |
| unSubnetId | String | Subnet ID under VPC (recommended) |
| status | Int | Current status of instance. 0: To be initialized; 1: In process; 2: Running; -2: Isolated |
| statusDesc | String | Description of instance status |
| vip | Int | Virtual IP of instance |
| vport | Int | Port number of instance |
| createtime | String | Creation time of instance |
| deadline | String | Expiration time of instance |
| typeId | String | Name of instance type |  For example, GIO: High IO; TGIO: High IO (10 GB) |
| version | String | Database version number, for example: MONGO_3_MMAP, MONGO_3_WT |
| memSize| Int | Memory size of instance (in MB) |
| diskSize | Int | Disk capacity of instance (in GB) |
| diskusedCapacity | Int | Actually used capacity of disk of instance (in MB) |
| nodenum | Int | Number of nodes of replica set |
| autoRenewFlag | Int | Auto renewal flag set for the instance: 0 - Do not set auto renewal; a notification will be given upon expiration of instance; 1 - Set auto renewal; instance will be automatically renewed upon expiration; 2 - Neither renewal nor notification will be made upon the expiration of instance |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11050 | InvalidParameter | Incorrect business parameter |

## 5. Example
<pre>
https://mongodb.api.qcloud.com/v2/index.php?Action=DescribeMongoDBInstances
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&limit=10
&offset=0
</pre>
The returned results are as below:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 10,
    "data": {
        "mongodbSet": [
            {
                "zoneId": 300001,
                "instanceId": "cmgo-mmifbo25",
                "instanceName": "cmgo-mmifbo25",
                "projectId": 0,
                "vpcId": 0,
 				"unVpcId": null,
                "subnetId": 0,
				"unSubnetId": null,
                "status": 2,
                "statusDesc": "Running",
                "vip": "10.66.187.159",
                "vport": 27017,
                "createtime": "2016-11-09 10:54:47",
                "deadline": "2016-12-09 10:54:47",
                "typeId": "GIO",
                "version": "MONGO_3_MMAP",
                "memSize": 2048,
                "diskSize": 30,
                "diskusedCapacity": 3398,
                "nodenum": 2,
                "autoRenewFlag": 0
            },
            {
                "zoneId": 800001,
                "instanceId": "cmgo-2njfb6z1",
                "instanceName": "cmgo-2njfb6z1",
                "projectId": 0,
                "vpcId": 4864,
 				"unVpcId": "vpc-j5yvvkul",
                "subnetId": 14158,
				"unSubnetId": "subnet-py2q60ty",
                "status": 2,
                "statusDesc": "Running",
                "vip": "10.66.194.3",
                "vport": 27017,
                "createtime": "2016-12-23 19:19:27",
                "deadline": "2017-02-23 19:19:27",
                "typeId": "CY",
                "version": "MONGO_3_MMAP",
                "memSize": 4096,
                "diskSize": 60,
                "diskusedCapacity": 8476,
                "nodenum": 2,
                "autoRenewFlag": 0
            },
            {
                "zoneId": 100002,
                "instanceId": "cmgo-6ozqe0uh",
                "instanceName": "test_API",
                "projectId": 10,
                "vpcId": 4864,
 				"unVpcId": "vpc-j5yvvkul",
                "subnetId": 14158,
				"unSubnetId": "subnet-py2q60ty",
                "status": 2,
                "statusDesc": "Running",
                "vip": "10.66.168.6",
                "vport": 27017,
                "createtime": "2017-02-06 14:07:46",
                "deadline": "2017-04-06 14:07:46",
                "typeId": "GIO",
                "version": "MONGO_3_MMAP",
                "memSize": 8192,
                "diskSize": 60,
                "diskusedCapacity": 6206,
                "nodenum": 3,
                "autoRenewFlag": 1
            }
        ]
    }
}

```
