## 接口描述
### 功能描述
给国内用户发送指定语音文件 fid 语音通知。

### URL 示例
`POST https://cloud.tim.qq.com/v5/tlsvoicesvr/sendfvoice?sdkappid=xxxxx&random=xxxx`
**注**：sdkappid 请填写您在腾讯云上申请到的，random 请填成随机正整数。

## 请求参数

```json
{
  "fid": "8550911c8631f8bcee5e31da6bb551c996dc4a26.wav",
  "playtimes": 2,
  "sig": "08d7ca56081a32f77d0c54ef5b7aff304fb871522bb9db63bfe56b700d4dbb00",
  "tel": {
    "nationcode": "86",
    "mobile": "13788888888"
  },
  "time": 1520333948,
  "ext": ""
}
```

| 参数      | 必选 | 类型   | 描述                                                                                             |
|-----------|------|--------|--------------------------------------------------------------------------------------------------|
| fid       | 是   | string | 语音文件 fid，由语音文件上传接口返回的唯一语音文件标识
| playtimes | 否   | number | 播放次数，可选，最多3次，默认2次                                                                 |
| sig       | 是   | string | App 凭证，具体计算方式见下注                                                                      |
| tel       | 是   | object | 电话号码                                                                                         |
| time      | 是   | number | 请求发起时间，UNIX 时间戳(单位秒)，如果和系统时间相差超过10分钟则会返回失败                               |
| ext       | 否   | string | 用户的 session 内容，腾讯 server 回包中会原样返回                                                    |

- 参数`tel`:

| 参数       | 必选 | 类型   | 描述     |
|------------|------|--------|----------|
| mobile     | 是   | string | 手机号码 |
| nationcode | 是   | string | 国家码   |

## 响应参数

```json
{
    "result": 0,
    "errmsg": "ok",
    "callid": "9277cf828943eb70b3cea31890008ad0",
    "ext": ""
}
```

| 参数   | 必选 | 类型   | 描述                                          |
|--------|------|--------|-----------------------------------------------|
| result | 是   | number | 错误码，0表示成功（计费依据），非0表示失败      |
| errmsg | 是   | string | 错误消息，result 非0时的具体错误信息           |
| callid | 否   | string | 标识本次发送 ID，标识一次下发记录              |
| ext    | 否   | string | 用户的 session 内容，腾讯 server 回包中会原样返回 |

### App 凭证计算

- c++

```c++
// 格式字符串
string fmt = "appkey=%s&random=%lu&time=%lu&mobile=%s";
// sdkappid 对应的 appkey，业务方需高度保密
string appkey = "5f03a35d00ee52a21327ab048186a2c4";
// 请求 URL 中的随机值
uint64_t random = 7226249334;
// 当前请求时间，UNIX 时间戳，单位秒
time_t now = time(NULL);
// 手机号码
string mobile = "13788888888";
// 计算 sig
string sig = sha256hex(format(fmt, appkey, random, now, mobile));
```

- python

```python
import hashlib
import time

# 格式字符串
fmt = "appkey={}&random={}&time={}&mobile={}"
# sdkappid 对应的 appkey，业务方需高度保密
appkey = "5f03a35d00ee52a21327ab048186a2c4"
# 请求 URL 中的随机值
random = 1234
# 当前请求时间，UNIX 时间戳，单位秒
now = int(time.time())
# 手机号码
mobile = "13788888888"
# 计算 sig
sig = hashlib.sha256(fmt.format(appkey, random, now, mobile)).hexdigest()
```


## DEMO
腾讯云短信服务为您提供了 [Java SDK](https://cloud.tencent.com/document/product/382/5804)、[PHP SDK](https://cloud.tencent.com/document/product/382/5804)、[Python SDK](https://cloud.tencent.com/document/product/382/5804)、[Node.js SDK](https://cloud.tencent.com/document/product/382/5804) 和 [C# SDK](https://cloud.tencent.com/document/product/382/5804) 供您参考，欢迎查阅。
