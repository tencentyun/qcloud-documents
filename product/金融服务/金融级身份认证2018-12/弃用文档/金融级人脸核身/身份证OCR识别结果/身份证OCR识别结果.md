### 1. 前端获取结果验证签名
为了确保前端SDK的结果真实性且未被篡改，合作伙伴服务端可以验证结果，
1.合作伙伴APP端身份证OCR识别SDK返回的带签名结果。
2.合作伙伴APP端调用其服务端接口进行签名认证，接口认证成功后继续业务流程。

#### 1.1 合作方后台生成签名
合作方根据本次人脸验证的如下参数生成签名：


| 参数 | 说明 | 
|---------|---------|
| app_id | 腾讯服务分配的app_id | 
| order_no | 订单号，本次人脸验证合作伙伴上送的订单号，唯一标识。 | 
| api ticket | 合作伙伴服务端缓存的tikcet,注意是sign 类型 | 
将app_id、order_no、连同ticket(SIGN)共三个参数的值进行字典序排序
将排序后的所有参数字符串拼接成一个字符串进行SHA1编码
SHA1编码后的40位字符串作为签名(**sign**)
示例代码及用法
示例：
请求参数：
app_id = appId001
order_no= userID19959248596551
ticket= duSz9ptwyW1Xn7r6gYItxz3feMdJ8Na5x7JZuoxurE7RcI5TdwCE4KT2eEeNNDoe

字典排序后的参数为：
[appId001, duSz9ptwyW1Xn7r6gYItxz3feMdJ8Na5x7JZuoxurE7RcI5TdwCE4KT2eEeNNDoe, test1480921551481]
拼接后的字符串为：
appId001duSz9ptwyW1Xn7r6gYItxz3feMdJ8Na5x7JZuoxurE7RcI5TdwCE4KT2eEeNNDoetest1480921551481
计算 SHA1 得到签名：
B02CEBEB07F792B2F085E8CB1E7BA9EC19284F
54
该字串就是最终生成的签名(40位)，不区分大小写。
#### 1.2 比对签名
合作方服务端生成的签名与SDK返回的签名比对，如果相同即可信任SDK的刷脸结果。

注：合作方必须定时刷新ticket(SIGN)保证远程身份认证后台缓存有该合作方的ticket(SIGN)，否则后台无法生成签名值。

### 2.合作伙伴服务端查询结果
合作伙伴服务端生成签名，并调用身份证OCR识别服务端查询结果，鉴权完成后返回结果（服务端上送 order_no和app_id查询）。

#### 2.1 合作方后台生成签名
合作方根据本次人脸验证的如下参数生成签名：

| 参数 | 说明 | 
|---------|---------|
| app_id | 腾讯服务分配的app_id | 
| order_no | 订单号，本次人脸验证合作伙伴上送的订单号，唯一标识。 | 
| version | 默认值：1.0.0 | 
| api ticket | 合作伙伴服务端缓存的tikcet,注意是sign 类型，具体见6.1获取规则 | 
| nonceStr | 32位随机字符串,字母和数字 | 

生成一个 32 位的随机字符串(字母和数字) nonceStr，将app_id、order_no、version 连同ticket、nonceStr 共五个参数的值进行字典序排序再SHA1编码生成签名。具体签名算法见章节7。

#### 2.2 身份证OCR识别结果查询接口
请求URL：https://idasc.webank.com/api/server/getOcrResult
请求方法:GET
请求参数：

| 标题1 | 标题2 | 标题3 |标题3 |标题3 |
|---------|---------|---------|---------|---------|
| app_id | 腾讯服务分配的app_id | 字符串 |腾讯服务分配 |必输，腾讯服务分配的app_id |
| order_no | 订单号 | 字符串 |32 |必输，合作方订单的唯一标识 |
| get_file | 是否需要获取身份证OCR图片文件 | 字符串 |1 |非必输，值为1则返回文件；其他则不返回。 |
| nonce | 随机数 | 字符串 |32 |必输 |
| version | 版本号 | 字符串 |20 |必输，默认值：1.0.0 |
| sign | 签名值 | 字符串 |40 |必输，使用上面生成的签名。 |

请求示例：
https://idasc.webank.com/api/server/getOcrResult?app_id=xxx&nonce=xxx&order_no=xxx&version=1.0.0&sign=xxx&get_file=xxxx

返回参数：

| 参数 | 类型 | 说明 |
|---------|---------|---------|
| frontCode | string | “0”说明人像面识别成功 |
| backCode | string | “0”说明国徽面识别成功 |
| orderNo | string | 订单编号 |
| Name | string | frontCode为0返回:证件姓名 |
| Sex | string | frontCode为0返回:性别 |
| Nation | string | frontCode为0返回:民族 |
| Birth | string | frontCode为0返回:出生日期 |
| Address | string | frontCode为0返回:地址 |
| Idcard | string | frontCode为0返回:身份证号 |
| validate | string | backCode为0返回:证件的有效期 |
| Authority | string | backCode为0返回:发证机关 |
| frontPhoto | Base 64 string | 人像面照片，转换后为JPG格式 |
| backPhoto | Base 64 string | 国徽面照片，转换后为JPG格式 |
| operateTime | string | 做OCR的操作时间 |

**注意：**
1)身份证照片信息作为存证，合作伙伴可以通过此接口拉取识别结果和文件，需要注意请求参数的get_file需要设置为1；如果不上送参数或者参数为空，默认不返回照片信息。
2)照片均为base64位编码，其中照片解码后格式一般为jpg。
