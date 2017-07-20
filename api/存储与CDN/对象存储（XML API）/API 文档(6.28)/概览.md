腾讯云对象存储服务（COS）相关接口及说明如下：

## 关于 Service 操作
<style rel="stylesheet">
table th:nth-of-type(1) {
width: 350px;	
}
table th:nth-of-type(2) {
width:550px;	
}
</style>

| API | 描述 |
|---------|---------|
| [Get Service](https://www.qcloud.com/document/product/436/8291) | 列出该账户下所有 Bucket  | 

## 关于 Bucket 操作

| API | 描述 |
|---------|---------|
| [Get Bucket](https://www.qcloud.com/document/product/436/7734) | 列出指定 Bucket 下的部分或者全部 Object | 
| [Get Bucket ACL](https://www.qcloud.com/document/product/436/7733) | 获取 Bucket 的 ACL 表 | 
| [Get Bucket CORS](https://www.qcloud.com/document/product/436/8274) | 获取 Bucket 的跨域访问配置信息 | 
| [Get Bucket Location](https://www.qcloud.com/document/product/436/8275) | 获取 Bucket 所在的地域信息 | 
| [Put Bucket](https://www.qcloud.com/document/product/436/7738) | 在指定账号下创建一个 Bucket | 
| [Put Bucket ACL ](https://www.qcloud.com/document/product/436/7737)| 写入 Bucket 的 ACL 表 | 
| [Put Bucket CORS](https://www.qcloud.com/document/product/436/8279) | 配置 Bucket 的跨域访问权限 | 
| [Delete Bucket](https://www.qcloud.com/document/product/436/7732) | 删除指定账号下的 Bucket  | 
| [Delete Bucket CORS](https://www.qcloud.com/document/product/436/8283) | 删除 Bucket 的跨域访问权限配置  | 
| [Head Bucket](https://www.qcloud.com/document/product/436/7735) | 确认指定账号下是否存在指定 Bucket | 
| [List Multipart Uploads](https://www.qcloud.com/document/product/436/7736) | 查询正在进行中的分块上传信息 | 

## 关于 Object 操作

| API | 描述 |
|---------|---------|
| [Append Object](https://www.qcloud.com/document/product/436/7741) | 将一个Object（文件/对象）以分块追加的方式上传至指定 Bucket  | 
| [Get Object](https://www.qcloud.com/document/product/436/7753) | 将一个Object（文件/对象）下载至本地 | 
| [Get Object ACL](https://www.qcloud.com/document/product/436/7744) | 获取 Object（文件/对象）的ACL表 | 
| [Put Object](https://www.qcloud.com/document/product/436/7749) | 将一个Object（文件/对象）上传至指定 Bucket  | 
| [Put Object ACL](https://www.qcloud.com/document/product/436/7748) | 写入 Object （文件/对象）的 ACL 表 | 
| [Delete Object](https://www.qcloud.com/document/product/436/7743) | 在 Bucket 中删除指定 Object （文件/对象） | 
| [Delete Multiple Object](https://www.qcloud.com/document/product/436/8289) | 在 Bucket 中批量删除 Object （文件/对象） | 
| [Head Object](https://www.qcloud.com/document/product/436/7745) | 获得 Object 的 meta 信息 | 
| [Options Object](https://www.qcloud.com/document/product/436/8288) | 跨域访问 preflight 请求| 
| [Initiate Multipart Upload](https://www.qcloud.com/document/product/436/7746) | 初始化 Multipart Upload 上传操作 | 
| [Upload Part](https://www.qcloud.com/document/product/436/7750) | 分块上传文件 | 
| [List Parts](https://www.qcloud.com/document/product/436/7747) | 查询特定分块上传操作中的已上传的块 | 
| [Complete Multipart Upload](https://www.qcloud.com/document/product/436/7742) | 完成整个文件的分块上传 | 
| [Abort Multipart Upload](https://www.qcloud.com/document/product/436/7740) | 实现舍弃一个分块上传操作并删除已上传的块 | 


