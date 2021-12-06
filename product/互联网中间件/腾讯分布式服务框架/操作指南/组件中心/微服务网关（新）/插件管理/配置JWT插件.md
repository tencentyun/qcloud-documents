## JWT 原理

JWT（JSON Web Token）本质是一个 Token，是一种紧凑的 URL 安全方法，用于在网络通信的双方之间传递声明。
JWT 的原理是，客户端通过 JWT 认证服务器认证以后，会返回给客户端一个 JWT 令牌（Token），示例如下（真实长度会更长）：
![](https://main.qcloudimg.com/raw/1c85a220f3e0f2543f93ec8b030774be.png)
JWT 分为三部分：Header（头部）、Payload（负载）、Signature（签名），中间用点（`.`）分隔成三个部分。
此后，客户端与服务端通信的时候，都要携带这个 JWT 令牌（Token）。微服务网关 JWT 插件凭此令牌（Token）来校验客户端权限，服务端就不再保存任何 session 数据，此时服务端变成无状态了，比较容易实现横向扩展

### Header

Header 部分是一个 JSON 对象，描述 JWT 的元数据，示例如下：

```javascript
{
   "alg": "HS256",
   "typ": "JWT"
}
```

- `alg` 属性表示签名的算法（algorithm），默认是 HMAC SHA256（写成 HS256）。
- `typ` 属性表示这个令牌（token）的类型（type），JWT 令牌统一写为 `JWT`。

最后，将上面的 JSON 对象使用 Base64URL 算法转成字符串，即为 JWT 令牌中的 Header 部分。

### Payload 

Payload 部分也是一个 JSON 对象，用来存放实际需要传递的数据，包括官方定义的字段和用户自定义字段。

| 参数       | 英文全称                               | 是否必选 | 说明                                                         | 取值要求                                                     |
| ---------- | -------------------------------------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| iss        | Issuer Identifier                      | 是       | 提供认证信息者的唯一标识。                                   | 一般是一个 HTTPS 的 URL（不包含 querystring 和 fragment 部分） |
| ѕub        | Ѕubjесt ldеntіfіеr                     | 是       | iss 提供的 EU 的标识，在 iss 范围内唯一。它会被 RP 用来标识唯一 的用户。 | 最长为255个 ASCII 字符                                       |
| aud        | Audience(s)                            | 是       | 标识 ID Token 的受众。                                       | 必须包含 OAuth2 的 client_id                                 |
| exp        | Expiration time                        | 是       | 过期时间，超过此时间的 ID Token 会作废不再被验证通过。       | -                                                            |
| iat        | Issued At Time                         | 是       | JWT 构建的时间。                                             | -                                                            |
| auth_ time | AuthenticationTime                     | 否       | EU 完成认证的时间 。如果 RP 发送 AuthN 请求的时候携带 max_age 的参数，则此 Claim 是必须的。 | -                                                            |
| nоnсе      | -                                      | 否       | RP 发送请求的时候提供的随机字符串，用来减缓重放攻击，也可以来关联  ID Token 和 RP 本身的 Session 信息。 | -                                                            |
| асr        | Аuthеntісаtіоn Соntехt Сlаѕѕ Rеfеrеnсе | 否       | 表示一个认证上下文引用值，可以用来标识认证上下文类。         | -                                                            |
| amr        | Authentication Methods References      | 否       | 表示一组认证方法。                                           | -                                                            |
| azp        | Authorized party                       | 否       | 结合 aud 使用。只有在被认证的一方和受众（sud）不一致时才使用此值，一般情况下很少使用。 | -                                                            |

下面是一个典型数据格式的示例，供参考：

```json
{
    "iss": "https://cloud.tencent.com/tsf/msgw/jwt",
    "sub": "aaaaaaaa-bbbb-cccc-dddd-example",
    "aud": "tsf",
    "exp": 1500013000,
    "iat": 1500009400,
    "auth_time": 1500009400,
    "nonce": "x-03_si1h4t",
    "acr": "1",
    "azp": "tsf",
    "given_name": "Anaya",
    "email": "anaya@example.com"
}
```

最后，将上面的 JSON 对象使用 Base64URL 算法转成字符串，即为 JWT 令牌中的 Payload 部分。

### Signature

Signature 部分是对前两部分的签名，防止数据篡改。

生成 JWT 令牌（token）需要私钥，[点此](https://mkjwk.org/) 生成与验证的公钥与私钥。使用 Header 里面指定的签名算法（默认是 HMAC SHA256），按照下面的公式产生签名。

```javascript
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

算出签名以后，把 Header、Payload、Signature 三个部分拼成一个字符串，每个部分之间用"点"（`.`）分隔，即为JWT 令牌（token），最后返回客户端。

## 使用 Java 生成 JWT 令牌（Token）

1. 添加 JWT 的 pom 依赖。
   微服务网关使用 jose4j 来实现。在 pom 文件中添加以下依赖：
```xml
<!-- jwt -->
<dependency>
    <groupId>org.bitbucket.b_c</groupId>
    <artifactId>jose4j</artifactId>
    <version>0.6.5</version>
</dependency>
```

2. 编写生成令牌的 Java 代码。
```java
// 下面省略了无关代码
import org.jose4j.json.JsonUtil;
import org.jose4j.jwa.AlgorithmConstraints;
import org.jose4j.jwa.AlgorithmConstraints.ConstraintType;
import org.jose4j.jwk.PublicJsonWebKey;
import org.jose4j.jwk.RsaJsonWebKey;
import org.jose4j.jws.JsonWebSignature;
import org.jose4j.jwt.JwtClaims;
import org.jose4j.jwt.MalformedClaimException;
import org.jose4j.jwt.consumer.InvalidJwtException;
import org.jose4j.jwt.consumer.JwtConsumer;
import org.jose4j.jwt.consumer.JwtConsumerBuilder;
import org.jose4j.lang.JoseException;
public static void main(String[] args) throws JoseException, MalformedClaimException {
        // 通过私钥对生成jwk
        RsaJsonWebKey  jwk = new RsaJsonWebKey(JsonUtil.parseJson("{"
            + "    \"kty\": \"RSA\","
            + "    \"alg\": \"RS256\","
            + "    \"n\": \"mrX5ROEw4kCYDXR94FQsm33gr5o5dQXvuOoe-eG_yvdNW83MMt9GgG_eBBq_1b7HgyP9lo15BfKX3GH1igCjEKoXJxcHC5xox4xC0tvbBNCDwG_987ZsqlgCb4f7X66DCcHh17AyAHYa8JhO2kXvtD1OIQxSajSgmk1C1sxI5kqJXfvJwRLcCEK87P6Bs9YNLnnJeouSkYce04AhspmyQKKax4GllbMjcrUUMRoqpCBMklh5Pgl9sOGRLo-6uzzowtI_SyF03YsE2ejh9m-YWqTYsx7PIg6SdWrNRIprKtjnhc9nk-QBzWbOTFH3bpMoXl0T9KPndaLpi1pXtaej9Q\","
            + "    \"e\": \"AQAB\","
            + "    \"d\": \"lL9vqdUl7fMS_qTJPf1QYjPV6qBKrAQIJ28aV0DA6YF6pFCrCyJ3I5frC2E4nmbuZl0dPTpKaPiFIAQjUwsnvSb8Wb4fLP-2El3-BcQSwX9FnalPrpnvwpwZw2gnvSgJn0EFRh6HBMCJSFf4QI7LWC01SDsTpj9xRsoQAHurf5YZ8YRpi_-XEWBaL-4R_RxpoeAnSgSbJkcGoJNcxqwWbCun37KYBS_71sd155VWycMd-uHtTRnW6SenVG49pexXq-tIQxOwmatpTj0XF7hhshKgdTF1xXPbMSX6XOvxiy929jPMercBL_-OUu0PPUZTTVp0gNziGdevzufHkEfHxQ\","
            + "    \"p\": \"5dOs8Q0SHIuCq-gAOx2c2JaqXzPRsmmZ7nXx1P1jbddDIenVPA6q5zUVqXIRRQgMA7AdD9x7anJ2_kaKSFoE2D8peuObvmjrbmJeYE4F4138pNESOHlBmhUH93Oo4i5TvmNZ5hxu3CmonGKMafeDoMpopN15yeDGkTVFKoOfuys\","
            + "    \"q\": \"rFRhmJIIj3o__CbjVOlUgiVzrk-ZgK9jGXHhyt6LELQae1nUiZNZuwZeHwgzTonsTMJ2JHnmCuDpwuhjf_kha5KHeuczE7gmnlaGd3s6kaKDyB9bXbMTs122SnNiB-lJcwm4wRNWI-irSh8PyHSQVnjvKkQCCEPi4i0Ky1KgDV8\","
            + "    \"dp\": \"qBUJNDn09v9pD8Ra9uEPZq-55mqFgFAPDgEgXj76yshWBqV3F7c6cmG2d_g-fRgHgWL5vjHn6M_SCuEYHRYI2QZIleGEc9tT46T5lME7OS_xp7Bn_PlhawjajLT_3Hs5L9KFWu-MfGPTNpw0SQOGNsARjBGWEnjbgDNPZGpjFYU\","
            + "    \"dq\": \"F_0rFNUHUgm_jHdRYAmXFQLnppU4FhzUG7-podb23t1jblZj6r7TV-CcC4_VrJIwjcLoNU2uw0bp45L7_t2MVHAyYd57Urxoy9PZphpGXe2UkLAkxNdf37Ek5hpHxDgqXFQ3HtF1RUxnQ8stJEdtrEvrZyPOcJ4aoEeK4CDhXNs\","
            + "    \"qi\": \"QdwkKs9n6jswVsbYKprvpNr2Mbg-RBPp5xx1p-ypVJnFOd_lnCA6P3gRJ-pe6tSCIB6AYViEhZpzKMSu47f27_38VHkH9qOOL38ZVeVFo8Yt8lkBwMEKQdDOghfF74L5Fczo9bH7QX679dC847cDEa1oaV2Cdv6XcSKGywwvq3Y\""
            + "}"));

        // 创建Claims，放在JWT payload位置
        // Create the Claims, which will be the content of the JWT
        JwtClaims claims = new JwtClaims();
        claims.setIssuer("Issuer");  // who creates the token and signs it
        claims.setAudience("Audience"); // to whom the token is intended to be sent
        claims.setExpirationTimeMinutesInTheFuture(10); // time when the token will expire (10 minutes from now)
        claims.setGeneratedJwtId(); // a unique identifier for the token
        claims.setIssuedAtToNow();  // when the token was issued/created (now)
        claims.setNotBeforeMinutesInThePast(2); // time before which the token is not yet valid (2 minutes ago)
        claims.setSubject("subject"); // the subject/principal is whom the token is about
        claims.setClaim("email","mail@example.com"); // additional claims/attributes about the subject can be added
        List<String> groups = Arrays.asList("group-one", "other-group", "group-three");
        claims.setStringListClaim("groups", groups); // multi-valued claims work too and will end up as a JSON array

        JsonWebSignature jws = new JsonWebSignature();
    
        // The payload of the JWS is JSON content of the JWT Claims
        jws.setPayload(claims.toJson());

        // The JWT is signed using the private key
        jws.setKey(jwk.getPrivateKey());

        // Set the Key ID (kid) header because it's just the polite thing to do.
        // We only have one key in this example but a using a Key ID helps
        // facilitate a smooth key rollover process
        jws.setKeyIdHeaderValue("kid");

        // Set the signature algorithm on the JWT/JWS that will integrity protect the claims
        jws.setAlgorithmHeaderValue(jwk.getAlgorithm());

        // 生成JWT 令牌
        // Sign the JWS and produce the compact serialization or the complete JWT/JWS
        // representation, which is a string consisting of three dot ('.') separated
        // base64url-encoded parts in the form Header.Payload.Signature
        // If you wanted to encrypt it, you can simply set this jwt as the payload
        // of a JsonWebEncryption object and set the cty (Content Type) header to "jwt".
        String jwt = jws.getCompactSerialization();

        long expirationTime = claims.getExpirationTime().getValueInMillis();
        DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss z", Locale.SIMPLIFIED_CHINESE);
        String msg = String.format("JWT expired at (%d -> %s)", expirationTime, dateFormat.format(expirationTime));
        
        // 打印JWT 令牌过期时间
        System.out.println(msg);
        // 打印JWT 令牌
        System.out.println(jwt);
    }
```


##  JWT 插件配置步骤

### 1. 新建插件

微服务网关已经对外提供了 JWT 认证功能，用户可在 [TSF 控制台](https://console.cloud.tencent.com/tsf?rid=1) > **微服务网关** > **插件管理**页面创建 JWT 类型插件。
![](https://main.qcloudimg.com/raw/c5a490b04b9168b1d2ee56b9df2e25a1.png)

* 校验参数值：指用户存放 JWT 令牌（Token）参数名称，示例中参数名为 `token`。

* 校验参数携带位置：指用户存放 JWT 令牌（Token）的位置，目前支持 Query 和 Header 两种携带方式，示例中为 Query 方式。

* 公钥对 kid：密钥 ID（“kid”），用来标识此密钥。

* 公钥对 JSON 串：公钥对，示例中值为：

  ```json
  {
      "kty": "RSA",
      "alg": "RS256",
      "n": "mrX5ROEw4kCYDXR94FQsm33gr5o5dQXvuOoe-eG_yvdNW83MMt9GgG_eBBq_1b7HgyP9lo15BfKX3GH1igCjEKoXJxcHC5xox4xC0tvbBNCDwG_987ZsqlgCb4f7X66DCcHh17AyAHYa8JhO2kXvtD1OIQxSajSgmk1C1sxI5kqJXfvJwRLcCEK87P6Bs9YNLnnJeouSkYce04AhspmyQKKax4GllbMjcrUUMRoqpCBMklh5Pgl9sOGRLo-6uzzowtI_SyF03YsE2ejh9m-YWqTYsx7PIg6SdWrNRIprKtjnhc9nk-QBzWbOTFH3bpMoXl0T9KPndaLpi1pXtaej9Q",
      "e": "AQAB"
  }
  ```

* claim 参数映射关系 JSON：指 JWT 令牌（Token）中 claim 携带的数据是否需要透传（可配置多组），示例中值为：

  ```json
  [{
      "parameterName":"email",
      "mappingParameterName":"new_email",
      "location":"header"
  }]
  ```

  该示例表示，将 claim 中参数为 `email` 的值，通过放入 HTTP header 透传给下游，并重新命名为 `new_email`。

 - `parameterName` 属性表示 claim 数据中待透传参数的名称。
 - `mappingParameterName` 属性表示需要转换的参数名称。
 - `location` 属性表示透传此值的位置。

### 2. 插件绑定对象  

微服务网关插件通过绑定分组或 API 来生效。 
![](https://main.qcloudimg.com/raw/0bfe7c09a5c98059a52e886ef8f4b8c2.png)

