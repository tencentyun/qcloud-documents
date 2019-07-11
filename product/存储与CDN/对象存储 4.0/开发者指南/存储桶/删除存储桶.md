## 适用场景
当您在某些情况下需要删除存储桶时，您可以通过控制台、API 或 SDK 的方式来删除存储桶。

>!目前仅支持删除已经清空的存储桶，如果存储桶中仍有对象，将会删除失败。请在执行删除存储桶前确保存储桶内已经没有对象。

当删除存储桶时，您需要确保操作的身份已被授权该操作，并确认传入了正确的存储桶名称（Bucket）和地域（Region）参数。

## 使用方法

### 使用对象存储控制台

您可以使用对象存储控制台删除存储桶，详情请参见 [删除存储桶](https://cloud.tencent.com/document/product/436/32433) 控制台指南文档。

### 使用 REST API

您可以直接使用 REST API 发起删除存储桶请求，详情请参见 [DELETE Bucket](https://cloud.tencent.com/document/product/436/7732) API 文档。

### 使用 SDK

您可以直接调用 SDK 的删除存储桶方法，详情请参见下列各语言 SDK 文档：

- [Android SDK](https://cloud.tencent.com/document/product/436/34535#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [C SDK](https://cloud.tencent.com/document/product/436/35557#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [C++ SDK](https://cloud.tencent.com/document/product/436/35160#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [C# SDK](https://cloud.tencent.com/document/product/436/32820#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [Go SDK](https://cloud.tencent.com/document/product/436/35056#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [iOS SDK](https://cloud.tencent.com/document/product/436/34106#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [Java SDK](https://cloud.tencent.com/document/product/436/35214#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [JavaScript SDK](https://cloud.tencent.com/document/product/436/35648#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [Node.js SDK](https://cloud.tencent.com/document/product/436/36118#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [PHP SDK](https://cloud.tencent.com/document/product/436/34277#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)
- [Python SDK](https://cloud.tencent.com/document/product/436/35150#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6)

