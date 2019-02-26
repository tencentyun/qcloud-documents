This API is used to query information of a token of the App (to check whether it is valid.
URL path: `http://domain name for API/v2/application/get_app_token_info?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| device_token | String | Yes | None | None |
### Response Parameters
In the common response parameters, the json of the field result is as follows:
```
{
 "isReg": 1, (1: token is registered. 0: token is not registered)
 "connTimestamp" :1426493097, (Latest active timestamp)
 "msgsNum": 2 (The number of offline messages of this App)
}
```
### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.
#### Before MD5 encryption:
```
GETopenapi.xg.qq.com/v2/application/get_app_token_infoaccess_id=2100240957device_token=76501cd0277cdcef4d8499784a819d4772e0fddetimestamp=1502698593f255184d160bad51b88c31627bbd9530
```

#### Rest API URL:
```
http://openapi.xg.qq.com/v2/application/get_app_token_info?access_id=2100240957&device_token=76501cd0277cdcef4d8499784a819d4772e0fdde&timestamp=1502698593&sign=c4f650c6c468adba2e2b82a15ca68c3e
```
