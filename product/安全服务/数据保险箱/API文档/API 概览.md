
## 保险箱管理

接口名称 | 接口功能
----- | ---
[PutCoffer](https://cloud.tencent.com/document/product/1232/44720) | 创建保险箱|
[DeleteCoffer](https://cloud.tencent.com/document/product/1232/44721) | 删除保险箱|
[GetService](https://cloud.tencent.com/document/product/1232/44719) | 查询保险箱列表|

## 文件管理

接口名称 | 接口功能
----- | ---
[GetCoffer](https://cloud.tencent.com/document/product/1232/44729) | 获取文件列表|
[GetObject](https://cloud.tencent.com/document/product/1232/44722) | 下载文件|
[HeadObject](https://cloud.tencent.com/document/product/1232/44724)| 获取文件信息|
[PutObject](https://cloud.tencent.com/document/product/1232/44723) | 上传文件|

## 生命周期管理

接口名称 | 接口功能
----- | ---
[PutCofferLifecycle](https://cloud.tencent.com/document/product/1232/44732) | 创建生命周期|
[GetCofferLifecycle](https://cloud.tencent.com/document/product/1232/44790) | 获取生命周期配置|


## 访问策略

接口名称 | 接口功能
----- | ---
[GetCofferPolicy](https://cloud.tencent.com/document/product/1232/44735) | 查看访问策略|
[PutCofferPolicy ](https://cloud.tencent.com/document/product/1232/44736)| 设置访问策略|
[DeleteCofferPolicy](https://cloud.tencent.com/document/product/1232/44734) | 清除访问策略|

## 分片上传

接口名称 | 接口功能
----- | ---
[InitiateMultipartUpload](https://cloud.tencent.com/document/product/1232/44677) | 初始化分片上传 |
[UploadPart](https://cloud.tencent.com/document/product/1232/44742) | 将对象按照分块的方式上传到保险箱|
[ListParts](https://cloud.tencent.com/document/product/1232/44741) | 查询特定分块上传中已上传的块|
[CompleteMultipartUpload](https://cloud.tencent.com/document/product/1232/44739) | 完成整个分块上传 |
[AbortMultipartUpload](https://cloud.tencent.com/document/product/1232/44738) | 舍弃一个分块上传并删除已上传的块|
[ListMultipartUploads](https://cloud.tencent.com/document/product/1232/44740) | 查询正在进行中的分块上传任务|
