## 1. API Description
This API (GetLimit) is used to query user limit.
Domain name for API request: `ccr.api.qcloud.com`.

## 2. Input Parameters
No parameter is provided for this API. Other parameters can be found in [Common Request Parameters](/doc/api/457/9463).

## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |
| limitInfo | Limit information | Object Array |

"limitInfo" is composed as follows:

| Parameter Name | Description | Type | 
|---------|---------|---------|
| username | User name of an image repository | String |
| type | Limit type.<br>namespace: Namespace<br>repo: Repository<br>tag: Image tag<br>triggers: Trigger | String |
| value | Limit value | Int |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=GetLimit
  &reponame=test/kube_test
  &other common parameters
```
Output

```
{
    "code": 0,
    "message": "", 
    "codeDesc": "Success",
    "data": {
        "limitInfo": [
            {
                "username": "100001066666",
                "type": "namespace",
                "value": 10
            },
            {
                "username": "100001066666",
                "type": "repo",
                "value": 100
            },
            {
                "username": "100001066666",
                "type": "tag",
                "value": 100
            },
            {
                "username": "100001066666",
                "type": "triggers",
                "value": 10
            }
        ]
    }
}

```
