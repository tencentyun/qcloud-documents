合作方后台服务上送 sign、请求参数到二要素验证后台服务。
请求 URL：`https://ida.webank.com/api/paas/ocrauth`
请求方法：POST
报文格式：Content-Type: application/json
## 请求参数

| 参数 | 说明   | 类型   | 长度（字节） | 是否必填 |
| ---- | ----- | ----- | ---- | --- |
| webankAppId | WebankAppId，由腾讯指定 |String|腾讯云线下对接决定 |是|
| version     | 接口版本号</br>默认值：1.0.0   | String     | 20   | 是 |
| nonce       | 随机数</br>32 位随机串（字母 + 数字组成的随机数）| String     | 32   | 是 |
| sign        | 签名：使用上面生成的签名| String     | 40 | 是  |
| orderNo     | 订单号，由合作方上送，每次唯一 | String  | 32  | 是       |
| name        | 姓名 | String     | 30          | 是 |
| idNo        | 身份证号码    | String     | 18   | 是   |
| bizScene    | 场景编号，两位数字，具体如下：</br>01：贷款申请</br>02：信用卡申请</br>03：开户</br>04：修改密码</br>05：重置密码</br>06：转账</br>07：挂失 / 解挂</br>08：登录</br>09：信息维护 | String     | 2 | 否   |

## 响应参数

| 参数         |     类型   | 说明        |
| ----------- | ---------- | ---------- |
| code       |  String        | 二要素验证结果的返回码</br>0：成功</br>非 0：失败     |
| orderNo    |  String        | 订单号，由合作方上送，每次唯一，此信息为本次二要素验证上送的信息 |
| msg        |  String      | 二要素验证返回结果描述                       |
