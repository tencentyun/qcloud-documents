## 操作场景

在使用 Consul 过程中需要对 Consul 运行状态进行监控，以便了解 Consul 服务是否运行正常，排查 Consul 故障等。 Prometheus 监控服务提供基于 Exporter 的方式来监控 Consul 运行状态，并提供了开箱即用的 Grafana 监控大盘。本文为您介绍如何使用 Prometheus 监控服务 Consul。

## 操作步骤

1. 登录 [ Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 在实例列表中，选择对应的 Prometheus 实例。
3. 进入实例详情页，单击**集成中心**。
4. 在集成中心选择 `Consul` 单击安装进行集成。

### 配置说明

![](https://main.qcloudimg.com/raw/aa067a598b3bde56103190dfafaf919e.png)

| 名称                       | 描述                                                         |
| -------------------------- | ------------------------------------------------------------ |
| 名称              | 每个集成需要一个唯一名称 |
| 地址                  | 要采集的 Consul 实例的地址和端口 |
| 标签   | 增加具有业务含义的标签，会自动添加到 Prometheus 的 Label 中 |

### 查看监控

可以通过监控大盘清晰看到如下监控状态：
1. Consul 集群节点状态
2. Consul 上注册服务的状态


![](https://main.qcloudimg.com/raw/874942517b27836d21df51fa62293903.png)
![](https://main.qcloudimg.com/raw/842d30018bb6f0dc7cead10fb10f3ffe.png)
