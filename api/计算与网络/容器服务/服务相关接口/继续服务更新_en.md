## 1. API Description
 
This API (ResumeClusterService) is used to resume a paused service update.

Domain for API request: <font style="color:red">ccs.api.qcloud.com</font>



## 2. Input Parameters


The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://www.qcloud.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the clusterId in the returned fields of the API "Query Clusters".  |
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
  https://domain/v2/index.php?Action=ResumeClusterService
  &clusterId=cls-xxxxx
  &serviceName=test-web-service
  &namespace=default
  &Other common parameters
```
Output

```
  {
      "code" : 0,
      "message" : "ok",
  }

```
