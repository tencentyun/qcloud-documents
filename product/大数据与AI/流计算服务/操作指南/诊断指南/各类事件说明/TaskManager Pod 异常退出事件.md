## 事件介绍
Flink 作业的 TaskManager 运行在 Kubernetes Pod 中，当 Pod 终止时，我们可以监测到该事件，并根据返回码、状态信息等维度，判断 Pod 是否发生了异常。
> !
> - 该功能目前为 Beta 版，告警推送等能力会于近期上线。
> - 同一个 Pod 可能因为异常而被 Kubernetes 多次重建。因此，如果您收到多条同样的事件，属于正常现象。

## 判定标准
系统实时监测 TaskManager Pod 的退出事件，判断退出时的状态码是否为 SIGTERM 造成的（即正常的退出码为143）。如果退出码异常，说明该停止请求并非由 JobManager 发出，而是因为 TaskManager 自身发生了错误，此时会判定为 Pod 异常退出事件。

## 处理建议

| 状态码 | 可能原因                                                    | 解决方案                                                     |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------ |
| 137    | 作业内存占用过大，超出 Pod 配额，导致被 OOMKilled           | 可参考 [作业资源配置](https://cloud.tencent.com/document/product/849/57772) 增加算子并行度、提升 TaskManager 的 CU 规格。 |
| -1     | 兜底策略，表示 Pod 退出但是并未得到退出码，可能是系统错误等 | 请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查。 |
|     0    |     Pod 启动过程中，由于无法在用户绑定的子网中分配 IP（例如 IP 耗尽），导致启动失败退出     |   检查集群绑定的 VPC 的子网是否有剩余 IP。如果 IP 余量充足，请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查。   |
| 1      | Flink 初始化期间发生了异常，导致启动失败                    | 通常是基础类冲突或者关键配置文件被覆盖导致的，可在日志中搜索 `Could not start cluster entrypoint` 关键字附近的异常信息。<br>如果未能确定原因，请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查。 |
| 2      | Flink JobManager 启动期间发生了致命错误                     | 日志中搜索 `Fatal error occurred in the cluster entrypoint` 关键字附近的异常信息。<br>如果未能确定原因，请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查。 |
| 239    | Flink 的执行线程发生了未捕获的致命错误                      | 日志中搜索 `produced an uncaught exception. Stopping the process` 等关键字附近的异常信息。<br>如果未能确定原因，请提 [工单](https://console.cloud.tencent.com/workorder) 联系技术支持排查。 |

