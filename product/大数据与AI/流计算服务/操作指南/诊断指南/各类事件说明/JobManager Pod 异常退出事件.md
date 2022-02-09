## 事件介绍
Flink 作业的 JobManager 负责整个作业的管理和调度工作，一旦其发生故障，可能造成作业崩溃、状态丢失等严重后果，因此我们会持续检测并推送 JobManager 异常退出事件。此外，为了保证 JobManager 的可用性，我们为每个作业启用了高可用（High Availability）配置，以便在 JobManager 意外退出时可以自动重新选举和恢复作业运行。
当发生 JobManager Pod 异常退出事件时，作业通常可以自行恢复，但恢复的完整程度取决于 Flink 作业是否开启快照功能，以及每个算子的具体实现逻辑。因此，我们建议用户在作业恢复正常后，检查输出是否正常（例如错误数据、重复数据等）。

> !同一个 Pod 可能因为异常而被 Kubernetes 多次重建，因此如果您收到多条同样的事件，属于正常现象。

## 判定标准
系统实时监测 TaskManager Pod 的退出事件，判断退出时的状态码是否为 SIGTERM 造成的（即正常的退出码为143）。如果退出码异常，说明该停止请求并非由 JobManager 发出，而是因为 TaskManager 自身发生了错误，此时会判定为 Pod 异常退出事件。

## 告警配置
用户可以对该事件 **配置作业监控告警（异常事件）**，并实时接收触发和恢复的告警通知。

## 处理建议

| 状态码 | 可能原因                                                     | 解决方案                                                     |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 137    | 作业内存占用过大，超出 Pod 配额，导致被 OOMKilled            | 可能是 Source Connector 实现不当，给 JobManager 造成较大内存压力。<br>如果未能确定原因，请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查 |
| -1     | 兜底策略，表示 Pod 退出但是并未得到退出码，可能是系统错误等  | 请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查 |
| 0      | Pod 启动过程中，由于无法在用户绑定的子网中分配 IP（例如 IP 耗尽），导致启动失败退出 | 检查集群绑定的 VPC 的子网是否有剩余 IP。如果 IP 余量充足，请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查 |
| 1      | Flink 初始化期间发生了异常，导致启动失败                     | 通常是基础类冲突或者关键配置文件被覆盖导致的，可在日志中搜索 `Could not start cluster entrypoint` 关键字附近的异常信息。<br>如果未能确定原因，请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查. |
| 2      | Flink JobManager 启动期间发生了致命错误                      | 日志中搜索 `Fatal error occurred in the cluster entrypoint` 关键字附近的异常信息。<br>如果未能确定原因，请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查 |
| 239    | Flink 的执行线程发生了未捕获的致命错误                       | 日志中搜索 `produced an uncaught exception. Stopping the process` 等关键字附近的异常信息。<br>如果未能确定原因，请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查 |

