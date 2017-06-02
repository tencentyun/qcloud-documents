## 1. API Description
 
This API (DescribeServiceInstance) is used to query the list of service instances.

Domain for API request: ccs.api.qcloud.com



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://www.qcloud.com/document/api/457/9463).

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the clusterId in the returned fields of the API "Query Clusters".  |
| serviceName   | Yes    | String | Service name |
| offset | No | Int | Offset. Default is 0 |
| limit | No | Int| Maximum displayed entries. Default is 20 |
| namespace   | No | String      | Namespace. Default is "default" |

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: successful. Other values: failed. |
| message | String | Module error message description depending on API. |
| totalCount | Int | Total number of instances |
| instances | Object Array | Instance list. Details are shown below |

"instances" parameter details


| Parameter Name | Type | Description |
|---------|---------|---------|
| name | String | Instance name (corresponding to the pod name of kubernetes) |
| status | String| Instance status. See the definitions for instance and container statuses below |
| reason | String | Reason why the instance is in the current status. For example, container failed to download image |
| nodeIp | String | Server IP |
| nodeName | String| Server name |
| ip | String| Instance IP |
| restartCount | Int | Number of restarts performed for the container in the instance |
| readyCount | Int | Number of ready containers in the instance |
| createdAt | String | Launch time of the instance |
| containers | Object Array | Container array. See the container definition below |


container definition (The container fields here are mainly used to describe the current status and status cause for the container. For detailed definitions of containers in instances, see API "Acquire Service", which returns detailed container parameters)

| Parameter Name | Type | Description |
|---------|---------|---------|
| containerId  | String | Container ID (docker id) |
| status | String | Container status. See the definitions for instance and container statuses below |
| reason | String | Reason why the container is in the current status. For example, failed to download image |
| image | String | Container image |


Definition of instance and container statuses

| Status Type | Description |
|---------|---------|
| Running | Running |
| Waiting | Waiting to run, such as downloading image |
| Terminating | Certain container in the instance is being terminated |
| Terminated | Certain container in the instance has terminated |
| NotReady | Certain container in the instance is not ready, such as the container failed to pass health check |


## 4. Example
Input

```
  https://domain/v2/index.php?Action=DescribeClusterContainer
  &clusterId=cls-xxxxx
  &serviceName=simon
  &offset=0
  &limit=20
  &namespace=default
  &Other common parameters
```
Output

```
{
    "returnCode": 0,
    "returnMsg": "ok",
    "data": {
        "totalCount": 1,
        "instanaces": [
             {
                "name": "simon-1272463236-574ou",
                "status": "Waiting",
                "reason": "Container process crashed",
                "ip": "100.70.0.10",
                "restartCount": 11,
                "readyCount": 0,
                "nodeName": "10.133.0.44",
                "nodeIp": "10.133.0.44",
                "createdAt": "2016-12-14 15:31:56",
                "containers": [
                    {
                        "containerId": "e341e732e18da7015c440de0b26617725718d289e7c5187177dd91318dc6550d",
                        "status": "Waiting",
                        "reason": "Container process crashed",
                        "image": "registry.ccs.tencentyun.com/test/test2:latest"
                    }
                ]
            }
        ]
    }
}

```
