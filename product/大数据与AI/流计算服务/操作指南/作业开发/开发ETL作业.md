## 前提条件
流计算作业需运行于流计算独享集群，若还没有集群，请参考 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。

## 创建作业
在 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus) 中选择**作业管理 > 新建作业**，在弹窗中选择作业类型、作业名称和运行集群，单击**确定**，即可在作业列表中看到新建的作业。
![](https://qcloudimg.tencent-cloud.cn/raw/2c337d653e20f78f7a81cb9654b8d1f9.png)
创建 ETL 作业后，在**作业管理**中单击要进行开发的作业名称，然后单击**开发调试**，即可进入ETL作业开发界面。 

## 添加数据源表和目的表
从左侧组件面板可以拖拽出需要的数据源与数据目的。
![](https://qcloudimg.tencent-cloud.cn/raw/f3c3b89106ff754d8db140597eb3d841.png)

## 配置下游算子

移动鼠标到数据源并单击右边的加号可以添加下游算子。
![](https://qcloudimg.tencent-cloud.cn/raw/03bc9d7d4f744bbb88172612ec4c62e3.png)

## 连接组件

移动鼠标到组件并单击连接点可以对组件进行连接。
![](https://qcloudimg.tencent-cloud.cn/raw/b25f80633d6e1f01aad423d581aaa9da.png)

## 配置数据源

单击数据源可以进行数据源相关的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/e87178965245dd730e7e8ea75a79eadc.png)

## 管理连接信息

配置数据源或数据目的时，如果需要对连接进行管理，可以单击管理连接信息对连接进行新增、删除、修改的操作。
![](https://qcloudimg.tencent-cloud.cn/raw/171ad22d0f2d251cfc708ca59a1e83ba.png)

## 配置数据清洗

数据清洗组件可以对数据进行进一步的计算，例如修改字段取值、修改字段类型、对字段进行函数计算、以及新增字段等。字段取值可以输入字段值或者表达式，可以对从数据源表抽取出来的字段数据进行 [内置函数](https://cloud.tencent.com/document/product/849/18083) 数值转换或者计算。
![](https://qcloudimg.tencent-cloud.cn/raw/8de95d85739a9fbc367ae26a62fbeace.png)

## 配置数据目的

目前ETL作业支持多种数据目的端，单击相应的数据目的组件可以进行数据目的组件的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/b422f2bfc13086f2801b802aaaf809f9.png)

## 作业参数
ETL作业同样支持作业参数，通过作业参数可以对作业的Checkpoint、日志采集、高级参数、并行度、资源规格进行配置。
![](https://qcloudimg.tencent-cloud.cn/raw/9085987b5cf6c5c895b2cb585013fba0.png)

## 日志与监控

当作业运行成功后，可以通过上方按钮查看作业的日志与监控。
![](https://qcloudimg.tencent-cloud.cn/raw/1d28d7b640d633e68516fe54465e332b.png)
![](https://qcloudimg.tencent-cloud.cn/raw/5569a64d58e88b6277cabc9e421d9850.png)
