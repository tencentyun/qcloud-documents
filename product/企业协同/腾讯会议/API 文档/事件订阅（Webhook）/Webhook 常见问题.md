配置消息通知时，提示“code:10002,msg:通知 URL 不可用，请修改后重试！”
配置时会发送 GET 请求校验 URL 的响应内容是否满足要求，请确认是否正确通过签名校验且是否对 check_str 进行 base64 解码并将解码后的字符串正确返回，签名算法请参考 [签名校验](https://cloud.tencent.com/document/product/1095/51612)。
