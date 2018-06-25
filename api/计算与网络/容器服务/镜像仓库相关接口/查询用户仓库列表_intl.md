## 1. API Description
This API (SearchUserRepository) is used to query user's repository list.
Domain name for API request: `ccr.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/doc/api/457/9463).

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| offset | Offset. Default is 0. | Uint | No |
| limit | Maximum number of returned results. Defaults is 20, and maximum is 100. | Uint | No |
| reponame | Name of the repository to be queried. All repositories are listed if this is left empty. Otherwise, an exact match query is performed based on this name | String | No |
| public | Filter condition. 1: public; 0: private. Query all if this parameter is not specified. | String | No |
| namespace | Namespace | String | No |

## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |
| totalCount | Number of query results | String |
| privilegeFiltered | false: Return all results; true: Not return all results | Bool |
| repoInfo | Repository information | Object Array |

"repoInfo" is composed as follows:

| Parameter Name | Description | Type | 
|---------|---------|---------|
| reponame | Repository name | String |
| repotype | Repository type.<br>QCLOUD HUB: Tencent Cloud repository<br>DOCKER HUB: DockerHub image | String |
| tagCount | Number of tags | Int |
| public | Whether the repository is available to the public. 1: Public; 0: Private | Int |
| isUserFavor | Whether the repository is added to Favorites by the user. true: Yes; false: No | Bool |
| isQcloudOfficial | Whether Tencent Cloud official repository is used. true: Yes; false: No | Bool |
| favorCount | The number of times a repository is added to Favorites by all users | Int |
| pullCount | Number of pulls | Int |
| description | Description | String |
| creationTime | Creation time | String |
| updateTime | Update time | String |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=SearchUserRepository
  &offset=0
  &limit=20
  &reponame=test/kubetest
  &public=1
  &namespace=test
  &other common parameters
```
Output

```
{
    "code": 0,
    "message": "", 
    "codeDesc": "Success",
    "data": {
		"totalCount": 1
	    "privilegeFiltered": false,
	    "repoInfo": [
	      {
	        "reponame": "test/kubetest",
	        "repotype": "QCLOUD HUB",
	        "tagCount": 2,
	        "public": 0,
	        "isUserFavor": false,
	        "isQcloudOfficial": false,
	        "favorCount": 0,
	        "pullCount": 5137,
	        "description": "",
	        "creationTime": "2017-09-12 13:02:58",
	        "updateTime": "2018-02-28 14:26:06"
	      }
	   ],
	}
}

```

