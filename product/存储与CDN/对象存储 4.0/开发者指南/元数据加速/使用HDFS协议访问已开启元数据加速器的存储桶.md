
## 元数据加速器概述

元数据加速器是由腾讯云对象存储（Cloud Object Storage，COS）服务提供的高性能文件系统功能。元数据加速器底层采用了云 HDFS 卓越的元数据管理功能，支持用户通过文件系统语义访问对象存储服务，系统设计指标可以达到2.4Gb/s带宽、10万级 QPS 以及 ms 级延迟。存储桶在开启元数据加速器后，可以广泛应用于大数据、高性能计算、机器学习、AI 等场景。详情请参见 [元数据加速器](https://cloud.tencent.com/document/product/436/56971)。


<dx-alert infotype="explain" title="">
使用元数据加速器需进行申请，请通过 [联系我们](https://cloud.tencent.com/document/product/436/37708) 申请开通此功能。
</dx-alert>



## 使用 HDFS 协议访问的优势

传统基于对象存储 COS 的大数据访问是采用 Hadoop-COS 工具进行访问。Hadoop-COS 工具内部将 HCFS 接口适配为对象存储的 Restful 接口，从而对对象存储上的数据进行访问。但对象存储和文件系统在元数据组织方式上存在差异，导致元数据操作性能上存在性能差异，从而影响了大数据分析性能。
而开启了元数据加速器的 Bucket，完全兼容 HCFS 协议，可以采用原生的 HDFS 接口直接访问，省去 HDFS 协议到对象协议的转换开销外，还可提供原生 HDFS 的一些功能，例如目录原子高效 Rename、文件 Atime、Mtime 更新、高效目录 du 统计、Posix ACL 权限支持等原生特性。


## 操作步骤
1. [创建 COS 存储桶](https://cloud.tencent.com/document/product/436/13309)，并开启元数据加速。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/148ce1336e35c53d3f7ef4cd95e2a35c.png)
2. 单击存储桶 ID 进入详情页，可查看存储桶的相关配置项。
3. 选择左侧菜单栏中的**性能配置** > **元数据加速**，可在控制台进行文件上传和下载操作。如下图所示
![](https://qcloudimg.tencent-cloud.cn/raw/828ad666b7e1755da0a11887b4f9e243.png)
4. 登录 [云 HDFS 控制台](https://console.cloud.tencent.com/chdfs)，在“文件系统”页面上方选择存储桶所在地域，并单击对应的文件系统 ID。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/43fd295cae1d00ae35c6c3fd6fda2e46.png)
5. [](id:step5)进入文件系统的配置页，创建文件系统的权限组和挂载点信息，详情请参见 [创建权限组](https://cloud.tencent.com/document/product/1105/37235)。创建完成后如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f18b78c5fcf9110ede8a86019f86d97a.png)
6. 文件系统配置完成后，即可在大数据集群中挂载已开启元数据加速器的存储桶，详情请参见 [挂载 CHDFS](https://cloud.tencent.com/document/product/1105/36368)。
7. 执行以下命令，测试配置及挂载是否成功。
```
hadoop fs -ls ofs://挂载地址
```
返回结果如下图所示，即代表配置和挂载均已成功。
![](https://qcloudimg.tencent-cloud.cn/raw/c0ea5f78f7a9724277916fa732b774ef.png)
8. 前往 [COS 控制台](https://console.cloud.tencent.com/cos/bucket)，进入存储桶文件列表，查看文件和目录是否一致。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fb09d62399d783351977df1832b2c75e.png)

## 大数据访问
在 `core-stie.xml` 中配置 HDFS 协议相关挂载点信息。
- 挂载点信息请参见 [步骤5](#step5)。
- 相关文档请参见 [CDH 配置 CHDFS 指引](https://cloud.tencent.com/document/product/1105/47062)。

