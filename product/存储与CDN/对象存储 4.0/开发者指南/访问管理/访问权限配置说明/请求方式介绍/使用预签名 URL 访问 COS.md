对象存储（Cloud Object Storage，COS）支持使用预签名 URL 进行对象的上传、下载，原理是将签名嵌入 URL 生成签名链接。您可以通过签名的有效期，控制预签名 URL 的生效时间。

您可以使用预签名 URL 进行下载，获取临时 URL 用于临时分享文件、文件夹，也可以通过设置一个很长的签名有效期，获得长期有效的 URL 用于长期分享文件；详情可参考 [文件分享](#文件分享)。

您也可以使用预签名 URL 进行上传，详情可参考使用 [上传文件](#上传文件)。

<span id="文件分享"></span>
## 文件分享（下载文件）

COS 支持对象的分享，您可以使用预签名 URL 将文件、文件夹限时分享给其他用户。预签名 URL 的原理是将签名嵌入拼接在对象 URL 之后，签名生成算法请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778)。

存储桶默认为私有读，直接通过对象 URL 下载会提示访问失败。在对象 url 后拼接了有效的签名后，得到**预签名 URL**；签名携带了身份信息，因此预签名 URL 可以用于下载对象。
```
// 对象 URL
https://test-12345678.cos.ap-beijing.myqcloud.com/test.png

// 预签名 URL（拼接了签名值的对象 URL）
https://test-12345678.cos.ap-beijing.myqcloud.com/test.png?q-sign-algorithm=sha1&q-ak=xxxxx&q-sign-time=1638417770;1638421370&q-key-time=1638417770;1638421370&q-header-list=host&q-url-param-list=&q-signaturexxxxxfxxxxxx6&x-cos-security-token=xxxxxxxxxxxx
```
以下提供的文件分享的几种方法，本质上都是在自动为您生成签名，并拼接到对象 URL 后面，生成可以直接用于下载、预览的临时链接。


### 快速获取临时链接（有效期1 - 2小时）

您可以通过控制台或 COSBrowser 工具快速获取对象的临时链接。

#### 控制台（Web 页面）

1. 登录 [COS 控制台](https://console.cloud.tencent.com/cos5)，单击存储桶名称，进入“文件列表”，单击对象**详情**。
![](https://qcloudimg.tencent-cloud.cn/raw/72a4c937ea9a2e9f44349b215828d590.png)
2. 进入对象详情页面，复制临时链接，有效期为1小时。
![](https://qcloudimg.tencent-cloud.cn/raw/4ea811f3a49709c73d7a8d3bfb171aaa.png)

#### COSBrowser（客户端）

参考文档 [生成文件链接](https://cloud.tencent.com/document/product/436/38103#generatelinks)，使用主账号密钥可获取最长2小时的临时链接，使用子账号密钥可获取最长1.5天的临时链接。

### 获取自定义时长的临时链接

#### 使用签名工具

**适合场景：对编程不熟悉的用户**

操作步骤如下：
1. 文件链接：登录 [COS 控制台]( https://console.cloud.tencent.com/cos5)，在对象详情中获取不带签名的“对象地址”。
2. 从 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
3. 单击 [COS 签名工具]( https://cos5.cloud.tencent.com/static/cos-sign/)，获取签名链接。
有效时间：支持秒、分钟、小时、天级别设置。
![](https://qcloudimg.tencent-cloud.cn/raw/0c9a4378cf8ba2e90b216abc0b030067.png)

#### 使用 SDK 批量获取预签名 URL

**适合场景：批量获取临时链接、有编程基础的用户**

控制台和 COSBrowser 获取的临时链接有效期很短，若需要时间更长的临时链接，也可以使用 SDK 生成预签名 URL，通过控制签名时长实现。生成方法可参考 [预签名授权下载](https://cloud.tencent.com/document/product/436/14116)，选择您熟悉的开发语言。

您可以使用临时密钥或永久密钥用于生成预签名 URL。两者的区别在于，临时密钥的最长时效不超过36小时，永久密钥不会过期，这间接影响了预签名 URL 的有效期。

**使用永久密钥生成预签名 URL（任意时长）**

永久密钥不会过期，预签名 URL 的有效期取决于您设置的签名有效期。您可以直接调用 SDK 的预签名 URL 方法。操作步骤如下：
1. 输入 secret_id、secret_key、region 等初始化 client。
2. 输入您的存储桶名称、对象名称、签名有效期，生成自定义时长的预签名 URL。详情请参见下列各语言 SDK 文档：
<table>
<tr>
<td><a href="https://cloud.tencent.com/document/product/436/46421">Android SDK</a>
<td><a href="https://cloud.tencent.com/document/product/436/35560">C SDK</td>
<td><a href="https://cloud.tencent.com/document/product/436/35163">C++ SDK</td>
<td><a href="https://cloud.tencent.com/document/product/436/32873">.NET SDK</a>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/436/35059">Go SDK</a>
<td><a href="https://cloud.tencent.com/document/product/436/46388">iOS SDK</a>
<td><a href="https://cloud.tencent.com/document/product/436/35217">Java SDK</a></td>
<td><a href="https://cloud.tencent.com/document/product/436/35651">JavaScript SDK</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/436/36121">Node.js SDK</a></td>
<td><a href="https://cloud.tencent.com/document/product/436/34284">PHP SDK</a></td>
<td><a href="https://cloud.tencent.com/document/product/436/35153">Python SDK</a></td>
<td><a href="https://cloud.tencent.com/document/product/436/36162">小程序 SDK</a></td>
</tr>
</table>


**使用临时密钥生成预签名 URL（不超过36小时）**

在前端直传的场景中，经常需要使用到临时密钥。关于临时密钥的说明和生成指引您可以参考：
- [使用临时密钥访问COS](https://cloud.tencent.com/document/product/436/68283)
- [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)
- [用于前端直传 COS 的临时密钥安全指引](https://cloud.tencent.com/document/product/436/40265)

临时密钥最长为36小时，预签名 URL 的有效期回取您设置的签名有效期和临时密钥有效期的最小值。假设您设置的签名有效期为 X，临时密钥的有效期为 Y，链接的实际生效时间为 T：
```
T=min(X,Y)；由于 X<=36，所以 T<=36。
```
使用临时密钥生成预签名 URL，需要两步：
1. [获取临时密钥](https://cloud.tencent.com/document/product/436/14048#.E8.8E.B7.E5.8F.96.E4.B8.B4.E6.97.B6.E5.AF.86.E9.92.A5)。
2. 获取临时密钥后，可以使用与永久密钥类似的函数生成预签名 URL。需要注意的是，使用临时密钥初始化 client，不仅需要输入 SecretId、SecretKey 还需要输入 token，并且携带参数`x-cos-security-token`。详情请参见下列各语言 SDK 文档：
<table>
<tr>
<td><a href="https://cloud.tencent.com/document/product/436/46421">Android SDK</a>
<td><a href="https://cloud.tencent.com/document/product/436/35560">C SDK</td>
<td><a href="https://cloud.tencent.com/document/product/436/35163">C++ SDK</td>
<td><a href="https://cloud.tencent.com/document/product/436/32873">.NET SDK</a>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/436/35059">Go SDK</a>
<td><a href="https://cloud.tencent.com/document/product/436/46388">iOS SDK</a>
<td><a href="https://cloud.tencent.com/document/product/436/35217">Java SDK</a></td>
<td><a href="https://cloud.tencent.com/document/product/436/35651">JavaScript SDK</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/436/36121">Node.js SDK</a></td>
<td><a href="https://cloud.tencent.com/document/product/436/34284">PHP SDK</a></td>
<td><a href="https://cloud.tencent.com/document/product/436/35153">Python SDK</a></td>
<td><a href="https://cloud.tencent.com/document/product/436/36162">小程序 SDK</a></td>
</tr>
</table>

<span id="上传文件"></span>
## 文件夹分享

文件夹是一种特殊的对象，您可以通过控制台或 COSBrowser 工具分享文件夹，详情请参见 [分享文件夹](https://cloud.tencent.com/document/product/436/60351)。

## 上传文件
如果您希望第三方可以上传对象到存储桶，又不希望对方使用 CAM 账户或临时密钥等方式时，您可以使用预签名 URL 的方式将签名提交给第三方，以供完成临时的上传操作。收到有效预签名 URL 的任何人都可以上传对象。

- 途径一：使用 SDK 生成预签名 URL
各语言 SDK 提供了生成上传预签名 URL 的方法，生成方法可参考 [预签名授权上传](https://cloud.tencent.com/document/product/436/14114)，选择您熟悉的开发语言。
- 途径二：自行拼接签名链接
预签名 URL 实际上就是在对象 URL 之后拼接了签名；因此，您也可以通过 SDK、签名生成工具等，自行生成签名，将 URL 与签名拼接成签名链接用于对象上传。然而，由于签名生成算法较为复杂，一般情况下不推荐这种使用方式。
