## 1. API Description
 
This API (DeleteClusterNamespace) is used to delete namespace.

Domain for API request: ccs.api.qcloud.com



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.  |
| names   | Yes    | String Array |Array of the namespace you want to delete. Please enter the *namespaces* returned by the [*DescribeClusterNameSpaces*](https://cloud.tencent.com/document/api/457/9430) API. |


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
  &name=xxxx
  &Other common parameters
```

Output

```
  {
    "code": 0,
    "message": "", 
}

```
