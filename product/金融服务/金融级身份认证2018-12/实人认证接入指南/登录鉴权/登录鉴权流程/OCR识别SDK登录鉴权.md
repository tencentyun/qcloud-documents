## 第一步：Access Token 获取
Access Token 有效期7200秒，建议合作方缓存在服务器，必须在临近过期和使用中失效时重新获取。获取方式请参见 [Access Token 获取](https://cloud.tencent.com/document/product/655/31946)。
## 第二步：SDK 登录鉴权
- NONCE ticket 有效期120秒，且仅一次性有效。
- 在用户登录流程中，获取 API ticket 请求的 user_id 为必填参数，type 为 NONCE。获取方式请参见 [NONCE ticket 获取](https://cloud.tencent.com/document/product/655/31957)。

## 第三步：返回结果服务端验证
SIGN ticket 有效期3600秒，建议合作方缓存在服务器，必须在临近过期和使用中失效时重新获取。流程中，获取 API ticket 请求的 type 为 SIGN。获取方式请参见 [SIGN ticket 获取](https://cloud.tencent.com/document/product/655/31956)。现有以下两种方式返回结果验证：
- 方式一：签名验证
合作伙伴 App 端调用其服务后台验证签名，验证成功后即可信任前端的返回结果。
- 方式二：服务端查询结果
合作伙伴 App 端调用其服务后台查询识别结果，由 OCR 识别服务端鉴权并返回最终结果。

详细接入开发指南请参见：[身份证 OCR SDK 接入](https://cloud.tencent.com/document/product/655/32069)

## 流程图示
OCR 识别 SDK 登录鉴权流程图示：
 ![](https://main.qcloudimg.com/raw/0e7d7c6ea07fd0dd5a1c6d15e37dd44c.png)
 
>!
- Access Token 有效期7200秒，建议合作方缓存在服务器，必须在临近过期和使用失效时重新获取。
- NONCE ticket 有效期120秒，且一次性有效。
- 在用户登录流程中，获取 API ticket 请求的 user_id 为必填参数，type 为 NONCE。
- SIGN ticket 有效期3600秒，建议合作方缓存在服务器，必须在临近过期和使用失效时重新获取。
- 在查询刷脸结果流程中，获取 API ticket 请求的 type 为 SIGN。
