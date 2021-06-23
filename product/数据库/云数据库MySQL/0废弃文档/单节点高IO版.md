云数据库 MySQL 支持四种架构：高可用版、金融版、单节点高 IO 版、基础版。本文为您介绍单节点高 IO 版架构。


单节点高 IO 版采用单个物理节点部署，性价比高。

## 适用场景
有读写分离需求的各个行业应用。

## 架构特点
底层存储使用本地 NVMe SSD 硬盘，提供强大的 IO 性能。目前应用于 [只读实例](https://cloud.tencent.com/document/product/236/7270)，帮助业务分摊读压力。

## 架构基本框架图
![Alt text](http://imgcache.qq.com/open_proj/proj_qcloud_v2/gateway/shopcart/database/css/img/mysql-frame3.svg)
>!
>- 单节点部署存在单点风险，在只购买一个只读实例情况下，无法保证业务高可用，单个只读实例故障，会导致业务中断而影响客户。
>- 单个只读实例恢复时长受业务数据量大小影响，无法得到保证。因此，建议对可用性有要求的业务 [RO 组](https://cloud.tencent.com/document/product/236/11361) 内至少选购两个只读实例，保证可用性。


## 相关操作
- 云数据库 MySQL 支持创建一个或多个只读实例，以支持读写分离和一主多从应用场景，请参见 [创建只读实例](https://cloud.tencent.com/document/product/236/7270)。
- 云数据库 MySQL 支持创建一个或多个只读实例组成只读实例 RO 组，以保证可用性，请参见 [管理只读实例 RO 组](https://cloud.tencent.com/document/product/236/11361)。

