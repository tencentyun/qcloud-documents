## 1. API Description
 
This API (CreateClusterNamespace) is used to create namespace.

Domain for API request: ccs.api.qcloud.com



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.  |
| name   | Yes | String       | Namespace name |
| description   | Yes | String |Description of the namespace|



## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed |
| codeDesc | String |Service error code. Returns *Success* for successful operation, and detailed reason for failed operation.|
| message | String | Module error message description depending on API|


## 4. Example

Input

```
  https://domain/v2/index.php?Action=CreateClusterNamespace
  &clusterId=cls-xxxxx
  &name=tst
  &Other common parameters
```

Output

```
  {
    "code": 0,
    "message": "", 
}

```
