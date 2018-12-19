## 1. API Description
 
This API (DeleteClusterService) is used to delete service.

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
