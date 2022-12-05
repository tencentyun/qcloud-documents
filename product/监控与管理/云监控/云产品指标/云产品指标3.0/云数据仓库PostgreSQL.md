## 命名空间

Namespace=QCE/SNOVA

## 监控指标

### 集群指标

| 指标英文名  | 指标中文名               | 单位 | 维度                  |
| ----------- | ------------------------ | ---- | --------------------- |
| Connections | 连接数                   | 个   | appId、snovaClusterId |
| LongTxNum   | 还在进行的长事务查询个数 | 个   | appId、snovaClusterId |
| ResQueueNum | 默认资源队列使用情况     | 个   | appId、snovaClusterId |

### 节点指标

| 指标英文名                      | 指标中文名            | 单位  | 维度                        |
| ------------------------------- | --------------------- | ----- | --------------------------- |
| CpuUtilization                  | CPU 利用率            | %     | appId、snovaClusterId、host |
| CpuUtilizationMaster            | CPU 利用率-主节点     | %     | appId、snovaClusterId、host |
| MemUtilizationMaster            | 内存利用率-主节点     | %     | appId、snovaClusterId、host |
| NetworkReceiveThroughput        | 网络接收吞吐量        | Mbps  | appId、snovaClusterId、host |
| NetworkReceiveThroughputMaster  | 网络接收吞吐量-主节点 | Mbps  | appId、snovaClusterId、host |
| NetworkTransmitThroughput       | 网络传输吞吐量        | Mbps  | appId、snovaClusterId、host |
| NetworkTransmitThroughputMaster | 网络传输吞吐量-主节点 | Mbps  | appId、snovaClusterId、host |
| PercentageDiskUsed              | 磁盘利用率            | %     | appId、snovaClusterId、host |
| ReadIops                        | 读取 IOPS             | 个/秒 | appId、snovaClusterId、host |
| WriteIops                       | 写入 IOPS             | 个/秒 | appId、snovaClusterId、host |
| ReadLatency                     | 读取延时              | ms    | appId、snovaClusterId、host |
| WriteLatency                    | 写入延时              | ms    | appId、snovaClusterId、host |
| ReadThroughput                  | 磁盘读取吞吐量        | Mbps  | appId、snovaClusterId、host |
| WriteThroughput                 | 磁盘写入吞吐量        | Mbps  | appId、snovaClusterId、host |
| MemUtilization                  | 内存利用率            | %     | appId、snovaClusterId、host |

## 各维度对应参数总览

| 数名称                         | 维度名称       | 维度解释               | 格式                                                         |
| ------------------------------ | -------------- | ---------------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.Name  | appId          | 主账号 APPID的维度名称 | 输入 String 类型维度名称：appId                              |
| Instances.N.Dimensions.0.Value | appId          | 主账号 APPID           | 输入主账号具体 APPID，例如：1250000000。可在 [账号信息控制台中获取](https://console.cloud.tencent.com/developer) APPID。 |
| Instances.N.Dimensions.0.Name  | snovaClusterId | 集群 ID 的维度名称     | 输入 String 类型维度名称：snovaClusterId                     |
| Instances.N.Dimensions.0.Value | snovaClusterId | 具体集群 ID            | 输入具体集群 ID，例如：snova-12345678                        |
| Instances.N.Dimensions.0.Name  | host           | 主机信息的维度名称     | 输入 String 类型维度名称：host                               |
| Instances.N.Dimensions.0.Value | host           | 具体主机信息           | 输入具体主机信息，例如：mdw-snova-12345678 。不同节点的主机 ID 命名规则：<br><li> master 节点：mdw-{集群 ID} <li> master 备节点：smdw-{集群 ID} <li> 第一个计算节点：sdw1-{集群 ID} <li>  第二个计算节点：sdw2-{集群 ID}  <li>第三个计算节点：sdw3-{集群 ID} <li>  第四个计算节点：sdw4-{集群 ID} |

## 入参说明

**查询云数据仓库 PostgreSQL -集群指标监控数据，入参取值如下：**
&Namespace=QCE/SNOVA
&Instances.N.Dimensions.0.Name=appId
&Instances.N.Dimensions.0.Value=主账号具体 APPID
&Instances.N.Dimensions.1.Name=snovaClusterId
&Instances.N.Dimensions.1.Value=集群 ID

**查询云数据仓库 PostgreSQL -节点指标监控数据，入参取值如下：**
&Namespace=QCE/SNOVA
&Instances.N.Dimensions.0.Name=appId
&Instances.N.Dimensions.0.Value=主账号具体 APPID
&Instances.N.Dimensions.1.Name=snovaClusterId
&Instances.N.Dimensions.1.Value=集群 ID
&Instances.N.Dimensions.2.Name=host
&Instances.N.Dimensions.2.Value=主机信息，请根据各维度对应参数总览填写

