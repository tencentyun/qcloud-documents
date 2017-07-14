## Delete a Service

## 1. API Description
 
This API (DeleteClusterService) is used to delete service

Domain for API request: <font style="color:red">ccs.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://www.qcloud.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId | Yes| String | Cluster ID. You can obtain this ID from the clusterId in the returned fields of the API "Query Clusters".  |
| serviceName | Yes | String | Service name |
| namespace | No | String      | Namespace. Default is "default" |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: successful. Other values: failed. |
| message | String | Module error message description depending on API. |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=DeleteClusterService
  &clusterId=clus-xxxxx
  &serviceName=test-web-service
  &namespace=default
```
Output

```
  {
      "code" : 0,
      "message" : "ok",
  }

```
