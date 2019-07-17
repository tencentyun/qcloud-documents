## 适用场景

腾讯云对象存储 COS 支持批量删除多个对象。您可以通过控制台、 API、SDK 等多种方式批量删除对象。

默认情况下，当删除任务都成功完成时，返回的内容通常为空。若有发生错误，则会返回错误信息。

>!单次请求最多可删除1000个对象，若需要删除更多对象，请将列表拆分后分别发送请求。

## 使用方法

### 使用对象存储控制台

您可以使用对象存储控制台批量删除多个对象，详情请参见 [删除对象](https://cloud.tencent.com/document/product/436/13323) 控制台指南文档。

### 使用 REST API

您可以直接使用 REST API 发起删除多个对象请求，详情请参见 [DELETE Multiple Objects](https://cloud.tencent.com/document/product/436/8289) API 文档。

### 使用 SDK

您可以直接调用 SDK 的删除多个对象方法，详情请参见下列各语言 SDK 文档：

- [Android SDK](https://cloud.tencent.com/document/product/436/34536#.E5.88.A0.E9.99.A4.E5.A4.9A.E4.B8.AA.E5.AF.B9.E8.B1.A1)
- [C SDK](https://cloud.tencent.com/document/product/436/35558#.E5.88.A0.E9.99.A4.E5.A4.9A.E4.B8.AA.E5.AF.B9.E8.B1.A1)
- [C++ SDK](https://cloud.tencent.com/document/product/436/35161#.E5.88.A0.E9.99.A4.E5.A4.9A.E4.B8.AA.E5.AF.B9.E8.B1.A1)
- [Go SDK](https://cloud.tencent.com/document/product/436/35057#.E5.88.A0.E9.99.A4.E5.A4.9A.E4.B8.AA.E5.AF.B9.E8.B1.A1)
- [iOS SDK](https://cloud.tencent.com/document/product/436/34107#.E5.88.A0.E9.99.A4.E5.A4.9A.E4.B8.AA.E5.AF.B9.E8.B1.A1)
- [JavaScript SDK](https://cloud.tencent.com/document/product/436/35649#.E5.88.A0.E9.99.A4.E5.A4.9A.E4.B8.AA.E5.AF.B9.E8.B1.A1)
- [Node.js SDK](https://cloud.tencent.com/document/product/436/36119#.E5.88.A0.E9.99.A4.E5.A4.9A.E4.B8.AA.E5.AF.B9.E8.B1.A1)
- [PHP SDK](https://cloud.tencent.com/document/product/436/34282#.E5.88.A0.E9.99.A4.E5.A4.9A.E4.B8.AA.E5.AF.B9.E8.B1.A1)
- [Python SDK](https://cloud.tencent.com/document/product/436/35151#.E5.88.A0.E9.99.A4.E5.A4.9A.E4.B8.AA.E5.AF.B9.E8.B1.A1)
