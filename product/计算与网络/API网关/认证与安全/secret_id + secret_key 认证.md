您可以使用 secret_id 和 secret_key 对您的 API 进行认证管理。secret_id 和 secret_key 成对出现，这里将它们将称为 secret_id/secret_key 对。
在使用 secret_id/secret_key 对认证前，需要先创建好一对 secret_id 和 secret_key。在服务发布时，您可以在选择发布服务的认证方式时选定为使用 secret_id + secret_key，然后在 secret_id/secret_key 对的选择处选择已经创建好的 secret_id/secret_key 对。
一对 secret_id/secret_key 可用于多个已发布的服务，一个已发布的服务也可以选择使用多个 secret_id/secret_key 对。

使用 secret_id + secret_key 完成认证的方式如下：

## 密钥内容

【secret_id】举例 AKIDCgOPWjQ6BAxvHtyckhWABJVYSBj548pN  用于标识所使用的哪个密钥，并参与签名计算，传输过程中体现。

【secret_key】举例  ZxF2whO0RhuwnVCj5JMMAuqcDcN2oPrC  用于签名计算，传递过程中无体现。

## 计算方法

### 最终发送内容
最终发送的 http 请求内至少包含两个 header：Date 和 X-Date 二选一以及 Authorization，可以包含更多 header。

Date header 的值为 GMT 格式的 http 请求构造时间，例如 Fri, 09 Oct 2015 00:00:00 GMT。

X-Date header 的值为 GMT 格式的 http 请求构造时间，例如：Mon, 19 Mar 2018 12:08:40 GMT。15分钟超时。

Authorization header 的形如 `Authorization: hmac id="secret_id", algorithm="hmac-sha1", headers="date source", signature="Base64(HMAC-SHA1(signing_str, secret_key))"`。

现对 Authorization 内的各部分分别解释：

【hmac】固定内容，用于标识计算方法。
【ID】其值为密钥内的 secret_id 的值。
【algorithm】加密算法，当前支持的是 hmac-sha1。
【headers】参与签名计算的 header，按实际计算时的顺序排列。
【signature】计算签名后得到的签名。

### 签名计算方法
签名由两部分并根据指定加密算法进行计算，以 hmac-sha1 算法举例：

#### 签名内容
首先生成签名内容，签名内容由自定义的 header 组成，header 内建议至少包含 date，可以包含更多其他 header。

header 按如下要求转换后按顺序排列：
* header 名转换为小写，跟上 **ascii 字符** 和 **ascii 空格字符**。
* 然后附加 header 值。
* 如果不是最后一条需构造签名的 header，附上 **ascii 换行字符`\n`**。

例如有两个 header 参与构建签名内容：
```
Date:Fri, 09 Oct 2015 00:00:00 GMT
Source:AndriodApp
```
生成的签名内容为：
```
date: Fri, 09 Oct 2015 00:00:00 GMT
source: AndriodApp
```

#### 计算签名
将上一步生成的签名内容，使用 Base64(HMAC-SHA1(signing_str, secret_key)) 算法进行计算生成签名，也就是：
* 使用签名内容作为输入信息，密钥内的 secret_key 内容作为密钥，使用 HMAC-SHA1 算法进行计算得出加密签名内容。
* 使用 Base64 对算出的加密签名内容进行转换生成可传递的签名内容。

#### 使用签名
如 **最终发送内容** 中所示的一样，在 Authorization header 的 signature 处填入上一步计算完成后的签名。

## 注意事项

### header 对应

Authorization 中 headers 位置填入的需要是参与计算签名的 header 的名称，并建议转换为小写，以 ascii 空格分隔。

### 签名内容生成

排列内容时，请注意 header 名后面跟的冒号和空格，如有遗失也可能导致校验无法通过。

[常用语言的签名 demo>>](https://github.com/apigateway-demo)
