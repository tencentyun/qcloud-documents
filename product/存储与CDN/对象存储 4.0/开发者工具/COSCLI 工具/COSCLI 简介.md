
COSCLI 是腾讯云对象存储（Cloud Object Storage，COS）提供的客户端命令行工具。通过 COSCLI 工具，您可以通过简单的命令行指令对您 COS 中的对象（Object）实现批量上传、下载、删除等操作。

COSCLI 使用 Go 编写，基于 Cobra 框架，支持配置多个存储桶和跨桶操作。您可以通过 `./coscli [command] --help` 来查看 COSCLI 的使用方法。


## 功能列表

- [生成与修改配置文件 -  config](https://cloud.tencent.com/document/product/436/63679)
- [创建存储桶 - mb](https://cloud.tencent.com/document/product/436/63145)
- [删除存储桶 - rb](https://cloud.tencent.com/document/product/436/63667)
- [查询存储桶或文件列表 - ls](https://cloud.tencent.com/document/product/436/63668)
- [获取不同类型文件的统计信息   - du](https://cloud.tencent.com/document/product/436/63146)
- [上传下载或拷贝文件 - cp](https://cloud.tencent.com/document/product/436/63669)
- [同步上传下载或拷贝文件 - sync](https://cloud.tencent.com/document/product/436/63670)
- [删除文件 - rm](https://cloud.tencent.com/document/product/436/63671)
- [获取文件哈希值 -   hash](https://cloud.tencent.com/document/product/436/63672)
- [列出分块上传中产生的碎片   - lsparts](https://cloud.tencent.com/document/product/436/63673)
- [清理碎片 -   abort](https://cloud.tencent.com/document/product/436/63674)
- [取回归档文件 -   restore](https://cloud.tencent.com/document/product/436/63675)
- [获取预签名 URL -   signurl](https://cloud.tencent.com/document/product/436/63676)






