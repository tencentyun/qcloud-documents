## 1. API Description
 
This API (DescribeClusterService) is used to query the list of services. The list returned only contains general information about the services, call the API "DescribeClusterServiceInfo" if you need detailed service information.

Domain for API request: ccs.api.qcloud.com



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [DescribeCluster](https://cloud.tencent.com/document/api/457/9448) API.  |
| namespace      | No | String      | Namespace. Default is "default" |
| allnamespace      | No | Int      | Indicates whether to show services under all namespaces. 1: Yes. 0 (or leave blank): No |

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed |
| message | String | Module error message description depending on API |
| services | Object Array | Service list. Details are shown below |

"service" parameter details

| Field | Type | Description |
|---------|---------|---------|
| serviceName | String | Service name |
| status | String | Service status. See the table below |
| reasonMap | map[string]int | A set containing the reasons for why the service is in the current status. The map key is reason, while the map value is the number of containers with the same reason. Suppose a pair of key and value: {"Failed to download image":2}, this means two containers failed to download image |
| createdAt | String | Creation time of service |
| currentReplicas | Int | Number of running pod replicas |
| desiredReplicas | Int | Number of pod replicas that are expected to run. This is specified when creating the service |
| lbId | String | Corresponding public Lb ID of the service. This is only created if the service is specified to access the Internet upon creation |
| lbStatus | String | Public network load balancer status. Possible values are: None (the service has no public network load balancer), Creating (load balancer is being created) and Running (load balancer is running) |
| externalIp | String | Corresponding public IP of the service |
| namespace  | String      | Namespace |


| Status Type | Description |
|---------|---------|
| Normal | Running |
| Abnormal | Service exception, such as container failed to launch |
| Waiting | Service waiting, such as container is currently downloading image |
| Paused | Update paused. This status occurs if the user pauses update operation in the middle of service update |
| Updating | Service updating |
| RollingBack | Service rolling back |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=DescribeClusterService
  &clusterName=test-cluster
  &Other common parameters
```
Output

```
{
    "returnCode": 0,
    "returnMsg": "ok",
    "data": {
        "services": [
            {
                "serviceName": "xxx",
                "status": "Waiting",
                "reasonMap": { 
                   "Failed to download image" : 1
                 },
                "externalIp" : "",
                "lbId" : "",
	            "lbStatus" : "None",
                "desiredReplicas": 1,
                "currentReplicas": 0,
                "createdAt": "2016-12-08 12:44:21"
				"namespace": "default"
            }
        ]
    }
}

```
