版本 ：1.0.2
Host : api.meeting.qq.com
Protocols : https
Accepts : application/json
Responds With : application/json

所有 API 都是基于 Restful 规范通过 HTTPS 协议访问特定的 API 网关来完成，例如访问 URL:
```
https://api.meeting.qq.com/v1
```


完整的资源访问请求 URL 格式取决于要访问的资源，例如，查询一个会议的信息，需要通过 GET 方法：
```
GET https://api.wemeet.tencent.com/v1/meetings/{meetingId}
```


在 API 的参考指引页面，可以查阅 API 的具体说明和请求/回复的参数说明。
