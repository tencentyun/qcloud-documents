### 生成签名
-  **前置条件**：按照 **[NONCE ticket 获取](https://cloud.tencent.com/document/product/655/13816)** 进行操作。
-  合作方根据本次身份证识别验证的如下参数生成签名，需要签名的参数信息如下：

  | 参数名      | 说明                                       |
  | -------- | ---------------------------------------- |
  | appId    | 腾讯服务分配的 App ID                           |
  | userId   | 用户唯一标识                                   |
  | version  | 1.0.0                                    |
  | ticket   | 合作伙伴服务端缓存的 tikcet，注意是 NONCE 类型，具体见 [Access Token 获取](https://cloud.tencent.com/document/product/655/13813) |
  | nonceStr | 必须是 32 位随机数                              |

合作方需要生成一个 32 位的随机字符串（字母和数字）nonceStr（登录时也要用到），将 appId、userId、version 连同 ticket、nonceStr 共五个参数的值进行字典序排序。将排序后的所有参数字符串拼接成一个字符串进行 SHA1 编码，编码后的 40 位字符串作为签名（sign）。签名算法可参考 [签名算法说明](https://cloud.tencent.com/document/product/655/13817)。

#### 参考示例

  请求参数：
| 参数名      | 参数值                                      |
| -------- | ---------------------------------------- |
| appId    | TIDA0001                                 |
| userId   | userID19959248596551                     |
| nonceStr | kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T         |
| version  | 1.0.0                                    |
| ticket   | XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMS |

字典排序后的参数为：
```
[1.0.0,TIDA0001,XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMS，kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T, userID19959248596551]
```
拼接后的字符串为：
```
1.0.0TIDA0001XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMSkHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7TuserID19959248596551
```
计算 SHA1 得到签名：
```
4AE72E6FBC2E9E1282922B013D1B4C2CBD38C4BD
```
该字串就是最终生成的签名（40 位），不区分大小写。



下一步：[Android SDK 接入](https://cloud.tencent.com/document/product/655/13847)

​              [iOS SDK 接入](https://cloud.tencent.com/document/product/655/13848)