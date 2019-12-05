## 1. API Description
 
This API (PauseClusterService) is used to pause a service update process. Using this feature on a service that is not being updated also pauses capacity scaling operations on the containers, and subsequent service update operations will not launch.

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


## 4. Example
Input

```
  https://domain/v2/index.php?Action=PauseClusterService
  &clusterId=cls-xxxxx
  &serviceName=test-web-service
  &namespace=default
  &Other common parameters
```
Output

```
 {
    "code" : 0,
    "message":""
}

```
