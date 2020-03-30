## 1. 接口描述

域名：monitor.api.qcloud.com
接口：GetMonitorData

云数据库 MariaDB（TencentDB for MariaDB）（曾用名：金融级数据库 TDSQL） 定位于 OLTP 场景下高安全性的企业级云数据库，十余年来一直应用于腾讯计费业务，MariaDB 兼容 MySQL 语法，拥有诸如线程池、审计、异地容灾等高级功能，同时具有云数据库的易扩展性、简单性和性价比。具体介绍请参见 [云数据库 MariaDB](https://cloud.tencent.com/document/product/237/1054)。

查询云数据库 MariaDB 产品监控数据，入参取值如下：
namespace：qce/tdsql
dimensions.0.name=uuid
dimensions.0.value 为实例的 uuid

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 GetMonitorData。

### 2.1 输入参数

| 参数名称               | 必选   | 类型       | 输入内容      | 描述                                       |
| ------------------ | ---- | -------- | --------- | ---------------------------------------- |
| namespace          | 是    | String   | qce/tdsql   | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏。          |
| metricName         | 是    | String   | 具体的指标名称   | 指标名称，具体名称见2.2                            |
| dimensions.0.name  | 是    | String   | uuid      | 入参为实例的 uuid                               |
| dimensions.0.value | 是    | String   | 实例具体的 uuid | 输入实例的具体 uuid，例如 tdsql-0gfryg60              |
| period             | 否    | Int      | 60/300    | 监控统计周期，绝大部分指标支持60s统计粒度，部分指标仅支持300s统计粒度，统计粒度根据指标的不同而变。输入参数时可参考2.2的指标详情列表。 |
| startTime          | 否    | Datetime | 起始时间      | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| endTime            | 否    | Datetime | 结束时间      | 结束时间，默认为当前时间。 endTime 不能小于 startTime       |

### 2.2 指标名称

| 指标名称                  | 含义           | 单位   |
| --------------------- | ------------ | ---- |
| data_disk_available   | 数据磁盘可用大小     | MB   |
| binlog_disk_available | BINLOG 磁盘可用大小 | MB   |
| select_total          | SELECT 请求总数   | 次/秒  |
| long_query            | SELECT 慢查询数   | 次/秒  |
| update_total          | UPDATE 请求总数   | 次/秒  |
| insert_total          | INSERT 请求总数   | 次/秒  |
| delete_total          | DELETE 请求总数   | 次/秒  |
| mem_available         | 内存可用大小       | GB   |
| disk_iops             | 磁盘 IOPS       | 次/秒  |
| conn_active           | 总连接数       | 次/秒  |
| conn_running          | 活跃连接数          | 次/秒  |
| is_master_switched    | 监控是否主备切换     | 无    |
| cpu_usage_rate        | CPU 使用率       | %    |


## 3. 输出参数

| 参数名称       | 类型       | 描述                  |
| ---------- | -------- | ------------------- |
| code       | Int      | 错误码, 0: 成功, 其他值表示失败 |
| message    | String   | 返回信息                |
| startTime  | Datetime | 起始时间                |
| endTime    | Datetime | 结束时间                |
| metricName | String   | 指标名称                |
| period     | Int      | 监控统计周期              |
| dataPoints | Array    | 监控数据列表              |


## 4. 错误码表

| 错误代码 | 错误描述    | 英文描述                                 |
| ---- | ------- | ------------------------------------ |
| -502 | 资源不存在   | OperationDenied.SourceNotExists      |
| -503 | 请求参数有误  | InvalidParameter                     |
| -505 | 参数缺失    | InvalidParameter.MissingParameter    |
| -507 | 超出限制    | OperationDenied.ExceedLimit          |
| -509 | 错误的维度组合 | InvalidParameter.DimensionGroupError |
| -513 | DB 操作失败  | InternalError.DBoperationFail        |

## 5. 示例

#### 输入

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>
&namespace=qce/tdsql
&metricName=data_disk_available
&dimensions.0.name=uuid
&dimensions.0.value=tdsql-0gfryg60
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

#### 输出

```
{
	"code": 0,
	"message": "",
	"metricName": "data_disk_available",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		28.3,
        28.3,
		28.3
	]
}
```
