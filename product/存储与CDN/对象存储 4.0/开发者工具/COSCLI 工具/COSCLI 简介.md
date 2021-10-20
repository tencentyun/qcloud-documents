
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
      <td><a href="https://cloud.tencent.com/document/product/436/63145#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6---mb">创建存储桶 - mb</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63145#.E5.88.A0.E9.99.A4.E5.AD.98.E5.82.A8.E6.A1.B6---rb">删除存储桶 - rb</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63145#.E5.88.97.E5.87.BA.E5.AD.98.E5.82.A8.E6.A1.B6.E6.88.96.E6.96.87.E4.BB.B6---ls">列出存储桶或文件 - ls</a></td>
   </tr>
   <tr>
      <td rowspan=9>常用对象命令</td>
      <td><a href="https://cloud.tencent.com/document/product/436/63146#.E8.8E.B7.E5.8F.96.E4.B8.8D.E5.90.8C.E7.B1.BB.E5.9E.8B.E6.96.87.E4.BB.B6.E7.9A.84.E7.BB.9F.E8.AE.A1.E4.BF.A1.E6.81.AF---du">获取不同类型文件的统计信息 - du</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63146#.E4.B8.8A.E4.BC.A0.E3.80.81.E4.B8.8B.E8.BD.BD.E3.80.81.E6.8B.B7.E8.B4.9D.E6.96.87.E4.BB.B6---cp">上传、下载、拷贝文件 - cp</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63146#.E5.90.8C.E6.AD.A5.E4.B8.8A.E4.BC.A0.E3.80.81.E4.B8.8B.E8.BD.BD.E3.80.81.E6.8B.B7.E8.B4.9D.E6.96.87.E4.BB.B6---sync">同步上传、下载、拷贝文件 - sync</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63146&!preview#.E5.88.A0.E9.99.A4.E6.96.87.E4.BB.B6---rm">删除文件 - rm</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63146#.E8.8E.B7.E5.8F.96.E6.96.87.E4.BB.B6.E5.93.88.E5.B8.8C.E5.80.BC---hash">获取文件哈希值 - hash</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63146#.E5.88.97.E5.87.BA.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0.E4.B8.AD.E4.BA.A7.E7.94.9F.E7.9A.84.E7.A2.8E.E7.89.87---lsparts">列出分块上传中产生的碎片 - lsparts</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63146#.E6.B8.85.E7.90.86.E7.A2.8E.E7.89.87---abort">清理碎片 - abort</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63146#.E5.8F.96.E5.9B.9E.E5.BD.92.E6.A1.A3.E6.96.87.E4.BB.B6---restore">取回归档文件 - restore</a></td>
   </tr>
   <tr>
      <td><a href="https://cloud.tencent.com/document/product/436/63146#.E8.8E.B7.E5.8F.96.E9.A2.84.E7.AD.BE.E5.90.8D-url---signurl">获取预签名 URL - signurl</a></td>
   </tr>
</table>






