message 参数应为 APNS 规定的 payload（也是一个 json 字符串），详细定义参考 APNS 官方手册。
信鸽在其基础上仅增添了两保留字段 xg 和 accept_time。payload 不能超过 800 字节。需要注意的是 accept_time 字段不会传递给 APNS，因此不占用 payload 容量。

## 普通通知示例
```
{
"aps" : { // apns规定的key-value
"alert" : { //设置消息通知栏的字段
"title": "this is a title", //通知标题
"body" : "Bob wants to play poker", //通知内容
},
"badge" : 5,
“category” : “INVITE_CATEGORY”,
},
"accept_time":[ //允许推送给用户的时段，选填。accept_time不会占用payload容量
{
"start":{"hour":"13","min":"00"},
"end": {"hour":"14","min":"00"}
},
{
"start":{"hour":"00","min":"00"},
"end": {"hour":"09","min":"00"}
}
] // 仅0~9点和13~14点这两个时段可推送
"custom1" : "bar", // 合法的自定义key-value，会传递给app
"custom2" : [ "bang", "whiz" ], // 合法的自定义key-value，会传递给app
"xg" : "oops" // 错误！xg为信鸽系统保留key，其value会被信鸽系统覆盖，应避免使用
}
```
## 静默通知示例

```
{
"aps" : { // apns规定的key-value
"badge" : 5,
"category" : “INVITE_CATEGORY”,
"content-available": 1, //静默通知的标识
},
"custom1" : "bar", // 合法的自定义key-value，会传递给app
"custom2" : [ "bang", "whiz" ], // 合法的自定义key-value，会传递给app
"xg" : "oops" // 错误！xg为信鸽系统保留key，其value会被信鸽系统覆盖，应避免使用
}
```
