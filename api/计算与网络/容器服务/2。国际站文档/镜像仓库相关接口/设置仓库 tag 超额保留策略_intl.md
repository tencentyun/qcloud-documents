## 1. API Description
This API (SetAutoDelStrategy) is used to set the auto deletion strategy for repository tag. Tags are automatically deleted when the quota limit is reached.
Domain name for API request: `ccr.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/doc/api/457/9463).

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| reponame | Repository name | String | Yes |
| type | Strategy type<br>keep\_last\_days: Retain the data of last few days<br>keep\_last\_nums: Retain a specified amount of recent data | String | Yes |
| val | Strategy value | Int | Yes |


## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=SetAutoDelStrategy
  &reponame=test/kube_test
  &type=keep_last_nums
  &val=10 
  &other common parameters
```
Output

```
{
    "code": 0,
    "message": "", 
    "codeDesc": "Success"
}

```

