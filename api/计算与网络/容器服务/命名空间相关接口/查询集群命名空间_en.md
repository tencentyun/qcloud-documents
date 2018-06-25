## 1. API Description
 
This API (DescribeClusterNameSpaces) is used to query the namespace of cluster.

Domain for API request: ccs.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.  |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed |
| codeDesc | String |Service error code. Returns *Success* for successful operation, and detailed reason for failed operation.|
| message | String | Module error message description depending on API. For more information, please see Module Error Codes on Error Codes page. |
| namespaces | Obj Array |namespaces|

Details of *namespaces* 

| Field | Type | Description |
|---------|---------|---------|
| name | String | Name of the namespace |
| status | String| Status of the namespace ["Active","Terminating"] |
| description | string |  |
| createdAt | String | Creation time of the namespace |

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
        "totalCount": 2,
        "namespaces": [
            {
              "name":"default",
              "status":"Active",
              "description":""
              "createdAt":"2017-06-08 19:10:01"
            },
			{
              "name":"tst",
              "status":"Active",
              "description":"test"
              "createdAt":"2017-06-27 19:10:01"
            },
        ]
    }
}
```

