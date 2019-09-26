## 适用场景

利用生命周期设置，可以让符合规则的对象在指定的条件下自动执行一些操作。例如：

- 转换存储类型：将创建的对象在指定时间后转换为低频存储类型 STANDARD_IA 或者归档存储类型 ARCHIVE。
- 过期删除：设置对象的过期时间，使对象到期后被自动删除。

详情请参见 [生命周期概述](https://cloud.tencent.com/document/product/436/17028) 文档和 [生命周期配置元素](https://cloud.tencent.com/document/product/436/17029) 文档。

## 使用方法

### 使用对象存储控制台

您可以使用对象存储控制台配置生命周期，详情请参见 [设置生命周期](https://cloud.tencent.com/document/product/436/14605) 控制台指南文档。

### 使用 REST API

您可以直接使用 REST API 配置和管理存储桶中对象的生命周期，详情请参见以下 API 文档：

- [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/8280)
- [GET Buket lifecycle](https://cloud.tencent.com/document/product/436/8278)
- [DELETE Bucket lifecycle](https://cloud.tencent.com/document/product/436/8284)

### 使用 SDK

您可以直接调用 SDK 的生命周期方法，详情请参见下列各语言 SDK 文档：

- [Android SDK](https://cloud.tencent.com/document/product/436/34537#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [C SDK](https://cloud.tencent.com/document/product/436/35559#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [C++ SDK](https://cloud.tencent.com/document/product/436/35162#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [C# SDK](https://cloud.tencent.com/document/product/436/32872#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [Go SDK](https://cloud.tencent.com/document/product/436/35058#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [iOS SDK](https://cloud.tencent.com/document/product/436/34108#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [Java SDK](https://cloud.tencent.com/document/product/436/35216#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [JavaScript SDK](https://cloud.tencent.com/document/product/436/35650#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [Node.js SDK](https://cloud.tencent.com/document/product/436/36120#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [PHP SDK](https://cloud.tencent.com/document/product/436/34283#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
- [Python SDK](https://cloud.tencent.com/document/product/436/35152#.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F)
