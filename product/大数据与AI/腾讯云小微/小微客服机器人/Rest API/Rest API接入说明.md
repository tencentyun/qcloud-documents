## Rest API 接入说明

Rest API 接入是提供给第三方后台，微信公众号后台接入或第三方 App 调用接入小微机器人客服平台功能。Rest API 功能可以实现控制台中除用户注册外的全部功能。第三方使用 Rest API 前需要先通过 [TLS后台API使用手册](https://cloud.tencent.com/document/product/269/1510) 生成操作者 identifier 的 usersig 字段，这是使用 Rest API 方式接入小微客服机器人的前提条件。这一步将生成操作者 identifier 的鉴权数据信息，Rest API 请求接入小微客服机器人后台时会校验 usersig 字段的合法性，如果 usersig 字段不合法，则该请求将被拒绝。
Rest API 接入流程如下：
![](//mc.qcloudimg.com/static/img/6ee9c38421513642266ed50c2de89a1e/image.png)





