## 1. API Description
This API (DescribeScalingConfiguration) is used to query scaling configuration information. Users can specify scaling group ID to query all the scaling configurations under this group.
Domain for API request: scaling.api.qcloud.com
Note: When calling the API, `Region` parameter is optional.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DescribeScalingConfiguration.

| Parameter Name | Required | Type | Description | 
|---------|---------|---------|---------|
| scalingConfigurationIds.n | No | String | An array of scaling configurations IDs to be queried. The array subscript is started with 0 and up to 20. |
| scalingConfigurationName | No | String | Scaling configuration names to be queried. Passing of scaling configuration name arrays is currently not supported.  |
| offset | No | Int | Offset; default is 0.  | 
| limit | No | Int | The maximum of scaling configurations that can be queried at a time. Default is 20.  | 
| projectId | No | String | Project ID. If it is left empty, the scaling configurations of all projects will be queried. 0 means default project. To specify other projects, you can call API <a href="/doc/api/403/4400" title="Query Project List">Query Project List</a> (DescribeProject) to query. |



## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes ">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | Output results. Scaling group list information returned for the query.  |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalCount | Int | Number of scaling configurations returned for the query.  |
| scalingConfigurationSet | Array | Set of scaling configuration information returned for the query.  |

scalingConfigurationSet contains an amount of scaling configuration information, and the information about each scaling group is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| scalingConfigurationId | String | Scaling configuration ID returned for the query. |
| scalingConfigurationName | String | Scaling configuration name returned for the query. |
| scalingGroupIdSet | Array | All scaling groups information that use this scaling configuration.  |
| cpu | Int | Number of Server CPU cores  | 
| mem | Int | Server memory capacity (in GB).  | 
| imageType | Int | Image type. A value of 1 indicates that it is a private image; A value of 2 indicates that it is a public image. | 
| imageId | String | Image ID.  | 
| storageType | Int | Data disk type. A value of 1 indicates that it is a local disk; A value of 2 indicates that it is a cloud disk. | 
| storageSize | Int | Size of data disk (in GB). | 
| rootSize | Int | Size of system disk (in GB). |
| bandwidthType | String | Bandwidth type. PayByHour: Charge by bandwidth usage time; PayByTraffic: Charge by traffic. 
| bandwidth | Int | Public network bandwidth (in Mbps). | 
| wanIp | Int |Public IP. 1 means enable; 0 means not enable. | 
| keyId | String | ID of key.  | 
| password | String | Password. | 
| sgSet | Array | Security group information. | 
| needMonitorAgent | Int |Activate cloud monitor service or not. 1 means activate; 0 means not activate. | 
| needSecurityAgent | Int |Activate cloud security service or not. 1 means activate; 0 means not activate. | 
| createTime | String | Creation time of the scaling configuration. | 
| projectId | Int | Project ID. | 

scalingGroupIdSet contains all scaling groups information that use this scaling configuration. It consists of a series of scaling group information, and each group information is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| scalingGroupIdSet.n.scalingGroupName| String | Scaling group ID. |
| scalingGroupIdSet.n.scalingGroupName| String | Scaling group name. |

## 4. Error Codes
For common errors on this API, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
```
Example of returned result is as follows. The `totalCount` is 1, indicating that this user has only one scaling configuration. The `scalingGroupIdSet` parameter in this scaling configuration contains only one set of information, indicating that only one scaling group uses this scaling configuration.
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",    
    "data":{
        "totalCount":1,
        "scalingConfigurationSet": [
            {
                "scalingConfigurationId": "xxx",
                "scalingConfigurationName": "xxxx",
                "scalingGroupIdSet": [
                    {
                        "scalingGroupId": "xxxxxx",
                        "scalingGroupName": "xxx"
                    }
                ],
                "sgSet": [],
                "needMonitorAgent": 1,
                "bandwidthType": 1,
								"projectId":0,
                "cpu": 1,
                "needSecurityAgent": 1,
                "rootSize": 20,
                "wanIp": 1,
                "imageType": 1,
                "keyId": "skey-xxx",
                "bandwidth": 1,
                "storageType": 1,
                "createTime": "2016-03-16 16:52:06",
                "imageId": "img-xxx",
                "mem": 1,
                "storageSize": 10,
                "password": ""
            },
        ]
    }
}
```


