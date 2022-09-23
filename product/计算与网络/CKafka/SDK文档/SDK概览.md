消息队列 CKafka 支持多语言SDK，客户端可以通过VPC网络和公网访问两种方式接入 CKafka 并收发消息。两种接入方式对应的协议说明如下：

| 网络 | VPC 网络                                                     | 公网域名接入                                         |
| :--- | ------------------------------------------------------------ | ---------------------------------------------------- |
| 协议 | <li>PLAINTEXT</li><li>SASL_PLAINTEXT</li><li>SASL_SSL（专业版支持）</li> | <li>SASL_PLAINTEXT</li><li>SASL_SSL（专业版支持）</li> |

各语言 SDK 的使用方式如下：
<table>
<thead>
<tr>
<th>SDK 类型</th>
<th>文档</th>
</tr>
</thead>
<tbody><tr>
<td>Java SDK</td>
<td><li><a href="https://cloud.tencent.com/document/product/597/54825">VPC 网络接入</a></li><li><a href="https://cloud.tencent.com/document/product/597/63531">公网 SASL_PLAINTEXT 方式接入</a></li><li><a href="https://cloud.tencent.com/document/product/597/54826">公网 SASL_SSL 方式接入</a></li>
<li><a href="https://cloud.tencent.com/document/product/597/70211">VPC 网络 SASL_SCRAM 方式接入</a></li></td>
</tr>
<tr>
<td>Python SDK</td>
<td><li><a href="https://cloud.tencent.com/document/product/597/55034">VPC 网络接入</a></li><li><a href="https://cloud.tencent.com/document/product/597/63537">公网 SASL_PLAINTEXT 方式接入</a></li><li><a href="https://cloud.tencent.com/document/product/597/55035">公网 SASL_SSL 方式接入</a></li></td>
</tr>
<tr>
<td>Go SDK</td>
<td><li><a href="https://cloud.tencent.com/document/product/597/54822">VPC 网络接入</a></li><li><a href="https://cloud.tencent.com/document/product/597/54819">公网 SASL_PLAINTEXT 方式接入</a></li></td>
</tr>
<tr>
<td>PHP SDK</td>
<td><li><a href="https://cloud.tencent.com/document/product/597/54829">VPC 网络接入</a></li><li><a href="https://cloud.tencent.com/document/product/597/54830">公网 SASL_PLAINTEXT 方式接入</a></li></td>
</tr>
<tr>
<td>C++ SDK</td>
<td><li><a href="https://cloud.tencent.com/document/product/597/54866">VPC 网络接入</a></li><li><a href="https://cloud.tencent.com/document/product/597/54867">公网 SASL_PLAINTEXT 方式接入</a></li></td>
</tr>
<tr>
<td>Node.js SDK</td>
<td><li><a href="https://cloud.tencent.com/document/product/597/55484">VPC 网络接入</a></li><li><a href="https://cloud.tencent.com/document/product/597/55485">公网 SASL_PLAINTEXT 方式接入</a></li></td>
</tr>
</tbody></table>
