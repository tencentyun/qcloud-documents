### 生成签名
1.**前置条件**：必须按照[获取NONCE ticket](https://cloud.tencent.com/document/product/295/10136).
2.合作方根据本次人脸验证的如下参数生成签名,需要签名的参数信息如下：

| 参数 | 说明 | 
|---------|---------|
| appId | 腾讯服务分配的app_id |
| userId | 用户唯一标识 |
| version | 1.0.0|
| ticket | 合作伙伴服务端缓存的tikcet,注意是NONCE 类型，具体见[Access Token获取](https://cloud.tencent.com/document/product/295/10118)|
| nonceStr | 必须是32位随机数 |
生成一个 32 位的随机字符串(字母和数字) nonceStr(登录时也要用到)，将appId、userId、version 连同ticket、nonceStr 共五个参数的值进行字典序排序。
1.将排序后的所有参数字符串拼接成一个字符串进行SHA1编码
2.SHA1编码后的40位字符串作为签名(sign)
3.签名算法参考章节7，示例如下：
请求参数：
appId = TIDA0001
userId= userID19959248596551
nonceStr = kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T (必须为32位)
version = 1.0.0
ticket=XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMS

字典排序后的参数为：
[1.0.0, TIDA0001, XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMS ， kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T, userID19959248596551]
拼接后的字符串为：
**1.0.0TIDA0001XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMSkHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7TuserID19959248596551**
计算 SHA1 得到签名：
4AE72E6FBC2E9E1282922B013D1B4C2CBD38C4BD
该字串就是最终生成的签名(40位)，不区分大小写。
