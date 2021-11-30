本文将为您介绍如何安装 Prometheus 监控服务的 Grafana 插件。

## 前提条件

已创建 [ Prometheus 实例](https://cloud.tencent.com/document/product/1416/55982)。

## 操作步骤

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 在实例列表中，选择对应的 Prometheus 实例。
3. 在左侧菜单栏中选择 **Grafana**。
4. 在 Grafana 中勾选对应的插件，勾选完后，单击**安装**，待系统提示“提交安装 Grafana 插件任务成功”即安装成功。
 - grafana-clock-panel：“时钟”图表类型插件。
 - grafana-piechart-panel：“饼图”图表类型插件。
   ![](https://main.qcloudimg.com/raw/74e8f3a097815ad192882d743529afc4.png)
5. 插件安装成功后，您可以在 [Prometheus 实例](https://console.cloud.tencent.com/monitor/prometheus) 列表，找到对应的 Prometheus 实例，单击实例 ID 右侧<img src="https://main.qcloudimg.com/raw/978c842f0c093a31df8d5240dd01016d.png" width="2%">图标，打开您的专属 Grafana，输入账号密码，即可在创建图表中应用此插件。
   ![](https://main.qcloudimg.com/raw/513b8665dcdd66415b9ad2f66ae8ab80.png)
