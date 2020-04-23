
针对视频行业对于版权保护的需求，云点播提出了一套基础级别的 DRM（数字版权管理） 方案，使用 HLS 的普通 AES 加密技术对视频内容加密，保障您的内容安全。您可以通过 [点播文件加密 DEMO](http://demo.vod.qcloud.com/encryption/index.html) 了解该 DRM 方案，登录用户名：test，密码：111111。

##  HLS 普通加密方案

#### 加密算法
云点播系统目前支持 [HLS](https://tools.ietf.org/html/draft-pantos-http-live-streaming-23) 中规定的加密方案（HLS 普通 AES 加密技术），使用 AES-128 对视频内容本身进行加密。

#### 播放器适配性
云点播视频加密方案能够支持所有 HLS 播放器。

#### 局限性

- 仅支持2017版接口：使用 [ProcessFile](https://cloud.tencent.com/document/product/266/9642) 发起加密任务，[GetTaskInfo](https://cloud.tencent.com/document/product/266/11724) 查询加密结果。
- 新版接口 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) 和 [DescribeTaskDetail](https://cloud.tencent.com/document/product/266/33431) 不支持 HLS 普通加密。

### 术语介绍

#### 密钥管理服务（Key Management Service，简称 KMS）
一项安全管理服务，主要负责数据密钥的生产、加密和解密等工作。例如腾讯云的 [密钥管理服务](https://cloud.tencent.com/product/kms)。

#### 数据密钥（Data Key，简称 DK）
由 KMS 系统生成的，用于对称加解密的密钥。

#### 加密后的数据密钥（Encrypted Data Key，简称 EDK）
经过 KMS 系统加密之后的 DK，可以用于公开分发。要通过 EDK 换取 DK，必须调用 KMS 的解密接口。

### 整体架构
![](https://main.qcloudimg.com/raw/387bf80046e8b8b38d3e6c3a359cbc03.png)
视频加密过程是通过转码操作来实现的，不会产生新的 fileId。与一般转码场景相比，视频加密转码的主要区别在于：
- 加密转码，转出来的视频是经过加密的。
- 加密转码完成后，如果通过点播播放器来播放视频，源文件播放地址是不会被获取到的。

### 准备工作

#### 建立密钥管理服务（KMS）
密钥管理服务主要用于管理视频密钥。视频加密过程需要与 KMS 系统进行交互的步骤包括：

1. 生成用于视频加密的数据密钥，即架构图中第II步。这一步将返回 DK 和 EDK。在后续环节中，能够接触到 DK 的角色包括：云点播转码服务、App 后台和经过合法身份校验的最终用户。EDK 可以分发给任意用户，但通过 EDK 获取 DK 这一步，必须由 App 后台进行身份校验。
2. 根据 EDK 获取 DK 来进行数据播放，即架构图中的第4步。App 后台在通过用户的身份验证之后，需要调用 KMS 相关接口，使用 EDK 去获取 DK，即架构图中的第5步。

为最大限度地降低开发者的接入成本，云点播内部集成了 KMS 服务，并且提供了最简单的调用接口。在整个视频加密方案中，App 后台与 KMS 服务唯一需要交互的地方在于获取解密密钥（架构图中的第5步）。

#### 搭建鉴权与密钥派发服务

对于已经加密的视频，只有经过 App 后台认证过的客户端才能得到 DK。因此，最终客户获取密钥的行为必须要有 App 后台参与鉴权。该服务的主要业务逻辑是：
1. 对于客户端携带 EDK 换取 DK 的请求（即架构图中第4步），对请求方进行身份认证。
2. 如果身份认证通过，则去 KMS 系统获取对应的 DK（即架构图中第5步），并返回给客户端。

#### 建议
- 由于 EDK 所对应的 DK 总是固定的，故 App 后台可以缓存（甚至永久保存）EDK 和 DK 之间的对应关系，以降低调用 KMS 系统的次数（即减少架构图中第5步的调用次数）。
- App 后台给客户端的应答，可以增加 HTTP 缓存控制参数（例如 Cache-Control），以降低客户端到 App 后台获取 DK 的次数（即减少架构图中第4步的调用次数）。
- 如需支持浏览器播放，为了避免跨域问题，请确保“鉴权与密钥派发服务”与“视频播放页面”使用的域名相同（例如，若视频播放页面的域名是`v.myvideo.com`，则密钥派发服务的域名也需要是`v.myvideo.com`）。

#### 配置视频加密模板
为确保云点播后台能够进行正确的加密操作，您需要配置视频加密模板，详细请参见 [HLS 普通加密模板](https://cloud.tencent.com/document/product/266/9645)。

### 业务流程

#### 视频上传
可以通过服务端上传、客户端上传、控制台上传、录制上传以及 URL 拉取上传等方式来将已有视频文件上传到云点播平台。

#### 视频加密

视频加密主要步骤如下：

#### 1. App 后台发起视频加密

目前您可以通过 [ProcessFile](https://cloud.tencent.com/document/product/266/9642) 接口发起视频加密，目前只支持对 HLS 文件进行加密。

如下示例的含义是：

- 对视频文件进行转码，转码目标输出模板为210、220、230、240。禁止从较低码率转为较高码率。
- 转码过程使用加密模板10进行加密。
- 事件通知模式为：待整个事件执行完毕之后发起一次事件通知。

<pre>
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFile
&transcode.definition.0=210
&transcode.definition.1=220
&transcode.definition.3=230
&transcode.definition.4=240
&transcode.drm.definition=10
&amp;notifyMode=Finish
&COMMON_PARAMS
</pre>

#### 2. 点播平台获取加密密钥
云点播平台根据调用方指定的加密参数模板，读取密钥获取方式、最终用户获取解密密钥的 URL（如 `https://getkey.example.com`），然后从指定 KMS 系统中获取视频加密密钥 DK 和 EDK。

#### 3. 点播平台发起视频加密转码

云点播转码平台在进行视频加密时，不仅会依照指定的加密算法和密钥对目标输出文件进行加密，而且会将获取解密密钥的 URL 写入视频文件中。例如，对于 HLS，该 URL 会被写入到 M3U8 文件的`EXT-X-KEY`标签中，但在写入之前，转码平台会在该 URL 的 QueryString 中增加三个参数：

- fileId：被加密文件的 ID。
2. keySource：固定为 VodBuildInKMS，表示腾讯云点播内置 KMS。
3. edk：即 DK 对应的 EDK。

在增加上述参数之后，写入转码目标视频文件的 URL 可能为

<pre>
https://getkey.example.com?fileId=123456&keySource=VodBuildInKMS&edk=abcdef
</pre>


该 URL 也是客户端最终在视频播放过程中获取解密密钥时访问的 URL。

#### 4. 点播平台发起加密完成回调
包含加密操作的任务流状态发生变化（或者执行完毕）之后，点播平台将发起 [任务流状态变更通知](/document/product/266/9636)。

### 媒资管理
视频加密操作完成后，可以通过 [GetVideoInfo](/document/product/266/8586) 接口获取视频的加密信息。
- GetVideoInfo 接口会返回该视频 ID 所有转码规格的视频播放地址，包括源文件的播放地址，由于源文件是没有加密处理的，App 服务端可以过滤掉源文件的播放地址，只提供加密视频的播放地址给客户端。
- GetVideoInfo 获取到的源文件 definition 参数是0，可以根据这个值来过滤源文件的视频播放地址。

## 视频播放综述

只有经过合法身份认证的客户才应当得到视频解密密钥。因此，在播放过程中如何对用户的身份信息校验就成为关键因素。

播放过程中，播放器会访问 M3U8 文件中`EXT-X-KEY`标签所标识的 URL 以获取密钥，播放器需要在这一步中携带观看者的身份认证信息。此时有两种方式可以将这一信息传递给 App 鉴权服务：

1. 将用户身份信息通过参数的方式追加到 URL 中，带给 App 的鉴权服务。该方案适用于所有的 HLS 播放器。具体方案请参见 [视频播放方案1](#p1)：通过 QueryString 传递身份认证信息。
2. 将用户身份信息通过 Cookie 带给 App 的鉴权服务。该方案安全性更高，但仅适用于在访问`EXT-X-KEY`标签所标识的 URL 时会携带 Cookie 的播放器。具体方案请参见 [视频播放方案2](#p2)：通过 Cookie 传递身份认证信息。

### <span id="p1"></span>视频播放方案1

视频播放方案1：通过 QueryString 传递身份认证信息，该方案适用于任意支持 HLS 的播放器。

#### 1. 登录并派发用于身份校验的 Token
只有经过合法身份认证的客户才应当得到视频解密密钥。因此在视频播放之前，客户端必须进行登录操作，并由 App 服务端给客户端派发包含身份认证信息的签名，我们称其为 Token。

#### 2. 获取包含 Key 防盗链签名的多码率播放地址
加密转码 API ProcessFile 的回调通知或者 GetVideoInfo API 都可以获取到加密视频的多码率播放地址。
在拿到多码率播放地址后，客户端需要将用户身份信息添加到播放地址中。对于任意播放 URL，增加用户身份信息的方法是：在 URL 中的**文件名**前增加`voddrm.token.<Token>`。

例如，用户身份信息标识为 ABC123；某一码率的播放地址为：
<pre>
http://example.vod2.myqcloud.com/path/to/a/video.m3u8
</pre>

则最终 URL 为：
<pre>
http://example.vod2.myqcloud.com/path/to/a/voddrm.token.ABC123.video.m3u8
</pre>


#### 3. 获取视频内容（已加密）

当播放器访问已经按照上一步所述流程携带用户身份信息的 URL 时，云点播后台会自动将 Token 信息以 QueryString 的方式附加到原始 M3U8 文件`EXT-X-KEY`标签所标识的 URL 中。

例如，某一码率的已加密视频 URL 为：
<pre>
http://example.vod2.myqcloud.com/path/to/a/video.m3u8
</pre>

该文件中，`EXT-X-KEY`标签所标识的获取视频解密密钥的 URL 为：
<pre>
https://getkey.example.com?fileId=123456&keySource=VodBuildInKMS&edk=abcdef
</pre>

则当播放器访问携带 Token 信息的播放地址，即：
<pre>
http://example.vod2.myqcloud.com/path/to/a/voddrm.token.ABC123.video.m3u8
</pre>

其中`EXT-X-KEY`标签所标识的获取视频解密密钥的 URL 会被替换为：
<pre>
https://getkey.example.com?fileId=123456&keySource=VodBuildInKMS&edk=abcdef&token=ABC123
</pre>

此时，播放器获取解密密钥 DK 时便会带上第1步派发的 Token。

#### 4. 获取视频解密密钥（携带身份验证 Cookie）

当播放器获取到视频索引文件（M3U8 文件）后，会在播放视频文件之前自动发起第4步。App 后台在收到客户端的请求后，首先对 QueryString 中的 Token 进行校验。如果用户身份非法，则直接拒绝请求。如果用户身份合法，则根据 URL 中携带的 fileId、keySource、edk 等参数，到 KMS 系统中获取 DK，并返回给客户端。
以上步骤均完成后，客户端便拿到了视频解密密钥，从而可以进行正常的视频解密与播放。

### <span id="p2"></span>视频播放方案2
视频播放方案2：通过 Cookie 传递身份认证信息。该方案仅适用于 iOS/PC 平台的 H5/Flash 播放器。在该平台下，播放器在访问`EXT-X-KEY`标签所标识的 URL 时会带上 Cookie。

>!实际测试发现，Android 平台的 H5 播放器在访问`EXT-X-KEY`标签所标识的 URL 时不会携带 Cookie，所以 Android 平台目前只能使用**方案1**。

#### 1. 登录并派发用于身份校验的 Cookie
只有经过合法身份认证的客户才应当得到视频解密密钥。因此在视频播放之前，客户端必须进行登录操作，并由 App 服务端给客户端派发签名。例如，客户端通过`login.example.com`进行账号密码登录，App 后台在通过身份认证后，给客户端下发`example.com`域的 Cookie 来标识用户身份。

#### 2. 获取指定视频的多码率播放地址
云点播 Web 端视频播放器提供了多码率播放能力，可以根据 fileId 获取一个视频对应的多码率播放地址。如果您使用了其他播放器，则必须自行获取多码率播放地址。

#### 3. 获取视频内容（已加密）
当开始播放视频时，视频播放器会自动发起这一步。
视频播放器开始播放视频时，会向点播 CDN 边缘节点请求视频数据文件。对于 HLS 格式的视频，播放器会根据 M3U8 文件中的`EXT-X-KEY`标签来获取视频解密密钥。例如，`EXT-X-KEY`标签中获取视频解密密钥的 URL 为：
<pre>
https://getkey.example.com?fileId=123456&keySource=VodBuildInKMS&edk=abcdef
</pre>

当播放器获取解密密钥 DK 时，会带上第1步由 App 后台派发的`example.com`域的 Cookie。

#### 4. 获取视频解密密钥（携带身份验证 Cookie）

当播放器获取到视频索引文件（M3U8 文件）后，会在播放视频文件之前自动发起第4步。

App 后台在收到客户端的请求之后，首先对 Cookie 中的身份认证标识进行校验。如果用户身份非法，则直接拒绝请求。如果用户身份合法，则根据 URL 中携带的 fileId、keySource、edk 等参数，到 KMS 系统中获取 DK，并返回给客户端。
以上步骤均完成后，客户端便拿到了视频解密密钥，从而可以进行正常的视频解密与播放。

## FAQ

####  1. 加密 HLS 与普通 HLS 有什么差异？
根据 HLS 文档规范，HLS 加密是对媒体文件（TS 文件）进行加密，M3U8 文件描述了播放器如何解密 TS 文件的方法。加密 HLS 的 M3U8 文件里包含了`EXT-X-KEY`标签，该参数包含`METHOD`和`URI`属性。`METHOD`属性描述了加密的算法，如`AES-128`，`URI`属性描述了获取解密密钥的地址，播放器访问这个 URI 就可以获取到解密的密钥数据。如 URI 为：
<pre>
http://www.test.com/getdk?fileId=123&edk=14cf
</pre>

播放器解析该 M3U8 文件时就会向这个 URI 发起 HTTP 请求，从返回包里获取到密钥数据。

####  2. 开通点播加密功能需要提供哪些信息？
开通云点播加密功能需要提供 getkeyurl，即`EXT-X-KEY`标签中的`URI`属性。
App 服务端需要部署客户端播放加密视频时获取密钥数据的 HTTP 服务。云点播服务在加密视频时，会把加密视频的 M3U8 文件`EXT-X-KEY`标签的`URI`属性设置为 getkeyurl。为了获取密钥和管理方便，我们会在 getkeyurl 后面附加三个参数 fileId、edk 和 keySource。
>?fileId 即视频 ID，edk 是加密后的密钥，keySource 是密钥来源，使用点播内置 KMS 系统的加密文件，keySource 为 VodBuildInKMS。播放器发起获取解密密钥请求时，App 服务端收到的 HTTP 请求的 QueryString 就会包含 fileId 和 edk 等参数，App 服务端可以根据 fileId 和 edk 等参数来返回对应的 DK 给播放器。

####  3. 播放器播放加密视频时从哪里获取解密密钥？
播放器播放加密视频时，根据 M3U8 文件里`EXT-X-KEY`的 URI，发起获取密钥的请求，即 App 提供给云点播的 getkeyurl 地址。
>! 播放器不是向点播服务器发起获取密钥的请求。App 服务器在调用点播 ProcessFile API 进行加密时，加密完成后再调用 [获取视频解密密钥](https://cloud.tencent.com/document/product/266/9643)  API 获取到密钥后，需要将密钥保存起来，当播放器请求密钥时，根据播放器的请求参数来返回对应的密钥。

####  4. App 服务端应如何处理从云点播获取到的密钥数据？
播放器向 App 服务端发起获取密钥请求时，App 服务端需要将对应的密钥数据返回给播放器，返回的密钥数据为16字节的二进制数据。通过 [获取视频解密密钥](https://cloud.tencent.com/document/product/266/9643) API 获取到密钥为 Base64 编码的字符串，返回给播放器时需要将这个字符串转换为二进制数据。
例如，dkData 为 Base64 编码的密钥数据：

Java
```java
  import java.util.Base64;
  byte[] dkBin = Base64.getDecoder().decode(dkData）;
```  

PHP
```php
$dkBin = base64_decode($dkData);
```
