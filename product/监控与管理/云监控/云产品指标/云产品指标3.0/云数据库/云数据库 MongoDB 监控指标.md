## 命名空间

Namespace = QCE/CMONGO



## 监控指标

### MongoDB

#### 1. 请求类

| 指标英文名 | 指标中文名      | 含义                       | 单位  | 维度              |
| :--------- | :-------------- | :------------------------- | :---- | :---------------- |
| Inserts    | 写入请求次数    | 单位时间内写入次数         | 次    | target（实例 ID） |
| Reads      | 读取请求次数    | 单位时间内读取次数         | 次    | target（实例 ID） |
| Updates    | 更新请求次数    | 单位时间内更新次数         | 次    | target（实例 ID） |
| Deletes    | 删除请求次数    | 单位时间内删除次数         | 次    | target（实例 ID） |
| Counts     | count 请求次数  | 单位时间内 count 次数      | 次    | target（实例 ID） |
| Success    | 成功请求次数    | 单位时间内成功请求次数     | 次    | target（实例 ID） |
| Commands   | command 请求次数 | 单位时间内 command 请求次数  | 次    | target（实例 ID） |
| Qps        | 每秒钟请求次数  | 每秒操作数，包含 CRUD 操作 | 次/秒 | target（实例 ID） |

#### 2. 时延请求类

| 指标英文名 | 指标中文名                   | 含义                                     | 单位 | 维度              |
| :--------- | :--------------------------- | :--------------------------------------- | :--- | :---------------- |
| Delay10    | 时延在10 - 50毫秒间请求次数  | 单位时间内成功请求延迟在10ms - 50ms次数  | 次   | target（实例 ID） |
| Delay50    | 时延在50 - 100毫秒间请求次数 | 单位时间内成功请求延迟在50ms - 100ms次数 | 次   | target（实例 ID） |
| Delay100   | 时延在100毫秒以上请求次数    | 单位时间内成功请求延迟在100ms以上次数    | 次   | target（实例 ID） |

#### 3. 连接数类

| 指标英文名  | 指标中文名 | 含义                                        | 单位 | 维度              |
| :---------- | :--------- | :------------------------------------------ | :--- | :---------------- |
| ClusterConn | 集群连接数 | 集群总连接数，指当前集群 proxy 收到的连接数 | 次   | target（实例 ID） |
| Connper     | 连接使用率 | 当前集群的连接数与集群总连接配置的比例      | %    | target（实例 ID） |

#### 4. 系统类

| 指标英文名       | 指标中文名 | 含义                                       | 单位 | 维度              |
| :--------------- | :--------- | :----------------------------------------- | :--- | :---------------- |
| ClusterDiskusage | 磁盘使用率 | 集群当前实际占用存储空间与总容量配置的比例 | %   | target（实例 ID） |

### MongoDB 副本集

#### 1. 系统类

| 指标英文名       | 指标中文名 | 含义             | 单位 | 维度                |
| :--------------- | :--------- | :--------------- | :--- | :------------------ |
| ReplicaDiskusage | 磁盘使用率 | 副本集容量使用率 | %    | target（副本集 ID） |

#### 2. 主从类

| 指标英文名        | 指标中文名    | 含义                                     | 单位 | 维度                |
| :---------------- | :------------ | :--------------------------------------- | :--- | :------------------ |
| SlaveDelay        | 主从延迟      | 主从单位时间内平均延迟                   | 秒   | target（副本集 ID） |
| Oplogreservedtime | oplog 保存时间 | oplog 记录中最后一次操作和首次操作时间差 | 小时 | target（副本集 ID)  |

#### 3. Cache 类

| 指标英文名 | 指标中文名         | 含义                          | 单位 | 维度               |
| :--------- | :----------------- | :---------------------------- | :--- | :----------------- |
| CacheDirty | Cache 脏数据百分比 | 当前内存 Cache 中脏数据百分比 | %    | target（副本集 ID) |
| CacheUsed  | Cache 使用百分比   | 当前 Cache 使用百分比         | %    | target（副本集 ID) |
| HitRatio   | Cache 命中率       | 当前 Cache 命中率             | %    | target（副本集 ID) |

### Mongo 节点

#### 1. 系统类

| 指标英文名 | 指标中文名   | 含义         | 单位 | 维度             |
| :--------- | :----------- | :----------- | :--- | :--------------- |
| CpuUsage   | CPU 使用率   | CPU 使用率   | %    | target（节点 ID) |
| MemUsage   | 内存使用率   | 内存使用率   | %    | target（节点 ID) |
| NetIn      | 网络入流量   | 网络入流量   | MB/s | target（节点 ID) |
| NetOut     | 网络出流量   | 网络出流量   | MB/s | target（节点 ID) |
| Disk       | 节点磁盘用量 | 节点磁盘用量 | MB   | target（节点 ID) |


#### 2. 读写类

| 指标英文名 | 指标中文名                 | 含义                       | 单位 | 维度             |
| :--------- | :------------------------- | :------------------------- | :--- | :--------------- |
| Qr         | Read 请求等待队列中的个数  | Read 请求等待队列中的个数  | 个   | target（节点 ID) |
| Qw         | Write 请求等待队列中的个数 | Write 请求等待队列中的个数 | 个   | target（节点 ID) |
| Ar         | WT 引擎的ActiveRead        | Read 请求活跃个数          | 个   | target（节点 ID) |
| Aw         | WT 引擎ActiveWrite         | Write 请求活跃个数         | 个   | target（节点 ID) |

#### 3. TTL 索引类

| 指标英文名 | 指标中文名         | 含义               | 单位 | 维度             |
| :--------- | :----------------- | :----------------- | :--- | :--------------- |
| TtlDeleted | TTL 删除的数据条数 | TTL 删除的数据条数 | 个   | target（节点 ID) |
| TtlPass    | TTL 运转轮数       | TTL 运转轮数       | 个   | target（节点 ID) |

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度信息。

## 各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释        | 格式                                                         |
| ------------------------------ | -------- | --------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.Name  | target   | target 维度名称 | 输入 String 类型维度名称：target                             |
| Instances.N.Dimensions.0.Value | target   | 视查询维度而定  | 请参考 [取值参照表](#dimensions.0.value-.E5.8F.96.E5.80.BC.E5.8F.82.E7.85.A7.E8.A1.A8) 取值 |

> ?云数据库 Instances.N.Dimensions.0.Value 的取值：
> 腾讯云提供的 MongoDB 为集群服务，可以查询“整个集群”、“某个副本集”、“某个节点”三个维度的监控数据：
> - “整个集群”维度：代表了您所购买的某一个 MongoDB 实例，这个维度可以查询整个实例的读写请求次数、容量使用率、超时请求等。
> - “某个副本集”维度：可查询集群下的某一个副本集内部的容量使用率和主从延迟。副本集实例本身只包含一个副本集，分片实例的每一片都是一个副本。
> - “某个节点”维度：可以查询集群内的任意节点的 CPU、内存等信息。

### dimensions.0.value 取值参照表

| 取值类型&nbsp;&nbsp; | 取值示例&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述                                                         |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 实例 ID              | cmgo-6ielucen                                                | 实例 ID，一个 MongoDB 实例的唯一标识：<br><li>可以在 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb) 获取<br><li>或者调用 MognoDB 的 API 获取 |
| 副本集 ID            | <li>cmgo-6ielucen_0<br><li>cmgo-6ielucen_2                   | 在实例 ID 后面拼接 “\_索引号”可以得到副本集 ID。<br>“索引号”从0开始，最大值为副本集个数-1；副本集实例只有一个副本集，所以固定拼接“\_0”即可；分片实例有多个片，每一片都是副本集，例如：第3个片的副本集 ID 就是拼接“\_2” |
| 节点 ID              | <li>cmgo-6ielucen_0-node-primary<br><li>cmgo-6ielucen_1-node-slave0<br><li>cmgo-6ielucen_3-node-slave2 | <li>在副本集 ID 后面拼接“-node-primary”得到该副本集的主节点 ID<br><li>在副本集 ID 后面拼接“-node-slave 从节点索引号”可得到对应的从节点的 ID，“从节点索引号”从0开始，最大值为从节点个数-1 |

## 入参说明

**查询云数据库 MongoDB 监控数据，入参取值如下：**
&Namespace=QCE/CMONGO
&Instances.N.Dimensions.0.Name=target
&Instances.N.Dimensions.0.Value=视查询维度而定
