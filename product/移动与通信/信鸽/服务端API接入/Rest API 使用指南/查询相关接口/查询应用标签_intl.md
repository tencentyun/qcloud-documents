This API is used to query tags set by the App.
URL path: `http://domain name for API/v2/tags/query_app_tags?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| start | uint | No | 0 | The starting value |
| limit | uint | No | 100 | Limited number |
### Response Parameters
In the common response parameters, the json format of the field result is as follows:
```
{
"total": 2, // The total number of tags in App. Note that it is not the number of tags returned by this query.
"tags":["tag1","tag2"]
}
```
### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.

#### Before MD5 encryption:

```
GETopenapi.xg.qq.com/v2/tags/query_app_tagsaccess_id=2100240957timestamp=1502699212f255184d160bad51b88c31627bbd9530
```
#### Rest API URL:

```
http://openapi.xg.qq.com/v2/tags/query_app_tags?access_id=2100240957&timestamp=1502699212&sign=5dbf914884378af6b62cba919e012b34
```
