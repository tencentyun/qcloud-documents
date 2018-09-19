This API is used to query the number of devices associated with a tag of the App.
URL path: `http://domain name for API/v2/tags/ query_tag_token_num?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| tag | String | Yes | None | None |
### Response Parameters
In the common response parameters, the json format of the field result is as follows:

```
{
"device_num":589874
}
```
### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.
	
#### Before MD5 encryption:
```
GETopenapi.xg.qq.com/v2/tags/query_tag_token_numaccess_id=2100240957tag=easonmipushtesttimestamp=1502699920f255184d160bad51b88c31627bbd9530
```
#### Rest API URL:
```
http://openapi.xg.qq.com/v2/tags/query_tag_token_num?access_id=2100240957&tag=easonmipushtest&timestamp=1502699920&sign=0ea7f16df1b59d69c9b81b385f938822
```

