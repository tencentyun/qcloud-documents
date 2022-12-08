若您需要在本地的 Grafana 系统中查看 Prometheus 监控服务相关数据，可以利用 Prometheus 监控服务提供的 HTTP API 来实现。本文介绍如何将 Prometheus 监控服务数据接入本地 Grafana 的实现方法。


## 操作步骤

### 步骤1：获取 Prometheus 监控服务提供的 HTTP API

1. 登录 [ Prometheus 服务监控控制台](https://console.cloud.tencent.com/monitor/prometheus)
2. 单击对应的按量付费实例，进入 Prometheus 基本信息页。
3. 在服务地址模块获取 HTTP API 地址。若您需要提高 Grafana 数据读取的安全性，可获取 Prometheus 实例的鉴权 Token，按照步骤2指引填入即可。
   
   ![](https://qcloudimg.tencent-cloud.cn/raw/262b83c88264b5526876ef8bf168c941.png)


### 步骤2：在本地 Grafana 添加数据源
1. 以**管理员账号**登录本地 Grafana 系统。
2. 在左侧导航栏中选择 **Configuration > Data Sources**（非管理员无法查看该菜单）。
3. 在 Data Sources页中单击 **Add data source**。
4. 在 Add data source 页面中选择 **Prometheus**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/412480d962cebcdb4d3a28c3fd23590f.png)
5. 在 Settings 页签的 Name 字段输入自定义的名称，在 URL 字段中粘贴步骤1：「Grafana 数据源配置信息」中的 **HTTP API**。
6. 在 Auth 区域开启 Basic Auth 开关，设置 User 为「Grafana 数据源配置信息」中的 **Basic auth user**，设置 Password 为「Grafana 数据源配置信息」中的 **Basic auth password**。
7. 完成后单击 **save & test** 即可。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e1e262e95ba91c8cd1c72f09b8ab5b86.png)


### 步骤3：验证是否添加成功

请按照以下步骤验证 Prometheus 监控服务是否成功接入本地 Grafana：
1. 登录您本地 Grafana 系统。
2. 在左侧导航栏中选择**+ > Create**。
3. 在 New dashboard 页面中单击 **Add a new panel** 。
4. 在 Edit Panel 页面的 Query 页面的下拉框中，选择步骤2中所添加的数据源，在 A 区域的 Metrics 字段输入指标名称并按回车。
5. 若能显示出相应指标的图表，则说明操作成功。否则请检查填写的接口地址或 Token 是否正确，以及数据源是否有 Prometheus 监控服务数据。
![](https://qcloudimg.tencent-cloud.cn/raw/39cc3b261672d0a1cf0306b332f6c823.png)
