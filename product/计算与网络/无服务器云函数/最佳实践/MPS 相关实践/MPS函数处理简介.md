
通过函数处理服务，可以快速完成对 [视频处理 MPS](https://cloud.tencent.com/document/product/862) 产生的回调事件进行处理及操作。通过 [MPS 触发器](https://cloud.tencent.com/document/product/583/50833) 将事件推送到云函数 SCF ，再通过 Serverless 无服务架构的函数计算提供回调事件的处理及响应。
整体数据处理流程如下图所示：
![](https://main.qcloudimg.com/raw/94d36f4b716b2a1ea6fbc499f93b3cfb.png)


## 函数处理场景实践

日志服务可以将日志主题中的数据通过 [MPS 日志触发器](https://cloud.tencent.com/document/product/583/50833) 投递至云函数进行处理，以满足对视频进行事件通知、状态监控、告警处理等应用场景需求，场景及具体说明如下表所示：


| 函数处理场景                                               | 描述说明                                |
| ------------------------------------------------------------ | --------------------------------------- |
| [视频任务回调备份 COS](https://cloud.tencent.com/document/product/583/50836) | 将 MPS 产生的回调任务通过 SCF 及时备份至 COS  |
| [视频任务回调通知工具](https://cloud.tencent.com/document/product/583/50837) | 实时接收 MPS 数据消息，并将消息推送至企业微信、邮件等 |


>! 数据投递至云函数，云函数侧将产生相应的计算费用，计费详情请参见 SCF [计费概述](https://cloud.tencent.com/document/product/583/17299)。
