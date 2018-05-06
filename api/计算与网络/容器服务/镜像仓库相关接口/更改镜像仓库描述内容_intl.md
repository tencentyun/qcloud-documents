## 1. API Description
This API (UpdateRepositoryDesc) is used to modify the description of an image repository.
Domain name for API request: `ccr.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/doc/api/457/9463).

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| reponame | Repository name | String | Yes |
| description | Repository description | String | Yes |


## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=UpdateRepositoryDesc
  &reponame=test/kube_test
  &description=test
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
