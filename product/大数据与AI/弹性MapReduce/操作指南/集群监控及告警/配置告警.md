## 操作场景
腾讯云云监控为 EMR 提供了丰富的告警服务，您可通过云监控控制台创建子机和集群告警策略。

## 操作步骤
1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor/policylist)，在左侧栏选择【告警策略】页，单击【新增】。
![](https://main.qcloudimg.com/raw/b53d5a371d2ffddc0204d9c6a595fc0c.png)
2. 配置策略信息，策略类型选择 EMR 策略。
EMR 告警策略类型目前分为子机告警和集群告警，其中子机告警又分为指标告警和事件告警，集群告警只有指标告警。
 - 若您要对各节点的硬件情况进行告警监控，例如 CPU 使用率、内存使用率、ping 通等情况，请选择子机告警。
 - 若您要对集群服务维度进行告警监控，例如 HDFS 存储空间、YARN 应用阻塞数、失败数等情况，请选择集群告警。
 
 ![](https://main.qcloudimg.com/raw/387bbaa4cb999345e8764e9510858a26.png)


