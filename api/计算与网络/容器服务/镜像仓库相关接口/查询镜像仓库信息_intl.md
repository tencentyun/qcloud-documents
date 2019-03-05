## 1. API Description
This API (GetRepositoryInfo) is used to query the information of an image repository.
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
| creationTime | Time when a repository is created | String |
| description | Repository description | String |
| favorCount | The number of times a repository is added to Favorites | String |
| isQcloudOfficial | Whether an official image is used. true: Tencent Cloud official image; false: Not Tencent Cloud official image | Bool |
| isUserFavor | Whether the repository is added to Favorites by its user. true: Yes; false: No | Bool |
| public | Whether the repository is available to the public. 1: Public; 0: Private | Uint |
| pullCount | Number of pulls | Uint |
| reponame | Repository name | String |
| repotype | repository type.<br>QCLOUD HUB: Tencent Cloud repository<br>DOCKER HUB: DockerHub image | String |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=GetRepositoryInfo
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
        "creationTime": "2017-12-28 11:00:10",
        "description": "",
        "favorCount": 0,
        "isQcloudOfficial": false,
        "isUserFavor": false,
        "public": 0,
        "pullCount": 0,
        "reponame": "test/kube_test",
        "repotype": "QCLOUD HUB"        
    }
}

```
