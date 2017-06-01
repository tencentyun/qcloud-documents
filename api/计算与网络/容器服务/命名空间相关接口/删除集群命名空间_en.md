## 1. API Description
 
This API (DeleteClusterNamespace) is used to delete namespace.

Domain for API request: <font style="color:red">ccs.api.qcloud.com</font>



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://www.qcloud.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the clusterId in the returned fields of the API "Query Clusters".  |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed |
| message | String | Module error message description depending on API|


## 4. Example

Input

```
  https://domain/v2/index.php?Action=DeleteClusterNamespace
  &clusterId=cls-xxxxx
  &Other common parameters
```

Output

```
  {
    "code": 0,
    "message": "", 
}

```
