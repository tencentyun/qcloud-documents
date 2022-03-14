

通过函数处理服务，可以快速完成云服务器 CVM 等云上资源的运行日志采集、ETL（Extraction-Transformation-Loading）加工和消息转储等复杂日志处理任务。函数处理为异步过程，凡是收集到日志服务的数据，均能通过配置将数据投递到云函数进行消费处理，您只需要在日志服务控制台进行简单的配置即可完成日志服务 CLS 对接云函数消费。

通过 [CLS 触发器](https://cloud.tencent.com/document/product/583/49587) 将日志源信息提交到 SCF，再通过 Serverless 无服务架构的函数计算提供数据加工与分析、事件触发、弹性伸缩，无需运维，按需付费。整体数据处理流程如下所示：
![](https://main.qcloudimg.com/raw/d00cc3cd47209169d809298f220caff5.svg)




## 使用函数处理优势

- 提供一站式采集、存储、加工、分析和展示。
- 全托管日志加工任务，按时间周期进行触发执行，自动重试。
- 持续增加内置函数模板，降低主流需求下的日志处理开发成本。
- 基于云函数提供数据加工及自定义代码逻辑。
- 基于云函数提供计算能力，拥有弹性伸缩、免运维、按需付费等特性。

## 多场景函数处理实践

日志服务可以将日志主题中的数据通过 [CLS 日志触发器](https://cloud.tencent.com/document/product/583/49587) 投递至云函数进行处理，以满足日志加工/日志清洗等应用场景需求，场景及具体说明如下表所示：


| 函数处理场景                                               | 描述说明                                |
| ------------------------------------------------------------ | --------------------------------------- |
| [ ETL 日志加工](https://cloud.tencent.com/document/product/583/49591) | 日志数据通过云函数进行日志清洗，日志加工，格式转换等操作  |
| [CLS 转储至 Ckafka](https://cloud.tencent.com/document/product/583/51595) | 日志数据通过云函数进行日志清洗等操作并投递至 Ckafka  |
| [CLS 转储至 COS](https://cloud.tencent.com/document/product/583/51596) | 日志数据通过云函数进行日志清洗等操作并投递至 COS   |
| [CLS 转储至 ES ](https://cloud.tencent.com/document/product/583/51597) | 日志数据通过云函数投递至 ES   |



>! 数据投递至云函数，云函数侧将产生相应的计算费用，计费详情请参见 [云函数 SCF 计费概述](https://cloud.tencent.com/document/product/583/17299)。
