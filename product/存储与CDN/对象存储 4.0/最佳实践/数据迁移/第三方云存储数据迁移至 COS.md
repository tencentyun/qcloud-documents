## 实践背景

对于使用第三方云平台存储的用户，对象存储 COS 支持以下两种迁移方式，帮助用户将第三方云平台的存储数据快速迁移至对象存储 COS。


| 迁移方式&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 交互形式                   | 区分大小文件的阈值 | 迁移并发度                     | HTTPS 安全传输                         |
| ------------------------------------------------------------ | -------------------------- | ------------------ | ------------------------------ | -------------------------------------- |
| [迁移服务平台 MSP](#msp)                                     | 可视化页面操作             | 采用默认设置       | 全局统一                       | 开启                                   |
| [COS Migration](#cos)                                        | 修改配置文件，非可视化操作 | 可自定义调整       | 针对大文件小文件分别定义并发度 | 可选择是否开启，关闭有利于加快迁移速度 |


这两种迁移方式都支持查看数据迁移进度、文件一致性校验、失败重传、断点续传等功能，能够满足用户数据基本的迁移需求。但这两种迁移方式在交互形式和功能特点等方面又有所差别，如上表所示。用户可根据以上的差异对比，选择最适合的一种方式进行数据迁移。


## 迁移实践

<span id=msp>

### 迁移服务平台 MSP

迁移服务平台 MSP 是集成了多种迁移工具，并且提供可视化界面的平台，能够帮助用户轻松监控和管理大规模的数据迁移任务。其中“文件迁移工具”能够帮助用户将数据从各类公有云或数据源站中迁移至对象存储 COS。

迁移操作步骤如下：

1. 登录 [迁移服务平台 MSP](https://console.cloud.tencent.com/msp)。
2. 在左导航栏中单击【对象存储迁移】，进入对象存储迁移页面。
3. 单击【新建任务】，新建迁移任务并配置任务信息。
4. 启动任务。

具体操作可参见以下迁移教程：

- [阿里云 OSS 迁移](https://cloud.tencent.com/document/product/659/37855)
- [七牛云 KODO 迁移](https://cloud.tencent.com/document/product/659/38008)
- [UCLOUD UFile 迁移](https://cloud.tencent.com/document/product/659/38003)
- [金山云 KS3 迁移](https://cloud.tencent.com/document/product/659/38007)
- [百度云 BOS 迁移](https://cloud.tencent.com/document/product/659/38006)
- [AWS S3 迁移](https://cloud.tencent.com/document/product/659/38799)

#### 操作技巧

在进行数据迁移过程中，数据源的读取速度会因为不同的网络环境而有所不同，但客户根据实际状况在“新建文件迁移任务”时选择较高的 QPS 并发度，有助于提高迁移速度 。





<span id=cos>

### COS Migration 

COS Migration 是一个集成了 COS 数据迁移功能的一体化工具。用户只需要通过简单的配置操作，便可将数据快速迁移至 COS 中。

迁移操作步骤如下：

1. 安装 Java 环境。
2. 安装 COS Migration 工具。
3. 修改配置文件。
4. 启动工具。

具体的操作方法，请参见 [COS Migration 工具](https://cloud.tencent.com/document/product/436/15392) 文档。

#### 操作技巧

下面介绍如何配置 COS Migration 能最大程度提高迁移速度：

1. 根据自身网络环境调整区分大小文件的阈值和迁移并发度，实现大文件分块，小文件并发传输的最佳迁移方式。调整工具执行时间和设立带宽限制，保证自身业务运行不受迁移数据带宽占用影响。上述调整可在配置文件 config.ini 中`[common]`分节，修改如下参数进行调整：
<table>
   <tr>
      <th>参数名称</td>
      <th>参数说明</td>
   </tr>
   <tr>
      <td>smallFileThreshold</td>
      <td>小文件阈值参数，大于等于这个阈值使用分块上传，默认设置为5MB。</td>
   </tr>
   <tr>
      <td>bigFileExecutorNum</td>
      <td>大文件并发度，默认值为8。<br>如果是通过外网来连接 COS，且带宽较小，请减小该并发度。</td>
   </tr>
   <tr>
      <td>smallFileExecutorNum</td>
      <td>小文件并发度，默认值为64。<br>如果是通过外网来连接 COS，且带宽较小，请减小该并发度。</td>
   </tr>
   <tr>
      <td>executeTimeWindow</td>
      <td>该参数定义迁移工具每天执行的时间段，其他时间则会进入休眠状态，休眠状态暂停迁移并会保留迁移进度，直到下一个时间窗口自动继续执行。</td>
   </tr>
</table>
2. 采用分布式并行传输可以进一步加快迁移速度。用户可以考虑使用多台机器安装 COS Migration 并分别执行不同源数据的迁移任务。



