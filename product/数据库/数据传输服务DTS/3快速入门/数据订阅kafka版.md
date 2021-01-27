数据传输服务 DTS 提供基于 binlog 的增量数据订阅功能，仅需几步简单操作，即可订阅云数据库 TencentDB 的增量更新数据。

数据订阅 Kafka 版支持通过 Kafka 客户端直接消费数据。通过数据订阅功能您可以轻松实现源库的增量数据变更订阅，方便您搭建云数据库和异构系统之间的数据同步，如缓存更新，ETL（数据仓库技术）实时同步，业务异步解耦等。
>?如需使用数据订阅 Kafka 版，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请。
>
## 前提条件
- 已准备好待订阅的腾讯云数据库 MySQL 或云数据库 MariaDB，云数据库 MySQL 支持同步的版本包括 MySQL 5.6、MySQL 5.7，云数据库 MariaDB 支持同步的版本包括 MariaDB 10.0.10、MariaDB 10.1.9、Percona 5.7.17。
- 已在源端实例中开启 binlog。
- 已在源端实例中创建订阅帐号，需要帐号权限如下：REPLICATION CLIENT、REPLICATION SLAVE、PROCESS 和全部对象的 SELECT 权限。

## 支持订阅的 SQL 操作
|  类型      | 数据变更                    | 结构变更                                                    | 数据+结构变更 |
| ------ | --------------------------- | ----------------------------------------------------------- | ------------- |
| 全实例 | DML：INSERT、UPDATE、DELETE | DDL：CREATE DATABASE、CREATE TABLE、ALTER TABLE、DROP TABLE | DML+DDL       |
| 数据库 | DML：INSERT、UPDATE、DELETE | DDL：CREATE TABLE、ALTER TABLE、DROP TABLE    | DML+DDL       |
| 数据表 | DML：INSERT、UPDATE、DELETE | DDL：ALTER TABLE、DROP TABLE                            | DML+DDL       |

## 操作步骤
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/dss)，在左侧导航选择【数据订阅】，单击【新建数据订阅】。
2. 在新建数据订阅页，选择相应配置，单击【立即购买】。
 - 计费模式：支持包年包月和按量计费。
 - 地域：地域需与待订阅的数据库实例订阅保持一致。
 - 数据库：目前支持 MySQL、Percona、MariaDB，请根据具体数据库类型进行选择。
 - 版本：选择【kafka 版】，支持通过 Kafka 客户端直接消费。
 - 订阅实例名称：编辑当前数据订阅实例的名称。
3. 购买成功后，返回数据订阅列表，单击”操作“列的【配置订阅】对刚购买的订阅进行配置，配置完成后才可以进行使用。
![](https://main.qcloudimg.com/raw/d45bbff5e702281fdc57984720999e6c.png)
4. 在配置数据库订阅页面，选择相应配置，单击【下一步】。
 - 实例：选择对应数据库实例，云数据库 MySQL 目前支持 MySQL 5.6、MySQL 5.7 高可用版的主实例，只读实例和灾备实例不支持数据订阅。
 - 数据库帐号：添加订阅实例的帐号和密码，帐号具有订阅任务需要的权限，包括 REPLICATION CLIENT、REPLICATION SLAVE、PROCESS 和全部对象的 SELECT 权限。注意根据权限最小化原则，授予的权限不能多也不能少，否则校验不通过。
![](https://main.qcloudimg.com/raw/5d4cb75fcadd6e33233781d09da10433.png)
5. 在订阅类型和对象选择页面，选择订阅类型，单击【保存配置】。
订阅类型，包括数据更新、结构更新和全实例。选择订阅类型后，选择待订阅的数据对象，包括数据库和数据表。
  - 数据更新：订阅选择对象的数据更新，包括数据 INSERT、UPDATE、DELETE 操作。
  - 结构更新：订阅实例中全部对象的结构创建、修改和删除。
  - 全实例：包括该订阅实例的全部对象的数据更新和结构更新。
![](https://main.qcloudimg.com/raw/edf52681e7fc00588697d1d7ccf7328f.png)
6. 在预校验页面，预校验任务预计会运行2分钟 - 3分钟，预校验通过后，单击【启动】完成数据订阅任务配置。
>?如果校验失败，请根据失败提示在待订阅实例中进行修正，并重新进行校验。
>
![](https://main.qcloudimg.com/raw/c47a857b65b6d3244b985e01492aff9f.png)
7. 单击启动后，订阅任务会进行初始化，预计会运行3分钟 - 4分钟，初始化成功后进入”运行中“状态。

## 后续操作
数据订阅 Kafka 版支持用户创建多个消费组，进行多点消费，请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
