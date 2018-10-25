This API is used to query the pushing status of group notifications.
URL path: `http://domain name for API/v2/push/get_msg_status?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| push_id | json | Yes | | [{"push_id": string}, {"push_id":"xxxx"}, ] |

### Response Parameters
In the common response parameters, the json format of the field result is as follows:
```
{
 "list": [
{
 "push_id": "27ABC5486977"
 "status": 0 (pending)/1 (pushing)/2 (pushing completed)/3 (pushing failed)
 "start_time":"year-mon-day hour:min:sec"
 "finished": xxxx (pushed)
 "total": xxxxx (to be pushed in total)
}
]
}
```
### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.

#### Before MD5 encryption:
```
GETopenapi.xg.qq.com/v2/push/get_msg_statusaccess_id=2100240957push_id=2841253998timestamp=1502698593f255184d160bad51b88c31627bbd9530
```
#### Rest API URL:
```
http://openapi.xg.qq.com/v2/push/get_msg_status?access_id=2100240957&push_id=2841253998&timestamp=1502698593&sign=39b62ab54f08e7844ed1d86e00cec76a
```

