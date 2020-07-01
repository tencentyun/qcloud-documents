## MQTT 协议说明

目前物联网通信支持 MQTT 标准协议接入(兼容3.1.1版本协议)，具体的协议请参考 [MQTT 3.1.1](http://mqtt.org/?spm=5176.doc30540.2.3.BU9nwt) 协议文档。

### 和标准 MQTT 区别
1. 支持 MQTT 的 PUB、SUB、PING、PONG、CONNECT、DISCONNECT、UNSUB 等报文。
2. 支持 cleanSession。
3. 不支持 will、retain msg。
4. 不支持 QOS2。

### MQTT 通道，安全等级
支持 TLSV1, TLSV1.1，TLSV1.2 版本的协议来建立安全连接，安全级别高。

### TOPIC 规范
默认情况下创建产品后，该产品下的所有设备都拥有以下 topic 类的权限：
1. `${productId}/${deviceName}/control` 订阅。
2. `${productId}/${deviceName}/event` 发布。
3. `$shadow/operation/${productId}/${deviceName}` 发布。通过包体内部 type 来区分：update/get，分别对应设备影子文档的更新和拉取等操作。
4. `$shadow/operation/result/${productId}/${deviceName}` 订阅。通过包体内部 type 来区分：update/get/delta，type 为 update/get 分别对应设备影子文档的更新和拉取等操作的结果；当用户通过 restAPI 修改设备影子文档后，服务端将通过该 topic 发布消息，其中 type 为 delta。


## 基于 MQTT 的签名认证接入指引
MQTT 协议支持通过设备证书和密钥签名两种方式接入物联网通信平台，您可根据自己的场景选择一种方式接入即可。

### 操作步骤
物联网平台支持 HMAC-SHA256，HMAC-SHA1 等方式生成摘要签名。通过签名方式接入物联云平台的流程如下：
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)。您可在控制台创建产品、添加设备、并获取设备密钥。
2. 按照物联网通信约束生成 username 字段，username 字段格式如下：
```
username字段的格式为：
    ${productid}${devicename};${sdkappid};${connid};${expiry}
注意：${}表示变量，并非特定的拼接符号。
```
其中各字段含义如下：
 - productid：产品 ID。
 - devicename： 设备名称。
 - sdkappid：固定填12010126。
 - connid ：一个随机字符串。
 - expiry ：表示签名的有效期， 从1970年1月1日00:00:00 UTC 时间至今秒数的 UTF8 字符串。
3. 用 base64 对设备私钥进行解码得到原始密钥 raw_key。
4. 用第3步生成的 raw_key，通过 HMAC-SHA1 或者 HMAC-SHA256 算法对 username 生成一串摘要，简称 token。
5. 按照物联网通信约束生成 password 字段，password 字段格式为：
```
password字段格式为： 
    ${token};hmac签名方法
其中hmac签名方法字段填写第三步用到的摘要算法，可选的值有 hmacsha256 和 hmacsha1。
```
作为对照，用户生成签名的 Python 代码为：
```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
import hashlib
import hmac
import random
import string
import time
import sys
# 生成指定长度的随机字符串
def RandomConnid(length):
        return  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
# 生成接入物联云需要的各参数
def IotHmac(productID, devicename, devicePsk):
        # 1. 生成connid为一个随机字符串,方便后台定位问题
        connid   = RandomConnid(5)
        # 2. 生成过期时间,表示签名的过期时间,从纪元1970年1月1日 00:00:00 UTC 时间至今秒数的 UTF8 字符串
        expiry   = int(time.time()) + 60 * 60
        # 3. 生成MQTT的clientid部分, 格式为${productid}${devicename}
        clientid = "{}{}".format(productID, devicename)
        # 4. 生成mqtt的username部分, 格式为${clientid};${sdkappid};${connid};${expiry}
        username = "{};12010126;{};{}".format(clientid, connid, expiry)
        # 5. 对username进行签名,生成token
        token = hmac.new(devicePsk.decode("base64"), username, digestmod=hashlib.sha256).hexdigest()
        # 6. 根据物联云通信平台规则生成password字段
        password = "{};{}".format(token, "hmacsha256")
        return {
            "clientid" : clientid,
            "username" : username,
            "password" : password
        }
if __name__ == '__main__':
    print IotHmac(sys.argv[1], sys.argv[2], sys.argv[3])
```
将上述代码保存到 IotHmac.py，执行下面的命令即可（Python2.7 版本）。这里 "YOUR_PRODUCTID"、 "YOUR_DEVICENAME" 和"YOUR_PSK" 是填写您实际创建设备的产品 ID、设备名称和设备密钥。
```
python IotHmac.py "YOUR_PRODUCTID" "YOUR_DEVICENAME" "YOUR_PSK" 
```
6. 最终将上面生成的参数填入对应的 mqtt connect 报文中。
 1. 将 clientid 填入到 MQTT 协议的 clientid 字段。
 2. 将 username 填入到 mqtt 的 username 字段。
 3. 将 password 填入到 mqtt 的 password 字段，即可接入到物联云通信平台。


>!
- 通过 psk 方式接入端口默认为`1883`。若客户端支持 ca 证书，您也可以使用`8883`端口接入。  
- MQTT 连接服务器地址请参见 [MQTT.fx 接入指南-参数说明部分](https://cloud.tencent.com/document/product/634/14630#.E5.8F.82.E6.95.B0.E8.AF.B4.E6.98.8E)。


