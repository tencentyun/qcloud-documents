本文将介绍您将在线客服链接嵌入 App 后，该在线客服链接可与 App 中用户昵称等相关参数进行对接，同时支持将自定义字段透传到企业业务系统。
![](https://qcloudimg.tencent-cloud.cn/raw/01e21fbfdc9a954b84a19841ff6bcd60.png)

1. 开发者页面登录请求
2. 开发者后台对开发者页面登录请求进行鉴权
3. [](id:step3)请使用 [创建用户数据签名](https://cloud.tencent.com/document/product/679/58260) API 对用户数据进行签名后台会返回 ClientDataUserSig
4. 开发者后台将业务本身的登录票据和用户数据签名(ClientDataUserSig)，而且也包括用户数据 ClientData
5. 拉起 TCCCWEB 时传递 ClientDataUserSig 和 ClientData
6. TCCCWEB 将 ClientDataUserSig 和 ClientData 透传给 TCCC 后台
7. TCCC 后台通过 ClientData 校验 ClientData
8. 注册成功

ClientData JSON 字符串，通过 TCCC 后台传递坐席的 Web 端，TCCC 会对其中的固定字段进行解析，固定字段如下：

| 字段名        | 类型  | 说明                            |
| ---------- | --- | ----------------------------- |
| peerSource | 字符串 | 会话来源，开发者可以传递实际的业务名称，比如xx商城，Tmall |
| uid        | 字符串 | 用户账号，与上述 [步骤 3](#step3) 中协议中的 uid 保持一致   |
| nickName   | 字符串 | 用户昵称，比如小马，小刚                  |

>!ClientData 请使用序列化后的 JSON 字符串，无需额外编码`{"peerSource":"XX商城","nickName":"张三","uid":"zhangsan","extra_phoneNumber":"15813812110","extra_ID":"611551555111XXX","extra_questionGroup":"投诉"}`

获取到签名之后将 ClientData 和 UserSig 通过 url 的 query string 传递给 TCCC，下面是一个典型的 TCCC WEB 页 URL：
```
https://tccc.qcloud.com/web/im/index.html#/chat?webAppId=9903496b6be2e67ad291dd2323f3ae9f&title=foo&clientData=%7B%22peerSource%22%3A%22%E4%BA%AC%E4%B8%9C%E5%95%86%E5%9F%8E%22%2C%22nickName%22%3A%22%E5%BC%A0%E4%B8%89%22%2C%22uid%22%3A%22zhangsan%22%2C%22extra_phoneNumber%22%3A%2215813812110%22%2C%22extra_ID%22%3A%22611551555111XXX%22%2C%22extra_questionGroup%22%3A%22%E6%8A%95%E8%AF%89%22%7D&userSig=eJxUkEtvm0AQx7-Lnut0WWArkHJw1qm82Os07rI8bhDWYcwjxJiXqn73CuMeMtLv8h-NTzPzB8n97wc9NnDRyDUpxt9uCWS6vsIJ9AW5SDLGVs*hPK5XPt*szN36k*bhr9V4L7TMtFmRNA1kyDUsjAm1iGHdO-COXDQ2PtDWUd-H3Vs9mJwOqt7k9md8wF68SQbzXbDJd9onyh-vyitUGrkGJRT-sB3iLGnX6kvanZCL9OQNcaAmnzjGW3Uo*fkD7JgJO4KUcnLiMEBalecE23ka*PAC*7LfbYqOF7BnnpEEr-ACnqW3*QLjLa*UlW29PDSfPlJil7JW16hS0*wWUlgLfBRSzI5Sb49TpBzvyDjl52gU0jdmDvJ5FCqPgi-On0YcHnASON3R9PosXM87VdCERW9jOL0*-j*9v72ePGD0918AAAD--2wfhLY_
其中 clientData 通过 URLDecode 之后，
{"peerSource":"XX商城","nickName":"张三","uid":"zhangsan","extra_phoneNumber":"15813812110","extra_ID":"611551555111XXX","extra_questionGroup":"投诉"}

```
完成后，在座席侧会展示xx商城张三投诉字样，便于座席识别。
