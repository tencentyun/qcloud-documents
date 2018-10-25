## 1 请求投递失败：
### 1.1 应答包体
应答包体是JSON格式，其格式符合如下特征：
```
{
    "ActionStatus": "FAIL",
    "ErrorInfo": "service timeout or request format error,please check and try again",
    "ErrorCode": 60008
}
```
应答包体中包含ActionStatus、ErrorInfo、ErrorCode这三个属性，其含义如下：
| 字段 | 类型| 说明 |
|---------|---------|---------|
|ActionStatus | String | 请求处理的结果，FAIL表示失败。 |
|ErrorInfo  | String | 失败原因 。|
|ErrorCode  | Integer | 错误码，为失败错误码。

### 1.2 错误码含义
| 错误码 |含义说明| 
|---------|---------|
| 60002 | HTTP解析错误 ，请检查HTTP请求URL格式。| 
| 60003 | HTTP请求JSON解析错误，请检查JSON格式 。| 
| 60006 | sdkappid失效，请核对sdkappid有效性 。| 
| 60007 | 接口调用频率超过限制，请降低请求频率 。| 
| 60008 | 服务请求超时或HTTP请求格式错误，请检查并重试 。| 
| 60009 | 请求资源错误，请检查请求URL。 | 
| 60012 | 接口需要带sdkappid，请检查请求URL中的sdkappid。 |
| 60013 | HTTP响应包JSON解析错误。 | 