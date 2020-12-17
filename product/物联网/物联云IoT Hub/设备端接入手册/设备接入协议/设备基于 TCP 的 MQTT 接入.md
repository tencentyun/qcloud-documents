## MQTT 协议说明

目前物联网通信支持 MQTT 标准协议接入(兼容3.1.1版本协议)，具体的协议请参见 [MQTT 3.1.1](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html) 协议文档。

### 和标准 MQTT 区别

1. 支持 MQTT 的 PUB、SUB、PING、PONG、CONNECT、DISCONNECT、UNSUB 等报文。
2. 支持 cleanSession。
3. 不支持 will、retain msg。
4. 不支持 QOS2。

### MQTT 通道，安全等级

支持 TLSV1，TLSV1.1，TLSV1.2 版本的协议来建立安全连接，安全级别高。

### TOPIC 规范

默认情况下创建产品后，该产品下的所有设备都拥有以下 topic 类的权限：

1. `${productId}/${deviceName}/control`订阅。
2. `${productId}/${deviceName}/event`发布。
3. `${productId}/${deviceName}/data`订阅和发布。
4. `$shadow/operation/${productId}/${deviceName}`发布。通过包体内部 type 来区分：update/get，分别对应设备影子文档的更新和拉取等操作。
5. `$shadow/operation/result/${productId}/${deviceName}`订阅。通过包体内部 type 来区分：update/get/delta，type 为 update/get 分别对应设备影子文档的更新和拉取等操作的结果；当用户通过 restAPI 修改设备影子文档后，服务端将通过该 topic 发布消息，其中 type 为 delta。
6. `$ota/report/${productID}/${deviceName}`发布。设备上报版本号及下载、升级进度到云端。
7. `$ota/update/${productID}/${deviceName}`订阅。设备接收云端的升级消息。

## MQTT 接入

MQTT 协议支持通过设备证书和密钥签名两种方式接入物联网通信平台，您可根据自己的场景选择一种方式接入即可。接入参数如下所示：

| 接入认证方式 | 连接域名及端口                                               | Connect报文参数                                              |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 证书认证     | MQTT 服务器连接地址，广州域设备填入：${ProductId}.iotcloud.tencentdevices.com，这里 ${ProductId} 为变量参数，用户需填入创建产品时自动生成的产品 ID，例如 1A17RZR3XX.iotcloud.tencentdevices.com；端口：8883 | <li> KeepAlive：保持连接的时间，取值范围为0 - 900s。若超过1.5倍 KeepAlive 时长物联网平台仍没收到客户端的数据，则平台将断开与客户端的连接；<br><li> ClientId：${ProductId}${DeviceName}，产品 ID 和设备名的组合字符串；<br><li>UserName：${productid}${devicename};${sdkappid};${connid};${expiry}，详情见下文中基于 MQTT 的签名认证接入指引 username 部分；<br><li>PassWord：密码（可赋任意值）。 |
| 密钥认证     | MQTT 服务器连接地址与证书认证一致；端口：1883                | <li>KeepAlive：保持连接的时间，取值范围为0-900s；<br><li>ClientId:${ProductId}${DeviceName}；<br><li>UserName：${productid}${devicename};${sdkappid};${connid};${expiry}，详情见下文中基于 MQTT 的签名认证接入指引 username 部分；<br><li>PassWord：密码，详情见下文中基于 MQTT 的签名认证接入指引 password 部分。 |

> ?采用证书认证的设备接入时不会对填写的 PassWord 部分进行验证，证书认证时 PassWord 部分可填写任意值。

### 证书认证设备接入指引

物联网平台采用 TLS 加密方式来保障设备传输数据时的安全性。证书设备接入时，获取到证书设备的证书、私钥与 CA 证书文件之后，设置好 KeepAlive，ClientId，UserName，PassWord 等内容（采用腾讯云设备端 SDK 方式接入的设备无需设置，SDK 可根据设备信息自动生成）。设备向证书认证对应的 URL 上传认证文件，通过之后发送 MqttConnect 消息即可完成证书设备基于 TCP 的 MQTT 接入。

### 密钥认证设备接入指引

物联网平台支持 HMAC-SHA256，HMAC-SHA1 等方式基于设备密钥生成摘要签名。通过签名方式接入物联云平台的流程如下：

1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)。您可在控制台创建产品、添加设备、并获取设备密钥。
2. 按照物联网通信约束生成 username 字段，username 字段格式如下：
```plaintext
username 字段的格式为：
${productid}${devicename};${sdkappid};${connid};${expiry}
注意：${} 表示变量，并非特定的拼接符号。
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
```plaintext
password 字段格式为： 
${token};hmac 签名方法
其中 hmac 签名方法字段填写第三步用到的摘要算法，可选的值有 hmacsha256 和 hmacsha1。
```
作为对照，用户生成签名的 Python、Java 代码示例如下；
Python 代码为：
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
# 生成接入物联网通信平台需要的各参数
def IotHmac(productID, devicename, devicePsk):
        # 1. 生成 connid 为一个随机字符串，方便后台定位问题
        connid   = RandomConnid(5)
        # 2. 生成过期时间，表示签名的过期时间,从纪元1970年1月1日 00:00:00 UTC 时间至今秒数的 UTF8 字符串
        expiry   = int(time.time()) + 60 * 60
        # 3. 生成 MQTT 的 clientid 部分, 格式为 ${productid}${devicename}
        clientid = "{}{}".format(productID, devicename)
        # 4. 生成 MQTT 的 username 部分, 格式为 ${clientid};${sdkappid};${connid};${expiry}
        username = "{};12010126;{};{}".format(clientid, connid, expiry)
        # 5. 对 username 进行签名，生成token
        token = hmac.new(devicePsk.decode("base64"), username, digestmod=hashlib.sha256).hexdigest()
        # 6. 根据物联网通信平台规则生成 password 字段
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
Java代码为：
```
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.util.*;
public class IotHmac {
 public static void main(String[] args) throws Exception {
System.out.println(IotHmac("YOUR_PRODUCTID","YOUR_DEVICENAME","YOUR_PSK"));
}
public static Map<String, String> IotHmac(String productID, String devicename, String 
devicePsk) throws Exception {
					final Base64.Decoder decoder = Base64.getDecoder();
			//1. 生成 connid 为一个随机字符串，方便后台定位问题
			String connid = HMACSHA256.getRandomString2(5);
			//2. 生成过期时间，表示签名的过期时间,从纪元1970年1月1日 00:00:00 UTC 时间至今秒数的 UTF8 字符串
			Long expiry = Calendar.getInstance().getTimeInMillis()/1000 +600;
			//3. 生成 MQTT 的 clientid 部分, 格式为 ${productid}${devicename}
			String clientid = productID+devicename;
			//4. 生成 MQTT 的 username 部分, 格式为 ${clientid};${sdkappid};${connid};${expiry}
			String username = clientid+";"+"12010126;"+connid+";"+expiry;
			//5.  对 username 进行签名，生成token、根据物联网通信平台规则生成 password 字段
			String password = HMACSHA256.getSignature(username.getBytes(), decoder.decode(devicePsk)) + ";hmacsha256";
			Map<String,String> map = new HashMap<>();
			map.put("clientid",clientid);
			map.put("username",username);
			map.put("password",password);
			return map;
		}
		public static class HMACSHA256 {
			private static final String HMAC_SHA256 = "HmacSHA256";
			/**
			 * 生成签名数据
			 *
			 * @param data 待加密的数据
			 * @param key  加密使用的key
			 * @return 生成16进制编码的字符串
			 */
			public static String getSignature(byte[] data, byte[] key)  {
					try {
							SecretKeySpec signingKey = new SecretKeySpec(key, HMAC_SHA256);
							Mac mac = Mac.getInstance(HMAC_SHA256);
							mac.init(signingKey);
							byte[] rawHmac = mac.doFinal(data);
							return bytesToHexString(rawHmac);
					}catch (Exception e) {
							e.printStackTrace();
					}
					return null;
			}
        /**
         * byte[]数组转换为16进制的字符串
         *
         * @param bytes 要转换的字节数组
         * @return 转换后的结果
         */
        private static String bytesToHexString(byte[] bytes) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < bytes.length; i++) {
                String hex = Integer.toHexString(0xFF & bytes[i]);
                if (hex.length() == 1) {
                    sb.append('0');
                }
                sb.append(hex);
            }
            return sb.toString();
        }
        public static String getRandomString2(int length) {
            Random random = new Random();
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < length; i++) {
                int number = random.nextInt(3);
                long result = 0;
                switch (number) {
                    case 0:
                        result = Math.round(Math.random() * 25 + 65);
                        sb.append(String.valueOf((char) result));
                        break;
                    case 1:
                        result = Math.round(Math.random() * 25 + 97);
                        sb.append(String.valueOf((char) result));
                        break;
                    case 2:
                        sb.append(String.valueOf(new Random().nextInt(10)));
                        break;
                }
            }
            return sb.toString();
        }
    }
}
```
6. 最终将上面生成的参数填入对应的MQTT connect 报文中。
7. 将 clientid 填入到 MQTT 协议的 clientid 字段。
8. 将 username 填入到 MQTT 的 username 字段。
9. 将 password 填入到 MQTT 的 password 字段，向密钥认证的域名与端口处发送MqttConnect信息即可接入到物联云通信平台。

