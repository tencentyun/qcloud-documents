本文主要介绍移动推送 TPNS  Basic Auth 的鉴权认证方法。

采用 AccessId 和 SecretKey 进行 Basic Auth 认证鉴权，密钥容易被获取，安全性不高，推荐使用 [签名认证](https://cloud.tencent.com/document/product/548/41046)。



## 获取密钥
1. 登录 [移动推送 TPNS 控制台](https://console.cloud.tencent.com/tpns)，选择左侧菜单**配置管理 > 基础配置**。
2. 在应用信息一栏中，获取应用`Access ID` 和`SECRET KEY`（仅主账号可见）。


## 生成签名
1. **拼接请求字符串** 
此步骤生成请求字符串。
生成算法为：`base64(Access ID:SECRETKEY)`，即对`Access ID`加上冒号，加上`SECRETKEY`拼装起来的字符串，再做`base64`转换。
示例如下：
```
base64(150000****:cf43dac624820*****c1fe5fc993)
```

2. **进行 Basic Auth 认证鉴权**
 采用基础鉴权的方式，在 HTTP Header（头）里加一个字段（ Key/Value 对）：
  ```
  Authorization: Basic base64_auth_string
  ```
示例如下：
```
Authorization:Basic base64(150000****:cf43dac624820*****c1fe5fc993)
```
