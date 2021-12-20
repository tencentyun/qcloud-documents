

## 简介

物联使能 API 是物联使能平台为帮助用户快速开发并高效托管物联网 SaaS 而提供的接口操作与云端服务，包括设备管理与控制、设备数据查询、数据模板查询等管理能力。用户可通过调用物联使能 API 来使用物联使能服务，支持的全部 API 请参见 [物联使能 API 概览](https://cloud.tencent.com/document/product/1081/50241)。

## 调用方式

 **API URL 为 `https://iot.cloud.tencent.com/api/exploreropen/serviceapi`**。
其中公共参数有： Action，RequestId，AppKey，Signature，Timestamp，Nonce。具体说明如下：
- **Action**：用于标识请求的方法名称。
- **RequestId**：用于标识一个唯一请求，推荐使用 uuid 作为参数值，定位问题时建议提供该参数值。
- **AppKey**：为 SaaS 的密钥。
-  **Signature**：为本次请求的签名，具体计算方法见本文下方示例。
-  **Timestamp**：为本次请求的 Unix 秒级时间戳。
-  **Nonce**：为随机正整数，用于和时间戳一起，防范 API 重放攻击。


## 签名算法

### 获取 SaaS 的 AppKey 和 AppSecret

在创建 SaaS 时，平台将会为用户生成对应的安全凭证。安全凭证包括 AppKey 和 AppSecret。AppKey 是用于标识 API 调用者身份，AppSecret 是用于加密签名字符串和服务器端验证签名字符串的密钥。**用户应严格保管其 AppSecret，避免泄露**。

具体获取步骤如下：
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，选择已有项目进入项目详情页。
2. 选择左侧菜单**物联使能** > **SaaS 服务**，单击**新建**按钮 [创建 SaaS](https://cloud.tencent.com/document/product/1081/50038#.E6.96.B0.E5.BB.BA-saas)。
3. 创建 SaaS 成功后，即可获取系统自动生成的 AppKey 与 AppSecret。

### 生成签名串

有了安全凭证 AppKey 和 AppSecret 后，即可生成签名串。下面给出一个生成签名串的详细过程。

假设用户的 AppKey 和 AppSecret 分别是：

- AppKey： `ServiceAppKey`
- AppSecret： `ServiceAppSecret`

>?本文仅为示例，请您根据自己实际的 `AppKey` 和 `AppSecret` 进行后续操作。
>
以获取设备物模型数据 `ServiceDescribeDeviceData` 请求为例，当用户调用这一接口时，其请求参数**可能**如下：

| 参数名称   | 类型   | 描述                                                         | 参考数值                             |
| ---------- | ------ | ------------------------------------------------------------ | ------------------------------------ |
| RequestId  | String | 公共参数，唯一请求 ID，可自行生成，推荐使用 uuid。定位问题时，需要提供该次请求的 RequestId | 476c990a-f5b7-1575-987c-4ef70e474932 |
| Action     | String | 公共参数，调用的接口方法名称                                 | ServiceDescribeDeviceData            |
| AppKey     | String | 公共参数，物联网 SaaS 的 AppKey ，用于标识对应的物联网 SaaS         | ServiceAppKey                        |
| Signature  | String | 公共参数，请求的签名                                         | 根据实际算法生成                     |
| Timestamp  | Int64  | 公共参数，当前的  UNIX 时间戳（秒级）                        | 1546315200                           |
| Nonce      | Int64  | 公共参数，随机正整数，与时间戳一起，用于 API 防重放          | 71087795                             |
| ProductId  | String | 产品 ID                                                       | ProductA                             |
| DeviceName | String | 设备名称                                                     | Device001                            |


>?
- 请求参数中的公共请求参数有：RequestId、Action、AppKey、Timestamp、Nonce、Signature。
- ServiceDescribeDeviceData 接口特有参数：ProductId、DeviceName。

而参数 Signature（签名串）正是由上述参数共生成的，具体步骤如下：

1. 对参数排序
   对所有请求参数按参数名做字典序升序排列，所谓字典序升序排列，直观上就如同在字典中排列单词一样排序，按照字母表或数字表里递增顺序的排列次序，即先考虑第一个 “字母”，在相同的情况下考虑第二个 “字母”，依此类推。您可以借助编程语言中的相关排序函数来实现这一功能，例如 PHP 中的 ksort 函数。上述示例参数的排序结果如下：
```
{
			Action=ServiceDescribeDeviceData,
			AppKey=ServiceAppKey,
			DeviceName=Device001,
			Nonce=71087795,
			ProductId=ProductA,
			RequestId=476c990a-f5b7-1575-987c-4ef70e474932,
			Timestamp=1546315200
}
```

使用其它程序设计语言开发时, 可对上面示例中的参数进行排序，得到的结果一致即可。
2. 拼接请求字符串
   将把上一步排序好的请求参数格式化成“参数名称”=“参数值”的形式，如对 Action 参数，其参数名称为 "Action"，参数值为 "AppCreateCellphoneUser"，因此格式化后就为 Action=AppCreateCellphoneUser。
  - “参数值” 为原始值而非 URL 编码后的值。
  - 若输入参数中包含下划线，则需要将其转换为 `“.”`。

将格式化后的各个参数用 `"&"` 拼接在一起，最终生成的请求字符串为：
<dx-codeblock>
::: Java Java
Action=ServiceDescribeDeviceData&AppKey=ServiceAppKey&DeviceName=Device001&Nonce=71087795&ProductId=ProductA&RequestId=476c990a-f5b7-1575-987c-4ef70e474932&Timestamp=1546315200
:::
</dx-codeblock>


3. 生成签名串
使用 HMAC-SHA1 算法对上一步中获得的签名原文字符串进行签名，然后将生成的签名串使用 Base64 进行编码，即可获得最终的签名串。
具体代码如下，以 PHP 语言为例：
<dx-codeblock>
::: Java PHP
$secretKey = 'ServiceAppSecret';
$srcStr = 'Action=ServiceDescribeDeviceData&AppKey=ServiceAppKey&DeviceName=Device001&Nonce=71087795&ProductId=ProductA&RequestId=476c990a-f5b7-1575-987c-4ef70e474932&Timestamp=1546315200';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr
:::
</dx-codeblock>

最终得到的签名串为：
```
P206d+JzP37FLKBDkD689wqnl4k=
```

使用其它程序设计语言开发时，可用上面示例中的原文进行签名验证，得到的签名串与例子中的一致即可。


