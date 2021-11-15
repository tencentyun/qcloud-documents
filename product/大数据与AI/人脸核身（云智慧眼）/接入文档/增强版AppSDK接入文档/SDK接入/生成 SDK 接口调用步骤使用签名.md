### 准备步骤
- 前置条件：请合作方确保 NONCE  ticket 已经正常获取，获取方式见   [NONCE ticket 获取](https://cloud.tencent.com/document/product/1007/57614)。
-  NONCE 类型的 ticket，其有效期为120秒，且一次性有效，即每次启动 SDK 刷脸都要重新请求 NONCE ticket，重新算 sign。同时建议合作方做前端保护，防止用户连续点击，短时间内频繁启动 SDK。
- 合作方为人脸核身服务生成签名，需要具有以下参数：

| 参数名 | 说明 | 来源 |
|---------|---------|---------|
| wbappId | 业务流程唯一标识 | 参考 [获取 WBappid](https://cloud.tencent.com/document/product/1007/49634) 指引在人脸核身控制台内申请 | 
| userId | 用户唯一标识 | 合作方自行分配（和 SDK 里面定义的 userId 保持一致） | 
| version | 参数值为：1.0.0 | - |
| ticket | 合作伙伴服务端获取的 ticket，注意是 NONCE 类型 | 获取方式见 [NONCE ticket 获取](https://cloud.tencent.com/document/product/1007/57614) |
| nonce | 必须是32位随机数 | 合作方自行生成（和 SDK 里面定义的随机数保持一致） | 

>!签名的数据需要和使用该签名的 SDK 中的请求参数保持一致。

### 基本步骤
1. 生成一个 32 位的随机字符串 nonce（其为字母和数字，登录时也要用到）。
2. 将 wbappId、userId、version 连同 ticket、nonce 共五个参数的值进行字典序排序。
3. 将排序后的所有参数字符串拼接成一个字符串。
4. 将排序后的字符串进行 SHA1 编码，编码后的 40 位字符串作为签名（sign）。

>!签名算法可参考 签名算法说明 。

### 参考示例
- **请求参数：**

|参数名|	参数值|
|---------|---------|
|appId	|IDAXXXXX|
|userId	|userID19959248596551|
|nonce|	kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T|
|version	|1.0.0|
|ticket	|XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMS|

 - 字典排序后的参数为：
```
[1.0.0, IDAXXXXX, XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMS ， kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T, userID19959248596551]
```

- 拼接后的字符串为：
```
1.0.0IDAXXXXXXO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMSkHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7TuserID19959248596551
```

- 计算 SHA1 得到签名：
```
D7606F1741DDCF90757DA924EDCF152A200AC7F0
该字符串就是最终生成的签名（40 位），不区分大小写。
```
