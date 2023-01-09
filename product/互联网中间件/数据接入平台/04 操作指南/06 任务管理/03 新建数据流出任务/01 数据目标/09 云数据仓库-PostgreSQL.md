## 操作场景

数据接入平台提供数据流出能力，您可以将 CKafka 数据分发至云数据仓库-PostgreSQL 版以对数据进行存储、查询和分析。

## 前提条件

- 该功能依赖云数据仓库 PostgreSQL 服务，使用前需要先开通相关功能。
- 创建对应实例的云数据仓库 PostgreSQL 连接管理时，设置的角色需要配置相应的白名单，否则无法创建成功或流出失败。
  
### 白名单网段
支持配置以下白名单网段：
- 9.0.0.0/8 
- 30.0.0.0/8 
- 11.0.0.0/8 
  
例如：
![](https://qcloudimg.tencent-cloud.cn/raw/5f38e136133040ba7c6871d344c7b3b4.png)
![](https://qcloudimg.tencent-cloud.cn/raw/9b5afae80e3492c56554481f0d405574.png)
若在创建任务后提示 "org.postgresql.util.PSQLException: FATAL: no pg_hba.conf entry for host "30.xx.xx.xx", user "user", database "test", SSL off"，也需要加上相应的白名单。
![](https://qcloudimg.tencent-cloud.cn/raw/5f90e1d38a4835b2fb7d1d2b33ff7d33.png)
  

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据流出**，数据目标类型选择 **云数据仓库-PostgreSQL**，单击**下一步**。
4. 配置数据源信息。
  ![](https://qcloudimg.tencent-cloud.cn/raw/f8b47026ccb8b0982605b59d7b926f5b.png)
  - 源 Topic 类型：选择数据源 Topic
    - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/1591/77020)。
    - CKafka Topic：选择在 CKafka 创建好的实例和 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
  - 起始位置：选择转储时历史消息的处理方式，topic offset 设置。
5. 设置上述信息后，单击**下一步**，单击**预览 Topic 数据**，将会选取**源 Topic** 中的第一条消息进行解析。
<dx-alert infotype="explain" title="目前解析消息需要满足以下条件：">
- 消息为 JSON 字符串结构。
- 源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用使用 [数据处理](https://cloud.tencent.com/document/product/1591/77082#3) 进行简单的消息格式转换。
</dx-alert>
6. （可选）开启数据处理规则，具体配置方法请参见 [简单数据处理](https://cloud.tencent.com/document/product/1591/74495)。
7. 单击**下一步**，配置数据目标信息。
  ![](https://qcloudimg.tencent-cloud.cn/raw/b0c7ae657dbc55d6995edf6ffd0de664.png)
  - 数据目标：选择提前创建好的云数据仓库-PostgreSQL 连接。
  - database：选择数据流出的数据库。
  - table：选择数据流出的表。
  - 数据库同步模式
    - **默认字段匹配**：本选项仅用于：
      1. 源 topic 数据为 DIP 从 MySQL/PostgreSQL 中订阅的、单张表的 Binlog/row-level changes 数据（增删改）；
      2. 源 topic 数据必须有主键，且必须包含 schema；
    - **字段逐一匹配：**
      - 源数据：点击拉取源 Topic 数据，需要逐一给消息字段选择匹配的目标表字段。
      - 插入模式：支持 **insert** 或者 **upsert**，选择 upsert 时需选择**主键**（当插入行冲突时，任务将更新冲突行除主键之外其余的列）。
  - 上游数据格式：支持 JSON 和 Debezium。
    > ?当上游 MySQL Binlog/PostgreSQL row-level changes 数据表结构变化时，变化可以同步更新到下游 PostgreSQL。  
  - 失败消息处理：失败消息处理：选择投递失败的消息的处理方式，支持**丢弃**、**保留**和**投递至 CLS**（需指定投递到的日志集和日志主题并授权访问日志服务 CLS）三种方式。
    - 保留：适合用于测试环境，任务运行失败时将会终止任务不会重试，并且在事件中心中记录失败原因。
    - 丢弃：适合用于生产环境，任务运行失败时将会忽略当前失败消息。建议使用 "保留" 模式测试无误后，再将任务编辑成 "丢弃" 模式用于生产。
    - 投递至 CLS：适合用于严格生产环境，任务运行失败时会将失败消息及元数据和失败原因上传到指定 CLS 主题中。
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以查看任务创建进度。
