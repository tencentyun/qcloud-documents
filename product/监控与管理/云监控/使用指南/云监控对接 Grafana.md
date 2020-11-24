## 简介

[腾讯云监控](https://cloud.tencent.com/product/cm) 为用户提供云服务器、云数据库等多个云产品的负载和性能监控指标，用户可以使用云监控控制台、云监控 API 等方式获取相关监控数据。还可以通过腾讯云监控应用插件 Tencent Cloud Monitor，将云监控数据添加到 Grafana 中展示。

#### 支持的云产品：

- 支持云服务器监控指标数据源
- 支持云数据库 MySQL 监控指标数据源
- 支持云数据库  PostgreSQL  监控指标数据源
- 支持私有网络 NateGateway 监控指标数据源
- 支持私有网络对等连接 监控指标数据源
- 提供了云服务器、云数据库 MySQL 的具有代表性的 Dashboard 模板

>?更多云产品的监控指标数据源在陆续完善中。


## 前提条件

腾讯云监控应用插件运行在 Grafana 6.0或更新的版本上，请先安装 Grafana 环境，详情请参见 [Grafana 安装文档](https://grafana.com/docs/grafana/latest/installation/)。

## 步骤1：基于源码的插件安装

1. 确保本地的 Grafana 是6.0版本或更新的版本。
2. 下载最新版本的 [腾讯云监控应用插件代码](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app)，并将解压后的代码放置在 Grafana 的 `${GRAFANA_HOME}/data/plugins` 目录。
3. 重启 Grafana 服务。
4. 鼠标悬浮左侧导航栏的**齿轮**按钮，单击【Plugins】，进入 Plugins 管理页面，如果插件列表中正常展示 Tencent Cloud Monitor APP 插件，表示插件安装成功。
<img src="https://main.qcloudimg.com/raw/59d7abe67bb4442555c137fc74a51d8f.png" width="50%"></img>
5. 进入应用详情页面，单击【Enable】 ，启用成功后，即可在 Grafana 中使用腾讯云监控应用插件。

## 步骤2：配置数据源

腾讯云监控应用插件通过调用 [云监控 API](https://cloud.tencent.com/document/product/248/30342) 的方式获取各云产品的监控指标数据，通过以下步骤，配置相应云产品的数据源。    

1. 鼠标悬浮左侧导航栏的**齿轮**按钮，单击【Data Sources】 ，进入数据源管理页面。
	 ![](https://main.qcloudimg.com/raw/044b0dd3f315aa4bb1f885421d85b388.png)
2. 单击右上角的【Add data source】，然后单击【Tencent Cloud Monitor Datasource】 数据源，进入数据源配置页面。
	 ![](https://main.qcloudimg.com/raw/edb2c6817062ad2595e94548ec392510.png)
3. 在数据源配置页面中，配置如下选项：
 - **Name**：数据源名称，可以是任意名称，默认为 Tencent Cloud Datasource。
 - **SecretId** 和 **SecretKey**：调用云监控 API 必需的安全证书信息，请前往腾讯云控制台 [云 API 密钥页面](https://console.cloud.tencent.com/capi) 获取。
 - **Monitor Services**：开启云产品右侧的开关，选择需要获取监控数据的云产品。 
	 ![](https://main.qcloudimg.com/raw/79f2562911bce8f7bb9ac9db2a761c95.png)
4. 单击【Save & Test】，测试数据源的配置信息是否正确，配置成功后，即可以在 Dashboard 中使用该数据源。


## 步骤3：创建 Dashboard

下文为您介绍创建 Dashboard 的三种方式： 快捷创建、在管理页面创建，导入模板


#### 方式一：快捷创建

鼠标悬浮左侧导航栏的**加号**按钮，单击【+Dashboard】选项，即可创建一个新的 Dashboard。

#### 方式二：管理页面

1. 鼠标悬浮左侧导航栏的**田字格**按钮，单击【Manage】选项，进入 Dashboard 管理页面。
2. 单击【New Dashboard】，创建一个新的 Dashboard。同时，在该页面可以对 Dashboard 进行各种管理操作，例如新建文件夹、移动 Dashboard、导入 Dashboard 等。

#### 方式三：导入模板

1. 鼠标悬浮左侧导航栏的**齿轮**按钮，单击 【Plugins】，进入 Plugins 管理页面。
2. 单击【Tencent Cloud Monitor】，进入应用详情页面，切换至【Dashboards】 选项卡，选择 Dashbboard 模板导入。
![](https://main.qcloudimg.com/raw/deaa0dee580261470bdc08c0f4e8dc6c.png)


## 步骤4：配置 Panel 数据

创建 Dashboard 之后，通过配置 Panel 信息，即可获取腾讯云监控的相应监控数据。下文以简单的 Graph 为例，介绍如何配置 Panel 信息。

### 云服务器 CVM 监控

1. 单击 **New Panel** 面板的 【Add Query】，进入 Panel 配置页面。在左侧第一个【Queries】选项卡，通过配置选项获取腾讯云 CVM 云服务器的监控数据。
2. 【Queries to】数据源列表，选择已配置的包含 CVM 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云服务器监控接口的输入参数，可参见 [拉取监控数据接口](https://cloud.tencent.com/document/product/248/31014)、 [云服务器监控指标](https://cloud.tencent.com/document/product/248/6843) 文档，了解各配置项的详细说明。
   - **Namespace**：命名空间，云服务器监控的命名空间为 **QCE/CVM**。
   - **Region**：地域，地域列表会根据 **Namespace** 选项自动获取，单击选择某一地域。
   - **MetricName**：指标名称，指标列表会根据 **Namespace** 和 **Region** 选项自动获取，单击选择某一指标。
   - **Period**：监控统计周期，周期列表会根据 **MetricName** 选项自动获取，单击选择某一统计周期。
   - **Instance**：实例，对应输入参数的 **Instances.N** 字段，实例列表会自动获取。
     - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 **As InstanceId**，以**实例 ID** 展示实例列表。此外，可以选择 **As InstanceName** 实例名称、**As PrivateIpAddress** 主网卡的内网 IP、 **As PublicIpAddress** 主网卡的公网IP。
     - 可实例列表的获取可参考 [云服务器查询实例列表接口文档](https://cloud.tencent.com/document/api/213/15728)。切换 **Show Details** 为 **true**，可展示实例请求参数，默认参数为 **Offset = 0**和 **Limit = 20**。如果需要变更实例查询条件，可参考接口文档，配置相应参数。
     >!在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，可单击右上角的【Add Query】增加新的查询。  
     
![](https://main.qcloudimg.com/raw/4b341292c5103164b070a4cf3cc2b8cd.png)

### 云数据库 MySQL 监控

1. 单击 **New Panel** 面板的【Add Query】，进入 Panel 配置页面。在左侧第一个 【Queries】 选项卡，通过配置选项获取腾讯云数据库 MySQL 的监控数据。
2. 【Queries to】 数据源列表，选择已配置的包含云数据库监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云数据库 MySQL 监控接口的输入参数，可参见 [拉取监控数据接口](https://cloud.tencent.com/document/product/248/31014)、[云数据库 MySQL 监控指标](https://cloud.tencent.com/document/product/248/45147) 文档，了解各配置项的详细说明。
   - **Namespace**：命名空间，云服务器监控的命名空间为 **QCE/CDB**。
   - **Region**：地域，地域列表会根据 **Namespace** 选项自动获取，单击选择某一地域。
   - **MetricName**：指标名称，指标列表会根据 **Namespace** 和 **Region** 选项自动获取，单击选择某一指标。
   - **Period**：监控统计周期，周期列表会根据 **MetricName** 选项自动获取，单击选择某一统计周期。
   - **Instance**：实例，对应输入参数的 **Instances.N** 字段，实例列表会自动获取。
     - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 **As InstanceId**，以 **实例 ID** 展示实例列表。此外，可以选择 **As InstanceName** 实例名称、 **As Vip** 内网IP。
     - 实例列表的获取可参见 [云数据库 MySQL 查询实例列表接口文档](https://cloud.tencent.com/document/api/236/15872)。切换 **Show Details** 为 **true**，可展示实例请求参数，默认参数为 **Offset = 0** 和 **Limit = 20**。如果需要变更实例查询条件，可参考接口文档，配置相应参数。
     >!在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，可单击右上角的【Add Query】增加新的查询。  

![](https://main.qcloudimg.com/raw/27668754fe4c608a01755b0bb5c9e0df.png)

## 模板变量

模板变量 [Variables](https://grafana.com/docs/reference/templating/) 是 Grafana 提供的一种 Dashboard 优化特性，用于创建高度可复用和交互式 Dashboard。模板变量允许 Grafana 从数据源获得不同的度量，并提供一种无需修改仪表板就可动态更改它的方法。腾讯云监控应用目前提供了地域、云服务器实例、云数据库 MySQL 实例等变量。已经提供的模板变量如下表所示：  

| 变量    | 示例   | 描述 |   
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | 
| 地域                      | Namespace=QCE/CVM&Action=DescribeRegions                     | 参考 [地域接口文档](https://cloud.tencent.com/document/api/213/15708)<br><li>`Action` 固定为 `DescribeRegions`<br><li>`Namespace` 为云产品对应的命名空间，例如 `QCE/CVM` `QCE/CDB`等<br><li>地区作为变量模板，只支持单选，例如设置成多选或者选中 `All`, 默认选中第一个地区值 |      
| 云服务器实例              | Namespace=QCE/CVM&Region=ap-beijing&Action=DescribeInstances&Instance<br>Alias=PublicIpAddresses | 参考 [云服务器查询实例列表接口文档](https://cloud.tencent.com/document/api/213/15728)<br><li>`Namespace` 固定为`QCE/CVM`<br><li>`Action` 固定为`DescribeInstances`<br><li>`Region` 为地域参数，可以为特定的地域值，例如 `ap-beijing`；也可以为变量值，例如 `$region`<br><li>`InstanceAlias` 为实例的展示字段，默认为 `InstanceId`，可选值为 `InstanceName`、`PrivateIpAddresses`、`PublicIpAddresses`<br><li>云服务器实例作为模板变量，同时支持单选和多选 |      
| 云数据库 MySQL 实例       | Namespace=QCE/CDB&Region=ap-beijing&Action=DescribeInstances&Instance<br>Alias=InstanceId | 参考 [云数据库MySQL查询实例列表接口文档](https://cloud.tencent.com/document/api/236/15872)<br><li>`Namespace` 固定为`QCE/CDB`<br><li>`Action` 固定为`DescribeInstances`<br><li>`Region` 为地域参数，可以为特定的地域值，例如 `ap-beijing`；也可以为变量值，例如 `$region`<br><li>`InstanceAlias` 为实例的展示字段，默认为 `InstanceId`，可选值为 `InstanceName`、`Vip`<br><li>云数据库实例作为模板变量，同时支持单选和多选 |      
| 云数据库 PostgreSQL 实例  | Namespace=QCE/POSTGRES&Region=ap-beijing&Action=DescribeInstances&Instance<br>Alias=DBInstanceId | 参考 [云数据库PostgreSQL查询实例列表接口文档](https://cloud.tencent.com/document/api/409/16773)<br><li>`Namespace` 固定为`QCE/CDB`<br><li>`Action` 固定为`DescribeInstances`<br><li>`Region` 为地域参数，可以为特定的地域值，例如 `ap-beijing`；也可以为变量值，例如 `$region`<br><li>`InstanceAlias` 为实例的展示字段，默认为 `DBInstanceId`，可选值为 `DBInstanceName`，`PrivateIpAddresses`， `PublicIpAddresses`<br><li>云数据库实例作为模板变量，同时支持单选和多选 |      
| 私有网络 NateGateway 实例 | Namespace=QCE/NAT_GATEWAY&Region=ap-beijing&Action=DescribeInstances&Instance<br>Alias=NatGatewayId | 参考 [私有网络 Nat 网关查询实例列表接口文档](https://cloud.tencent.com/document/api/215/4088)<br><li>`Namespace` 固定为`QCE/NAT_GATEWAY`<br><li>`Action` 固定为`DescribeInstances`<br><li>`Region` 为地域参数，可以为特定的地域值，例如 `ap-beijing`；也可以为变量值，例如 `$region`<br><li>`InstanceAlias` 为实例的展示字段，默认为 `NatGatewayId`，可选值为 `NatGatewayName`<br><li>NateGateway 网关实例作为模板变量，同时支持单选和多选 |      
| 私有网络对等连接实例      | Namespace=QCE/PCX&Region=ap-beijing&Action=DescribeInstances&Instance<br>Alias=peeringConnectionId | 参考 [私有网络对等连接查询实例列表接口文档](https://cloud.tencent.com/document/api/215/2101)<br><li>`Namespace` 固定为`QCE/PCX`<br><li>`Action` 固定为`DescribeInstances`<br><li>`Region` 为地域参数，可以为特定的地域值，例如 `ap-beijing`；也可以为变量值，例如 `$region`<br><li>`InstanceAlias` 为实例的展示字段，默认为 `peeringConnectionId`，可选值为 `peeringConnectionName`<br><li>对等连接实例作为模板变量，同时支持单选和多选 |      





#### 创建变量

1. 进入某一 Dashboard 页面，单击右上角的**齿轮**按钮，进入 Dashboard 设置页面。
2. 在左侧菜单中，选择【Variables】>【+ Add variable】，进入编辑变量页面。
	- **Name**：变量名，一般为英文字符串，在 Dashboard 的编辑中使用该变量名替换原特定值。
	- **Label**：变量的可见标签，用于更显式地描述变量名称。例如，**Name** 设置为“region”，**Lable** 可设置为“地区”。
	- **Type**：变量查询方式，此处只能选择 **Query** 方式，即通过向数据源发送请求获取变量的列表。
	- **Data source**：要获取变量列表的数据源，选择已配置的任意腾讯云监控数据源。
	- **Refresh**：更新变量的方式，定义变量数据何时被更新。
	- **Query**：变量查询语句，详情参见 [上述表格](#.E6.A8.A1.E6.9D.BF.E5.8F.98.E9.87.8F) 的变量示例和描述。
3. 变量信息填写完毕，可在页面下方预览查询得到的变量值，如果与期望值相符，即可单击【Add】添加变量。
4. 添加成功后，单击右侧菜单的【Save】保存至 Dashboard 配置。

#### 配置示例
以云服务器单机监控 Dashboard 为例，展示如何配置级联变量：地域变量、云服务器实例变量，如下图所示。
![](https://main.qcloudimg.com/raw/ca9bee86bcc812135701417e3e01d632.png)
![](https://main.qcloudimg.com/raw/5a1747fe167cdb00fdb0e3172cccfc9e.png)



## 应用变量

创建变量后，在 Dashboard 页面的左上角会展示变量选择框，可以切换变量值。变量有两种引用语法，`$varname` 和 `[[varname]]`。变量常用于 Panel 的查询语句中，以云服务器单机监控 Dashboard 为例，展示如何在查询中使用变量，如下图所示。此外，变量还可以应用在 Panel 标题、Text 文本面板等。


![](https://main.qcloudimg.com/raw/1fb3b205cf0c64e51de7f3a69047ed7f.png)
![](https://main.qcloudimg.com/raw/4b6e33f105c4f0ff8304b757c93e81c7.png)
