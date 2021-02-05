## 概述

[腾讯云监控](https://cloud.tencent.com/product/cm) 为用户提供云服务器、云数据库等多个云产品的负载和性能监控指标，用户可以使用云监控控制台、云监控 API 等方式获取相关监控数据。腾讯云监控应用插件 Tencent Cloud Monitor App，是一款适配开源软件 Grafana 的应用插件，通过调用 [腾讯云监控 API 3.0](https://cloud.tencent.com/document/product/248/30342) 的方式获取监控数据，并对数据进行自定义 Dashboard 展示。

## 特点

- 支持云服务器监控指标数据源
- 支持云数据库 MySQL 监控指标数据源
- 支持云数据库 PostgreSQL 监控指标数据源
- 支持私有网络 NateGateway 监控指标数据源
- 支持私有网络对等连接 监控指标数据源
- 支持公网负载均衡（LB_PUBLIC）数据源
- 支持内网负载均衡四层协议（LB_PRIVATE）数据源
- 支持负七层协议监控指标（LOADBALANCE）数据源
- 提供了云服务器、云数据库 MySQL 的具有代表性的 Dashboard 模板
- 更多云产品的监控指标数据源在陆续完善中

## 步骤1：安装 Grafana

腾讯云监控应用插件是运行在 Grafana 6.x 或更新的版本上，请先安装 Grafana 环境，详情请参见 [Grafana 安装文档](https://grafana.com/docs/grafana/download/)。

### 插件安装方式

1. 已将本地的 Grafana 升级到 6.x 版本或更新的版本。
2. 在 [Releases](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/releases) 中下载最新版本的腾讯云监控应用插件代码（资源名为 `tencentcloud-monitor-app-1.x.x.zip`），并将解压后的代码放置在 Grafana 的 `${GRAFANA_HOME}/data/plugins` 目录。
3. 重启 Grafana 服务。
4. 鼠标悬浮左侧导航栏的【齿轮】图标，单击【Plugins】，进入 Plugins 管理页面，如果插件列表中正常展示 `Tencent Cloud Monitor` APP 插件，表示插件安装成功。
![Plugin APP](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/plugin-app.png?raw=true)
5. 进入应用详情页面，单击【Enable】，启用成功后，即可在 Grafana 中使用腾讯云监控应用插件。

### 支持 Docker

为了更快地开发与测试，需添加 docker-compose.yml 文件，执行以下命令：

```plaintext
docker-compose up
```

折行成功后，在浏览器输入 `http://localhost:3000` 访问 Grafana。


## 步骤2：配置数据源

腾讯云监控应用插件通过调用[云监控 API](https://cloud.tencent.com/document/product/248/30342) 的方式获取各云产品的监控指标数据，通过以下步骤，配置相应云产品的数据源。    

1. 鼠标悬浮左侧导航栏的 **齿轮** 图标，点击 `Data Sources` 选项，进入数据源管理页面。
   ![Datasource Add](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/datasource-add.png?raw=true)

2. 点击右上角的 `Add data source` 按钮，然后点击 `Tencent Cloud Monitor Datasource` 数据源，进入数据源配置页面；
   ![Datasource Add](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/datasource-choose.png?raw=true)

   配置项说明如下。

   - `Name` 数据源名称，可以是任意名称，默认为 Tencent Cloud Datasource；  
   - SecretId` 和 `SecretKey` 是调用云监控 API 必需的安全证书信息，二者可以通过腾讯云控制台 [云 API 密钥页面](https://console.cloud.tencent.com/capi) 获取；
   - 选择需要获取监控数据的云产品；  
   - 点击 `Save & Test` 按钮，测试数据源的配置信息是否正确，配置成功后，即可以在 Dashboard 中使用该数据源。
     ![Datasource Config](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/datasource-config.png?raw=true)


## 步骤3：创建 Dashboard

创建 Dashboard 支持三种方式： 快捷创建、管理页面和导入模板。

### 快捷创建

鼠标悬浮左侧导航栏的 **加号** 图标，点击 `+Dashboard` 选项，即可创建一个新的 Dashboard。

### 管理页面

1. 鼠标悬浮左侧导航栏的 **田字格** 图标，
2. 点击 `Manage` 选项，进入 Dashboard 管理页面
3. 点击 `New Dashboard` 按钮，即可创建一个新的 Dashboard。同时，在该页面可以对 Dashboard 进行各种管理操作，如新建文件夹、移动 Dashboard、导入 Dashboard 等。

### 导入模板

1. 鼠标悬浮左侧导航栏的 **齿轮** 图标。
2. 点击 `Plugins` 选项，进入 Plugins 管理页面。
3. 点击 `Tencent Cloud Monitor` 应用，进入应用详情页面，切换至 `Dashboards` 选项卡，选择 Dashbboard 模板导入。

![Import Plugin Dashboard](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/plugin-dashboard.png?raw=true)

## 步骤4：配置 Panel 数据

创建 Dashboard 之后，通过配置 Panel 信息，即可获取腾讯云监控的相应监控数据。现在以简单的 Graph 为例，展示如何配置 Panel 信息。

### CVM 云服务器监控

1. 点击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Queries` 选项卡，通过配置选项获取腾讯云 CVM 云服务器的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 CVM 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云服务器监控接口的输入参数，可参考 [云服务器监控接口文档](https://cloud.tencent.com/document/api/248/30385)，更好地理解各配置项。
   - `Namespace` 命名空间，云服务器监控的命名空间为 `QCE/CVM`。
   - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
   - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
   - `Period` 监控统计周期，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计周期。
   - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
     - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例ID** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称、`As PrivateIpAddress` 主网卡的内网IP、 `As PublicIpAddress` 主网卡的公网IP。
     - 可实例列表的获取可参考 [云服务器查询实例列表接口文档](https://cloud.tencent.com/document/api/213/15728)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参考接口文档，配置相应参数。
     - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，点击右上角的 `Add Query` 增加新的查询。  
       ![CVM Panel Query](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/panel-cvm-query.png?raw=true)

### CDB 云数据库MySQL监控

1. 点击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Queries` 选项卡，通过配置选项获取腾讯云数据库 MySQL 的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含CDB监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云数据库MySQL监控接口的输入参数，可参考 [云数据库MySQL监控接口文档](https://cloud.tencent.com/document/api/248/30386)，更好地理解各配置项。
   - `Namespace` 命名空间，云服务器监控的命名空间为 `QCE/CDB`。
   - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
   - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
   - `Period` 监控统计周期，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计周期。
   - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
     - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例ID** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称、 `As Vip` 内网IP。
     - 实例列表的获取可参考 [云数据库MySQL查询实例列表接口文档](https://cloud.tencent.com/document/api/236/15872)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参考接口文档，配置相应参数。
     - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，点击右上角的 `Add Query` 增加新的查询。  

![CDB Panel Query](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/panel-cdb-query.png?raw=true)

### CLB 负载均衡监控

1. 点击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Queries` 选项卡，通过配置选项获取腾讯云 负载均衡的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 CLB 监控服务的腾讯云监控数据源。
3. 负载均衡指标分三个命名空间：公网负载均衡监控指标（Namespace=QCE/LB_PUBLIC），内网负载均衡四层协议监控指标（Namespace=QCE/LB_PRIVATE）， 七层协议监控指标（Namespace=QCE/LOADBALANCE），可根据自己需要在`Namespace`选择。
4. 配置项的内容对齐腾讯云服务器监控接口的输入参数，可参考 [负载均衡云监控接口文档](https://cloud.tencent.com/document/product/248/51898)，更好地理解各配置项。
   - `Namespace` 命名空间，比如 `QCE/LB_PUBLIC`。
   - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
   - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
   - `Period` 监控统计周期，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计周期。
   - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
     - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As LoadBalancerId`，以 **实例ID** 展示实例列表。此外，可以选择 `As LoadBalancerName` 实例名称、`As LoadBalancerVips` 网络ip。
     - 实例列表的获取可参考 [负载均衡实例列表接口文档](https://cloud.tencent.com/document/api/214/30685)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参考接口文档，配置相应参数。
     - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，点击右上角的 `Add Query` 增加新的查询。  
   - `Listener` 监听器，对应输入参数的 `Listener.N` 字段，列表会自动获取。
     - 为了适应不同用户的习惯，监听器列表会以不同的字段展示，默认为 `As ListenerId`，以 **监听器ID** 展示实例列表。此外，可以选择 `As ListenerName` 监听器名称、`As Port` 端口。
     - 监听器列表的获取可参考 [负载均衡监听器列表接口文档](https://cloud.tencent.com/document/api/214/30686)。

![Clb Panel Query](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/panel-clb-query.png?raw=true)

## 步骤5：模板变量

模板变量 [Variables](https://grafana.com/docs/reference/templating/) 是 Grafana 提供的一种 Dashboard 优化特性，用于创建高度可复用和交互式 Dashboard。模板变量的一般是允许 Grafana 从数据源获得不同的度量，并提供一种无需修改仪表板即可动态更改它的方法。腾讯云监控应用目前提供了地域、云服务器实例、云数据库 MySQL 实例 等变量。已经提供的模板变量如下表所示：  

| 变量                      | 示例                                                         | 描述                                                         |      |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 地域                      | Namespace=QCE/CVM&Action=DescribeRegions                     | 参考 [地域接口文档](https://cloud.tencent.com/document/api/213/15708)。`Action` 固定为 `DescribeRegions`，`Namespace` 为云产品对应的命名空间，如 `QCE/CVM` `QCE/CDB`等。地区作为变量模板，只支持单选，如设置成多选或者选中 `All`, 默认选中第一个地区值。 |      |
| 云服务器实例              | Namespace=QCE/CVM&Region=ap-beijing&Action=DescribeInstances&InstanceAlias=PublicIpAddresses | 参考 [云服务器查询实例列表接口文档](https://cloud.tencent.com/document/api/213/15728)。`Namespace` 固定为`QCE/CVM`，`Action` 固定为`DescribeInstances`。`Region` 为地域参数，可以为特定的地域值，如 `ap-beijing`；也可以为变量值，如 `$region`。`InstanceAlias` 为实例的展示字段，默认为 `InstanceId`，可选值为 `InstanceName`、`PrivateIpAddresses`、`PublicIpAddresses`。云服务器实例作为模板变量，同时支持单选和多选。 |      |
| 云数据库 MySQL 实例       | Namespace=QCE/CDB&Region=ap-beijing&Action=DescribeInstances&InstanceAlias=InstanceId | 参考 [云数据库MySQL查询实例列表接口文档](https://cloud.tencent.com/document/api/236/15872)。`Namespace` 固定为`QCE/CDB`，`Action` 固定为`DescribeInstances`。`Region` 为地域参数，可以为特定的地域值，如 `ap-beijing`；也可以为变量值，如 `$region`。`InstanceAlias` 为实例的展示字段，默认为 `InstanceId`，可选值为 `InstanceName`、`Vip`。云数据库实例作为模板变量，同时支持单选和多选。 |      |
| 云数据库 PostgreSQL 实例  | Namespace=QCE/POSTGRES&Region=ap-beijing&Action=DescribeInstances&InstanceAlias=DBInstanceId | 参考 [云数据库PostgreSQL查询实例列表接口文档](https://cloud.tencent.com/document/api/409/16773)。`Namespace` 固定为`QCE/CDB`，`Action` 固定为`DescribeInstances`。`Region` 为地域参数，可以为特定的地域值，如 `ap-beijing`；也可以为变量值，如 `$region`。`InstanceAlias` 为实例的展示字段，默认为 `DBInstanceId`，可选值为 `DBInstanceName`, `PrivateIpAddresses`, `PublicIpAddresses`。云数据库实例作为模板变量，同时支持单选和多选。 |      |
| 私有网络 NateGateway 实例 | Namespace=QCE/NAT_GATEWAY&Region=ap-beijing&Action=DescribeInstances&InstanceAlias=NatGatewayId | 参考 [私有网络Nat网关查询实例列表接口文档](https://cloud.tencent.com/document/api/215/4088)。`Namespace` 固定为`QCE/NAT_GATEWAY`，`Action` 固定为`DescribeInstances`。`Region` 为地域参数，可以为特定的地域值，如 `ap-beijing`；也可以为变量值，如 `$region`。`InstanceAlias` 为实例的展示字段，默认为 `NatGatewayId`，可选值为 `NatGatewayName`。NateGateway 网关实例作为模板变量，同时支持单选和多选。 |      |
| 私有网络对等连接实例      | Namespace=QCE/PCX&Region=ap-beijing&Action=DescribeInstances&InstanceAlias=peeringConnectionId | 参考 [私有网络对等连接查询实例列表接口文档](https://cloud.tencent.com/document/api/215/2101)。`Namespace` 固定为`QCE/PCX`，`Action` 固定为`DescribeInstances`。`Region` 为地域参数，可以为特定的地域值，如 `ap-beijing`；也可以为变量值，如 `$region`。`InstanceAlias` 为实例的展示字段，默认为 `peeringConnectionId`，可选值为 `peeringConnectionName`。对等连接实例作为模板变量，同时支持单选和多选（如果是负载均衡则不支持多选，可选多个监听器）。 |      |
| 负载均衡监听器            | Namespace=QCE/LB_PRIVATE&Action=DescribeListeners&Region=$region&Instance=$instance&listenerAlias=ListenerId | 参考 [负载均衡监听器列表接口文档](https://cloud.tencent.com/document/product/214/30686)。`Namespace` 可为`QCE/LB_PRIVATE`，`QCE/LB_PUBLIC`，`QCE/LOADBALANCE`，`Action` 固定为`DescribeListeners`。`Region` 为地域参数，可以为特定的地域值，如 `ap-guangzhou`；也可以为变量值，如 `$region`。`Instance` 为实例id，可以为特定的实例，如 `lb-rbw529fz`；也可以为变量值，如 `$instance`。`listenerAlias` 为监听器的展示字段，默认为 `ListenerId`，可选值为 `ListenerName`，`Port`。同时支持单选和多选。 |      |

### 创建变量

1. 进入某一 Dashboard 页面，点击右上角的 **齿轮** 图标，进入 Dashboard 设置页面；
2. 点击左侧 **Variables** 选项，进入变量设置页面，然后点击 `+ Add variable` 按钮，进入变量编辑页面；

### 编辑变量

- `Name` 变量名，一般为英文字符串，在 Dashboard 的编辑中使用该变量名替换原特定值。
- `Label` 变量的可见标签，用于更显式地描述变量名称。例如，`Name` 设置为 "region"，`Lable` 可设置为 "地区"。
- `Type` 变量查询方式，此处只能选择 `Query` 方式，即通过向数据源发送请求获取变量的列表。
- `Data source` 要获取变量列表的数据源，选择已配置的任意腾讯云监控数据源。
- `Refresh`  更新变量的方式，定义变量数据何时被更新。
- `Query` 变量查询语句，详情参见上述表格的变量示例和描述。

变量信息填写完毕，可在页面下方预览查询得到的变量值，如果与期望值相符，点击 `Add` 按钮添加变量。添加成功后，点击右侧菜单的 `Save` 保存至 Dashboard 配置。

以云服务器单机监控 Dashboard 为例，展示如何配置级联变量：地域变量、云服务器实例变量，如下图所示。

![Variable Region Config](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/variable-region-config.png?raw=true)

![Variable Instance Config](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/variable-instance-config.png?raw=true)

### 应用变量

创建变量后，在 Dashboard 页面的左上角会展示变量选择框，可以切换变量值。变量有两种引用语法，`$varname` 和 `[[varname]]`。变量常用于 Panel 的查询语句中，以云服务器单机监控 Dashboard 为例，展示如何在查询中使用变量，如下图所示。此外，变量还可以应用在 Panel 标题、Text 文本面板等。

![Variable Dashboard](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/variable-cvm-dashboard.png?raw=true)

![Variable Panel Query](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/blob/master/src/image/variable-panel-query.png?raw=true)
