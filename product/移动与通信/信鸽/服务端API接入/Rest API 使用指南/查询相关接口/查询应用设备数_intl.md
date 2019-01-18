This API is used to query the number of devices (number of tokens) covered by the App.
URL path: `http://domain name for API/v2/application/get_app_device_num?params`

### Request Parameters
This API only includes [common parameters](https://cloud.tencent.com/document/product/548/14705).

### Response Parameters
In the common response parameters, the json format of the field result is as follows (If the information of an App in the request App list is invalid, no result is returned in the "result" field):
```
{
 "device_num": 34,567 (number of devices)
}
```

### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.
#### Before MD5 encryption:
```
GETopenapi.xg.qq.com/v2/application/get_app_device_numaccess_id=2100240957timestamp=1502701471f255184d160bad51b88c31627bbd9530
```
#### Rest API URL:

```
http://openapi.xg.qq.com/v2/application/get_app_device_num?access_id=2100240957&timestamp=1502701471&sign=e4385f856ddaa932170c181927965cb1
```
