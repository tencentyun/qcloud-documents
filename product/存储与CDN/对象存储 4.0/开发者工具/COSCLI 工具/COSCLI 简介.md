
COSCLI 是腾讯云对象存储（Cloud Object Storage，COS）提供的客户端命令行工具。通过 COSCLI 工具，您可以通过简单的命令行指令对您 COS 中的对象（Object）实现批量上传、下载、删除等操作。

COSCLI 使用 Go 编写，基于 Cobra 框架，支持配置多个存储桶和跨桶操作。您可以通过 `./coscli [command] --help` 来查看 COSCLI 的使用方法。


## 功能列表

<table>
   <tr>
      <th>类型</td>
      <th>操作命令</td>
   </tr>
   <tr>
      <td rowspan=3>常用存储桶命令</td>
      <td><a href="https://cloud.tencent.com/document/product/436/63145">创建存储桶 - mb</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63145">删除存储桶 - rb</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63668">查询存储桶或文件列表 - ls</a></td>
   </tr>
   <tr>
      <td rowspan=9>常用对象命令</td>
      <td><a href="https://cloud.tencent.com/document/product/436/63146">获取不同类型文件的统计信息 - du</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63669">上传下载及拷贝文件 - cp</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63670">同步上传下载及拷贝文件 - sync</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63671">删除文件 - rm</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63672">获取文件哈希值 - hash</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63673">列出分块上传中产生的碎片 - lsparts</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63674">清理碎片 - abort</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63675">取回归档文件 - restore</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63676">获取预签名 URL - signurl</a></td>
   </tr>
</table>






