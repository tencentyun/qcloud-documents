消息队列 CKafka 支持多语言SDK，客户端可以通过VPC网络和公网访问两种方式接入 CKafka 并收发消息。两种接入方式对应的协议说明如下：

| 网络 | VPC 网络                                                     | 公网域名接入                                         |
| :--- | ------------------------------------------------------------ | ---------------------------------------------------- |
| 协议 | <li>PLAINTEXT</li><li>SASL_PLAINTEXT</li><li>SASL_SSL（专业版支持）</li> | <li>SASL_PLAINTEXT</li><li>SASL_SSL（专业版支持）</li> |

各语言 SDK 的使用方式如下：

| SDK 类型    | 文档                                                         |
| ----------- | ------------------------------------------------------------ |
| Java SDK    | <li>[VPC 网络接入](https://cloud.tencent.com/document/product/597/54825)</li><li>[公网 SASL_PLAINTEXT 方式接入](https://cloud.tencent.com/document/product/597/63531)</li><li>[公网 SASL_SSL 方式接入](https://cloud.tencent.com/document/product/597/54826)</li> |
| Python SDK  | <li>[VPC 网络接入](https://cloud.tencent.com/document/product/597/55034)</li><li>[公网 SASL_PLAINTEXT 方式接入](https://cloud.tencent.com/document/product/597/63537)</li><li>[公网 SASL_SSL 方式接入](https://cloud.tencent.com/document/product/597/55035)</li> |
| Go SDK      | <li>[VPC 网络接入](https://cloud.tencent.com/document/product/597/54822)</li><li>[公网 SASL_PLAINTEXT 方式接入](https://cloud.tencent.com/document/product/597/54819)</li> |
| PHP SDK     | <li>[VPC 网络接入](https://cloud.tencent.com/document/product/597/54829)</li><li>[公网 SASL_PLAINTEXT 方式接入](https://cloud.tencent.com/document/product/597/54830)</li> |
| C++ SDK     | <li>[VPC 网络接入](https://cloud.tencent.com/document/product/597/54866)</li><li>[公网 SASL_PLAINTEXT 方式接入](https://cloud.tencent.com/document/product/597/54867)</li> |
| Node.js SDK | <li>[VPC 网络接入](https://cloud.tencent.com/document/product/597/55484)</li><li>[公网 SASL_PLAINTEXT 方式接入](https://cloud.tencent.com/document/product/597/55485)</li> |

