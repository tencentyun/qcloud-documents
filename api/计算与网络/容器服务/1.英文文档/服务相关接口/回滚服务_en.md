## 1. API Description
 
This API (RollBackClusterService) is used to restore the service back to the configuration prior to update (to the previous configuration only).

Domain for API request: ccs.api.qcloud.com



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.  |
| serviceName   | Yes    | String | Service name. You can obtain this name from the returned serviceName of the API "Query Service List" |
| namespace | No | String      | Namespace. Default is "default" |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed |
| message | String | Module error message description depending on API |


## 4. Example
Input

```
  https://domain/v2/index.php?Action=RollBackClusterService
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
