## 适用场景

分块上传适合于在弱网络或高带宽环境下上传较大的对象。COS 的控制台和 SDK 会协助您将单个对象切成一组分块并完成上传，您也可以自行切分对象并分别调用 API 上传各个分块。分块上传优势如下：

- 在弱网络环境中，使用较小的分块可以将网络失败导致的中断影响降低，实现对象续传。
- 在高带宽环境中，并发上传对象分块能充分利用网络带宽，乱序上传并不影响最终组合对象。
- 使用分块上传，您可以随时暂停和恢复单个大对象的上传。除非发起终止操作，所有未完成的对象将可随时继续上传。
- 分块上传也适用于在未知对象总大小的情况下上传对象，您可以先发起上传，再组合对象以获得完整大小。

上传时，这组分块将会按连续的序号编号，您可以独立上传或者按照任意顺序上传各个分块，最终 COS 将会根据分块编号顺序重新组合出该对象。任意分块传输失败，都可以重新传输当前分块，不会影响其他分块和内容完整性。一般在弱网络环境中，当单个对象大于20MB可优先考虑分块上传，在大带宽环境中可将超过100MB的对象进行分块上传。

## 使用方法

### 使用 REST API

您可以直接使用 REST API 发起分块上传请求，详情请参见以下 API 文档：

- [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746)
- [Upload Part](https://cloud.tencent.com/document/product/436/7750)
- [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742)
- [Abort Multipart Upload](https://cloud.tencent.com/document/product/436/7740)

### 使用 SDK

您可以直接调用 SDK 的分块操作方法，详情请参见下列各语言 SDK 文档：

- [Android SDK](https://cloud.tencent.com/document/product/436/34536#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
- [C SDK](https://cloud.tencent.com/document/product/436/35558#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
- [C++ SDK](https://cloud.tencent.com/document/product/436/35161#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
- [C# SDK](https://cloud.tencent.com/document/product/436/32869#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
- [Go SDK](https://cloud.tencent.com/document/product/436/35057#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
- [iOS SDK](https://cloud.tencent.com/document/product/436/34107#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
- [Java SDK](https://cloud.tencent.com/document/product/436/35215#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
- [JavaScript SDK](https://cloud.tencent.com/document/product/436/35649#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
- [Node.js SDK](https://cloud.tencent.com/document/product/436/36119#.E6.9F.A5.E8.AF.A2.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0)
- [PHP SDK](https://cloud.tencent.com/document/product/436/34282#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
- [Python SDK](https://cloud.tencent.com/document/product/436/35151#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)
