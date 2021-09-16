## 调用 API 时返回签名错误的原因有哪些？
调用 API 时需要签名验证以保证接口数据的安全，避免出现例如请求数据被劫持篡改、请求超过时效、数据重复提交攻击等问题。
 - 如果您是通过企业内部应用鉴权访问，则详细请参考 [企业内部应用鉴权](https://cloud.tencent.com/document/product/1095/42413) 章节描述的算法；
 - 如果您是通过第三方应用鉴权访问，则详细请参考 [第三方应用鉴权（OAuth2.0）](https://cloud.tencent.com/document/product/1095/51257) 章节描述的算法。
 
调用方使用指定的签名算法计算方法对 HTTP 请求进行签名，通过 `"X-TC-Signature"` 将签名送到后台进行校验。校验签名通过，则会继续业务处理和返回结果。校验失败则会返回签名错误`"signature failed"`。

**签名算法步骤**
签名算法的步骤，可以简单概括为以下四步：
1. 生成签名串；
2. 对签名串进行 “HMAC-SHA256” 哈希计算；
3. 将哈希串转换成16进制字符串；
4. 对16进制字符串进行 Base64 编码。

**被签名串**
签名算法的步骤中，第一步很重要。被签名串分4个部分，由“\n”分割：
1. HTTP 方法的大小字符串 (“POST”，“GET”，“PUT”，“DELETE”)；
2. 参加签名的 HTTP 头组成的串；
3. HTTP URI；
4. HTTP body，如 body 为空，例如 GET 消息，则用空字符串(“”)。

**被签名串的注意点**
1. HTTP 方法要大写：“POST”，“GET”，“PUT”，“DELETE”；
2. URI 包含请求地址端口后面的全部串，例如：
```Plaintext
https://api.meeting.qq.com/v1/meetings/7567173273889276131?userid=tester1&instanceid=1
```
	则此处的 URI 为`"/v1/meetings/7567173273889276131?userid=tester1&instanceid=1"`；
3. 注意在组织被签名串时，切勿忘记各部分之间的回车换行符 “\n”；
4. [企业内部应用鉴权](https://cloud.tencent.com/document/product/1095/42413) 或 [第三方应用鉴权（OAuth2.0）](https://cloud.tencent.com/document/product/1095/51257)中的 Params，指的是 HTTP 请求的整个消息体 body。请注意，如果 body 为空，例如 GET 消息，则用空串；
5. HTTP 请求头里的字段 X-TC-Key 参与签名计算，该字段填写的是用户获得的密钥对当中的 secret_id，此处容易误解而使用 secret_key。



## 出现请求错误码400的原因有哪些？
常见的请求错误码400有以下几种原因：
1. 请求头忘记带必填字段 AppId，因为不参与签名，容易被遗忘。
2. API 对请求字段的大小写敏感，请注意严格按照文档中的参数字段大小写要求。注意小写“i”和大写“I”。
3. 参数名拼写错误。
4. 时间戳过期错误，如果请求体里的时间戳 X-TC-Timestamp 和请求到达 API 服务器时的当前时间差大于5分钟，将被判定为无效请求。
5. 重放错误，用户调试阶段容易发生的错误，构造请求的时候没有改时间戳 X-TC-Timestamp 和随机数 X-TC-Nonce，则同一个 AppId 下面的请求，将被判定为重放请求而拒绝。

详细的错误码列表请参见 [错误码](https://cloud.tencent.com/document/product/1095/43704)。



## 调用 API 创建会议后，为何在 App 上看不到会议列表？
腾讯会议支持企业用户接入时通过以下两种方式：
1. SSO 单点登录和腾讯会议账号体系对接。
2. 直接通过腾讯会议账号体系注册和创建用户。

>?
- 通过这两种方式接入的用户，在调用 API 时需要在 HTTP 请求头里带公共参数 X-TC-Registered：1。
- 不带这个参数，调用 API 的 userid 会默认为未注册用户。则打开 App，使用企业账号登录后，无法看到未注册用户创建的会议。


## 指定主持人失败的原因有哪些？

可能有以下原因：
1. 是否为注册用户 (已被 SSO 集成或者通过 API 用户管理接口注册完成) ，是否携带 X-TC-Registered=1。
2. 客户 userid 必须严格匹配(大小写需要区分) 。

## 企业用户无法调用 API 的原因有哪些？

可能有以下原因：
1. 检查是否缺少必要的 Header。
2. 检查是否缺少 AppId 等。
3. 可能和用户使用的 HTTP 发送组件有关，请检查请求体的字段名是否正确，是否符合 JSON 格式，必带参数是否带齐。


## 访问凭证（access_token）过期怎么办？
访问凭证（access_token）目前有效期为6小时。过期后，您可以使用续约凭证（refresh_token）调用 `https://meeting.tencent.com/wemeet-webapi/v2/oauth2/oauth/refresh_token` 接口，以获取新的访问凭证（access_token）。

## 续约凭证（refresh_token）过期怎么办？
续约凭证（refresh_token）目前有效期为30天。过期后，您需要引导用户重新授权 OAuth 应用。当再次授权后，同一会议用户、同一 OAuth 应用（sdk_id），得到的用户 ID（open_id）不变。
>!用户可能有多个会议 ID 身份，如使用其它用户 ID 身份进行授权，则将得到不一样的的 open_id。


