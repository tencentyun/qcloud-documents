## 保险箱管理

接口名称 | 接口功能
----- | ---
[GET Service](https://cloud.tencent.com/document/product/1232/44718) | 查询数据保险箱列表|
[DELETE Coffer](https://cloud.tencent.com/document/product/1232/44721) | 删除指定的保险箱|
[PUT Coffer](https://cloud.tencent.com/document/product/1232/44720) | 在指定账号下创建保险箱|

## 文件管理

接口名称 | 接口功能
----- | ---
[GET Coffer](https://cloud.tencent.com/document/product/1232/44729) | 查看保险箱信息并列出部分或者全部对象|
[GET Object](https://cloud.tencent.com/document/product/1232/44722) | 将保险箱中的对象下载至本地|
[PUT Object](https://cloud.tencent.com/document/product/1232/44723) | 将本地的对象上传至指定保险箱中|
[HEAD Object](https://cloud.tencent.com/document/product/1232/44724)| 判断指定对象是否存在并有权限|

## 生命周期管理

接口名称 | 接口功能
----- | ---
[PUT Coffer Lifecycle](https://cloud.tencent.com/document/product/1232/44732) | 创建一个新的生命周期配置以设置过期时间|

## 访问策略

接口名称 | 接口功能
----- | ---
[GET Coffer Policy](https://cloud.tencent.com/document/product/1232/44735) | 查看保险箱权限策略|
[PUT Coffer Policy ](https://cloud.tencent.com/document/product/1232/44736)| 设置保险箱权限策略|
[DELETE Coffer Policy](https://cloud.tencent.com/document/product/1232/44734) | 清除保险箱权限策略|

## 分片上传

接口名称 | 接口功能
----- | ---
Get Coffer Lifecycle | 获取生命周期配置|
[Initiate Multipart Upload](https://cloud.tencent.com/document/product/1232/44677) | 初始化分片上传 |
[Upload Part](https://cloud.tencent.com/document/product/1232/44742) | 将对象按照分块的方式上传到保险箱|
[List Parts](https://cloud.tencent.com/document/product/1232/44741) | 查询特定分块上传中的已上传的块|
[Complete Multipart Upload](https://cloud.tencent.com/document/product/1232/44739) | 完成整个分块上传 |
[Abort Multipart Upload](https://cloud.tencent.com/document/product/1232/44738) | 舍弃一个分块上传并删除已上传的块|
[List Multipart Uploads](https://cloud.tencent.com/document/product/1232/44740) | 查询正在进行中的分块上传任务|