## 功能介绍
随着终端用户个性化的需求愈加丰富，简单的文字交互和图片上传已经不能满足展示与分享信息的诉求，UGC(User Generated Content)也就应运而生。腾讯视频云点播业务的UGC功能，即客户端上传视频功能，支持终端用户将一段短小的视频快速地上传到云端。另外，值得一提的是，依托于腾讯云的支持，后续也能做到播放流畅。

目前腾讯云点播提供给如下平台的UGC上传SDK：

1. [iOS UGC SDK](/document/product/266/7836)；
2. [Android UGC SDK](/document/product/266/7837)；
3. [Web UGC SDK](/document/product/266/7938)。

如果您有其他平台的UGC上传需求，可以基于点播UGC视频上传接口进行开发，包括如下三个接口：

1. [初始化上传(UGC)](/document/product/266/7902)；
1. [分片上传(UGC)](/document/product/266/7903)；
1. [结束上传(UGC)](/document/product/266/7904)。

## 业务流程
UGC视频上传的整体流程分为如下两步：

1. 客户端向服务端申请上传签名；
2. 调用腾讯云点播的UGC SDK（或者上传接口），进行视频上传。

如下图所示：

![](//mc.qcloudimg.com/static/img/460e9bda01a743188498d046a30e8300/image.png)

注意：

1. APP**千万不要**把自己的SecretID和SecretKey暴露给客户端，这两个关键信息泄露将导致很严重的安全隐患；
1. 为了确保APP在点播的存储空间不被恶意使用，点播要求UGC上传必须携带APP后台派发的上传签名；
1. 视频上传之后是否进一步进行处理（例如转码、鉴黄），是由APP服务端通过签名进行控制的。

## UGC视频上传签名生成

点播UGC视频上传签名是一段经过[Base64](https://tools.ietf.org/html/rfc4648)编码的二进制串，其中包含的主要信息如下：

1. 上传参数信息，包括：
    1. APP的SecretID；
    1. 视频的基本信息，例如视频名称、标签；
    1. 视频上传到点播之后的处理方式，例如是否进行转码、是否进行鉴黄等；
1. 用SecretKey生成的[HMAC-SHA1](https://www.ietf.org/rfc/rfc2104.txt)签名，点播后台据此来校验UGC上传签名的合法性。

### 上传参数信息

| 字段 | 类型 | 必填 | 说明 |
|---------|---------|---------|---------|
| s | String | 是 | 云api管理页中的Secret ID |
| f | String | 是 | 视频文件本地名称，长度在40个字节以内，不得包含\ / : * ? " < > 等字符 |
| t | Integer | 是 | 当前时间戳，是一个符合 Unix Epoch 时间戳规范的数值，单位为秒 |
| e | Integer | 是 | 签名失效时刻，是一个符合Unix Epoch时间戳规范的数值，单位为秒。e 的计算方式为 e = t + 签名有效时长。签名有效时长最大取值为7776000（90天）|
| r | Integer | 是 | 随机串，无符号10进制整数，用户需自行生成，最长10位 |
| fs | String | 是 | 文件的SHA-1签名，由客户端计算并提交到APP后台 |
| ft | String | 是 | 文件类型，例如mp4,flv,avi等，注意不需要"." |
| uid | String | 是 | 用户在APP内的唯一标识，建议取md5计算结果，例如对qq，号码12345就是uid=md5(12345)|
| tc | Integer | 否 | 是否转码，需要转码时，tc=1 |
| ss | Integer | 否 | 转码时是否截图，需要截图时，ss=1。本参数仅tc=1时有效 |
| wm | Integer | 否 | 转码时是否加水印，需要转码加水印时，wm=1。本参数仅tc=1时有效 |
| cid | Integer | 否 | 文件分类id，需要指定分类id时填入 |
| tag.n | String | 否 | 文件标签，可指定最多10个标签，使用方式：例如三个标签就是tag.1=a&tag.2=b&tag.3=c|

## UGC视频上传签名生成
计算UGC视频上传签名，主要分为如下三个步骤：

1. 获取签名计算所需信息；
1. 拼接明文字符串；
1. 依照文字符串构造签名。

云点播提供了多种不同语言的签名上传示例代码，参见[UGC上传签名生成示例代码](#ugc.E4.B8.8A.E4.BC.A0.E7.AD.BE.E5.90.8D.E7.94.9F.E6.88.90.E7.A4.BA.E4.BE.8B.E4.BB.A3.E7.A0.81)。

### 获取签名计算所需信息

在生成签名所需信息中，Secret ID和Secret Key需要在腾讯云管理中心控制台页面的**【云产品】**---**【监控与管理】**下的**【云 API 密钥】**页面查看。

其他信息，除了文件的SHA信息必须依赖客户端提交，其他参数都可以由APP后台控制。

### 拼接签名明文字符串

拼接签名明文字符串，形式为HTTP QueryString。格式如下：

```
s=[SecretID]&f=[FileName]&fs=[FileSha]&t=[currentTime]&e=[expiredTime]&r=[rand]&uid=[uid]
```

我们设拼接好的明文字符串为Original。

> 注意：
> 
> 1. 与服务端API的签名生成方式不同，这里不需要对所有参数进行排序；
> 1. 建议APP使用编程语言已有的QueryString相关类库来生成签名，而不是手工拼装字符串。

### 将明文字符串转化为签名

拼接好签名的明文字符串Original后，用已经获取的SecretKey对明文串进行[HMAC-SHA1](https://www.ietf.org/rfc/rfc2104.txt)加密，得到SignTmp：

```
SignTmp = HMAC-SHA1(SecretKey, Original) 
```

将密文串SignTmp放在明文串Origin前面，拼接后进行[Base64](https://tools.ietf.org/html/rfc4648)编码，得到最终的签名Sign：

```
Sign = Base64(append(SignTmp, Original)) 
```

## UGC上传签名生成示例代码

- [PHP示例](/document/product/266/7906)
- [Node.js示例](/document/product/266/7905)