## 1. API Description
This API returns relevant function information according to the query parameters you passed.

Domain name for API access: scf.api.qcloud.com
## 2. Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is ListFunctions.     

| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| order | No | String | Whether the result is returned in ascending order or descending order. Available values: asc, desc. |
| orderby | No | String | This determines the field based on which the returned result is sorted. Available fields: addtime, modtime, functionname. |
| offset | No | Int | Data offset. Default: 0. |
| limit | No | Int | Length of returned data. Default: 20. |
| searchKey | No | String | Result is returned based on fuzzy match with the functionName field. |
## 3. Response Parameters
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| data | String | JSON data which contains function list information for the user. |

The "data" field contains function list information for the user, where the "total" field indicates the total number of functions for the user, in the current region. The data structures for the functions are as follows:

| Parameter Name | Type | Description |
|-------|---|---------------|
| modTime | String | The last time when the function was modified. |
| functionName | String | Function name. |
| addTime | String | Function creation time. |


## 4. Example
Input
```
https://scf.api.qcloud.com/v2/index.php?Action=ListFunctions
&<Common request parameters>
&limit=2
&order=asc
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "functions": [
            {
                "modTime": "2017-05-04 19:40:38",
                "addTime": "2017-05-04 19:40:38",
                "functionName": "test6"
            },
            {
                "modTime": "2017-05-02 09:39:49",
                "addTime": "2017-05-02 09:39:49",
                "functionName": "test4"
            }
        ],
        "total": 6
    }
}
```

