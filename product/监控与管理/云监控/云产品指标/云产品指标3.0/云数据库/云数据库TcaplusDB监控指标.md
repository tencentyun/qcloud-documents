## 命名空间
Namespace=QCE/TCAPLUS

## 监控指标
| 指标英文名       | 指标中文名 | 指标含义 | 单位   | 维度 |
| ------------- | ----- | ---- | ---- | ---- |
| Avgerror | 平均错误率 | 表格操作平均错误的比例 | % | TableInstanceId、ClusterId |
| Writelatency  | 平均写时延 | 表格一般操作的错误比例 | 微秒 | TableInstanceId、ClusterId |
| Comerror     | 一般错误率 | 对表格实际读取的容量单位数量 | %  | TableInstanceId、ClusterId |
| Readlatency      | 平均读时延 | 平均读取数据时延 | 微秒  | TableInstanceId、ClusterId |
| Volume | 存储容量 | 表格所占用的存储容量 | KBytes | TableInstanceId、ClusterId |
| Syserror  | 系统错误率 | 系统错误比例 | % | TableInstanceId、ClusterId |
| Writecu | 实际写容量单位 | 平均写入数据时延 | 个/秒   | TableInstanceId、ClusterId |
| Readcu     | 实际读容量单位 | 对表格实际写入的容量单位数量 | 个/秒  | TableInstanceId、ClusterId |

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称               | 维度名称             | 维度解释          | 格式                            |
| ------------------ | ---------------- | ------------- | ----------------------------- |
| Instances.N.Dimensions.0.Name  | TableInstanceId              | 数据库实例 ID 维度名称 | 输入 String 类型维度名称：TableInstanceId  |
| Instances.N.Dimensions.0.Value | TableInstanceId | 数据库的具体的实例 ID | 输入具体实例 ID，例如：tcaplus-123abc456 |
| Instances.N.Dimensions.1.Name  | ClusterId           | 集群 ID 维度名称 | 输入 String 类型维度名称：clusterId        |
| Instances.N.Dimensions.1.Value | ClusterId     | 具体集群 ID |输入具体的集群 ID，例如：clus-12345  |

## 入参说明

**查询游戏数据库 TcaplusDB 监控数据，入参取值如下：**
&Namespace=QCE/TCAPLUS
&Instances.N.Dimensions.0.Name=TableInstanceId
&Instances.N.Dimensions.0.Value=数据库的具体 ID
&Instances.N.Dimensions.1.Name=ClusterId
&Instances.N.Dimensions.1.Value=具体集群 ID


