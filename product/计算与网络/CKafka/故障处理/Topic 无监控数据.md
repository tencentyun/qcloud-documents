## 问题概述

Topic 无监控数据。

## 可能原因

- 客户端可能没生产消费。
- 监控采集系统存在故障。


## 解决方法

- **客户端可能没生产消费**
需确认客户端是否有生产消费的行为，可以使用原生的生产消费命令进行测试，再查看监控数据。具体操作参考 [运行 Kafka 客户端](https://cloud.tencent.com/document/product/597/56840)。

- **监控采集系统存在故障**
如果监控采集系统存在故障，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。

