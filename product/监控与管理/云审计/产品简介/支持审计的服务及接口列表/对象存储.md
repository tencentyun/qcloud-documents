对象存储（Cloud Object Storage，COS）是腾讯云提供的一种存储海量文件的分布式存储服务，具有高扩展性、低成本、可靠安全等优点。通过控制台、API、SDK 和工具等多样化方式，用户可简单、快速地接入 COS，进行多格式文件的上传、下载和管理，实现海量数据存储和管理。

下表为云审计支持的对象存储操作列表：

| 操作名称                    | 资源类型 | 事件名称                    |
|-------------------------|------|-------------------------|
| 删除 Bucket               | cos  | DeleteBucket            |
| 删除 BucketCORS           | cos  | DeleteBucketCORS        |
| 删除 Domain                | cos  | DeleteBucketDomain      |
| 删除 bucket 加密设置            | cos  | DeleteBucketEncryption  |
| 删除 Inventory             | cos  | DeleteBucketInventory   |
| 删除 Bucket 的生命周期配置       | cos  | DeleteBucketLifecycle   |
| BucketWrite\_All        | cos  | DeleteBucketOrigin      |
| 删除 Bucket 权限策略          | cos  | DeleteBucketPolicy      |
| DeleteBucketReplication | cos  | DeleteBucketReplication |
| DeleteBucketTagging     | cos  | DeleteBucketTagging     |
| DeleteBucketWebsite     | cos  | DeleteBucketWebsite     |
| DeleteObjectTagging     | cos  | DeleteObjectTagging     |
| GetBucketAccelerate     | cos  | GetBucketAccelerate     |
| 读 bucket acp 操作组          | cos  | GetBucketACL            |
| GetBucketCORS           | cos  | GetBucketCORS           |
| 获取 Domain                | cos  | GetBucketDomain         |
| 获取 bucket加密              | cos  | GetBucketEncryption     |
| 获取 Inventory             | cos  | GetBucketInventory      |
| GetBucketLifecycle      | cos  | GetBucketLifecycle      |
| GetBucketLogging        | cos  | GetBucketLogging        |
| GetBucketNotification   | cos  | GetBucketNotification   |
| GetBucketObjectVersions | cos  | GetBucketObjectVersions |
| BucketRead\_All         | cos  | GetBucketOrigin         |
| GetBucketPolicy         | cos  | GetBucketPolicy         |
| GetBucketReferer        | cos  | GetBucketReferer        |
| GetBucketReplication    | cos  | GetBucketReplication    |
| GetBucketTagging        | cos  | GetBucketTagging        |
| GetBucketVersioning     | cos  | GetBucketVersioning     |
| GetBucketWebsite        | cos  | GetBucketWebsite        |
| 读 obj acp 操作组             | cos  | GetObjectACL            |
| GetObjectTagging        | cos  | GetObjectTagging        |
| GetService              | cos  | GetService              |
| ListMultipartUploads    | cos  | ListMultipartUploads    |
| 恢复归档文件                  | cos  | PostObjectRestore       |
| PutBucket               | cos  | PutBucket               |
| PutBucketAccelerate     | cos  | PutBucketAccelerate     |
| 写 bucket acl 操作组          | cos  | PutBucketACL            |
| PutBucketCORS           | cos  | PutBucketCORS           |
| 设置 Domain                | cos  | PutBucketDomain         |
| 设置 bucket 加密              | cos  | PutBucketEncryption     |
| 设置 Inventory             | cos  | PutBucketInventory      |
| PutBucketLifecycle      | cos  | PutBucketLifecycle      |
| PutBucketLogging        | cos  | PutBucketLogging        |
| PutBucketNotification   | cos  | PutBucketNotification   |
| PutBucketOrigin         | cos  | PutBucketOrigin         |
| PutBucketPolicy         | cos  | PutBucketPolicy         |
| PutBucketReferer        | cos  | PutBucketReferer        |
| PutBucketReplication    | cos  | PutBucketReplication    |
| PutBucketTagging        | cos  | PutBucketTagging        |
| PutBucketVersioning     | cos  | PutBucketVersioning     |
| PutBucketWebsite        | cos  | PutBucketWebsite        |
| PutObjectTagging        | cos  | PutObjectTagging        |
