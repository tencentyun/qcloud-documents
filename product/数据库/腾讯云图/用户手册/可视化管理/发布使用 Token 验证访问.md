
## 应用场景 
• 需要将大屏嵌入到自己网站中，避免他人提取自行打开。
• 提供给 A 用户的大屏链接，避免被 B 用户打开。

## 加密方式 
• HMAC-SHA256
• BASE64

## 如何接入
### 获取 accessId/token
单击**发布**，记录下 accessId 和 token，具体如下图。
单击**确定**，如果您尝试直接打开您所发布的大屏，会提示：您没有权限访问。
 
 如果需要打开您的大屏，需要使用 accessId/token 通过加密后生成签名。
![](https://main.qcloudimg.com/raw/fac711403227883d9b1813bb98ad346e.png)

### 加密
PHP 生成签名示例：
```
 $accessId = "81a663dbaaab055xxxxxxxxxxxxx4a56";
 $token = "c6v9aw4gpRo1yn6DlIxxxxxxxxxxxxxK";
 $timestamp = time();
 $nonce = rand(10000, 99999);
 $signStr = $accessId . ',' . $timestamp . ',' . $nonce;
 $signRet = urlencode(base64_encode(hash_hmac('sha256', $signSt
r, $token, true))); // 下面生成的 url 用于访问大屏
 $url = 'http://v.yuntus.com/cloudv/' . $accessId . '?signature=' . $signRet . '&timestamp=' . $timestamp . '&nonce=' . $nonce);
```

NodeJS 生成签名示例：
```
 const crypto = require('crypto');
 const accessId = "81a663dbaaab055xxxxxxxxxxxxx4a56";
 const token = "c6v9aw4gpRo1yn6DlIxxxxxxxxxxxxxK";
 const timestamp = parseInt(Date.now() / 1000);
 const nonce = parseInt(Math.random() * 100000, 10);
 const signStr = accessId + ',' + timestamp + ',' + nonce;
 const signRet = encodeURIComponent(crypto.createHmac('sha256', token).update(signStr).digest().toString('base64')); // 下面生成的 url 用于访问大屏
 const url = 'http://v.yuntus.com/cloudv/' + accessId + '?signature='+ signRet + '&timestamp=' + timestamp + '&nonce=' + nonce;
```

Java 生成签名示例：
```
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

### 安全校验策略说明
链接校验具备时效性，生成链接1分钟内校验有效，在此时间内校验通过，之后连续访问时间间隔超过12小时则会失效。

