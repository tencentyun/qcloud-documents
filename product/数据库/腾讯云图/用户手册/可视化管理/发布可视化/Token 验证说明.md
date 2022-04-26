
## 应用场景

• 需要将大屏嵌入到自己网站中，避免他人访问。
• 提供给 A 用户的大屏链接，避免被 B 用户打开。

## 加密方式

• HMAC-SHA256
• BASE64

>?仅限企业版应用此功能。

## 如何接入

### 获取 accessId/token

单击**发布**，记录下 accessId 和 token，具体如下图。
单击**确定**，如果您尝试直接打开您所发布的大屏，会提示：您没有权限访问。

 如果需要打开您的大屏，需要使用 accessId/token 通过加密后生成签名。
![发布窗口](https://qcloudimg.tencent-cloud.cn/raw/3b24a89382757b3e07d4820ff8064ee0.png)

### 加密

#### 签名参数

| 参数名称 | 中文 | 参数值 | 说明 |
| --- | --- | --- | --- |
|accessId|访问 ID|81a663dbaaab055xxxxxxxxxxxxx4a56| 大屏的访问 ID |
|timestamp|当前时间戳|1647247729|返回当前时间的秒数|
|nonce|随机正整数|12979| |
|token|签名密钥|c6v9aw4gpRo1yn6DlIxxxxxxxxxxxxxK| |
|signature|签名结果| |

#### 签名示例

PHP 生成签名示例：

```php
 $accessId = "81a663dbaaab055xxxxxxxxxxxxx4a56";
 $token = "c6v9aw4gpRo1yn6DlIxxxxxxxxxxxxxK";
 $timestamp = time();
 $nonce = rand(10000, 99999);
 $signStr = $accessId . ',' . $timestamp . ',' . $nonce;
 $signRet = urlencode(base64_encode(hash_hmac('sha256', $signSt
r, $token, true))); // 下面生成的 url 用于访问大屏
 $url = 'https://v.yuntus.com/tcv/' . $accessId . '?signature=' . $signRet . '&timestamp=' . $timestamp . '&nonce=' . $nonce);
```

Python 生成签名示例：

```python
import time
import random
import hmac
import base64
from hashlib import sha256
from urllib import parse

accessId = '81a663dbaaab055xxxxxxxxxxxxx4a56'
token = 'c6v9aw4gpRo1yn6DlIxxxxxxxxxxxxxK'
timestamp = str(int(time.time()))
nonce = str(random.randint(10000, 99999))
signStr = accessId + "," + timestamp + "," + nonce
signRet = parse.quote(base64.b64encode(hmac.new(token.encode('utf-8'), signStr.encode('utf-8'), digestmod=sha256).digest()))
url = 'https://v.yuntus.com/tcv/' + accessId + '?signature=' + signRet + '&timestamp=' + timestamp + '&nonce=' + nonce
```

NodeJS 生成签名示例：

```JavaScript
 const crypto = require('crypto');
 const accessId = "81a663dbaaab055xxxxxxxxxxxxx4a56";
 const token = "c6v9aw4gpRo1yn6DlIxxxxxxxxxxxxxK";
 const timestamp = parseInt(Date.now() / 1000);
 const nonce = parseInt(Math.random() * 100000, 10);
 const signStr = accessId + ',' + timestamp + ',' + nonce;
 const signRet = encodeURIComponent(crypto.createHmac('sha256', token).update(signStr).digest().toString('base64')); // 下面生成的 url 用于访问大屏
 const url = 'https://v.yuntus.com/tcv/' + accessId + '?signature='+ signRet + '&timestamp=' + timestamp + '&nonce=' + nonce;
```

Java 生成签名示例：

```Java
import java.net.URLEncoder;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;

public class TcvTokenSignClientDemo {
    private final static String CHARSET = "UTF-8";

    public static String sign(String s, String key, String method) throws Exception {
        Mac mac = Mac.getInstance(method);
        SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(CHARSET), mac.getAlgorithm());
        mac.init(secretKeySpec);
        byte[] hash = mac.doFinal(s.getBytes(CHARSET));
        return DatatypeConverter.printBase64Binary(hash);
    }

    public static void main(String[] args) throws Exception {
        String accessId = "";
        String token = "";
        long timestamp = System.currentTimeMillis() / 1000;
        int nonce = (int)(Math.random() * 100000);
        String signStr = accessId + "," + timestamp + "," + nonce;
        String signRet = URLEncoder.encode(sign(signStr, token, "HmacSHA256"), CHARSET);
        String url = "https://v.yuntus.com/tcv/" + accessId + "?signature=" + signRet + "&timestamp=" + timestamp + "&nonce=" + nonce;
        System.out.println(url);
    }
}
```

### 生成地址说明

![访问地址](https://qcloudimg.tencent-cloud.cn/raw/345b4275c8b6596964c49c25acb82a33.png)

### 安全校验策略说明

链接校验具备时效性，生成链接 1 分钟内校验有效，在此时间内校验通过，之后连续访问时间间隔可通过验证有效期进行配置，如设置为 24 小时，则有效期在 24 小时之后会失效。

![验证有效期](https://qcloudimg.tencent-cloud.cn/raw/37a1ed5be535727a8931cb765be69664.png)
