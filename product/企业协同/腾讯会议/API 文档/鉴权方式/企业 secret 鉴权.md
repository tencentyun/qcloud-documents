REST API 对每个访问请求进行身份验证。没有安全凭证和签名无法调用 API 接口。用户可以参考腾讯云 API 的鉴权规则。

API 调用方需申请或持有安全凭证。安全凭证包括 SecretId 和 SecretKey。
- SecretId：用于表示 API 调用者身份。
- SecretKey：用于加密签名字符串和服务器端验证签名字符串的密钥。


## 公共参数
公共参数是用于标识用户和接口鉴权目的的参数，如非必要，在每个接口单独的接口文档中不再对这些参数进行说明，但每次请求均需要携带这些参数，才能正常发起请求。
API 采用 TC3-HMAC-SHA256 签名方法，公共参数需要统一放到 HTTP Header 请求头部中。


|参数名称 | 类型 | 必选 | 描述 |
|---------|---------|---------|---------|
| X-TC-Action | String| 否 |操作的接口名称。取值参考接口文档中输入参数公共参数 Action 的说明。例如云服务器的查询实例列表接口，取值为 DescribeInstances。 |
| X-TC-Region | String| 否 |地域参数，用来标识希望操作哪个地域的数据。接口接受的地域取值参考接口文档中输入参数公共参数 Region 的说明。注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。 |
| X-TC-Key | String| 是 |此参数参与签名计算。腾讯云 API 接入，申请的安全凭证密钥对中的 SecretId，其 secretkey 用于签名。企业管理员可以登录 [腾讯会议官网](https://meeting.tencent.com/)，在【企业管理】>【高级】>【restApi】中进行查看。 |
| X-TC-Timestamp | Integer| 是 |此参数参与签名计算。当前 UNIX 时间戳，可记录发起 API 请求的时间。例如1529223702，单位为秒。注意：如果与服务器时间相差超过5分钟，会引起签名过期错误。 |
| X-TC-Nonce | Integer| 是 |此参数参与签名计算。随机正整数。 |
| X-TC-Version | String|否 |应用 App 的版本号，建议设置，以便灰度和查找问题。 |
| X-TC-Signature | String|是 |放置由下面的签名方法产生的签名。 |
|X-TC-Token | String|否 |临时证书所用的 Token ，需要结合临时密钥一起使用。临时密钥和 Token 需要到访问管理服务调用接口获取。长期密钥不需要 Token。 |
|AppId | String|是 |腾讯会议分配给三方开发应用的 App ID。企业管理员可以登录 [腾讯会议官网](https://meeting.tencent.com/)，在【企业管理】>【高级】>【restApi】中进行查看。 |
|SdkId | String|否 |用户子账号或开发的应用 ID，未分配可不填。企业管理员可以登录 [腾讯会议官网](https://meeting.tencent.com/)，在【企业管理】>【高级】>【restApi】中进行查看。 |
|X-TC-Registered|Integer|否|非必填字段，表示是否启用了腾讯会议的企业用户管理功能。<br>请求头不带该字段或者该字段值为0，表示未启用企业用户管理功能。用户使用未注册的 userid 创建的会议，在会议客户端中无法看到会议列表，可以正常使用会议短链接或会议号加入会议。<br>以下两种场景，请求头必须带该字段且值为1<li>企业用户通过 SSO 接入了腾讯会议账号体系<li>企业用户通过腾讯会议企业用户管理创建用户|


## 生成签名串
参与签名的字符串包括：

>!此处为伪代码，拷贝粘贴不保证可编译运行。

```plaintext
String stringToSign=
HTTPMethod + "\n" +    //POST, GET
Headers + "\n" +       //指定的Header参数
URI + "\n" +           //eg: https://api.meeting.qq.com/v1/meetings, URI=/v1/meetings
Params                 // Http请求的Body, 如果Body为空(如HTTP GET方法), 请使用用空串("").
```
Header 中参与签名的字段包含：X-TC-Nonce，X-TC-Timestamp，X-TC-Key。 组成 Header 签名串时，参与签名的参数按参数名做字典序升序排列。X-TC-Signaure 为计算后的签名字段，不参与签名计算。标准的 HTTP Header 非空参数本手册约定不参与签名计算。

如果是带有查询参数的请求，URI 含所有的查询串，例如：查询会议请求
>!此处为伪代码，拷贝粘贴不保证可编译运行。

```plaintext
GET https://api.meeting.qq.com/v1/meetings/7567173273889276131?userid=tester1&instanceid=1

URI为“/v1/meetings/7567173273889276131?userid=tester1&instanceid=1“
```



例如，取消会议的 HTTP POST 请求示例：
>!此处为伪代码，拷贝粘贴不保证可编译运行。


```plaintext
POST http://api.meeting.qq.com/v1/meetings/7567454748865986567/cancel
X-TC-Key: AKID********************EXAMPLE
X-TC-Timestamp：1572168600
X-TC-Nonce：88080
content-type:application/json
AppId:1234567890

{
  "userid" : "test1",
  "instanceid" : 1,
  "reason_code" : 1,
  "reason_detail" : "取消会议"
}
```
步骤一：串联 Header 参数
>!此处为伪代码，拷贝粘贴不保证可编译运行。

```plaintext
headerString = "X-TC-Key=" + "AKIDz8krbsJ*********************XAMPLE" + "&X-TC-Nonce=" + 1234567 + "&X-TC-Timestamp=" + 1572168600
```

步骤二：组签名串
>!此处为伪代码，拷贝粘贴不保证可编译运行。

```plaintext
stringToSign = POST + "\n" +
               headerString + "\n" +
               "/v1/meetings/7567454748865986567/cancel" + "\n" +
               "{"userid":"test1","instanceid":1,"reason_code":1,"reason_detail":"取消会议"}"
```

## 计算签名
拼接好待签名的字符串后，用 SecretKey 密钥生成待签名字符串的 Hmac-SHA256 签名，将签名转换为16进制字符串形式，然后进行 Base64 编码。

参考以下 Java 示例代码。


## 传递签名
对每一个 HTTP 请求，都需要将签名放到 Request 的 Header 参数 X-TC-Signature 中去。

## 代码示例
#### Java(Java8) 代码示例
请根据使用的开发语言按此示例代码中的方法签名。
```
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public interface SignatureUtil {


  String HMAC_ALGORITHM = "HmacSHA256";

  char[] HEX_CHAR = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};

  static String bytesToHex(byte[] bytes) {

    char[] buf = new char[bytes.length * 2];
    int index = 0;
    for (byte b : bytes) {
      buf[index++] = HEX_CHAR[b >>> 4 & 0xf];
      buf[index++] = HEX_CHAR[b & 0xf];
    }

    return new String(buf);
  }

  /**
   * 生成签名，开发版本oracle jdk 1.8.0_221
   *
   * @param secretId 邮件下发的secret_id
   * @param secretKey 邮件下发的secret_key
   * @param httpMethod http请求方法 GET/POST/PUT等
   * @param headerNonce X-TC-Nonce请求头，随机数
   * @param headerTimestamp X-TC-Timestamp请求头，当前时间的秒级时间戳
   * @param requestUri 请求uri，eg：/v1/meetings
   * @param requestBody 请求体，没有的设为空串
   * @return 签名，需要设置在请求头X-TC-Signature中
   * @throws NoSuchAlgorithmException e
   * @throws InvalidKeyException e
   */
  static String sign(String secretId, String secretKey, String httpMethod, String headerNonce, String headerTimestamp, String requestUri, String requestBody)
      throws NoSuchAlgorithmException, InvalidKeyException {

    String tobeSig =
        httpMethod + "\nX-TC-Key=" + secretId + "&X-TC-Nonce=" + headerNonce + "&X-TC-Timestamp=" + headerTimestamp + "\n" + requestUri + "\n" + requestBody;
    Mac mac = Mac.getInstance(HMAC_ALGORITHM);
    SecretKeySpec secretKeySpec = new SecretKeySpec(secretKey.getBytes(StandardCharsets.UTF_8), mac.getAlgorithm());
    mac.init(secretKeySpec);
    byte[] hash = mac.doFinal(tobeSig.getBytes(StandardCharsets.UTF_8));
    String hexHash = bytesToHex(hash);
    return new String(Base64.getEncoder().encode(hexHash.getBytes(StandardCharsets.UTF_8)));
  }
}

```
#### PHP 代码示例

```
class SignatureUtil
{
    private static $secret_id = '';  // SecretId
    private static $secret_key = ''; // SecretKey

    public static function setSecretIdAndKey($secret_id, $secret_key)
    {
        self::$secret_id = $secret_id;
        self::$secret_key = $secret_key;
    }

    public static function getSecretId()
    {
        return self::$secret_id;
    }

    /**
     * @param $header = [
     * 'X-TC-Nonce' => '',  // X-TC-Nonce请求头，随机数
     * 'X-TC-Timestamp' => '', // X-TC-Timestamp请求头，当前时间的秒级时间戳
     * 'URI' => ''  //请求uri，eg：/v1/meetings,
     * ];
     * @param $body   请求体，没有的设为空串
     * @param $method  请求方式 字符串 "POST","GET"
     */
    public static function sign($header, $body, $method)
    {
        if (empty(self::$secret_id) || empty(self::$secret_key)) {
            return null;
        }
        $secret_id = self::$secret_id;
        $header_string = "X-TC-Key={$secret_id}&X-TC-Nonce={$header['X-TC-Nonce']}&X-TC-Timestamp={$header['X-TC-Timestamp']}";
        $str_to_sign = "{$method}\n{$header_string}\n{$header['URI']}\n{$body}";
        $hash = hash_hmac('sha256', $str_to_sign, self::$secret_key);
        return base64_encode($hash);
    }
}

```

## 鉴权错误返回参数
鉴权错误返回统一为400。
