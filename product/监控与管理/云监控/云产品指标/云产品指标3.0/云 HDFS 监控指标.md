## 命名空间

Namespace = QCE/CHDFS

## 监控指标

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

| 指标英文名             | 指标中文名         | 单位 | 维度         | 统计粒度                  |
| ---------------------- | ------------------ | ---- | ------------ | ------------------------- |
| ApiReadRequestCount    | 文件系统读请求数   | 个   | filesystemid | 60s、300s、 3600s、86400s |
| ApiWriteRequestCount   | 文件系统写请求数   | 个   | filesystemid | 60s、300s、 3600s、86400s |
| ApiReadBandwidth       | 文件系统读带宽     | MB/s | filesystemid | 60s、300s、 3600s、86400s |
| ApiFileInodeCount      | 文件系统文件数量   | 个   | filesystemid | 60s、300s、 3600s、86400s |
| ApiDirInodeCount       | 文件系统目录数量   | 个   | filesystemid | 60s、300s、 3600s、86400s |
| ApiCapacityAvailable   | 文件系统空间剩余量 | GB   | filesystemid | 60s、300s、 3600s、86400s |
| ApiCapacityUsed        | 文件系统空间使用量 | GB   | filesystemid | 60s、300s、 3600s、86400s |
| ApiCapacityPercentUsed | 文件系统空间使用率 | %    | filesystemid | 60s、300s、 3600s、86400s |

## 各维度对应参数总览

| 参数名称                       | 维度名称     | 维度解释               | 格式                                   |
| :----------------------------- | :----------- | :--------------------- | :------------------------------------- |
| Instances.N.Dimensions.0.Name  | filesystemid | 文件系统 ID 的维度名称 | 输入 String 类型维度名称：filesystemid |
| Instances.N.Dimensions.0.Value | filesystemid | 具体文件系统 ID        | 输入具体文件系统 ID，例如：f4mnvilzmdd |



## 入参说明

**查询云 HDFS控数据，入参取值如下：**

&Namespace =QCE/CHDFS
&Instances.N.Dimensions.0.Name =filesystemid
&Instances.N.Dimensions.0.Value =具体文件系统 ID
