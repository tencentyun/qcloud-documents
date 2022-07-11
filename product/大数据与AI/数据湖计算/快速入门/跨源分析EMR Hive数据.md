数据湖计算 DLC 支持配置 EMR Hive 的数据源进行跨源联合分析。
## 使用前准备
- 获取 EMR Hive 地址。
- 使用具备创建数据目录权限的账号，详细权限请参见 [DLC 权限概述](https://cloud.tencent.com/document/product/1342/61548)。

## 创建 EMR Hive 数据源
1. 登录 [数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择服务地域。
2. 通过左侧导航栏进入**数据探索**，单击库表栏的**+**按钮，选择**新建数据目录**。
![](https://qcloudimg.tencent-cloud.cn/raw/228e5cad1a453d1a0767b0ae2eae4d5a.png)
3. 选择连接类型为 EMR Hive（HDFS），选择 EMR 的对应实例，VPC 信息将在实例选择后默认填充。**EMR Hive 支持 EMR 的版本：2.3.5，2.3.7，3.1.1，3.1.2**。
>! 需具备 EMR Hive 实例的相关权限才可进行选择。
>
![](https://qcloudimg.tencent-cloud.cn/raw/2f60675acb724481d42873f4c5b1e4bd.png)
4. 选择运行集群，目前仅支持选择Presto的独享数据引擎，如无对应引擎可至数据引擎页进行数据引擎创建。购买流程请参见 [购买独享数据引擎](https://cloud.tencent.com/document/product/1342/74056)。
>! 所选数据引擎网段不可与 EMR 实例网段相同，否则将导致网络冲突，无法进行数据查询分析。
5. 单击**确认**按钮即可完成数据目录创建。

## 查询 EMR Hive 数据
完成数据目录创建之后，即可在**数据探索页**的数据目录菜单进行数据目录切换。
![](https://qcloudimg.tencent-cloud.cn/raw/6d456e7699d726afbcb9e3ed0aeadace.png)
此时您可通过 SQL 语句对该数据目录进行查询分析，SQL 语法请参见 [SQL 语法概览](https://cloud.tencent.com/document/product/1342/73439)。
选择创建数据目录时绑定的数据引擎即可单击**运行**按钮，获得查询结果。
>! 仅绑定的数据引擎可查询该数据目录，其他数据引擎将无法进行查询。如需变更绑定的引擎，可单击数据目录判的设置按钮就行编辑修改。
>
![](https://qcloudimg.tencent-cloud.cn/raw/ed478f96670cbe9bfb8f7be040691f89.png)
