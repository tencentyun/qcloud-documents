## 1. API Description
This API (UpdateRepositoryPublic) is used to modify the access attribute of an image repository.
Domain name for API request: `ccr.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/doc/api/457/9463).

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| reponame | Repository name | String | Yes |
| public | Whether the repository is available to the public: 0: Private; 1: Public | Int | Yes |


## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=UpdateRepositoryPublic
  &reponame=test/kube_test
  &public=0
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
