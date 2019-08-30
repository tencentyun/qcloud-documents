## 适用场景

在开始使用 COS 时，您需要先创建一个存储桶以便于对象的使用和管理。您可以通过控制台、API 或 SDK 的方式来创建存储桶。

当存储桶不存在时，您可以使用以下代码示例在指定地域创建存储桶，存储桶支持的参数为：

- Bucket：用于指定您的完整存储桶名称，形如`examplebucket-1250000000`。
- Region：选择您的存储桶所属地域，一旦存储桶创建完成，地域将无法修改，前往查看 COS 支持的 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。

## 使用方法

### 使用对象存储控制台

您可以使用对象存储控制台创建存储桶，详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 控制台指南文档。

### 使用 REST API

您可以直接使用 REST API 发起创建存储桶请求，详情请参见 [PUT Bucket](https://cloud.tencent.com/document/product/436/7738) API 文档。

### 使用 SDK

您可以直接调用 SDK 的创建存储桶方法，详情请参见下列各语言 SDK 文档：

- [Android SDK](https://cloud.tencent.com/document/product/436/34535#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [C SDK](https://cloud.tencent.com/document/product/436/35557#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [C++ SDK](https://cloud.tencent.com/document/product/436/35160#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [C# SDK](https://cloud.tencent.com/document/product/436/32820#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [Go SDK](https://cloud.tencent.com/document/product/436/35056#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [iOS SDK](https://cloud.tencent.com/document/product/436/34106#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [Java SDK](https://cloud.tencent.com/document/product/436/35214#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [Node.js SDK](https://cloud.tencent.com/document/product/436/36118#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [PHP SDK](https://cloud.tencent.com/document/product/436/34277#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [Python SDK](https://cloud.tencent.com/document/product/436/35150#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
- [小程序 SDK](https://cloud.tencent.com/document/product/436/31953#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)
