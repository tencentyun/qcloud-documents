## 1. API Description
 
This API (DescribeClusterInstances) is used to query the cluster nodes and return the information of nodes in the cluster.

Domain for API request: ccs.api.qcloud.com



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type     | Description                                                                                                                                                 |
|----------------|----------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| clusterId      | Yes      | String   | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.           |
| offset         | No       | Int      | Offset. Default is 0                                                                                                                                        |
| limit          | No       | Int      | Maximum displayed entries. Default is 20                                                                                                                    |
| namespace      | No       | String   | Namespace. Please enter the *namespace* returned by the [DescribeClusterService](https://cloud.tencent.com/document/api/457/9440) API. Default is "default" |
| instancesId    | No       | []String | The instance name of ClusterID. default is emtpy                                                                                                            |


## 3. Output Parameters
 
| Parameter Name | Type         | Description                                            |
|----------------|--------------|--------------------------------------------------------|
| code           | Int          | Common error code. 0: Successful; other values: Failed |
| message        | String       | Module error message description depending on API      |
| totalCount     | Int          | Total number of cluster nodes                          |
| nodes          | Object Array | Node list. Details are shown below                     |

Detailed description of ``nodes`` field

| Field                | Type   | Description                                                                                                                                                                                                                                                                               |
|----------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| instanceId           | String | Node ID                                                                                                                                                                                                                                                                                   |
| instanceName         | String | Node name                                                                                                                                                                                                                                                                                 |
| kernelVersion        | String | Node kernel version                                                                                                                                                                                                                                                                       |
| podCidr              | String | IP address range of container on the node                                                                                                                                                                                                                                                 |
| cpu                  | Int    | Number of CPU millicores on the node                                                                                                                                                                                                                                                           |
| mem                  | Int    | Size of memory on the node (in Mi)                                                                                                                                                                                                                                                        |
| wanIp                | String | Public IP of node                                                                                                                                                                                                                                                                         |
| lanIp                | String | Private IP of node                                                                                                                                                                                                                                                                        |
| isNormal             | Int    | Status of node in the cluster. 0: Exceptional ; 1: Normal                                                                                                                                                                                                                                 |
| cvmState             | Int    | Node status. For more information, please see the list of instance statuses in [View Instance List](https://cloud.tencent.com/document/api/213/831) page                                                                                                                                  |
| cvmPayMode           | Int    | Node billing modes. <br>0: Postpaid on a Monthly Basis; <br>1: Prepaid; <br>2: Postpaid                                                                                                                                                                                                   |
| networkPayMode       | Int    | Network billing modes. <br>0: Postpaid on a Monthly Basis; <br>1: Prepaid; <br> 2: Bill-by-traffic; <br> 3: Bill-by-bandwidth. <br>The difference between the network billing modes can be found in API [Purchase Network Bandwidth](https://cloud.tencent.com/document/product/213/509). |
| createdAt            | String | Time when a node is added to the cluster                                                                                                                                                                                                                                                  |
| instanceCreateTime   | String | Creation time of node                                                                                                                                                                                                                                                                     |
| instanceDeadlineTime | String | Expiration time of node with Prepaid mode                                                                                                                                                                                                                                                 |
| abnormalReason       | String | The reason for node exception. There can be several reasons, please see the table below                                                                                                                                                                                                   |

Details of ``abnormalReason`` parameter

| Exception Type | Description |
|---------|---------|
| MemoryPressure | Insufficient memory |
| OutOfDisk | Insufficient disk space |
| NetworkUnavailable | Incorrect network configuration |
| Unknown | Unknown exception |

## 4. Example

Input

```
  https://domain/v2/index.php?Action=DescribeClusterInstances
  &clusterId=cls-hd1jv48o
  &instancesId.0=ins-nt4ka2zs
  &offset=0
  &limit=20
  &namespace=default
  &Other common parameters
```

Output

```
 {
    "code": 0,
    "message": "", 
	"data":{
	    "totalCount":1,
	    "nodes": [
	        {   
                "createdAt": "2016-11-23 19:12:24",
                "instanceId": "ins-nt4ka2zs",
                "instanceName": "cls-hd1jv48o_node",
                "wanIp": "",
                "lanIp": "10.133.0.44",
                "kernelVersion": "4.4.0-47-generic",
                "osImage": "Ubuntu 16.04.1 LTS",
                "podCidr": "100.70.0.0/24",
                "isNormal": 0,
                "abnormalReason": "Unknown",
                "cvmState": 2
                "cvmPayMode": 1,
                "networkPayMode": 2,
                "createdAt": "2017-04-11 18:02:18",
                "instanceCreateTime": "2017-04-11 18:00:32",
                "instanceDeadlineTime": "0000-00-00 00:00:00"
	        }   
	    ]
 	}
}

```
