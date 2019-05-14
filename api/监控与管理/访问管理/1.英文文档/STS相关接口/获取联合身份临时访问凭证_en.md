## API Description
This API (GetFederationToken) is used to obtain the temporary credentials for a user with federated identity.
Domain for API request: sts.api.qcloud.com

## Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ------------ | ------------ | ------------ | ------------ |
| name | Yes | String | Nickname of the user with federated identity |
| policy | Yes | String | Policy description. Note: 1. It cannot contain spaces and line breaks; 2. For more information on the policy syntax, please see [CAM Policy Syntax](https://cloud.tencent.com/document/product/598/10603); 3. The policy cannot contain principal element |
| durationSeconds | No | Int | The validity period of the temporary credentials (in seconds). Default is 1,800 seconds. The maximum value is 7,200 seconds. |

## Output Parameters
 
| Parameter Name | Type |Description |
| ------------ | ------------ | ------------ |
| credentials | Object | The object contains a triad of token, tmpSecretId, and tmpSecretKey. |
| -token | String | The value of token |
| -tmpSecretId | String | ID of the temporary security certificate |
| -tmpSecretKey | String | Key of the temporary security certificate |
| expiredTime | Int | Expiration time of the certificate, expressed in a Unix timestamp with an accuracy down to seconds |

## Example
Input
```
https://domain/v2/index.php?Action=GetFederationToken&name=nickName&policy=%7b%22version%22%3a%222.0%22%2c%22statement%22%3a%5b%7b%22action%22%3a%5b%22name%2fqcisa%3aGetInfoByFields%22%5d%2c%22resource%22%3a%5b%22qcs%3a%3aqcisa%3a%3auin%2f90000000000%3aqcisa%2fbigCustomerDetail%22%2c%22qcs%3a%3aqcisa%3a%3auin%2f90000000000%3aqcisa%2fuserDetail%22%2c%22qcs%3a%3aqcisa%3a%3auin%2f90000000000%3aqcisa%2fauthDetail%22%5d%2c%22effect%22%3a%22allow%22%7d%5d%7d&durationSeconds=1800&<Common request parameters>
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "credentials": {
            "sessionToken": "9586a03c55b6cc088fb63461e88b4d4b5ceaeebf3",
            "tmpSecretId": "AKIDTs591htUbXKwmQryzpTvBF7nHZgdOlvv",
            "tmpSecretKey": "xjJhtujMq8E8tTcfbTFuRq8JMI7pQtHY"
        },
        "expiredTime": 1494309923,    
    }
}

````

