## 功能概述

COS 签名工具是腾讯云对象存储为用户提供的 Web 工具，可用于生成请求签名。您可以在工具页面上填入指定的参数，生成请求签名，以及校验请求签名的正确性。
- 目前 COS 存在 XML 和 JSON 两个不同版本的 API，两类 API 的签名入参有所差异，COS 推荐您使用 XML 版本的 API。JSON API 是腾讯云 COS 服务在推出 XML API 前为用户提供接入使用 COS 的 API 接口，接口与标准 XML 的 API 底层架构相同，数据互通，可以交叉使用，但是接口不兼容。
- 有关 XML 版本的签名介绍文档，请参见 XML 版本 [请求签名](https://cloud.tencent.com/document/product/436/7778)。
- 有关 JSON 版本的签名介绍文档，请参见 JSON 版本 [签名算法](https://cloud.tencent.com/document/product/436/6054)。

## 工具地址

单击进入 [COS 签名工具](https://cos5.cloud.tencent.com/static/cos-sign/)。

## 使用方法
### XML 版本签名工具

#### 输入基础配置信息
1. 单击 [COS 签名工具](https://cos5.cloud.tencent.com/static/cos-sign/)，进入 “COS 签名工具” 页面。
2. 在 “基础信息” 栏中，选择 API 版本，填写签名有效时间。
	- API 版本：选择 XML 版本 API。
	- 签名有效时间：签名的有效时间。您可以单击【获取（60分钟有效期）】，即可获取一个有效时长为60分钟的签名。也可以自行输入一个有效的起止时间用于复现在该起止时间下的签名结果。相关签名有效时间的介绍，请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778#.E7.AD.BE.E5.90.8D.E5.86.85.E5.AE.B9)。
![avatar](https://main.qcloudimg.com/raw/6855a2f6b18779037090e0769303bbc7.png)
>?基础信息中的参数均为必填项。


#### 输入 API 密钥信息

在 “API 密钥” 栏中，填写您的 API 密钥信息。如下图所示：
![avatar](https://main.qcloudimg.com/raw/c28b93819a8fdd9e121e6b0702d098d4.png)
API 密钥中的信息均为必填项。
- API 密钥的参数信息可从控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面中获取。
- 填写时，请确保该信息的准确性。填写错误将导致您的签名被视为无效签名。

#### 输入 HTTP 参数信息

在 “HTTP 参数” 栏中，填写相关参数。如下图所示：
![avatar](https://main.qcloudimg.com/raw/8fbc5566b31777e646aa457239468cda.png)
主要参数如下：
- **HttpMethod：**必选项。HTTP 请求方法，包括 GET，POST，PUT，DELETE 四种。
- **HttpURI：**必填项。HTTP 请求 URI 部分，即您需要发起请求的对象名称。
- **HttpParameters：**可选项。HTTP 请求参数。当您需验证 url 参数时可填写该参数。其中，key 小写，value 需要进行 URLEncode，多个 key 以字典排序。
 例如，“prefix=abc” 代表指定访问对象前缀为 abc 的对象。
- **HttpHeaders：**可选项。HTTP 请求头部。当您需验证 url 参数时可填写该参数。其中，key 小写，value 需要进行URLEncode，多个 key 以字典排序。
 例如，“Host: bucket1-1254000000.cos.ap-beijing.myqcloud.com ”代表该签名可访问账户 1254000000 的存储桶 bucket1 下的指定文件。

相关 HTTP 请求参数的详细描述，请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778#signature-.E8.AE.A1.E7.AE.97)。

#### 生成签名及查阅过程参数

单击【生成签名】，即可在右侧的 “结果反馈” 中，查看请求签名结果。如下图所示：
COS 签名工具将分别展示生成的最终签名及计算签名过程中的过程参数。相关过程参数的详细介绍，请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778#signature-.E8.AE.A1.E7.AE.97)。

![avatar](https://main.qcloudimg.com/raw/4e5d3164848078e4ac2dc0b9b767ca00.png)

### JSON 版本签名工具

#### 输入基础配置信息

1. 单击 [COS 签名工具](https://cos5.cloud.tencent.com/static/cos-sign/)，进入 “COS 签名工具” 页面。
2. 在 “基础信息” 栏中，填写 API 版本、存储桶名称以及当前时间。
	- API 版本：选择 JSON 版本 API。
	- 存储桶名称：填写需要访问的存储桶名称，格式如 bucketname-appid。
	- 当前时间：目前系统的时间，是一个符合 Unix Epoch 时间戳规范的数值，单位为秒。您也可以填入一个指定的时间用于复现在指定时间戳下的签名结果。
![avatar](https://main.qcloudimg.com/raw/8b764cd2bef9d2d64a3b8faeb26afff1.png)
>?API 密钥中的信息均为必填项。

#### 输入 API 密钥信息

在 “API 密钥” 栏中，填写您的 API 密钥信息。
该信息为必选项，可从控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面中获取。
填写时，请确保该信息的准确性。填写错误将导致您的签名被视为无效签名。

#### 输入 HTTP 参数信息

在 “HTTP 参数” 栏中，填写相关参数。如下图所示：
![avatar](https://main.qcloudimg.com/raw/621bd5458b8da2dcfc6eea7d707fecbb.png)
主要参数如下：
- **ExpiredTime：**必选项。签名的失效时间，单位为秒。您可以在【当前时间】的参数上加上一个有效时长，得到签名的失效时间。**单次签名时，失效时间必须设置为0**。
- **RandomId：**必选项。无符号10进制整数的随机串。
- **FilePath：**可选项。标识存储资源的相对路径。格式如：`/[dirname]/[filename]`。
   -  当操作对象为文件夹时，filename 缺省。filename 中要包含文件后缀名。
   -  当 FilePath 为空时，生成的请求签名将适用于访问存储桶内所有对象。
 
相关 HTTP 请求参数的详细描述，请参见 [请求签名](https://cloud.tencent.com/document/product/436/6054#.E8.8E.B7.E5.8F.96.E7.AD.BE.E5.90.8D.E6.89.80.E9.9C.80.E4.BF.A1.E6.81.AF)。

#### 生成签名及查阅过程参数

单击【生成签名】，即可在右侧的 “结果反馈” 中，查看请求签名结果。
COS 签名工具将分别展示生成的最终签名及计算签名过程中的过程参数。相关过程参数的详细介绍，请参见 [请求签名](https://cloud.tencent.com/document/product/436/6054#.E8.8E.B7.E5.8F.96.E7.AD.BE.E5.90.8D.E6.89.80.E9.9C.80.E4.BF.A1.E6.81.AF2)。

## 注意事项
- 本签名工具不识别和提示您填写的错误参数。如果您使用本工具计算请求签名并与 SDK 或其他工具的计算结果进行比较，本工具不会主动纠正您填写的错误参数。
- 本签名工具将识别您填写的不合法参数，并进行相应的提示。但仍可能生成一个无法通过签名验证的请求签名。
- 本签名工具将识别及提示您尚未填写的必填参数项，且如果您未完成必填参数项的填写，您将无法生成请求签名。
