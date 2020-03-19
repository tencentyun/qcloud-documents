Rest API 调用返回 HTTP Status Code，以及 Response Body 中错误信息的 JSON 串。

● 调用成功，Status Code 为 200。
● 后台错误，Status Code 统一返回 500。
● API请求错误，Status Code统一返回 400。
● 详细错误信息可解析返回消息体中的 JSON 串 。

示例 ：

```
HTTP/1.1 500
{"error_info":{"error_code":13005,"message":"CACHE SET MEMBER INFO FAILED"}}
```
