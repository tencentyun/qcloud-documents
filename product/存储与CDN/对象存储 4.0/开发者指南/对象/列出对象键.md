## 适用场景

腾讯云 COS 支持按照前缀顺序列出对象键，您也可以在对象键中使用`/`字符来实现类似传统文件系统的层级结构，COS 也支持按照分隔符来做层级结构的选择和浏览。

您可以列出单个存储桶中的所有对象键，根据前缀的 UTF-8 二进制顺序列出，或选择指定前缀过滤对象键的列表。例如加入参数`t`将列出`tencent`的对象，而跳过以`a`或其他字符为前缀的对象。

加入`/`分隔符可将根据此分隔符重新组织对象键，您可以结合前缀和分隔符来实现类似文件夹检索的功能。例如加入前缀参数`t`并加入分隔符`/`将会直接列出类似`tencent/cos`的对象键。

腾讯云 COS 在单个存储桶中支持无限数量的对象，因此对象键列表可能非常大。为了管理方便，单个列出对象接口将最多返回1000个键值的结果内容，同时会返回指示器来告知是否存在截断。您可以根据指示器和分隔符来发送一系列的列出对象键请求，实现列出所有键值，或寻找您所需要的内容。

## 使用方法

### 使用 REST API

您可以直接使用 REST API 发起列出对象键请求，详情请参见 [GET Bucket](https://cloud.tencent.com/document/product/436/7734) API 文档。

### 使用 SDK

您可以直接调用 SDK 的查询对象列表方法，详情请参见下列各语言 SDK 文档：

- [Android SDK](https://cloud.tencent.com/document/product/436/34536#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [C SDK](https://cloud.tencent.com/document/product/436/35558#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [C++ SDK](https://cloud.tencent.com/document/product/436/35161#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [C# SDK](https://cloud.tencent.com/document/product/436/32869#.E8.8E.B7.E5.8F.96.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [Go SDK](https://cloud.tencent.com/document/product/436/35057#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [iOS SDK](https://cloud.tencent.com/document/product/436/34107#.E8.8E.B7.E5.8F.96.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [Java SDK](https://cloud.tencent.com/document/product/436/35215#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [JavaScript SDK](https://cloud.tencent.com/document/product/436/35649#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [Node.js SDK](https://cloud.tencent.com/document/product/436/36119#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [PHP SDK](https://cloud.tencent.com/document/product/436/34282#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [Python SDK](https://cloud.tencent.com/document/product/436/35151#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
- [小程序 SDK](https://cloud.tencent.com/document/product/436/31953#.E6.9F.A5.E8.AF.A2.E5.AF.B9.E8.B1.A1.E5.88.97.E8.A1.A8)
