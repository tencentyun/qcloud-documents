This API is used to query tags set on a device that installs the App.
URL path: `http://domain name for API/v2/tags/query_token_tags?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| device_token | String | Yes | None | None |
### Response Parameters
In the common response parameters, the json format of the field result is as follows:
```
{
"tags":["tag1","tag2"]
}
```
### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.
#### Before MD5 encryption:

```
GETopenapi.xg.qq.com/v2/tags/query_token_tagsaccess_id=2100240957device_token=76501cd0277cdcef4d8499784a819d4772e0fddetimestamp=1502699212f255184d160bad51b88c31627bbd9530
```

#### Rest API URL:
```
http://openapi.xg.qq.com/v2/tags/query_token_tags?access_id=2100240957&device_token=76501cd0277cdcef4d8499784a819d4772e0fdde&timestamp=1502699212&sign=4cbd1b7a5553ed263f47a4a0b96402e9
```
