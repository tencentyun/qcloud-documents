### 迁移工具中途异常退出怎么办？

工具支持上传时断点续传, 对于一些大文件，如果中途退出或者因为服务故障，可重新运行工具，会对未上传完的文件进行续传。

### 对于迁移成功的文件，用户通过控制台或其他方式删除了 COS 上的文件，迁移工具会将这些文件进行重新上传吗？

不会。原因是，所有迁移成功的文件会被记录在 db 中，迁移工具运行之前会先扫描 db 目录，对于已被记录的文件不会再次上传，具体原因请参照 [迁移机制及流程](https://cloud.tencent.com/document/product/436/15392#.E8.BF.81.E7.A7.BB.E6.9C.BA.E5.88.B6.E5.8F.8A.E6.B5.81.E7.A8.8B)。

### 迁移失败，日志显示403 Access Deny，该如何处理？

请确认密钥信息，Bucket 信息，Region 信息是否正确，并且是否具有操作权限。如果是子账号，请让父账号授予相应的权限；如果是本地迁移和其他云存储迁移，需要对 Bucket 具有数据写入和读取权限；如果是 Bucket copy，还需要对源 Bucket 具有数据读取权限。

### 从其他云存储迁移 COS 失败，显示 Read timed out，该如何处理？

一般来说，这种失败情况是由网络带宽不足所造成，导致从其他云存储下载数据超时。例如，将 AWS 海外的数据迁移到 COS，在下载数据到本地时由于带宽能力不足，导致时延较高，可能会出现 read time out。因此，解决方法为增大机器的网络带宽能力，建议在迁移之前用 wget 测试下载速度。

### 迁移失败，日志显示503 Slow Down，该如何处理？

这是触发频控所导致，COS 目前对一个账号具有每秒30000QPS 的操作限制。建议调小配置中小文件的并发度,，并重新运行工具，则会将失败的重新运行。

### 迁移失败，日志显示404 NoSuchBucket，该如何处理？

请确认您的密钥信息，Bucket 信息，Region 信息是否正确。

### 运行异常，显示如下的信息该怎么办?

![img](https://main.qcloudimg.com/raw/9fdac231af66c991c13fe0440e8d7366.png)
此问题是因为工具使用了 rocksdb，需要使用64位的 JDK，请检查 JDK 版本是 X64的 JDK 。

### 在 Windows 环境下报找不到 rocksdb 的 jni 库，该如何处理？
在 Windows 环境下，工具需要在 Microsoft Visual Studio 2015环境下编译。若出现以上报错，需安装 [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/zh-CN/download/details.aspx?id=48145)。

### 如何修改日志级别？
修改文件 src/main/resources/log4j.properties，把 log4j.rootLogger 的值复制为对应的日志级别，如 DEBUG、INFO、ERROR。

如遇其他问题，请您尝试重新运行迁移工具。若仍然失败，请将配置信息（密钥信息请隐藏）与 log 目录打包后 [提交工单](https://console.cloud.tencent.com/workorder/category)。
