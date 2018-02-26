## 整体登录鉴权流程

### 第一步：Access Token 获取

- Access Token 有效期 7200 秒，建议合作方缓存在服务器，必须在临近过期和使用中失效时重新获取，获取方式见 [Access Token 获取]()。

### 第二步：生成签名

- 合作伙伴获取 SIGN ticket，有效期 3600 秒，且仅一次性有效，建议合作方缓存在服务器，必须在临近过期和使用中失效时重新获取。流程中，获取 API ticket 请求的 type 为 SIGN。获取方式见 [SIGN ticket 获取]()。

### 第三步：调用 API 服务

- 服务端查询结果：合作伙伴服务后台校验 SIGN，查询身份认证结果。


## 流程图示
![](https://mc.qcloudimg.com/static/img/e90548bcf95bb5c51b4a9f97ac015084/API.png)

更多产品鉴权流程：[登录鉴权概览](https://cloud.tencent.com/document/product/655/13663)




