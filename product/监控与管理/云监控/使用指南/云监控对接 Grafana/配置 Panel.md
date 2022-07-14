创建 Dashboard 之后，通过配置 Panel 信息，即可获取腾讯云监控的相应监控数据。现在以简单的 Graph 为例，展示如何配置 Panel 信息。

## CVM 云服务器监控

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云 CVM 云服务器的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 CVM 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云服务器监控接口的输入参数，可参见 [云服务器监控接口文档](https://cloud.tencent.com/document/api/248/30385)，更好地理解各配置项。
    - `Namespace` 命名空间，云服务器监控的命名空间为 `QCE/CVM`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例 ID** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称、`As PrivateIpAddress` 主网卡的内网IP、 `As PrivateIpAddresses` 主网卡的公网IP。
      - 可实例列表的获取可参见 [云服务器查询实例列表接口文档](https://cloud.tencent.com/document/api/213/15728)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/f36a04815d5d0c2157ef8450df658b1f.png)

## TencentDB 云数据库 MySQL

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云数据库 MySQL 的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 TencentDB 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云数据库MySQL监控接口的输入参数，可参见 [云数据库MySQL监控接口文档](https://cloud.tencent.com/document/api/248/30386)，更好地理解各配置项。
    - `Namespace` 命名空间，云服务器监控的命名空间为 `QCE/CDB`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例ID** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称、 `As Vip` 内网IP。
      - 实例列表的获取可参见 [云数据库MySQL查询实例列表接口文档](https://cloud.tencent.com/document/api/236/15872)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/fa269951d10a6bef77517b49bf15dc57.png)

## 云数据库 PostgreSql

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云数据库 PostgreSQL 的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 PostgreSQL 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云数据库PostgreSQL监控接口的输入参数，可参见 [云数据库PostgreSQL监控接口文档](https://cloud.tencent.com/document/product/248/45105)，更好地理解各配置项。
    - `Namespace` 命名空间，云服务器监控的命名空间为 `QCE/POSTGRES`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例ID** 展示实例列表。此外，可以选择 `As DBInstanceName`数据库名称, `PrivateIpAddresses`内网ip, `PublicIpAddresses`公网ip。
      - 实例列表的获取可参见 [云数据库PostgreSQL查询实例列表接口文档](https://cloud.tencent.com/document/api/409/16773)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/23b08f6712bf0ab80a7fea0fdc1194dd.png)

## 云数据库 MongoDB

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云云数据库 MongoDB 的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 mongodb 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云服务器监控接口的输入参数，可参见 [mongodb云监控接口文档](https://cloud.tencent.com/document/product/248/45104)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/CMONGO`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例id** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称。
      - 实例列表的获取可参见 [mongodb列表接口文档](https://cloud.tencent.com/document/api/240/38568)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/e631aa55f937e03aa5a7a90fbaaf4cde.png)

## 云数据库 Redis

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云云数据库 Redis的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 redis 监控服务的腾讯云监控数据源。
3. 云数据库 Redis 分两个命名空间：内存版（5秒）（Namespace=QCE/REDIS_MEM），ckv版和内存版（1分钟）（Namespace=QCE/REDIS）可根据自己需要在`Namespace`选择。
4. 配置项的内容对齐腾讯云服务器监控接口的输入参数，可参见 [Redis云监控接口文档](https://cloud.tencent.com/document/product/248/49729)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/REDIS_MEM`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例id** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称。
      - 实例列表的获取可参见 [Redis实例列表接口文档](https://cloud.tencent.com/document/api/239/20018)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/88d13ac80ec80bc2696371b43312f506.png)

## 云数据库 CYNOSDB_MYSQL

  1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云云数据库  CYNOSDB(CYNOSDB_MYSQL) 的监控数据。
  2. `Queries to` 数据源列表，选择已配置的包含 cynosdbMysql 监控服务的腾讯云监控数据源。
  3. 配置项的内容对齐腾讯云监控cynosdbMysql监控接口的输入参数，可参见 [云数据库 CYNOSDB(CYNOSDB_MYSQL) 云监控接口文档](https://cloud.tencent.com/document/product/248/45106)，更好地理解各配置项。

    - `Namespace` 命名空间，例如 `QCE/CYNOSDB_MYSQL`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例ID** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称。
      - 实例列表的获取可参见 [云数据库 CYNOSDB(CYNOSDB_MYSQL)列表接口文档](https://cloud.tencent.com/product/cynosdb)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/713309fe64571e80c221d7b110712c8e.png)
    

## 云数据库 TcaplusDB

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云云数据库 TcaplusDB(TCAPLUS)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 tcaplus 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控tcaplus监控接口的输入参数，可参见 [云数据库  TcaplusDB(TCAPLUS) 云监控接口文档](https://cloud.tencent.com/document/product/248/45107)，更好地理解各配置项。
  - `Namespace` 命名空间，例如 `QCE/TCAPLUS`。
  - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
  - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
  - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
  - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
    - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例ID** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称。
    - 实例列表的获取可参见 [云数据库 TcaplusDB(TCAPLUS)列表接口文档](https://cloud.tencent.com/document/api/1003/48334)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
    - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
    - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/cd365a087b317d0af25daed5161651c4.png)

## 云数据库 SQL Server

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云云数据库 sqlserver(SQLSERVER) 的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 sqlserver 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控 sqlserver 监控接口的输入参数，可参见 [云数据库sqlserver(SQLSERVER)云监控接口文档](https://cloud.tencent.com/document/product/248/45146)，更好地理解各配置项。
  - `Namespace` 命名空间，例如 `QCE/SQLSERVER`。
  - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
  - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
  - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
  - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
    - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例ID** 展示实例列表。此外，可以选择 `As Name` 实例名称。
    - 实例列表的获取可参见 [云数据库sqlserver(SQLSERVER)列表接口文档](https://cloud.tencent.com/document/api/238/19969)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
    - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
    - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/abe8a325cd0ee17114f8eae4b76068d9.png)

## CDN 内容分发式网络

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云 CDN 的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 CDN 监控服务的腾讯云监控数据源。
3. CDN 指标分两个命名空间：国内域名（Namespace=QCE/CDN），国外域名（Namespace=QCE/OV_CDN）可根据自己需要在`Namespace`选择。
4. 配置项的内容对齐腾讯 CDN 监控接口的输入参数，可参见 [CDN云监控接口文档](https://cloud.tencent.com/document/product/248/50386)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/CDN`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As Domain`，以 **域名** 展示实例列表。此外，可以选择 `As ProjectId` 项目id。
      - 域名列表的获取可参见 [CDN域名列表接口文档](https://cloud.tencent.com/document/api/228/41118)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

## BWP 带宽包

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云 BWP 的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 BWP 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云 BWP 监控接口的输入参数，可参见 [BWP云监控接口文档](https://cloud.tencent.com/document/product/248/45098)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/BWP`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为`As BandwidthPackageId`，以 **带宽包id** 展示实例列表。此外，可以选择 `As BandwidthPackageName` 名称。
      - 域名列表的获取可参见 [BWP域名列表接口文档](https://cloud.tencent.com/document/api/215/19209)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/5ab6db7adb0dfe9ab98258b84d44ee95.png)

## CKAFKA 消息队列

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云 ckafka 消息队列的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 ckafka 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯 ckafka 监控接口的输入参数，可参见 [ckafka云监控接口文档](https://cloud.tencent.com/document/product/248/45121)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/CKAFKA`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例id** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称。
      - 实例列表的获取可参见 [ckafka列表接口文档](https://cloud.tencent.com/document/api/597/40835)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 10`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/a4dbbbc2012ef393cc87419d7e531b2b.png)

## CLB 负载均衡

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云 负载均衡的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 CLB 监控服务的腾讯云监控数据源。
3. 负载均衡指标分三个命名空间：公网负载均衡监控指标（Namespace=QCE/LB_PUBLIC），内网负载均衡四层协议监控指标（Namespace=QCE/LB_PRIVATE）， 七层协议监控指标（Namespace=QCE/LOADBALANCE），可根据自己需要在`Namespace`选择。
4. 配置项的内容对齐腾讯云服务器监控接口的输入参数，可参见 [负载均衡云监控接口文档](https://cloud.tencent.com/document/product/248/51898)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/LB_PUBLIC`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As LoadBalancerId`，以 **实例ID** 展示实例列表。此外，可以选择 `As LoadBalancerName` 实例名称、`As LoadBalancerVips` 网络ip。
      - 实例列表的获取可参见 [负载均衡实例列表接口文档](https://cloud.tencent.com/document/api/214/30685)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。
    - `Listener` **可选**监听器，可不选择，这时采用实例维度请求，对应输入参数的 `Listener.N` 字段，列表会自动获取。
      - 为了适应不同用户的习惯，监听器列表会以不同的字段展示，默认为 `As ListenerId`，以 **监听器ID** 展示实例列表。此外，可以选择 `As ListenerName` 监听器名称、`As Port` 端口。
      - 监听器列表的获取可参见 [负载均衡监听器列表接口文档](https://cloud.tencent.com/document/api/214/30686)。

![](https://main.qcloudimg.com/raw/f0e32efbe3df41460ca53380baff3d25.png)

## LB 弹性公网 IP

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云lb弹性公网ip的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 lb 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯 lb 监控接口的输入参数，可参见 [lb云监控接口文档](https://cloud.tencent.com/document/product/248/45099)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/LB`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As AddressId`，以 **实例地址id** 展示实例列表。此外，可以选择 `As AddressName`地址名称和`As AddressIp` 地址IP。
      - 实例列表的获取可参见 [lb列表接口文档](https://cloud.tencent.com/document/api/215/16702)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/b9b926cd1a5e4720a99edaa1bd84dc21.png)

## CFS 文件存储

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云cfs文件存储的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 cfs 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯cfs监控接口的输入参数，可参见 [cfs云监控接口文档](https://cloud.tencent.com/document/product/248/45143)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/CFS`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As FileSystemId`，以 **文件系统id** 展示实例列表。此外，可以选择 `As FsName` 文件系统名称。
      - 实例列表的获取可参见 [CFS列表接口文档](https://cloud.tencent.com/document/api/582/38170)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/419b5c2db298315be1d8a704cc8c8b5d.png)

## SCF 云函数

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云scf云函数的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 scf 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯 scf 监控接口的输入参数，可参见 [ scf 云监控接口文档](https://cloud.tencent.com/document/product/248/45130)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/SCF_V2`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As FunctionId`，以 **函数id** 展示实例列表。此外，可以选择 `As FunctionName` 函数名称。
      - 实例列表的获取可参见 [ SCF 列表接口文档](https://cloud.tencent.com/document/api/583/18582)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/1c5ce839f001757f149635d798f4f6b4.png)

## DCX 专线接入-专用通道

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云专线接入-专用通道(DCX)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 dcx 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控dcx监控接口的输入参数，可参见 [专线接入-专用通道(DCX)云监控接口文档](https://cloud.tencent.com/document/product/248/45101)，更好地理解各配置项。
 - `Namespace` 命名空间，例如 `QCE/DCX`。
 - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
 - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
 - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
 - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
   - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As DirectConnectTunnelId`，以 **通道ID** 展示实例列表。此外，可以选择 `As DirectConnectTunnelName` 通道名称。
   - 实例列表的获取可参见 [专线接入-专用通道(DCX)列表接口文档](https://cloud.tencent.com/document/api/216/19819)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
   - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
   - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/7bfa939046d03bddcab30c44b3e14490.png)
    

## DC 专线接入-物理专线

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云专线接入-物理专线(DC)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 dc 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控dc监控接口的输入参数，可参见 [专线接入-物理专线(DC)云监控接口文档](https://cloud.tencent.com/document/product/248/45102)，更好地理解各配置项。
  - `Namespace` 命名空间，例如 `QCE/DC`。
  - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
  - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
  - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
  - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
    - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As DirectConnectId`，以 **专线ID** 展示实例列表。此外，可以选择 `As DirectConnectName` 专线名称。
    - 实例列表的获取可参见 [专线接入-物理专线(DC)列表接口文档](https://cloud.tencent.com/document/api/216/34826)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
    - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
    - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/7c509f6453fa4f07c05ca9a52e98e71d.png)

## VPNGW 私有网络-VPN 网关

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云私有网络-VPN 网关(VPNGW)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 vpngw 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控vpngw监控接口的输入参数，可参见 [私有网络-VPN 网关(VPNGW)云监控接口文档](https://cloud.tencent.com/document/product/248/45070)，更好地理解各配置项。
  - `Namespace` 命名空间，例如 `QCE/VPNGW`。
  - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
  - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
  - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
  - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
    - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As VpnGatewayId`，以 **VPN网关ID** 展示实例列表。此外，可以选择 `As VpnGatewayName` VPN网关名称。
    - 实例列表的获取可参见 [私有网络-VPN 网关(VPNGW)列表接口文档](https://cloud.tencent.com/document/api/215/17514)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
    - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
    - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/81b7d5b2b74fd9b3890ac3b47727e4ef.png)
    

## DCG 私有网络-专线网关

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云私有网络-专线网关(DCG)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 dcg 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控dcg监控接口的输入参数，可参见 [私有网络-专线网关(DCG)云监控接口文档](https://cloud.tencent.com/document/product/248/45072)，更好地理解各配置项。
  - `Namespace` 命名空间，例如 `QCE/DCG`。
  - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
  - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
  - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
  - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
    - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As DirectConnectGatewayId`，以 **专线网关ID** 展示实例列表。此外，可以选择 `As DirectConnectGatewayName` 专线网关名称。
    - 实例列表的获取可参见 [私有网络-专线网关(DCG)列表接口文档](https://cloud.tencent.com/document/api/215/30644)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
    - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
    - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/e7a2af8cf618ccc6e84709c0db295273.png)
    

## CDNPROVINCE 省份域名

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云省份域名(CDN_LOG_DATA)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 cdnProvince 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控 cdnProvince 监控接口的输入参数，可参见 [省份域名(CDN_LOG_DATA)云监控接口文档](https://cloud.tencent.com/document/product/248/50388)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/CDN_LOG_DATA`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As Domain`，以 **域名** 展示实例列表。此外，可以选择 `As ProjectId` 。
      - 实例列表的获取可参见 [省份域名(CDN_LOG_DATA)列表接口文档](https://cloud.tencent.com/document/api/228/41118)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。
    - `Isp` 运营商列表。
    - `Province` 可选省份列表。


![](https://main.qcloudimg.com/raw/9b09df7de6b157974d0bfcbbb38cd776.png)
    

## APIGATEWAY API 网关

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云API 网关(APIGATEWAY)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 apigateway 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控apigateway监控接口的输入参数，可参见 [API 网关(APIGATEWAY)云监控接口文档](https://cloud.tencent.com/document/product/248/45127)，更好地理解各配置项。
    - `Namespace` 命名空间，例如 `QCE/APIGATEWAY`。
    - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
    - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
    - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
    - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
      - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As ServiceId`，以 **协议端口 ID** 展示实例列表。此外，可以选择 `As ServiceName` 。
      - 实例列表的获取可参见 [API 网关(APIGATEWAY)列表接口文档](https://cloud.tencent.com/document/api/628/45198)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
      - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
      - `Show Details` 按钮仅在选择非模板变量时显示。
    - `EnvironmentName` 环境名称，会根据上面Instance内容获取。


![](https://main.qcloudimg.com/raw/a9ceee232b0d7e07c835e933a32c21e7.png)
    

## CBS 云硬盘

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云云硬盘(BLOCK_STORAGE)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 cbs 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控cbs监控接口的输入参数，可参见 [云硬盘(BLOCK_STORAGE)云监控接口文档](https://cloud.tencent.com/document/product/248/45411)，更好地理解各配置项。
  - `Namespace` 命名空间，例如 `QCE/BLOCK_STORAGE`。
  - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
  - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
  - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
  - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
    - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As DiskId`，以 **云硬盘ID** 展示实例列表。此外，可以选择 `As DiskName` 云硬盘名称。
    - 实例列表的获取可参见 [云硬盘(BLOCK_STORAGE)列表接口文档](https://cloud.tencent.com/document/api/362/16315)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
    - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
    - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/e022476856e5d42e2681d4dc608fba26.png)
    

## CES Elasticsearch指标

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云Elasticsearch指标(CES)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 ces 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控ces监控接口的输入参数，可参见 [Elasticsearch指标(CES)云监控接口文档](https://cloud.tencent.com/document/product/248/45129)，更好地理解各配置项。
  - `Namespace` 命名空间，例如 `QCE/CES`。
  - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
  - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
  - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
  - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
    - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As InstanceId`，以 **实例ID** 展示实例列表。此外，可以选择 `As InstanceName` 实例名称。
    - 实例列表的获取可参见 [Elasticsearch指标(CES)列表接口文档](https://cloud.tencent.com/document/api/845/30631)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
    - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
    - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/62f83d047bd95887f5be0a315d022cbd.png)
    

## CMQ 消息队列服务监控

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云消息队列CMQ(队列服务监控CMQ)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 cmq 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控cmq监控接口的输入参数，可参见 [消息队列CMQ(队列服务监控CMQ)云监控接口文档](https://cloud.tencent.com/document/product/248/45114)，更好地理解各配置项。
  - `Namespace` 命名空间，例如 `QCE/CMQ`。
  - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
  - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
  - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
  - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
    - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As QueueName`，以 **队列名称** 展示实例列表。此外，可以选择 `As QueueId` 队列ID。
    - 实例列表的获取可参见 [消息队列CMQ(队列服务监控CMQ)列表接口文档](https://cloud.tencent.com/document/api/406/42624)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
    - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
    - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/192fa4e13dd2a8374520373402c70dff.png)
    

## CMQTOPIC 消息队列主题订阅监控

1. 单击 **New Panel** 面板的 **Add Query** 选项，进入 Panel 配置页面。在左侧第一个 `Query` 选项卡，通过配置选项获取腾讯云消息队列CMQTOPIC(主题订阅监控)的监控数据。
2. `Queries to` 数据源列表，选择已配置的包含 cmqTopic 监控服务的腾讯云监控数据源。
3. 配置项的内容对齐腾讯云监控cmqTopic监控接口的输入参数，可参见 [消息队列CMQTOPIC(主题订阅监控)云监控接口文档](https://cloud.tencent.com/document/product/248/45113)，更好地理解各配置项。
  - `Namespace` 命名空间，例如 `QCE/CMQTOPIC`。
  - `Region` 地域，地域列表会根据 `Namespace` 选项自动获取，单击选择某一地域。
  - `MetricName` 指标名称，指标列表会根据 `Namespace` 和 `Region` 选项自动获取，单击选择某一指标。
  - `Period` 监控统计粒度，周期列表会根据 `MetricName` 选项自动获取，单击选择某一统计粒度。
  - `Instance` 实例，对应输入参数的 `Instances.N` 字段，实例列表会自动获取。
    - 为了适应不同用户的习惯，实例列表会以不同的字段展示，默认为 `As TopicName`，以 **主题名称** 展示实例列表。此外，可以选择 `As TopicId` 主题ID。
    - 实例列表的获取可参见 [消息队列CMQTOPIC(主题订阅监控)列表接口文档](https://cloud.tencent.com/document/api/406/42637)。切换 `Show Details` 为 `true`，可展示实例请求参数，默认参数为`Offset = 0` 和 `Limit = 20`。如果需要变更实例查询条件，可参见接口文档，配置相应参数。
    - **注意：** 在本应用中，监控数据的单次查询为原子操作，即查询某一实例的某一指标的监控数据，故实例只能单选，如需查询多实例的监控数据，单击右上角的 `Add Query` 增加新的查询。  
    - `Show Details` 按钮仅在选择非模板变量时显示。

![](https://main.qcloudimg.com/raw/17ea626b3c07132396ff5aa6bb78312d.png)
