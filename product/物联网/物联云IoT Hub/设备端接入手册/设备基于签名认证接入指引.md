MQTT 协议支持通过设备证书和密钥签名两种方式接入物联网通信平台，您可以根据实际的业务场景选择接入方式。

物联网平台支持 HMAC-SHA256， HMAC-SHA1 等方式生成摘要签名。通过签名方式接入物联云平台的流程如下：
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)。
2. 注册设备，并获取设备密钥。
3. 按照物联网通信约束生成 username 字段， username 字段格式如下：
```
 productid;devicename;sdkappid;connid;过期时间
```
 
 
其中各字段含义如下：

| 字段          | 含义                                       |
| ----------- | ---------------------------------------- |
| productid | 产品 ID                                    |
| devicename | 设备名称                                     |
| sdkappid   | 固定填12010126                             |
| connid    | 一个随机字符串                                  |
| 过期时间       | 表示签名的有效期, 从1970年1月1日 00:00:00 UTC 时间至今秒数的 UTF8 字符串 |

4. 使用 Base64 对设备私钥进行解码，并记录解码生成的原始密钥 raw_key。
5. 用步骤三生成的 raw_key，通过 HMAC-SHA1 或者 HMAC-SHA256 算法对 username 生成一串摘要，该摘要简称为 token。
6. 按照物联网通信约束生成 password 字段， password 字段格式为：
```
token;hmac签名方法
```

 其中 hmac 签名方法字段填写第三步用到的摘要算法，可选的值有 hmacsha256 和 hmacsha1
 例如，用户生成签名，其 Python 代码示例如下：
 ```
 #!/bin/env python
    
    import base64
    import hashlib
    import hmac
    import random
    import string
    import time
    
    # 生成指定长度的随机字符串
    def RandomConnid(length):
            return  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    
    # 生成接入物联云需要的各参数
    def IotHmac(productid, devicename, devicekey):
    
            # 1. 生成connid为一个随机字符串,方便后台定位问题
            connid   = RandomConnid(5)
    
            # 2. 生成过期时间,表示签名的过期时间,从纪元1970年1月1日 00:00:00 UTC 时间至今秒数的 UTF8 字符串
            expiry   = int(time.time()) + 60 * 60 
    
            # 3. 生成MQTT的clientid部分
            clientid = "{}{}".format(pid, dname):
    
            # 4. 生成mqtt的username部分
            username = "{};12010126;{};{}".format(clientid, connid, expiry)
    
            # 5. 对username进行签名,生成token
            token = hmac.new(devicekey.decode("base64"), username, digestmod=hashlib.sha256).hexdigest()
    
            # 6. 根据物联云通信平台规则生成password字段
            password = "{};{}".format(token, "hmacsha256")
    
            return {
                "clientid" : clientid,
                "username" : username,
                "password" : password
            }
  ```

   


7. 将步骤六将上面生成的 possword 字段填入 mqtt connect 报文中，即可完成接入。
 - 将 clientid 填入到 mqtt 的 clientid 字段；
 - 将 username 填入到 mqtt 的 username 字段；
 - 将 password 填入到 mqtt 的 password 字段，

>!通过 psk 方式接入端口是`1883`。
