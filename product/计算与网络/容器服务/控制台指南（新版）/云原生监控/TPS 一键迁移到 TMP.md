<dx-alert infotype="alarm" title="温馨提示">
感谢您对腾讯云原生监控 TPS 的认可与信赖，为提供更优质的服务和更强大的产品能力，TPS 与原腾讯云 Prometheus 监控服务进行融合和升级，升级为 [TMP](https://cloud.tencent.com/document/product/457/71896)。支持跨地域跨 VPC 监控，支持统一 Grafana 面板对接多监控实例实现统一查看。TMP 计费详情见 [按量计费](https://cloud.tencent.com/document/product/1416/65379)，相关云资源使用详情见 [计费方式和资源使用](https://cloud.tencent.com/document/product/457/71905)。若您只使用基础监控的 [免费指标](https://cloud.tencent.com/document/product/457/72136)，TMP 不会收取任何指标费用。<br>
TPS 将于2022年5月16日下线，详情见 [公告](https://cloud.tencent.com/document/product/457/72632)。TMP 已正式发布，欢迎 [了解试用](https://console.cloud.tencent.com/tke2/prometheus2)。TPS 已不支持创建新实例，我们提供一键 [迁移工具](https://cloud.tencent.com/document/product/457/72487)，帮您一键将 TPS 实例迁移到 TMP，迁移前请 [精简监控指标](https://cloud.tencent.com/document/product/457/72482) 或降低采集频率，否则可能产生较高费用，再次感谢您对 TPS 的支持和信任。
</dx-alert>

TPS 支持一键迁移到 TMP。您可以迁移单独的实例，也可以批量迁移单地域下的实例。每个 TPS 实例的迁移时间一般在十分钟左右。**新的 TMP 实例将以 “旧实例名 (trans-from-prom-xxx)”命名，其中“旧实例名”为原 TPS 的实例名，“xxx” 为原 TPS 实例 ID。**迁移之后，您可以在新的 TMP 实例查看新的监控数据，也可以在旧的实例中查看以前的监控数据，需注意，旧实例将在服务停止时删除。




迁移步骤如下：
<dx-steps>
-迁移 Grafana 配置
-创建 Grafana 实例
-创建 TMP 实例
-TMP 绑定 TPS 之前关联的集群
-迁移采集配置
-迁移告警策略
-迁移聚合规则
</dx-steps>

## 迁移注意事项

### 迁移后的预估费用

TPS 和 TMP 已上线“收费指标采集速率”的能力，您可以用该数值估算监控实例/集群/采集对象/指标等多个维度的预估费用：

>! 仅 TMP 实例会产生费用，TPS 实例不会产生费用。

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的 **[云原生监控](https://console.cloud.tencent.com/tke2/prometheus)**。
2. 在云原生监控列表中，查看“收费指标采集速率”。该指标表示迁移到 TMP 实例的收费指标采集速率，根据用户的指标上报量和采集频率预估算出。该数值乘以 86400 则为一天的监控数据点数，根据 [按量计费](https://cloud.tencent.com/document/product/1416/65379) 可以计算预估的监控数据刊例价。
![](https://qcloudimg.tencent-cloud.cn/raw/0b4e14f6fc8433fd42aaf48f2f4e5a36.png)
您也可以单击实例名称右侧的**一键迁移**，获取该 TPS 实例迁移到 TMP 之后的预估价格。或者在“关联集群”、“数据采集配置”、“指标详情”等多个页面查看到不同维度下的“收费指标采集速率”。

### （旧）TPS Prometheus 数据查询地址和 Grafana 地址 

如果您有相关的程序平台或系统依赖 TPS 的 **Prometheus 数据查询地址和 Grafana 地址**。迁移后请及时更换为 TMP 里面相应的地址。否则旧的 TPS 实例在服务停止删除后，您的 **Prometheus 数据查询地址和 Grafana 地址** 将失效。

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的 **[云原生监控](https://console.cloud.tencent.com/tke2/prometheus)**。
2. 单击实例 ID ，进入实例的“基本信息”页，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e2ed79d929472bbc1da0fb1e9cbb3fef.png)

### （新）TMP Prometheus 数据查询地址和 Grafana 地址 

>? TMP 对查询接口增加了鉴权，例如您需要将 TMP 的监控实例对接到您自己的 Grafana 页面，TMP 实例的用户名为您腾讯云账号的 APPID，密码为下图中的 Token。具体可参考 [监控数据查询](https://cloud.tencent.com/document/product/1416/56026)。

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的 **[Prometheus 监控](https://console.cloud.tencent.com/tke2/prometheus2)**。
2. 单击实例 ID ，进入实例的“基本信息”页，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7fe17b8320f9bd8daab0b842b4606b86.png)

>! 迁移完成后，请勿在旧的 TPS 实例里面关联新的集群或采集规则，这部分新增的改变将不会自动同步到新的 TMP 实例中。

## 操作步骤

### 单实例迁移

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的 **[云原生监控](https://console.cloud.tencent.com/tke2/prometheus)**。
2. 在当前的云原生监控的实例列表页，在上方选择需要迁移的实例所在的地域。
3. 单击实例右方的**一键迁移**。
4. 在弹窗中，选择新的 TMP 实例需要的**网络**和**数据存储时间**。
![](https://qcloudimg.tencent-cloud.cn/raw/2952b6a8025ae06d8ed0de2abcf020d4.png)
   - **网络**：新的 TMP 实例的 VPC 和子网默认和原来的 TPS 实例一样。若您要选择其它 VPC，请注意该 VPC 首先需要和监控的集群所在的 VPC 网络已打通。
   - **数据存储时间**：默认15天，目前仅支持额外选择30天，45天。
   - **标签**：非必填字段，根据实际需要选择。
   - **预估费用**：如上图所示，迁移的时候会显示当前 TPS 实例，在迁移到 TMP 之后的收费指标采集速率，以及预估的一天费用。

>! 具体费用请查看 TMP 涉及 [计费方式](https://cloud.tencent.com/document/product/1416/65379) 和相关 [云资源使用情况](https://cloud.tencent.com/document/product/457/71905)。若费用过高，建议您 [精简监控指标](https://cloud.tencent.com/document/product/457/72482)。
5. 单击**确定**。当 TPS 实例状态的括号中内容显示“已迁移”，表示迁移成功。
6. TPS 迁移完成后，您可以在 **[Prometheus 监控控制台](https://console.cloud.tencent.com/tke2/prometheus)** 中选择地域，同地域下中有一个名为**“旧实例名 (trans-from-prom-xxx)” 的 TMP 新实例，其中“旧实例名”为原 TPS 的实例名，“xxx” 为原 TPS 实例 ID。**如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/87e5de3e395a04015082bcdc56a6801c.png)
>? 迁移完成后，请勿在旧的 TPS 实例里面关联新的集群或采集规则，这部分新增的改变将不会自动同步到新的 TMP 实例中。

### 实例批量迁移

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的 **[云原生监控](https://console.cloud.tencent.com/tke2/prometheus)**。
2. 在当前的云原生监控的实例列表页，在上方选择需要迁移的实例所在的地域。
3. 勾选状态为“未迁移”的实例后，单击上方的“一键迁移”。
>! 
>- 批量迁移不支持选择新 TMP 实例的 VPC 和子网，如您有类似需求，请进行**单实例迁移**。
>- 迁移前请查看 TMP 涉及 [计费方式](https://cloud.tencent.com/document/product/1416/65379) 和相关 [云资源使用情况](https://cloud.tencent.com/document/product/457/71905)。若费用过高，建议您 [精简监控指标](https://cloud.tencent.com/document/product/457/72482)。
4. 单击**确定**。当 TPS 实例状态的括号中内容显示“已迁移”，表示迁移成功。
5. TPS 迁移完成后，您可以在 **[Prometheus 监控](https://console.cloud.tencent.com/tke2/prometheus)** 控制台，在同样的地域里找到一个名为**“旧实例名 (trans-from-prom-xxx)”的 TMP 新实例，其中“旧实例名”为原 TPS 的实例名，“xxx” 为原 TPS 实例 ID。**

>? 迁移完成后，请勿在旧的 TPS 实例里面关联新的集群或采集规则，这部分新增的改变将不会自动同步到新的 TMP 实例中。
