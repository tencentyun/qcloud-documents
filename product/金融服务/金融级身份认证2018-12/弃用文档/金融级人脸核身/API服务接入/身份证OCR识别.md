### 1.合作方生成签名

1.**前置条件**：必须按照文档[获取SIGN ticket](https://cloud.tencent.com/document/product/295/10118#1..E6.B3.A8.E6.84.8F.E4.BA.8B.E9.A1.B9).
2.合作方根据本次OCR识别的如下参数生成签名,需要签名的参数信息如下：


| 参数 | 说明 | 
|---------|---------|
| appId | 腾讯服务分配的app_id | 
| orderNo | 订单号，本次服务上送的订单号，唯一标识。 | 
| nonce | 随机数  32位随机串（字母+数字组成的随机数） | 
| version | 1.0.0 | 
| api ticket | 合作伙伴服务端缓存的tikcet,注意是SIGN 类型，具体见[获取SIGN ticket](https://cloud.tencent.com/document/product/295/10118#1..E6.B3.A8.E6.84.8F.E4.BA.8B.E9.A1.B9) | 

3.生成一个 32 位的随机字符串(字母和数字) nonce(登录时也要用到)，将webankAppId、orderNo,version、连同ticket、nonce 共5个参数的值进行字典序排序。
将排序后的所有参数字符串拼接成一个字符串进行SHA1编码
SHA1编码后的40位字符串作为签名(sign)
示例代码及用法：
请求参数：
webankAppId= appId001
nonce = kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T (必须为32位)
version = 1.0.0
orderNo = aabc1457895464
ticket=01.0.0FxlAe3HFtEy73Um0pJNzIUriwtfnS3KRcPXiesd5ulS4XRAIcT0FbfaP52dwZf5Saabc1457895464appId001

字典排序后的参数为：
[1.0.0, aabc1457895464, appId001, kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T , zxc9Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMS]拼接后的字符串为：
0, 1.0.0, FxlAe3HFtEy73Um0pJNzIUriwtfnS3KRcPXiesd5ulS4XRAIcT0FbfaP52dwZf5S, aabc1457895464, appId001
计算 SHA1 得到签名：
7E0DE0E46500D0327F12ED4274CFA188B80D7AF9
该字串就是最终生成的签名(40位)，不区分大小写。

### 2. 身份证识别API
合作方后台服务上送sign、请求参数到身份证识别后台服务。

请求URL: `https://ida.webank.com/api/paas/ocrapp`
请求方法:POST
请求参数：

| 参数 | 说明 | 类型 |长度  |是否必输 |
|---------|---------|---------|---------|---------|
| webankAppId | WebankAppId，由腾讯指定 | string | 由腾讯指定腾讯服务分配 | 必输 |
| version | 接口版本号 | string | 20 | 必输,默认值：1.0.0 |
| nonce | 随机数  32位随机串（字母+数字组成的随机数） | string | 32 | 必输 |
| sign | 签名:使用上面生成的签名。 | string | 40 | 必输 |
| orderNo | 订单号，由合作方上送，每次唯一 | string | 32 | 必输 |
| cardType | 身份证正反面标识：”0”为人像面，”1”为国徽面 | string | 1 | 必输 |
| idcardStr | 身份证人像面或者国徽面图片的BASE64，大小不超过3M | string | 314528 | 必输 |

返回参数：

| 参数 | 说明 |类型 |
|---------|---------|---------|
| code | 身份证ocr识别结果的返回码，0表示识别成功，其他错误码标识失败。 | 字符串|
| warning | Code=0是有值，姓名和身份证外的非关键信息有误会提示，合作方可以根据warning来确定。Warning明细请查看[身份证识别响应码。](https://cloud.tencent.com/document/product/295/10194#3.-.E8.BA.AB.E4.BB.BD.E8.AF.81.E8.AF.86.E5.88.AB.E5.93.8D.E5.BA.94.E7.A0.81)| 字符串 |
| msgstring |请求结果描述 | 字符串 |
|ocrId|保留字段，内部标识|字符串|
|orderNo|订单号，由合作方上送，每次唯一，此信息为本次身份证ocr识别上送的信息。|字符串|
|name|身份证识别结果：姓名|字符串|
|sex|身份证识别结果：性别|字符串|
|nation|身份证识别结果：民族|字符串|
|birth|身份证识别结果：出生日期|字符串| 
|idcard|身份证识别结果：身份证号|字符串|
|address|身份证识别结果：住址（如果用户没有正确上传身份证反面，则没有该字段）|字符串|
|authority|身份证识别结果：签发机关（如果用户没有正确上传身份证反面，则没有该字段）|字符串|
|validDate|身份证识别结果：有效日期（如果用户没有正确上传身份证反面，则没有该字段）|字符串|
