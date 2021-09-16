## 购买方式
高阶版监控告警可以通过以下两种途径购买：
1. 在集群新建时勾选 Grafana 监控，集群新建完毕，即可享受300+指标的监控服务。
![](https://main.qcloudimg.com/raw/cff694ed8a48d746d55360c137329c42.png)
2. 对于已经购买的集群，可以后购买 Prometheus 监控服务，在 [云数据仓库 ClickHouse 控制台](https://console.cloud.tencent.com/cdwch) 集群列表中，选择要配置的集群 **ID/名称**，然后选择**操作 > 更多 > 新建 grafana 监控**。
 ![](https://main.qcloudimg.com/raw/c628b01c73b2ae0e2e1e3a6c5c8eb1cb.png)
 - 输入密码，需要包含@$!%\*#?&特殊字符、字母和数字，密码需设置6位 - 20位。
 - 选择适合自己的集群规模的 Prometheus 服务，Prometheus 集群选择建议根据监控峰值 TPS 和监控数据存储总量上限来选择。**基础版：单实例，适用小业务量。集群版：分布式多实例，高性能，高可用**。
![](https://main.qcloudimg.com/raw/eb2f95c579a248f4a8912ceb871e418b.png)

## 监控使用帮助
### 监控页面入口
可以通过以下两种方式使用 ClickHouse 集群的高阶监控功能。
- 通过 ClickHouse 集群详情页面进入高阶监控
![](https://main.qcloudimg.com/raw/bb6722dc3e66f7964f81ff1974fc1af3.png)
- 通过 [云监控控制台](https://console.cloud.tencent.com/monitor/prometheus) 查看 ClickHouse 集群监控
  ![](https://main.qcloudimg.com/raw/6a7166de12457ed6c187b6f891545b7a.png)

单击 **Grafana 地址**即可进入 Prometheus 监控的 Grafana 页面，默认账号为 admin，其中密码为前面购买页面设置的密码。

### 初次使用 Grafana
第一次使用 Grafana 页面时，需要输入 admin 账号和密码。
 ![](https://main.qcloudimg.com/raw/402606f5b42bbd77304eec84860851fb.png)
输入账号密码后进入 Grafana 页面，第一次需要选择左侧菜单栏![](https://main.qcloudimg.com/raw/5e04977fa7f4cb100f2dab5486f4bbc7.png)，然后单击 **Manage**，进入我们已经为您配置好的内置 Clickhouse 监控面板，后续可直接在 **Home** 页面查看。
![](https://main.qcloudimg.com/raw/c99c33f472032dbce4ab40014bacd62b.png)
大数据文件夹下即为内置模板，分为4个 Dashboard，分别为集群看板、单节点主机看板、多节点主机看板以及节点概览看板。
- Clickhouse 集群：主要查看 Clickhouse 集群层面的指标。
- 主机单节点详情：主要查看 Clickhouse 集群所在节点的单主机指标展示，比较详细。
- 主机多节点详情：主要查看 Clickhouse 集群所在节点的多主机指标同时展示，重要指标横向比对。
- 主机节点概览：概览 Clickhouse 集群所在主机的整体主机情况。

![](https://main.qcloudimg.com/raw/623df61b0217413435bddfc33817f5d6.png)

