Prometheus 监控服务与 [Grafana 可视化服务](https://cloud.tencent.com/document/product/1437) 高度集成，一个 Grafana 实例可同时被多个 Prometheus 实例绑定，用于实现 Prometheus 数据的统一可视化。


## 操作步骤
Prometheus 监控服务支持您在 [创建实例](https://cloud.tencent.com/document/product/1416/55982) 时绑定 Grafana 实例，若您在购买 Prometheus 时未绑定实例可参考下列操作指引绑定。

### 绑定 Grafana 实例

1.  登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2.  在 Prometheus 列表中找对应的 Prometheus 实例，在操作列单击**更多**>**Grafana**>**绑定 Grafana**。
3.  在弹框中选择 Grafana 实例，并单击确定即可。
    ![](https://qcloudimg.tencent-cloud.cn/raw/fe9e2e241b40b5bb96e8f947f63f87e1.png)

>? 仅支持选择与 Prometheus 实例同一VPC（私有网络）的 Grafana 实例，若没有符合的 Grafana ，请参考<a href="https://cloud.tencent.com/document/product/1437/62194"> 操作指引 </a>创建。

### 解绑 Grafana 实例

1.  登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2.  在 Prometheus 列表中找对应的 Prometheus 实例，在操作列单击**更多 > Grafana > 解绑 Grafana**。
3.  在弹框中确定解绑即可。
    ![](https://qcloudimg.tencent-cloud.cn/raw/9ed3c244501499bbe71d9f5fcb46981a.png)

### 登录 Grafana 实例
1.  登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2.  在 Prometheus 列表中找对应的 Prometheus 实例，单击实例 ID/名称右侧的 Grafana 图标。
    ![](https://qcloudimg.tencent-cloud.cn/raw/4529775155add5bc86433a441b788687.png)
3.  进入 Grafana 界面输入账号和密码即可登录。
>?更多 Grafana 操作请参考[Grafana 可视化服务](https://cloud.tencent.com/document/product/1437) ，如Grafana 配置、图片渲染等操作。
