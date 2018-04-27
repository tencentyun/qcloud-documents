## API Description

This API (GetSessionToken) is used to acquire the temporary credential for MFA verification. 
Request domain name:

```
sts.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter | Required | Type | Description |
| --------------- | ---- | ------ | ------------------------------------------------------------ |
| tokenCode | Yes | string | Token code |
| tokenType | No | string | Token type. Optional parameters: softToken (virtual MFA devices), hardToken (hardware MFA devices). It takes softToken if left empty. For more information on MFA devices, please see [MFA Definition](https://cloud.tencent.com/document/product/378/8641) |
| durationSeconds | No | string | The validity period (in sec) of the temporary credentials, with the value range of 300-7,200. Default is 1,800 seconds. |

## Output Parameters

| Parameter | Type | Description |
| -------------- | ------ | ---------------------------------------------------- |
| credentials | object | The object contains a triad of token, tmpSecretId and tmpSecretKey. |
| --token | string | Token value for authentication |
| --tmpSecretId | string | tmpSecretId for generating signature |
| --tmpSecretKey | string | tmpSecretKey for generating signature |
| expiredTime | string | Expiration time of certificate, expressed in a UTC time in iso8601 format |

## Example

### Input

```
https://domain/v2/index.php?Action=GetSessionToken&tokenCode=123456&tokenType=softToken&durationSeconds=1800&<Common request parameters>
```

### Output

#### Verification succeeded

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
        "expiredTime": "2018-03-14T13:41:09Z",    
    }
}
```

#### MFA verification failed

```
{
    "code": 4106,
    "message": "(60006)MFA Invalid",
    "codeDesc": "MFACheckFailed",
    "data": []
}
```




