## 背景信息
ClickHouse 集群实现监控告警需要在进群购买时已开启监控配置 Grafana（Prometheus）的用户可以按需配置集群的监控告警。集群创建完成后，[云数据仓库 ClickHouse 控制台](https://console.cloud.tencent.com/cdwch) 中集群详情页面会有一个 Grafana 地址，其中 prom-xxxxxx 即为您购买的 Prometheus 的实例名。
![](https://main.qcloudimg.com/raw/50a27fa5bd90cce730d235c0b3f87f1b.png)

## 配置告警
1. 若需要配置 ClickHouse 的集群告警，需进入云监控控制台的 [Prometheus 监控](https://console.cloud.tencent.com/monitor/prometheus)。根据地域和实例名选择您 ClickHouse 集群对应的 prom 监控实例，单击**实例 ID/名称**即可进入详情页面。
![](https://main.qcloudimg.com/raw/506a8f0b8629f64321c918364dd9d163.png)
2. 在实例详情页，选择**告警策略 > 新建**，新建告警策略，选择已内置的几款基础策略（包含连接数、cpu、内存、数据盘等内容），告警规则应用集群的所有节点。
 ![](https://main.qcloudimg.com/raw/ff6f3455368a6c7296513ea9b329f951.png)
下图为数据节点的容量超85%告警的配置。
![](https://main.qcloudimg.com/raw/b4bd4c07484703cd055c6aed099e77d7.png)
3. 配置（新建）通知模版，触发阈值时告警信息通知至模版的相关人，告警策略保存即生效。
