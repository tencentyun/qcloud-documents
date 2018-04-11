This API is used to query the token mapped with an account of the App (to view the mapping relationship between the account and the token).
URL path: `http://domain name for API/v2/application/get_app_account_tokens?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| account | String | Yes | None | Account |

### Response Parameters
In the common response parameters, the json of the field result is as follows:
```
{
 "tokens":["token1","token2"]
}
```
### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.
#### Before MD5 encryption:

```
GETopenapi.xg.qq.com/v2/application/get_app_account_tokensaccess_id=2100240957account=easonshipushtestaccounttimestamp=1502699212f255184d160bad51b88c31627bbd9530
```

#### Rest API URL:
```
http://openapi.xg.qq.com/v2/application/get_app_account_tokens?access_id=2100240957&account=easonshipushtestaccount&timestamp=1502699212&sign=015ef9e7fde208f2d12674f731e13e8c
```
