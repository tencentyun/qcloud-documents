### 请求地址

COS 提供的Restful API 请求结构如下：

`web.file.myqcloud.com/files/v1/[appid]/[bucket_name]`



### 字段限制

appid：数字

bucket_name：为字母、数字

url：总长度不超过2048字节



### Header 通用内容

| **参数名称**      | **必选** | **类型** | **描述**                            |
| ------------- | ------ | ------ | --------------------------------- |
| Host          | 是      | String | 文件云服务器域名，固定为web.file.myqcloud.com |
| Authorization | 是      | String | 签名,用于鉴权. 格式为：[有效签名]               |



Header 格式要求

Content-Type: **application/json**

Content-Length: xxx



### API概览

|  功能  | 请求方式 |      详细说明      |
| :--: | :--: | :------------: |
| 创建目录 | POST | [创建目录API说明](/doc/product/227/创建目录) |
| 目录列表 | GET  | [目录列表API说明](/doc/product/227/目录列表) |
| 目录更新 | POST | [目录更新API说明](/doc/product/227/目录更新) |
| 目录查询 | GET  | [目录查询API说明](/doc/product/227/目录查询) |
| 删除目录 | POST | [删除目录API说明](/doc/product/227/删除目录) |
| 上传文件 | POST | [上传文件API说明](/doc/product/227/创建文件) |
| 文件分片 | POST | [文件分片API说明](/doc/product/227/文件分片) |
| 文件更新 | POST | [文件更新API说明](/doc/product/227/文件更新) |
| 文件查询 | GET  | [文件查询API说明](/doc/product/227/文件查询) |
| 删除对象 | POST | [删除文件API说明](/doc/product/227/删除对象) |