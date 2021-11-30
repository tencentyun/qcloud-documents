## 命名空间

Namespace=QCE/TXMR_SPARK

## 监控指标

#### SPARK-SparkJobHistory 

| 指标英文名              | 指标中文名       | 指标含义                              | 单位 | 维度                                                         |
| ----------------------- | ---------------- | ------------------------------------- | ---- | ------------------------------------------------------------ |
| SparkShGcUtilGcCountYgc | GC 次数_YGC       | Young GC 次数                         | 次   | host4sparksparkjobhistoryserver<br>id4sparksparkjobhistoryserver |
| SparkShGcUtilGcCountFgc | GC 次数_FGC       | Full GC 次数                          | 次   | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |
| SparkShGcUtilGcTimeFgct | GC 时间_FGCT      | Full GC 消耗时间                      | s    | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |
| SparkShGcUtilGcTimeGct  | GC 时间_GCT       | 垃圾回收时间消耗                      | s    | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |
| SparkShGcUtilGcTimeYgct | GC 时间_YGCT      | Young GC 消耗时间                     | s    | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |
| SparkShGcUtilMemoryS0   | 内存区域占比_S0  | Survivor 0 区内存使用占比             | %    | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |
| SparkShGcUtilMemoryE    | 内存区域占比_E   | Eden 区内存使用占比                   | %    | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |
| SparkShGcUtilMemoryCcs  | 内存区域占比_CCS | Compressed class space 区内存使用占比 | %    | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |
| SparkShGcUtilMemoryS1   | 内存区域占比_S1  | Survivor 1 区内存使用占比             | %    | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |
| SparkShGcUtilMemoryO    | 内存区域占比_O   | Old 区内存使用占比                    | %    | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |
| SparkShGcUtilMemoryM    | 内存区域占比_M   | Metaspace 区内存使用占比              | %    | host4sparksparkjobhistoryserver<br/>id4sparksparkjobhistoryserver |

## 各维度对应参数总览

| 参数名称                       | 维度名称                        | 维度解释                     | 格式                                                     |
| :----------------------------- | :------------------------------ | :--------------------------- | :------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4sparksparkjob<br/>historyserver   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4sparksparkjobhistoryserver  |
| Instances.N.Dimensions.0.Value | id4sparksparkjob<br/>historyserver   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                |
| Instances.N.Dimensions.1.Name  | host4sparksparkjob<br/>historyserver | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4sparksparkjobhistoryserver |
| Instances.N.Dimensions.1.Value | host4sparksparkjob<br/>historyserver | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |

## 入参说明

查询弹性 MapReduce（SPARK）监控数据，入参取值如下：
&Namespace=QCE/TXMR_SPARK
&Instances.N.Dimensions.0.Name=id4sparksparkjobhistoryserver
&Instances.N.Dimensions.0.Value=EMR 实例具体 ID
&Instances.N.Dimensions.1.Name=host4sparksparkjobhistoryserver
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP 
