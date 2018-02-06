## API Description
This API (AssumeRole) is used to apply for temporary credentials for a role.
Domain for API request: sts.api.qcloud.com

## Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------ | ------------ | ------------ | ------------ |
| roleArn | Yes | String | Description of a role's resources. For example: qcs::cam::uin/12345678:role/4611686018427397919, qcs::cam::uin/12345678:roleName/testRoleName |
| roleSessionName | Yes | String | User-defined name of a temporary session |
| durationSeconds | No | Int | The validity period of the temporary credentials (in seconds). Default is 1,800 seconds. The maximum value is 7,200 seconds. |

## Output Parameters
 
| Parameter Name | Type |Description |
| ------------ | ------------ | ------------ |
| credentials | Object | The object contains a triad of token, tmpSecretId, and tmpSecretKey. |
| -token | String | The value of token |
| -tmpSecretId | String | ID of the temporary security certificate |
| -tmpSecretKey | String | Key of the temporary security certificate |
| expiredTime | Int | Expiration time of certificate, expressed in a Unix timestamp with an accuracy down to seconds |
| expiration | String | Expiration time of certificate, expressed in a UTC time in iso8601 format |

## Example
Input
```
https://domain/v2/index.php?Action=AssumeRole&roleArn=qcs%3a%3acam%3a%3auin%2f12345678%3arole%2f4611686018427397919
&roleSessionName=abc&durationSeconds=1800&<Common request parameters>
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "credentials": {
            "sessionToken": "5e776c4216ff4d31a7c74fe194a978a3ff2a42864",
            "tmpSecretId": "AKIDcAZnqgar9ByWq6m7ucIn8LNEuY2MkPCl",
            "tmpSecretKey": "VpxrX0IMCpHXWL0Wr3KQNCqJix1uhMqD"
        },
        "expiredTime": 1506433269,
        "expiration": "2017-09-26T13:41:09Z"
    }
}

````

