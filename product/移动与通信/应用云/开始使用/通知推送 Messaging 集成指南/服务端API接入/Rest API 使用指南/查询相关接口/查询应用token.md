查询应用的某个 token 的信息（查看是否有效）
URL 路径：`http://接口域名/v2/application/get_app_token_info?params`

### 请求参数
除了 [通用参数](https://cloud.tencent.com/document/product/666/15603) 外，还包括如下参数：

|参数名|	类型	|必需	|默认值|	描述|
|-|-|-|-|-|
|device_token|	string|	是	|无|	无|

### 响应结果
在通用返回结果参数中，result 字段的 json 如下：
```
{
 "isReg":1, //（1为token已注册，0为未注册）
 "connTimestamp":1426493097, //（最新活跃时间戳）
 "msgsNum":2 //（该应用的离线消息数）
}
```
### 示例
MD5 加密前 url 用作生成 sign，Rest Api Url 为最终请求的 url（以下为 Android 推送示例，需替换通用参数后使用）。
#### MD5 加密前：
```
GETopenapi.xg.qcloud.com/v2/application/get_app_token_infoaccess_id=2100240957device_token=76501cd0277cdcef4d8499784a819d4772e0fddetimestamp=1502698593f255184d160bad51b88c31627bbd9530
```

#### Rest Api Url:
```
http://openapi.xg.qcloud.com/v2/application/get_app_token_info?access_id=2100240957&device_token=76501cd0277cdcef4d8499784a819d4772e0fdde&timestamp=1502698593&sign=c4f650c6c468adba2e2b82a15ca68c3e
```
