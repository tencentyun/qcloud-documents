## 操作场景

本文介绍如何使用 Prometheus 获取云原生 API 网关 Kong 的监控数据。

## 前置条件
- 已购买 Kong 网关实例，详情请参见 [操作文档](https://cloud.tencent.com/document/product/1364/72495)。
- 已拥有腾讯云 [Prometheus 实例](https://cloud.tencent.com/document/product/1416/55778) 或自建 Prometheus 实例。

## 操作步骤
### 步骤1：开启 Prometheus 插件
使用 Prometheus 监控，需要在 Kong 云原生 API 网关开启普罗米修斯（Prometheus）插件，您可以根据需要选择以下两种特性场景：
- [针对指定 API 开启 Prometheus 插件](#model1)
- [开启全局 Prometheus 插件](#model2)

[](id:model1)
#### 场景1： 针对指定 API 开启 Prometheus 插件
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，进入需要配置 Prometheus 插件的 Kong 网关实例详情页，在**访问控制**页查看管理控制台登录方式。
  <img src="https://qcloudimg.tencent-cloud.cn/raw/296cd720bc50aba0da782189d28d0073.jpg"> 
2. 登录 Konga 管理控制台，进入需要添加 Prometheus 插件的 **Route 详情页**，单击 **Add Plugin** 按钮添加插件，在 **Analytics & Monitoring** 分组下选择 **Prometheus** 插件。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a2d748c8b8f61648ffd5ae4c41847e00.png)
3. 添加 Prometheus 插件配置中，若您不需要区分 consumer ，请直接用默认配置。<img src="https://qcloudimg.tencent-cloud.cn/raw/19657c755a335bd616717d2705dcdf81.jpg" width="720px"> 

[](id:model2)
#### 场景2：开启全局 Prometheus 插件
1. 进入左侧导航栏的 **PLUGINS** 页面，单击 **ADD GLOBAL PLUGINS** 按钮，在 **Analytics & Monitoring** 分组下选择 **Prometheus** 插件。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ef063441e219238f7d682415b29fa4b0.jpg"> 
2. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，进入需要配置限流插件的 Kong 网关实例详情页，在**配置管理**页查看管理控制台登录方式。

### 步骤2：配置数据拉取地址
1. 准备好**腾讯云**或**自建**的 Prometheus 实例。该步骤的 Prometheus 实例用于拉取云原生 API 网关 kong 的监控数据。
  > ?关于如何购买腾讯云 Prometheus 实例，以及开通配套的 Grafana 实例，可以参见 [Prometheus 监控服务](https://cloud.tencent.com/document/product/1416/55778) 相关文档。
2. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，进入需要的 Kong 网关实例详情页，在**访问控制**页查看 Kong 实例的内网节点地址。
<img src="https://qcloudimg.tencent-cloud.cn/raw/1a6e0f62f25d1e5db96c3dc6960ca474.jpg"> 
3. 若您使用 Prometheus agent，可以在 prometheus.yml 配置文件中的 scrape_configs.static_configs.targets 添加内网节点地址列表，注意端口必须为 8100。例如对于上图的内网地址列表，可以参照以下参数进行配置：
<dx-codeblock>
:::  yxml
job_name: kong
honor_timestamps: true
metrics_path: /metrics
scheme: http
static_configs:
- targets:
  - 172.27.0.35:8100
  - 172.27.0.133:8100
  - 172.27.0.79:8100
  labels:
    instance: gateway-f3bdaaa7
relabel_configs:
  - source_labels: [__address__]
    target_label: node

:::
</dx-codeblock>
>!请配置 relabel_configs 信息，以保证指标上报准确。
>
4. 若您使用自定义程序的拉取方式，可以通过云原生 API 网关 DescribeCloudNativeAPINodes 接口自动获取节点 IP 列表。

### 步骤3：在 Grafana 配置 Kong 模板的 Dashboard（可选）
该步骤指导您在 Grafana 实例展示 Prometheus 采集到的 Kong 监控数据。
1. 前往 [Grafana-Kong 官网](https://grafana.com/grafana/dashboards/14085)，下载 Dashboard 配置 JSON 文件。
<img src="https://qcloudimg.tencent-cloud.cn/raw/9aaa621e826c8934ca117a87ee1f6e58.jpg" width="720px"> 
2. 在您的 Grafana 上导入 Kong 的 Dashboard 模板。
<img src="https://qcloudimg.tencent-cloud.cn/raw/20668ba0d2cf964921f6d1a28ec29eb3.jpg" width="720px"> 
3. 导入 Kong 的 Dashboard 模板后，如果有数据上报到 Prometheus ，则 Grafana 上会展示类似下图的视图。
<img src="https://qcloudimg.tencent-cloud.cn/raw/67f104ab316b9c2f5604e7ce8731abf1.jpg" width="720px"> 


## 注意事项
- 开启 Prometheus 插件对于 Kong 的数据流性能有影响，建议只为需要监控的特定的 API(Route) 开启 Prometheus 插件。
- 在腾讯云上购买云监控 Prometheus 将产生费用，需要您自行承担。
- 为简单起见，上述操作依赖 Konga 控制台演示。您也可以调用 kong admin api 来绑定 Prometheus 插件，具体可以参见 [Kong-Prometheus 插件文档](https://docs.konghq.com/hub/kong-inc/prometheus/)。关于如何开启 kong admin api ，请参见 [开启admin-api并配置安全认证](https://cloud.tencent.com/document/product/1364/73237)。

## 参考
更多相关说明请参见 [Kong Prometheus 插件官方文档](https://docs.konghq.com/hub/kong-inc/prometheus/)。
