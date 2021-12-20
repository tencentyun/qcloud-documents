
Serverless 是腾讯自研云原生数据库 TDSQL-C 的无服务器架构版，是全 Serverless 架构的云原生数据库。Serverless 服务支持按实际计算和存储资源使用量收取费用，不用不付费，将腾讯云云原生技术普惠用户。
>?仅 TDSQL-C for MySQL 支持 Serverless 模式。

## 服务特性
- 自动驾驶（Autopilot）：数据库根据业务负载自动启动停止，无感扩缩容，扩缩容过程不会断开连接。
- 按使用计费（Utility Pricing）： 按实际使用的计算和存储量计费，不用不付费，按秒计量，按小时结算。

## 适用场景
- 开发、测试环境等低频数据库使用场景。
- 物联网（IoT）、边缘计算等不确定负载场景。
- 小程序云开发、中小企业建站等 SaaS 应用场景。

## 计费模式
计算和存储独立计费：计算按 CCU 个数计费，存储按使用量 GB 计费，计费系统按秒计费，按小时结算，详细价格请参见 [计费概述](https://cloud.tencent.com/document/product/1003/30493)。

CCU（CynosDB Compute Unit）为 Serverless 的计算计费单位，一个 CCU 近似等于1个 CPU 和 2GB 内存的计算资源，每个计费周期的 CCU 使用数量为：`数据库所使用的 CPU 核数` 与 `内存大小的1/2` 二者中取最大值。

您可以在 [购买页](https://buy.cloud.tencent.com/cynosdb) 根据业务情况选择所需数据库最小和最大的 CCU，该设置亦可在 [控制台](https://console.cloud.tencent.com/cynosdb) 进行修改。
![](https://main.qcloudimg.com/raw/20bdc2f419cb6666b0f7dd2cadbb47e1.png)

## 管理服务
### 暂停服务
- 您可根据业务需要自行开启或关闭自动暂停设置，该设置可在 [控制台](https://console.cloud.tencent.com/cynosdb) 进行修改。
 - 开启状态下，需要设定自动暂停时间，默认为1小时。数据库在该时间内没有连接和 CPU 使用时，将自动暂停，暂停后计算不计费，存储仍然按实际使用量计费。
 - 关闭状态下，数据库会保持持续运行，在没有连接和 CPU 使用时，按用户配置的最小 CCU 算力进行计费，适用于业务有心跳连接的应用场景。
![](https://main.qcloudimg.com/raw/68beac7929b10a1085e61b64956ea465.png)
- 您也可以在控制台对指定数据库进行手动暂停操作。
![](https://main.qcloudimg.com/raw/fa880723650d7cc8f86f888eb62e5521.png)
>!TDSQL-C Serverless 架构的自动暂停的判断条件为是否存在用户连接，如果业务场景需要使用 event_scheduler 来实现定时触发 SQL 的操作，则不建议开启自动暂停。
>
### 启动服务
处于暂停状态的数据库无法使用控制台功能，如需操作可待数据库自动启动后操作，或手动在 [控制台](https://console.cloud.tencent.com/cynosdb) 启动 Serverless 数据库。
![](https://main.qcloudimg.com/raw/a1068366aa2b08d3043d9852b7e73663.png)

当有连接访问时，系统会秒级自动启动处于暂停状态的数据库，短暂的启动过程中应用可能会收到以下报错信息，需要业务端具有重连的机制。
```
ERROR 9449 (08S01): CynosDB serverless instance is resuming, please try connecting again
ERROR 2003 (HY000): Can't connect to MySQL server on  'xxxx' (111)
```
![](https://main.qcloudimg.com/raw/938b717a6d5282ab386b0b33237645a8.png)

