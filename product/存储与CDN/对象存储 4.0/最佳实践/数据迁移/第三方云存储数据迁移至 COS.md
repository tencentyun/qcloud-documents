## 实践背景

对于使用第三方云平台存储的用户，对象存储（Cloud Object Storage，COS）可以帮助用户将第三方云平台的存储数据快速迁移至 COS。


| 迁移方式&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 交互形式       | 区分大小文件的阈值 | 迁移并发度 | HTTPS 安全传输 |
| ------------------------------------------------------------ | -------------- | ------------------ | ---------- | -------------- |
| [迁移服务平台 MSP](#msp)                                     | 可视化页面操作 | 采用默认设置       | 全局统一   | 开启           |


该平台支持查看数据迁移进度、文件一致性校验、失败重传、断点续传等功能，能够满足用户数据基本的迁移需求。


## 迁移实践

<span id=msp></span>

### 迁移服务平台 MSP

迁移服务平台（Migration Service Platform，MSP）是集成了多种迁移工具，并且提供可视化界面的平台，能够帮助用户轻松监控和管理大规模的数据迁移任务。其中“文件迁移工具”能够帮助用户将数据从各类公有云或数据源站中迁移至 COS。

迁移操作步骤如下：

1. 登录 [迁移服务平台控制台](https://console.cloud.tencent.com/msp)。
2. 在左导航栏中单击**对象存储迁移**，进入对象存储迁移页面。
3. 单击**新建任务**，新建迁移任务并配置任务信息。
4. 启动任务。

具体操作可参见以下迁移教程：

- [阿里云 OSS 迁移](https://cloud.tencent.com/document/product/659/37855)
- [华为云 OBS 迁移](https://cloud.tencent.com/document/product/659/65762)
- [七牛云 KODO 迁移](https://cloud.tencent.com/document/product/659/38008)
- [UCLOUD UFile 迁移](https://cloud.tencent.com/document/product/659/38003)
- [金山云 KS3 迁移](https://cloud.tencent.com/document/product/659/38007)
- [百度云 BOS 迁移](https://cloud.tencent.com/document/product/659/38006)
- [AWS S3 迁移](https://cloud.tencent.com/document/product/659/38799)

#### 操作技巧

在进行数据迁移过程中，数据源的读取速度会因为不同的网络环境而有所不同，但客户根据实际状况在“新建文件迁移任务”时选择较高的 QPS 并发度，有助于提高迁移速度。

<span id=cos>



