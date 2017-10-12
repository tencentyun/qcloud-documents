## 1. API Description
 
This API (DescribeServiceEvent) is used to query the list of events occurred for the service within the last hour.

Domain for API request: ccs.api.qcloud.com



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.  |
| serviceName   | Yes    | String | Service name. Please enter the *serviceName* returned by the [DescribeClusterService](https://cloud.tencent.com/document/api/457/9440) API.|
| namespace | No | String      | Namespace. Please enter the *namespace* returned by the [DescribeClusterService](https://cloud.tencent.com/document/api/457/9440) API. Default is "default" |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed |
| message | String | Module error message description depending on API |
| eventList | Object Array | Event list. Details are shown below |

``eventList`` parameter details


| Parameter Name | Type | Description |
|---------|---------|---------|
| firstSeen | String | Time when the event occurred for the first time (only one entry for each event, duplicate entries for the same event will be removed) |
| lastSeen | String | Time when the event occurred for the last time |
| count | Int | Total occurrences of the event |
| level | String | Event level. There are two levels: Normal (normal event), and Warning (exceptional event) |
| objType | String | Corresponding kubernetes resource type for the event, such as Pod, ReplicationController, Service, Node, Deployment, Daemonset, ReplicaSet, Job, Secret, Configmap. For the details about kubernetes resources, please see [kubernetes Resources](https://github.com/kubernetes/kubernetes/blob/b392910bc7de425372fe6bf03a2c2c92fe1bae12/docs/devel/api-conventions.md#types-kinds) |
| objName | String | Corresponding kubernetes resource name for the event |
| reason | String | Event reason |
| message | String | Event details |


## 4. Example
Input

```
  https://domain/v2/index.php?Action=DescribeServiceEvent
  &clusterId=cls-xxxxx
  &serviceName=test-web-service
  &namespace=default
  &Other common parameters
```
Output

```
 {
    "code" : 0,
    "message":"",
	"data":{
	    "eventList": [
	    {
        "firstSeen": "2016-11-08 16:15:15",
        "lastSeen": "2016-11-09 16:59:56",
        "count": 6530,
        "level": "Warning",
        "objType": "Pod",
        "objName": "frontend-542052039-h2yj8",
        "reason": "Failed to launch pod",
        "message": "Error syncing pod, skipping: failed to \"StartContainer\" for \"php-redis\" with ImagePullBackOff: \"Back-off pulling image \\\"gcr.io/google-samples/gb-frontend:v5\\\"\"\n"
       },
       {
        "firstSeen": "2016-11-08 16:15:15",
        "lastSeen": "2016-11-09 16:59:56",
        "count": 6530,
        "level": "Normal",
        "objType": "Pod",
        "objName": "frontend-542052039-h2yj8",
        "reason": "Retry operation",
        "message": "Back-off pulling image \"gcr.io/google-samples/gb-frontend:v5\""
       } 
	]
	} 
}

```
