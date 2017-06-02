## 1. API Description
 
This API (DeleteInstances) is used to delete instance

Domain for API request: <font style="color:red">ccs.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://www.qcloud.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId | Yes| String | Cluster ID. You can obtain this ID from the clusterId in the returned fields of the API "Query Clusters".  |
| instances.n | Yes | String | Array containing instance names. Use the "name" field returned when querying service instance list |
| namespace | No | String      | Namespace. Default is "default" |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: successful. Other values: failed. |
| message | String | Module error message description depending on API. |
| successList | String array | Name of instances that are successfully deleted |
| failedMap | Map[string]string | key is the name of the instance that failed to be deleted, value is the reason for the failure |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=DeleteInstances
  &clusterId=clus-xxxxx
  &instances.0=test-web-aweex
  &namespace=default
```
Output

```
  {
      "code" : 0,
      "message" : "ok",
	  "successList":[
       "test-web-aweex"
      ],
      "failedMap":{
      }
  }

```
