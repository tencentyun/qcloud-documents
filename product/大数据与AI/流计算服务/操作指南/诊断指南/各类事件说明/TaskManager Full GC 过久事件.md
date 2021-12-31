## 事件介绍
Flink 作业的 TaskManager 是一个 JVM 进程，它有自己的堆内存空间。Flink 算子的运行时状态存储以及其他的各类操作都可能造成堆内存空间占用过高。

当 JVM 的堆内存空间即将耗尽时，会通过 Full GC（内存回收机制）来释放空间。如果每次的回收量很小，难以及时释放堆内存空间时，JVM 会频繁而持续地触发 Full GC，该操作会占用大量的 CPU 时间，造成作业的执行线程无法正常工作，此时会触发本事件。

> !该功能目前为 Beta 版，告警推送和规则配置能力会陆续上线。

## 判定标准
系统每5分钟会检测一次 Flink 作业的所有 TaskManager 的 Full GC 耗时。

当发现某个 TaskManager 的 Full GC 耗时增量占整个检测周期的30%以上（即5分钟内 Full GC 耗时超过1.5分钟）时，表明作业出现了严重的 Full GC 问题，会触发该事件。

> ! 为了避免频繁告警，每个作业的每个运行实例 ID 每小时最多触发一次该事件的推送。

## 处理建议
收到该事件推送后，我们建议增加作业的 [资源配置](https://cloud.tencent.com/document/product/849/57772)，例如调大 TaskManager 的规格（提升 TaskManager 堆内存的最大可用空间，可以容纳更多的状态数据），提升作业的算子并行度（降低单个 TaskManager 的数据处理量，减少内存占用）等。

此外，调整 Flink [高级参数](https://cloud.tencent.com/document/product/849/53391)，例如减少 `taskmanager.memory.managed.size` 的值，也可以起到增加堆内存空间的效果。但请务必在熟悉 Flink 内存分配机制的专家指导下进行调优，否则极有可能造成其他问题。

如果您在作业的崩溃日志里发现有 `OutOfMemoryError: Java heap space` 等关键字，还可以启用 [Pod 崩溃事件采集](https://cloud.tencent.com/document/product/849/58709)，并设置文中描述的 `-XX:+HeapDumpOnOutOfMemoryError` 参数，以便在作业发生 OOM（内存不足）崩溃时，及时捕捉到堆内存的现场 Dump 文件以供后续分析。

如果作业日志中没有找到 `OutOfMemoryError: Java heap space` 等关键字，且目前作业暂时正常运行，我们建议对该作业 [配置告警](https://cloud.tencent.com/document/product/849/48293)，将**流计算作业失败事件**加入告警规则，以第一时间获取作业崩溃的事件推送。

如果以上方法均未能解决问题，可以通过 [工单](https://console.cloud.tencent.com/workorder) 等方式联系我们的技术人员以协助定位。



