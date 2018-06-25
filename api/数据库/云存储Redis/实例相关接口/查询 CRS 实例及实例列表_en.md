## 1. API Description
 
This API (DescribeRedis) is used to query the list of CRS instances.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DescribeRedis.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| limit | Yes | Int | Length of a page |
| offset | Yes | Int | Current page number. |
| redisId | String | Instance ID |
| redisName | No | String | Instance name |
| orderBy | No | String | Enumeration range: redisId, projectId, createtime |
| orderType | No | Int | 1: Backward sequence; 0: Forward sequence. The default is backward sequence |
| vpcIds.n  | No | Int | This parameter is retained for historical reasons. It is recommended to use the following parameter unVpcIds.  Array of VPC IDs, with the array subscript starting with 0. If it is left empty, the default is basic network |
| unVpcIds.n  | No | String | An array of VPC IDs, with the array subscript starting with 0. If it is left empty, the default is basic network. This value is subject to the unVpcId returned by API [Query VPC List](https://cloud.tencent.com/doc/api/245/1372), such as: vpc-kd7d06of |
| subnetIds.n | No | Int | This parameter is retained for historical reasons. It is recommended to use the following parameter unSubnetIds An array of subnet IDs under VPC, with the array subscript starting with 0 |
| unSubnetIds.n | No | String | An array of subnet IDs, with the array subscript starting with 0.  Under the VPC subnet, this value is subject to the unSubnetId returned by API [Query Subnet List](https://cloud.tencent.com/document/product/215/1371), such as subnet-3lzrkspo |
| projectIds.n | No | String | An array of project IDs, with the array subscript starting with 0.

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| totalCount | Int | Number of instances |
| data | Array |  |
| data.redisSet | Array | | 
| data.redisSet.redisName | String | Instance name | 
| data.redisSet.redisId | String | Unique ID of instance | 
| data.redisSet.appid | Int | appid | 
| data.redisSet.projectId | Int | Project ID | 
| data.redisSet.regionId | Int | Region ID | 
| data.redisSet.zoneId | Int | Zone ID | 
| data.redisSet.vpcId | Int | VPC ID (not recommended) |
| data.redisSet.unVpcId | String | VPC ID (recommended) |  
| data.redisSet.subnetId | Int | ID of a subnet under VPC (not recommended) |
| data.redisSet.unSubnetId | String | ID of a subnet under VPC (recommended) | 
| data.redisSet.status | Int | Current status of instance. 0: To be initialized; 1: In process; 2: Running; -2: Isolated | 
| data.redisSet.statusDesc | String | Description of instance status | 
| data.redisSet.wanIp | String | Instance VIP | 
| data.redisSet.port | Int | Instance port number | 
| data.redisSet.createtime | String | Creation time of instance | 
| data.redisSet.size | Int | Instance capacity (in MB) | 
| data.redisSet.sizeUsed | Int | Used capacity of instance (in MB) | 
| data.redisSet.typeId | Int | Instance type. 1: Cluster; 2: Standalone | 
| data.redisSet.typeIddesc | String | Description of instance type |
| data.redisSet.autoRenewFlag | Int | Whether the auto renewal indicator is set for the instance. 1: Yes; 0: No |  
| data.redisSet.deadlineTime | String | Expiration time of instance |


## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |

## 5. Example
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=DescribeRedis
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&limit=10
&offset=0
</pre>
The returned results are as below:
```
{
    "code": 0,
	"message": "",
	"codeDesc": "Success",
    "totalCount": 1,
    "data": {
        "redisSet": [
            {
                "redisName":"att_test",
                "redisId":"crs-ooakfyj3",
                "appid":"1251966477",
                "projectId":"0",
                "regionId":"1",
                "zoneId":"100002",
                "vpcId": 4864,
 				"unVpcId": "vpc-j5yvvkul",
                "subnetId": 14158,
				"unSubnetId": "subnet-py2q60ty",
                "status":"2",
                "statusDesc":"Running",
                "wanIp":"10.66.170.224",
                "port":"6379",
                "createtime":"2016-05-04 16:59:53",
                "size":"2048",
                "sizeUsed":"0",
                "typeId":"1",
                "typeIddesc":"Cluster",
				"autoRenewFlag": 1,
                "deadlineTime":"2016-08-14 16:59:53"
            }
        ]
    }
}
```
