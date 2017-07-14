## 1. API Description
 
This API (DescribeClusterNameSpaces) is used to query the namespace of cluster.

Domain for API request: <font style="color:red">ccs.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://www.qcloud.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Query nameSpaces under the cluster |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed |
| message | String | Module error message description depending on API. For more information, please see Module Error Codes on Error Codes page. |
| namespaces | Obj Array |namespaces|



## 4. Example
Input

```
  https://domain/v2/index.php?Action=DescribeClusterNameSpaces
  &clusterId=cls-xxxxxx
  &Other common parameters
```
Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalCount": 1,
        "namespaces": [
            "default"
			"t3"
        ]
    }
}
```

