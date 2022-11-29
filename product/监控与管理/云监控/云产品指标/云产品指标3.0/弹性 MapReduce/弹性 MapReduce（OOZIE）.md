## 命名空间

Namespace=QCE/TXMR_OOZIE

## 监控指标

| 指标英文名                 | 指标中文名       | 指标含义                              | 单位 | 维度                           |
| -------------------------- | ---------------- | ------------------------------------- | ---- | ------------------------------ |
| OozieOozieGcUtilGcCountFgc | GC次数_FGC       | Full GC 次数                          | 次   | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilGcCountYgc | GC次数_YGC       | Young GC 次数                         | 次   | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilGcTimeFgct | GC时间_FGCT      | Full GC 消耗时间                      | s    | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilGcTimeGct  | GC时间_GCT       | 垃圾回收时间消耗                      | s    | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilGcTimeYgct | GC时间_YGCT      | Young GC 消耗时间                     | s    | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilMemoryCcs  | 内存区域占比_CCS | Compressed class space 区内存使用占比 | %    | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilMemoryE    | 内存区域占比_E   | Eden 区内存使用占比                   | %    | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilMemoryM    | 内存区域占比_M   | Metaspace 区内存使用占比              | %    | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilMemoryO    | 内存区域占比_O   | Old 区内存使用占比                    | %    | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilMemoryS0   | 内存区域占比_S0  | Survivor 0区内存使用占比              | %    | host4oozieoozie、id4oozieoozie |
| OozieOozieGcUtilMemoryS1   | 内存区域占比_S1  | Survivor 1区内存使用占比              | %    | host4oozieoozie、id4oozieoozie |

## 各维度对应参数总览

| 参数名称                       | 维度名称        | 维度解释                     | 格式                                                         |
| :----------------------------- | :-------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4oozieoozie | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4oozieoozie                    |
| Instances.N.Dimensions.0.Value | host4oozieoozie | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4oozieoozie   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4oozieoozie                      |
| Instances.N.Dimensions.0.Value | id4oozieoozie   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（OOZIE）监控数据，入参取值如下：**

Namespace=QCE/TXMR_OOZIE
&Instances.N.Dimensions.0.Name=host4oozieoozie
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4oozieoozie
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID






