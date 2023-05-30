## 功能介绍
通过 Kudu 数据表监控及 Teblet 分析功能帮助排查表内数据热点倾斜、Tablet 部署层数据热点及倾斜等常见场景。
1. Kudu 数据表分析提供表级、表内 Tablet、TabletServer 读写 QPS、存储等相关负载维度信息
2. 提供 Tablet 分析，结合实际场景支持对所属表或所属 TabletServer 分析读取 QPS、写入 QPS 信息级历史变化趋势。

## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的**集群 ID/名称**进入集群详情页。
2. 在集群详情页中单击**集群服务**，然后选择 **Kudu组件右上角操作 >数据表分析**，即可进行相关 Kudu 数据表负载查询。

## 数据表列表		
Kudu 数据表列表可查看表级请求 QPS、写入 QPS、OnDiskDataSize 存储量信息，通过列 title 的排序按钮可定位集群 Top 数据表。
![](https://qcloudimg.tencent-cloud.cn/raw/db7e8039c2accda1cfd34964458971a8.png)
### 查看表详情
单击对应表名，即可弹出表详情。详情页可按整个表、节点维度展示所选择表的请求量（包括读和写）、store 大小（包括 OnDiskDataSize）两个指标数据，选择右上角的节点筛选器可切换节点查看。
![](https://qcloudimg.tencent-cloud.cn/raw/c1852a64ed3694fb6a6b9401862c3a52.png)
### Tablets 操作
单击 **Tablets 操作**，即可查看表所包含的各个 Tablet 的读写请求量，定位表内 Tablet 热点情况。
![](https://qcloudimg.tencent-cloud.cn/raw/a499ba555331ad4a06a804a4e59090c3.png)
### Tablet 详情
单击对应 Tablet 名，即可弹出 Tablet 详情，查看指标趋势。详情页可按不同时间粒度展示所选择表的请求量和扫描量等指标数据，选择右上角的时间粒度可切换粒度查看。
![](https://qcloudimg.tencent-cloud.cn/raw/43255830f702ee0f48395cc8f7598bb7.png)
### TabletServers 操作
单击 **TabletServers 操作**，即可查看表所分布的各个 TabletServer 的请求延迟及存储数据等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/6f588f01e03fdcb4b0f1cf520c710b0f.png)
## Tablet 分析
Tablet 分析可检索所属表或筛选所属 TabletServer，通过多维读请求、写请求、扫描量等指标信息定位集群热点请求分布。
![](https://qcloudimg.tencent-cloud.cn/raw/1f33a0121eb792b75378f185f7c63a7d.png)
单击信息列 title 的视图按钮，可查看当前页 Tablet 记录指标的历史趋势，观测突变请求信息，支持时间区间选择。
![](https://qcloudimg.tencent-cloud.cn/raw/fe5a500a15bc25d89b41ab9aa84fc2af.png)
