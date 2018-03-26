## Push 消息统一路径
消息相关的接口，统一的接口地址是`http://wns.api.qcloud.com/api/`
在统一地址后面加上不同的接口名字，实现响应的功能接口。

## 签名生成方法
sign=Base64(Hmac-sha1(plaintext, secretkey))
secretkey：摘要算法 key，在腾讯云创建 app 时分配，
plaintext（原文）：“appid&timestamp”

