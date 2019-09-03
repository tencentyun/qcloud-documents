## 适用场景

在默认情况下，存储桶和对象都是私有的。如果您希望第三方可以下载对象，又不希望对方使用 CAM 账户或临时密钥等方式时，您可以使用预签名 URL 的方式将签名提交给第三方，以供完成下载操作。收到有效预签名 URL 的任何人都可以下载对象。

预签名 URL 时，您可以在签名中设置将对象键包含在签名中，只允许下载指定的对象。您也可以在程序中指定预签名 URL 的有效时间，以保证超时后该 URL 不会被未授权方使用。

## 使用方法

### 使用 SDK

您可以直接调用 SDK 的预签名 URL 方法，详情请参见下列各语言 SDK 文档：

- [Android SDK](https://cloud.tencent.com/document/product/436/34538)
- [C++ SDK](https://cloud.tencent.com/document/product/436/35163)
- [C# SDK](https://cloud.tencent.com/document/product/436/32873)
- [Go SDK](https://cloud.tencent.com/document/product/436/35059)
- [iOS SDK](https://cloud.tencent.com/document/product/436/34109)
- [Java SDK](https://cloud.tencent.com/document/product/436/35217)
- [JavaScript SDK](https://cloud.tencent.com/document/product/436/35651)
- [Node.js SDK](https://cloud.tencent.com/document/product/436/36121)
- [PHP SDK](https://cloud.tencent.com/document/product/436/34284)
- [Python SDK](https://cloud.tencent.com/document/product/436/35153)
