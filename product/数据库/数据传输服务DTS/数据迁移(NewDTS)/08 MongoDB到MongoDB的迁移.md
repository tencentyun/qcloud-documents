 本文介绍使用 DTS 数据迁移功能从 MongoDB 迁移数据至腾讯云数据库 MongoDB 的操作指导。 

MongoDB 支持副本集、分片集群之间的异构迁移，即源端、目标端架构为副本集 - 副本集、副本集 - 分片集群、分片集群 - 副本集、分片集群 - 分片集群的4种场景。

## 注意事项
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您的数据库配置过低，建议您在业务低峰期进行迁移。
- 外网实例迁移时，请确保源实例服务在外网环境下可访问。

## 前提条件
- 已 [创建云数据库 MongoDB](https://cloud.tencent.com/document/product/240/3551)。
- 源数据库和目标数据库符合迁移功能和版本要求，请参见 [数据迁移支持的数据库](https://cloud.tencent.com/document/product/571/58686) 进行核对。
- 已完成 [准备工作](https://cloud.tencent.com/document/product/571/59968)。
- 需要在源实例创建一个只读账号供迁移使用，否则迁移前校验步骤将不通过。
```
use admin
db.createUser({
    user: "username",
    pwd: "password",
    roles:
        [
            {role: "readAnyDatabase", db: "admin"},
            {role: "read", db: "local"}
        ]
})
```

## 约束限制
- 为保障迁移效率，CVM 自建实例迁移不支持跨地域迁移。
- 由于单节点无 Oplog，所以自建实例是单节点时，不支持增量迁移。

## 操作限制
- 迁移过程中请勿进行如下操作，否则会导致迁移任务失败。 
  - 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
  - 请勿在源库上执行清除 oplog 的操作。
  - 在数据迁移阶段，请勿删除目的端数据库 TencetDTSData。
  - 在数据迁移阶段，请谨慎操作目的端数据，避免最终数据不一致。
  - 分片迁移请勿在源端执行除事务外的 DDL 操作，DTS 会过滤分片集群的 DDL 操作，避免导致最终数据不一致。
- 如果仅执行全量数据迁移，请勿在迁移过程中向源实例中写入新的数据，否则会导致源和目标数据不一致。针对有数据写入的场景，为实时保持数据一致性，建议选择全量+增量数据迁移。

## 支持的 SQL 操作
> ?仅副本集迁移支持 DDL 操作，分片迁移会过滤 DDL 操作（事务除外）。

| **操作类型** | **支持的 SQL 操作**                                            |
| ------------ | ------------------------------------------------------------ |
| DML          | INSERT、UPDATE、DELETE                                       |
| DDL          | INDEX：createIndexes、createIndex、dropIndex、dropIndexes<br>COLLECTION：createCollection、drop、collMod、renameCollection、convertToCapped<br>DATABASE：dropDatabase、copyDatabase |

## 环境要求

| **类型**       | **环境要求**                                                 |
| -------------- | ------------------------------------------------------------ |
| 源数据库要求   | <li>源库所在的服务器需具备足够的出口带宽，否则将影响迁移速率。<li>源库提供的用户需要有读取数据库的权限。<li>源库不能有和 TencetDTSData 同名的库。<li>源库若是集群模式，需在增量同步之前关闭 balancer。<li>进行全量 + 增量迁移时，需要能够从源端获取到 Oplog。 |
| 目标数据库要求 | <li>目标库的空间大小须是源库待迁移库表空间的1.3倍以上。<li>目标库提供的用户需要 root 权限。<li>目标库不能有和 TencetDTSData 同名的库。 <li>目标库不能有和源库同名的库表。<br><li>源库为分片时，需要正确填写对应 mongos、config server、mongod 节点信息。<li>目标库不能有负载业务进行，否则会报警告。<li>源库和目的库的片建信息需要一致，否则会报警告。</li> |

## 迁移步骤
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts )，在左侧导航选择**数据迁移**页，单击**新建迁移任务**，进入新建迁移任务页面。
2. 在新建迁移任务页面，选择迁移的目标实例所属地域，单击**0元购买**，目前 DTS 数据迁移功能免费使用。 
3. 在设置源和目标数据库页面，完成任务设置、源库设置和目标库设置。  
>?请在源实例创建一个只读帐号供迁移使用，否则迁移前校验步骤将不通过。
>
<img src="https://main.qcloudimg.com/raw/68b3b04023f54eb288de6464422c52cc.png"  style="zoom:80%;">
<table>
<thead><tr><th width="10%">设置类型</th><th width="15%">配置项</th><th width="75%">说明</th></tr></thead>
<tbody>
<tr>
<td rowspan=3>任务设置</td>
<td>任务名称</td>
<td>设置一个具有业务意义的名称，便于任务识别。</td></tr>
<tr>
<td>运行模式</td>
<td><ul><li>立即执行：完成任务校验通过后立即启动任务。</li><li>定时执行：需要配置一个任务执行时间，到时间后启动任务。</li></ul></td></tr>
<tr>
<td>标签</td>
<td>标签用于从不同维度对资源分类管理。如现有标签不符合您的要求，请前往控制台管理标签。</td></tr>
<tr>
<td rowspan=6>源库设置</td>
<td>源库类型</td><td>根据您的源数据库类型选择，本场景选择“MongoDB”。</td></tr>
<tr>
<td>接入类型</td><td>请根据您的场景选择，本场景选择“云数据库”。
<ul><li>公网：源数据库可以通过公网 IP 访问。</li>
<li>云主机自建：源数据库部署在 <a href="https://cloud.tencent.com/document/product/213">腾讯云服务器 CVM</a> 上。</li>
<li>专线接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/216">专线接入</a> 方式与腾讯云私有网络打通。</li>
<li>VPN接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/554">VPN 连接</a> 方式与腾讯云私有网络打通。</li>
<li>云数据库：源数据库属于腾讯云数据库实例。</li>
<li>云联网：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877">云联网</a> 与腾讯云私有网络打通。</li></ul>对于第三方云厂商数据库，一般可以选择公网方式，也可以选择 VPN 接入，专线或者云联网的方式，需要根据实际的网络情况选择。不同接入类型的准备工作请参考 <a href="https://cloud.tencent.com/document/product/571/59968">准备工作概述</a>。</td></tr>
<tr>
<td>所属地域</td><td>源库 MongoDB 所属地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标库的实例 ID。</td></tr>
<tr>
<td>帐号</td><td>源库 MongoDB 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库 MongoDB 的数据库帐号的密码。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>选择“MongoDB”。</td></tr>
<tr>
<td>接入类型</td><td>本场景选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>源库中已选择的地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标库的实例 ID。</td></tr>
<tr>
<td>帐号</td><td>目标库的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>目标库的数据库帐号的密码。</td></tr>
</tbody></table>
4. 测试源实例和目标实例的连通性。
![](https://main.qcloudimg.com/raw/43d1d1717e76331a9d2048428515cf75.png)
5. 在设置迁移选项及选择迁移对象页面，设置迁移选项和迁移对象（可选择部分库表）。
<img src="https://main.qcloudimg.com/raw/0392c50e0aa030d890c20f119e714579.png"  style="zoom:80%;">
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>迁移类型</td>
<td>请根据您的场景选择。<ul><li>结构迁移：迁移数据库中的库、表等结构化的数据。</li><li>全量迁移：迁移整个数据库。</li><li>全量 + 增量迁移：迁移整个数据库和后续增量数据，如果迁移过程中有数据写入，需要不停机平滑迁移，请选择此场景。</li></ul></td></tr>
<tr>
<td>迁移对象</td>
<td><ul><li>整个实例：迁移整个实例，但不包括系统库，如 postgres 中的系统对象，但是会迁移 role 与用户元数据定义。</li>
<li>指定对象：迁移指定对象。</li></ul> </td></tr>
<tr>
<td>指定对象</td>
<td>在源库对象中选择待迁移的对象，然后将其移到已选对象框中。</td></tr>
</tbody></table>
6. 在校验任务页面，完成迁移前校验工作，单击**启动任务**。
如果校验任务不通过，可以参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/58685) 修复问题后重新发起校验任务。
 - 失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。
 - 警告：表示检验项检查不完全符合要求，可以继续任务，但对业务有一定的影响，用户需要根据提示自行评估是忽略警告项还是修复问题再继续。
![](https://main.qcloudimg.com/raw/1182ccb4cfaa066e95e499c44f4363fe.png)
7. 返回迁移任务列表，待增量同步完成100%，在**操作**列单击**完成**，即可完成迁移任务。
 - 选择**结构迁移**或者**全量迁移**：任务完成后会自动结束，不需要手动结束。
 - 选择**全量 + 增量迁移**：全量迁移完成后会自动进入增量数据同步阶段，增量数据同步不会自动结束，需要您手动单击**完成**结束增量数据同步。
   - 请选择合适时间手动完成增量数据同步，并完成业务切换。
    - 观察迁移阶段为增量同步，并显示无延迟状态，将源库停写几分钟。
    - 目标与源库数据差距为0MB及目标与源库时间延迟为0秒时，手动完成增量同步。
![](https://main.qcloudimg.com/raw/2a14237df7258733a5c14ff68fc19cf3.png)
8. （可选）如果您需要进行查看任务、删除任务等操作，请单击对应的任务，在**操作**列进行操作，详情可参考 [任务管理](https://cloud.tencent.com/document/product/571/58674)。
9. 当迁移任务状态变为**任务成功**时，即可对业务进行正式割接，更多详情可参考 [割接说明](https://cloud.tencent.com/document/product/571/58660)。

