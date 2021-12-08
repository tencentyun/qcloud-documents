## 事件介绍
Flink 作业的 TaskManager 负责执行用户定义的各类算子逻辑，CPU 负载过高可能会导致吞吐量下降，以及延迟的上升等各类问题。当作业的大多数 TaskManager 长期接近满载时，会触发本事件。

> !该功能目前为 Beta 版，告警推送和规则配置能力会陆续上线。

## 判定标准
- 系统每5分钟会检测一次 Flink 作业中所有 TaskManager 的 CPU 使用率指标。
- 当某个 TaskManager 的 CPU 使用率连续5个数据点的值都超过90%，则说明这个 TaskManager 处于 CPU 超高负载状态。
- 如果该作业超过80%的 TaskManager 都处于超高负载状态，则会触发该事件的推送。

> !为了避免频繁告警，每个作业的每个运行实例 ID 每小时最多触发一次该事件的推送。

## 处理建议
如果用户使用的是 Flink 1.13 版本，可以使用 Flink UI 内置的 [火焰图功能](https://nightlies.apache.org/flink/flink-docs-release-1.13/docs/ops/debugging/flame_graphs/) 分析 CPU 调用热点，即占用 CPU 时间片较多的方法（首先需要在作业的 [高级参数](https://cloud.tencent.com/document/product/849/53391) 选项中，加入 `rest.flamegraph.enabled: true` 参数，并重新发布作业版本，才可使用火焰图绘制功能），如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/eb43f4c57bb26ccd161dd3447a298318.png)
如果未开启火焰图功能或者使用1.11等旧版本的 Flink，则可以多次查看 Flink UI 中 TaskManager 各线程的 Thread Dump 信息，寻找繁忙算子的调用频率较高的方法，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/7e56e4e29bfab9c37dd6b29c6f249dc6.png)
如果以上方法均未能解决问题，可以通过 [工单](https://console.cloud.tencent.com/workorder) 等方式联系我们的技术人员以协助定位。

