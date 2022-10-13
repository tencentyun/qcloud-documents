## 业务场景
当使用腾讯云容器服务 TKE 进行业务部署时，可通过配置 TKE Agent 来采集 TKE 集群内各个 pod 的标准输出日志并投递到下游目标端（如 Elasticsearch 集群等 ）。TKE Agent 是数据集成 DataInLong 提供的轻量型日志采集器，本文将向您介绍如何通过 TKE Agent 将集群 POD 标准日志全量投递到下游 Elasticsearch 集群。

## 操作步骤
### 配置项目空间
>? 若您使用的是 WeData 产品，配置项目空间操作请参见 [WeData 项目列表](https://cloud.tencent.com/document/product/1267/72614)。

1. 进入 [DataInLong 控制台](https://console.cloud.tencent.com/datainlong/projectlist)，单击**项目列表 > 新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/567def980c8354c4d368b9592168a4f4.png)
2. 配置项目空间信息。
<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>项目名称/标识</td>
<td>项目命名与唯一标识，其中唯一标识创建后不可修改</td>
</tr>
<tr>
<td>高级设置-项目成员</td>
<td>为此创建的项目中添加其他项目成员，创建者默认加入项目空间</td>
</tr>
<tr>
<td>成员角色</td>
<td>批量为项目成员配置角色<br>提示：此处默认为前面添加的成员添加统一的角色，后续可<b>项目管理</b>模块修改</td>
</tr>
</tbody></table>

### 配置集成资源组
>? 若有存量集成资源组，可直接操作 [配置 DataProxy](#配置DataProxy)。
>
1. 进入 [DataInLong 控制台](https://console.cloud.tencent.com/datainlong/projectlist)， 选择**集成资源**并单击**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/b9c8e6f70eead3e113e0daf460f747fd.png)
>? 若您使用的是 WeData 产品，请单击进入 [WeData 控制台](https://console.cloud.tencent.com/wedata/fusion/executorResource)。

2. 购买集成资源组。
![](https://qcloudimg.tencent-cloud.cn/raw/117fc0daa48422929beec20169c539ba.png)
     - TKE 日志采集是通过主动上报方式同步数据，在配置资源时候场景方案**离线+实时同步（含队列）**方案。选择后，系统将为资源组内置共享队列。
     - 离线资源包与实时资源包可根据实际数据情况配置规格、以及数量。
     - 资源组网络建议选择 TKE 集群和 ElasticSearch 数据源所在网络；若 TKE 集群和 ElasticSearch 不在一个 VPC 环境，可为 VPC 配置开通公网，详细操作参见 [资源组配置公网](https://cloud.tencent.com/document/product/1580/81042)。
3. 购买完成后返回控制台。[](id:配置DataProxy)
单击资源组名称，在右侧的弹窗抽屉内**离线资源包使用概况 > DataProxy规格及数量**单击**编辑**按钮，开启并配置 DataProxy 的数量。
![](https://qcloudimg.tencent-cloud.cn/raw/41adf36a0f1b1c32693a4717c0da9190.png)
配置后单击**确定**即完成 DataProxy 的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/0d1aea93f5683c7bebd41d42737b27c5.png)
>? 
>- 集成资源组需包含实时资源包才可成功配置 DataProxy。
>- DataProxy 总规格不可超过离线包规格的1/2。

4. 关联资源组与项目空间
>? 若在购买页面内已经关联资源组与项目空间，可忽略此步骤。
>
![](https://qcloudimg.tencent-cloud.cn/raw/420e93919f30316621b933e6ee099663.png)

### 创建数据源
配置 ElasticSearch 数据源。进入**项目管理**模块，选择**数据源管理 > 新建数据源 > 选择 ElasticSearch**。以 ElasticSearch 数据源为例，数据连通性测试成功后，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/d7cafe0f16d4b4dead7eb8bf7a408321.png)

###  创建配置 TKE Agent 采集器
1. 进入数据集成模块，单击**采集器管理 > Agent > 创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/464a816bc935fc375d8d3aef13d86bf2.png)
2. 在创建 Agent 采集器的弹窗中，配置 TKE Agent 的相关信息。
![](https://qcloudimg.tencent-cloud.cn/raw/d9b2f7bfde21c00c84b5b70e3c723825.png)
<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>类型</td>
<td>请选择 TKE Agent</td>
</tr>
<tr>
<td>地域</td>
<td>选择需要采集的 TKE 集群所属地域，可登录前往 <a href="https://console.cloud.tencent.com/tke2/cluster?rid=8">TKE 控制台</a> 查看集群信息</td>
</tr>
<tr>
<td><nobr>TKE 集群 ID</td>
<td>选择一个需安装 TKE 集群信息<br>提示：<br>1. 仅支持在“运行中”状态的 TKE 集群安装 Agent  <br>2. 一个 agent 将占用集群1C512M规格</td>
</tr>
<tr>
<td>关联资源组</td>
<td>将 Agent 与具体执行资源组进行绑定，Agent 将使用资源组中 manager url 进行数据上报<br>提示：TKE 集群（Agent）需与集成资源组位于同一个 VPC，或对应 VPC 已配置公网的情况可同步数据。资源组公网配置流程请参见 <a href="https://cloud.tencent.com/document/product/1580/81042">资源组配置公网</a></td>
</tr>
</tbody></table>
配置完成后，Agent 将作为 TKE 上的日志采集器，后续支持在多个实时任务中同时使用一个 Agent 用于 POD 日志提取。

### 配置实时同步任务
1. 创建任务。
进入数据集成模块，创建**实时同步任务**，在弹出的提示框中输入任务名称和备注，选择**画布模式**或**表单模式**并单击完成。
![](https://qcloudimg.tencent-cloud.cn/raw/8c903c8552b0535a7a43b2408580e12d.png)
本文以画布模式为例，创建完成任务后可在任务列表页面单击新建的实时同步任务名称进入任务编辑界面。画布模式下可分别拖拽新建读取数据源和写入数据源，连接对应读取与写入节点。
![](https://qcloudimg.tencent-cloud.cn/raw/23844852c583f6d4693a85880333c806.png)
2. 配置读取节点。
双击 TKE 读取节点，可在右侧抽屉弹窗中如下图所示配置需要读取的节点信息，完成后单击保存。
![](https://qcloudimg.tencent-cloud.cn/raw/c6b12987d1c95f0c1550d5a3318871aa.png)
    - 日志类型：选择**标准输出**，将默认采集 TKE 集群下任意服务的 stderr、stdout 的容器日志。
    - 命名空间：可根据具体需采集命名空间对象指定。为保障使用性能，建议单个 Agent 采集命名空间不超过15个文件。
    - 内容提取模式：选择**全内容**将默认将每条日志记录默认解析为名称为“__ CONTENT __”的完全字符串。
3. 配置写入节点。
双击 ElasticSearch 写入节点，可在右侧抽屉弹窗中配置需要写入的节点信息。
![](https://qcloudimg.tencent-cloud.cn/raw/4df2bdf1f6e3fbdfe2a2a7b1e9967927.png)
下拉至底部，配置 MySQL 与 DLC 表字段映射，完成后单击保存。选择 ES 不同资源与来源数据字段之间的映射关系。完成后单击保存。
![](https://qcloudimg.tencent-cloud.cn/raw/2380adea35bd6cda624416b5512033c9.png)
4. 任务保存与提交。
    - 配置完节点后，单击**任务数据**配置集成资源组。此资源组为已关联至本空间的资源组。
>? 此处请选择 TKE 采集器所绑定的集成资源，否则将导致任务运行失败。
>
![](https://qcloudimg.tencent-cloud.cn/raw/f3f339cc73a3497e2e1a88c3e336294d.png)
    - 完成后单击**提交**按钮，并在弹窗口中勾选**立即启动**。
![](https://qcloudimg.tencent-cloud.cn/raw/6dad775b1bd7595a594a765f6643a0b4.png)

### 任务运维
提交任务后，可进入**实时运维**页面查看并监控任务状态。
![](https://qcloudimg.tencent-cloud.cn/raw/369b0ec37026c3592f5df654ebac9a53.png)
单击**运行监控**，可查看当前任务数据指标统计、以及配置监控告警等。

