## 功能说明
Hbase 表级监控提供了 HBASE 中各表的读写请求数以及表存储情况的监控。
### 查看表监控概览
登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，单击左侧【组件管理】选择集群，在组件名称下选择 【HBase】或 HBase 右侧角色管理进入【表级监控】。
概览页以列表的形式展示了 HBase 表的实时读请求量、写请求量、memstore 大小、storeFile 大小四个维度的信息，单击表头可按相应维度进行排序，选择左上角的输入框可输入表名进行查询。
![](https://main.qcloudimg.com/raw/9222ab19772089e8871b0c026b9c85cc.png)
###  查看表详情
详情页进入路径：选择表级监控概览页【操作】>【详情】。 
详情页可按整个表、节点维度展示所选择表的请求量（包括读和写）、store 大小（包括 memstore 和 storeFile）两个指标数据，选择左上角的下拉框可在不同节点间切换。
![](https://main.qcloudimg.com/raw/c92aef0f13aaf5673f2aaffe9c276053.png)
