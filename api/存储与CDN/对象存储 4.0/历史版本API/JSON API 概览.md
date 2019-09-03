腾讯云对象存储服务（COS）相关 JSON API 接口及说明如下：<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }table th:nth-of-type(2) { width: 100px; }</style>

## 目录操作

| API  |  请求方式    | 功能说明  |  
| -- | ----- | -- | 
| [创建目录 API ](https://cloud.tencent.com/document/product/436/6061)   | POST |   在 Bucket 中创建一个新目录 | 
|  [查询目录属性 API ](https://cloud.tencent.com/document/product/436/6063)   | GET  |       查询目录的属性信息 |
|   [列出目录 API ](https://cloud.tencent.com/document/product/436/6062)    | GET  | 列出指定目录下的所有文件目录  |
|  [删除目录 API ](https://cloud.tencent.com/document/product/436/6064)    | POST |  删除指定目录 |

## 文件操作

|   API    | 请求方式 |                   功能说明                   |
| ----- | -- | -------------------------------------- |
|   [简单上传文件 API](https://cloud.tencent.com/document/product/436/6066)     | POST |  上传 ≤ 20MB 的文件到 Bucket   |
|   [初始化分片上传 API](https://cloud.tencent.com/document/product/436/6067)   | POST |   初始化文件分片上传流程  |
|  [逐个上传分片 API](https://cloud.tencent.com/document/product/436/6068)    | POST |  对大于 20 MB 的文件进行逐片上传   |
|  [结束分片上传API](https://cloud.tencent.com/document/product/436/6074)    | POST |  结束文件分片上传流程  | 
|   [查询上传分片 API](https://cloud.tencent.com/document/product/436/6070)     | GET  |  查询分片的断点和 session |
| [查询文件属性 API](https://cloud.tencent.com/document/product/436/6069)   | GET  |  查询文件的属性信息 |
|    [更新文件属性 API](https://cloud.tencent.com/document/product/436/6072)    | POST | 对 COS 中某个文件的属性进行设置或修改   |
|   [复制文件 API]( https://cloud.tencent.com/document/product/436/7419)   | POST  |  将 COS 中指定文件复制一份|
|   [下载文件 API]( https://cloud.tencent.com/document/product/436/8429)   | GET  |  将 COS 中指定文件下载到本地|
|   [移动文件 API](https://cloud.tencent.com/document/product/436/6730)   | POST | 将文件移动或重命名 |
|  [删除文件 API](https://cloud.tencent.com/document/product/436/6073)    | POST | 将 COS 中某个文件删除 |




