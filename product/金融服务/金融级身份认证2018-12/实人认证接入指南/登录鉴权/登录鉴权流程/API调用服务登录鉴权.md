## 整体登录鉴权流程
1. Access Token 获取
Access Token 有效期7200秒，建议合作方缓存在服务器，必须在临近过期和使用中失效时重新获取，获取方式见 [Access Token 获取]()。
2. 生成签名
合作伙伴获取 SIGN ticket，有效期3600秒，且仅一次性有效，建议合作方缓存在服务器，必须在临近过期和使用中失效时重新获取。流程中，获取 API ticket 请求的 type 为 SIGN。获取方式见 [SIGN ticket 获取]()。
3. 调用 API 服务
服务端查询结果：合作伙伴服务后台校验 SIGN，查询身份认证结果。

流程图示
![](https://main.qcloudimg.com/raw/211a6e63c095c1098c8052cf9e76d404.png)
 
>! 
1. Access Token 有效期7200秒，建议合作方缓存在服务器，必须在临近过期和使用失效时重新获取。
2. Nonce ticket 有效期120秒，且一次性有效。
3. 在用户登录流程中，获取 API ticket 请求的 user_id 为必填参数，type 为 NONCE。
4. SIGN ticket 有效期3600秒，建议合作方缓存在服务器，必须在临近过期和使用失效时重新获取。
5. 在查询刷脸结果流程中，获取 API ticket 请求的 type 为 SIGN。
