## 操作场景

消息队列 CKafka 支持用户转储消息的能力，您可以将 CKafka 消息转储至云数据库 MySQL（CDB）便于对筛选数据做持久化存储。

## 前提条件

该功能目前依赖云函数（SCF）、云数据库（CDB）服务。使用时需提前开通云函数 SCF ，云数据库MySQL 等相关服务及功能。

## 操作步骤

转储 MySQL 数据库的方案将使用 SCF 的 CKafka 触发器进行，通过 CKafka 触发器消息转储到  MySQL 数据库。

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击**topic管理**标签页，单击操作列的**消息转储**。
4. 单击**添加消息转储**，选择转储类型为**通用模板**。
![](https://qcloudimg.tencent-cloud.cn/raw/c246a9fdbf80859ba960b8fb30545202.png)
   - 转储类型：选择通用模板
   - 起始位置：转储时历史消息的处理方式，topic offset 设置。
   - 云函数授权：知晓并同意开通创建云函数，该函数创建后需用户前往云函数设置更多高级配置及查看监控信息。
5. 创建完成后单击**函数管理**链接，进入云函数控制台进行下一步操作。
![](https://qcloudimg.tencent-cloud.cn/raw/205da6c328f3312db3a507868ec89e99.png)
6. 在云函数控制台上传 CKafkaToMysql 模板代码（[Github下载地址](https://github.com/tencentyun/scf-demo-repo/tree/master/Python2.7-CkafkaToMysql)）。
   ![](https://main.qcloudimg.com/raw/41dce628f44c633eb8ff83a2197f97e8.png)
7. 在云函数的**函数配置**中添加如下环境变量。
   ![](https://main.qcloudimg.com/raw/a909865f3c7f3564505ab4d5e4ef240e.png)
   ```
   dbhost=172.16.0.59 // 数据库VPC HOST地址
   dbuser=tabor // 数据库用户名
   dbpwd=1237018 // 数据库密码
   dbdatabase=canmengtest // 数据库名
   dbtable=123321 // 数据表名
   ```
8. 在云函数的**函数配置**中修改 VPC 网络，将云函数 VPC 网络与云数据库 VPC 网络设为一致即可。
![](https://qcloudimg.tencent-cloud.cn/raw/08d3bde73c6666af3457b96ac007e92a.png)
9. 在云数据库 MySQL [DMC控制台](https://gz-dmc.cloud.tencent.com/v2/) 添加相关数据库，数据表与表结构。
   1. 创建数据库，与环境变量中的数据库名相同：
![](https://qcloudimg.tencent-cloud.cn/raw/714baaab76f7d01ab24931ffd55ae7c7.png)
   2. 创建数据表，与环境变量中的数据库表相同：
![](https://qcloudimg.tencent-cloud.cn/raw/2c6e6620f402455bcf86f6f7e03c5576.png)
   3. 创建表结构，与函数代码中的插入结构相同，默认插入 offset、Megs 列，可在 index.py 文件的33行修改相关插入结构：
![](https://qcloudimg.tencent-cloud.cn/raw/232186ebb53a2b3fd0f30430f4c7fd4f.png)
     数据表与数据结构创建亦可直接通过 MySQL 命令直接创建：
     ```
     CREATE TABLE `test_table` ( `offset` VARCHAR(255) NOT NULL , `Megs` LONGTEXT NOT NULL ) ENGINE = InnoDB;
     ```
10. 在云函数触发器控制台中打开 CKakfa 触发器。
![](https://qcloudimg.tencent-cloud.cn/raw/f7a532c94f31d30d742b1890644d07c0.png)


## 产品限制和费用计算

- 转储速度与 CKafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 CKafka 实例的峰值带宽。
- CKafkaToMySQL 方案采用 CKafka 触发器，重试策略与最大消息数等设置参见 [CKafka 触发器](https://cloud.tencent.com/document/product/583/17530)。
- 使用消息转储 MySQL 能力，默认转储的信息为 CKafka 触发器的 offset，msgBody 数据，如需自行处理参见 [CKafka 触发器的事件消息结构](https://cloud.tencent.com/document/product/583/17530#ckafka-.E8.A7.A6.E5.8F.91.E5.99.A8.E7.9A.84.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF.E7.BB.93.E6.9E.84)。 
- 该功能基于云函数 SCF 服务提供。SCF 为用户提供了一定 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。

