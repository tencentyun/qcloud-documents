## 1. API Description
This API (GetAutoDelStrategy) is used to obtain the auto deletion strategy for repository tag.
Domain name for API request: `ccr.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/doc/api/457/9463).

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| reponame | Repository name | String | Yes |


## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |
| totalCount | Number of strategies | Int |
| strategyInfo | List of strategy details | Object Array |

"strategyInfo" is composed as follows:

| Parameter Name | Description | Type | 
|---------|---------|------
| username | User name of an image repository | String |
| reponame | Repository name | String |
| type | Strategy type<br>keep\_last\_days: Retain the data of last few days<br>keep\_last\_nums: Retain a specified amount of recent data | String |
| value | Strategy value | Int |
| valid | Whether the strategy is valid. 1: Valid; 0: Invalid | Int |
| creation_time | Time when the strategy is created | String |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=GetAutoDelStrategy
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
        "strategyInfo": [
            {
                "username": "100001066666",
                "repo_name": "test/kube_test",
                "type": "keep_last_nums",
                "value": 10,
                "valid": 1,
                "creation_time": "2018-03-07T16:53:23+08:00"
            }
        ],
        "totalCount": 1
    }
}

```

