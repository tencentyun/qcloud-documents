## 简介
应用端 API 是开发平台为了满足智能家居场景，为用户开发自有品牌的小程序或 App 而提供的云端服务，用户无需实现用户管理、设备管理、设备定时、家庭管理等基础能力，可通过调用应用端 API 快速完成移动应用端的开发。


## 调用方式

1. **登录前所使用的 API URL 为 `https://iot.cloud.tencent.com/api/exploreropen/appapi`**。
其中公共参数有： Action，RequestId，AppKey，Signature，Timestamp，Nonce。其中 Action 用于标识请求的方法名称；RequestId 用于标识一个唯一请求，推荐使用 uuid 作为参数值，定位问题时建议提供该参数值；AppKey 为应用的密钥； Signature 为本次请求的签名，具体计算方法见本文下方示例；Timestamp  为本次请求的 UNIX 秒级时间戳； Nonce 为随机正整数，用于和时间戳一起，防范 API 重放攻击。
2. **登录后所使用的 API URL 为 `https://iot.cloud.tencent.com/api/exploreropen/tokenapi`**。
其中公共参数有: Action，RequestId，AccessToken。其中 Action 用于标识请求的方法名称；RequestId 用于标识一个唯一请求，推荐使用 uuid 作为参数值，定位问题时建议使用该参数值。AccessToken 用于标识一个已经登录的用户。

登录前，要通过相关用户接口换取 `accesstoken` 完成登录，调用url 为 `..../appapi`，`accesstoken` 用于标识一个用户。当用户登录完毕后，使用 url 为 `.../tokenapi` 的相关 API 完成其他操作。


## 签名算法

#### 获取应用 AppKey 和 AppSecret

如果用户不使用腾讯官方的“腾讯连连”小程序，用户也可通过平台开放能力开发自有品牌小程序。在创建应用的时候，平台会为用户生成小程序对应的安全凭证。安全凭证包括 AppKey 和 AppSecret。AppKey 是用于标识 API 调用者身份，AppSecret 是用于加密签名字符串和服务器端验证签名字符串的密钥。**用户应严格保管其 AppSecret，避免泄露**。

具体获取步骤如下：
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，进入开发中心。
2. 选择左侧菜单【应用开发】>【小程序开发】，新建小程序，具体新建步骤参见 [应用开发](https://cloud.tencent.com/document/product/1081/40291#.E6.96.B0.E5.BB.BA.E5.BA.94.E7.94.A8)。
3. 创建小程序成功后，即可获取系统自动生成的 AppKey 与 AppSecret。

#### 生成签名串

有了安全凭证 AppKey 和 AppSecret 后，就可以生成签名串了。下面给出了一个生成签名串的详细过程。

假设用户的 AppKey 和 AppSecret 分别是：
- AppKey： `ahPxdK****TGrejd`
- AppSecret： `NcbHqk****TCGbKnQH`

>?本文仅为示例，请您根据自己实际的 `AppKey` 和 `AppSecret` 进行后续操作。

以通过手机号注册账号 `AppCreateCellphoneUser` 请求为例，当用户调用这一接口时，其请求参数**可能**如下：

| 参数名称          | 类型      |  描述      |  参考数值                 |
| ---------------- | --------- | --------- | ------------------------ |
| RequestId        | String    | 公共参数，唯一请求 ID，可自行生成，推荐使用 uuid。定位问题时，需要提供该次请求的 RequestId  | 8b8d499bbba1ac28b6da21b4 |
| Action           | String    | 公共参数，调用的接口方法名称     | AppCreateCellphoneUser   |
| AppKey           | String    |公共参数，应用 AppKey ，用于标识对应的 App  | ahPxdK****TGrejd  |
| Signature        | String    | 公共参数，请求的签名   | Szxai9Qs7****OXahbFbseZ+uE= |
| Timestamp        | Int64     | 公共参数，当前的  UNIX 时间戳（秒级） | 1546315200               |
| Nonce            | Int       | 公共参数，随机正整数，与时间戳一起，用于 API 防重放 | 71087795                 |
| CountryCode      | String    | 国家区码     | 86                       |
| PhoneNumber      | String    | 手机号码     | 13900000000              |
| Password         | String    | 密码       | password              |
| VerificationCode | String    | 短信验证码 | 123456                   |

>?
- 请求参数中的公共请求参数有：RequestId、Action、AppKey、Timestamp、Nonce、Signature。
- AppCreateCellphoneUser 接口特有参数：CountryCode、PhoneNumber、Password、VerificationCode。

而参数 Signature（签名串）正是由上述参数共生成的，具体步骤如下：
1. 对参数排序
对所有请求参数按参数名做字典序升序排列，所谓字典序升序排列，直观上就如同在字典中排列单词一样排序，按照字母表或数字表里递增顺序的排列次序，即先考虑第一个 “字母”，在相同的情况下考虑第二个 “字母”，依此类推。您可以借助编程语言中的相关排序函数来实现这一功能，例如 PHP 中的 ksort 函数。上述示例参数的排序结果如下：
```
{
		Action=AppCreateCellphoneUser,
		AppKey=ahPxdK****TGrejd,
		CountryCode=86,
		Nonce=71087795,
		Password=My!P@ssword,
		PhoneNumber=13900000000,
		RequestId=8b8d499bbba1ac28b6da21b4,
		Timestamp=1546315200,
		VerificationCode=123456
}
```

使用其它程序设计语言开发时, 可对上面示例中的参数进行排序，得到的结果一致即可。

2. 拼接请求字符串
将把上一步排序好的请求参数格式化成“参数名称”=“参数值”的形式，如对 Action 参数，其参数名称为 "Action"，参数值为 "AppCreateCellphoneUser"，因此格式化后就为 Action=AppCreateCellphoneUser
  - “参数值” 为原始值而非 URL 编码后的值。
  - 若输入参数中的“键”包含下划线，则需要将其转换为 “.”。对于“值”不需要额外操作。。

将格式化后的各个参数用"&"拼接在一起，最终生成的请求字符串为：
```
Action=AppCreateCellphoneUser&AppKey=ahPxdK****TGrejd&CountryCode=86&Nonce=71087795&Password=My!P@ssword &PhoneNumber=13900000000&RequestId=8b8d499bbba1ac28b6da21b4&Timestamp=1546315200&VerificationCode=123456
```

3. 生成签名串
使用 HMAC-SHA1 算法对上一步中获得的签名原文字符串进行签名，然后将生成的签名串使用 Base64 进行编码，即可获得最终的签名串。
具体代码如下，以 PHP 语言为例：
```
$secretKey = 'NcbHqk****TCGbKnQH';
$srcStr = 'Action=AppCreateCellphoneUser&AppKey=ahPxdK****TGrejd&CountryCode=86&Nonce=71087795&Password=My!P@ssword&PhoneNumber=13900000000&RequestId=8b8d499bbba1ac28b6da21b4&Timestamp=1546315200&VerificationCode=123456';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr
```
最终得到的签名串为：
```
Szxai9Qs7O3lBoOXahbFbseZ+uE=
```
使用其它程序设计语言开发时，可用上面示例中的原文进行签名验证，得到的签名串与例子中的一致即可。

## 常见问题

对于参数为字符串且为空的，应将其从签名串中省略，不需要将其参与签名。


## 调试工具
使用应用端 API [调试工具](https://iot.cloud.tencent.com/apidebug)，快速调试应用端 API。
