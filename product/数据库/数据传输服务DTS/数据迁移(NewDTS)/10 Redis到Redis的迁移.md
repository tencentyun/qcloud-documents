本文介绍使用 DTS 数据迁移功能从自建/云数据库/第三方云厂商数据库部署形态的 Redis 迁移数据至腾讯云数据库 Redis 的操作指导。 

## 注意事项 
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您的数据库配置过低，建议您在业务低峰期进行迁移。

  

## 前提条件
- 已 [创建云数据库 Redis](https://cloud.tencent.com/document/product/239/30871)。
- 源数据库和目标数据库符合迁移功能和版本要求，请参见 [数据迁移支持的数据库](https://cloud.tencent.com/document/product/571/58686) 进行核对。
- 已完成 [准备工作](https://cloud.tencent.com/document/product/571/59968)。
- 
- 源数据库需要具备的权限如下：
  - “整个实例”迁移：
```

```
  - “指定对象”迁移：
```

```
- 需要具备目标数据库的权限：
- 源库为自建数据库，或者第三方云厂商数据库时，需要提供 SYNC 或者 PSYNC 命令权限。


## 应用限制
- 为保障迁移效率，源库为 CVM 自建的数据库不支持跨地域迁移。
- 只允许迁移正常运行状态下的数据库实例，未初始化密码或者有其他任务在执行中的数据库实例，不能进行数据迁移。
- 目标数据库必须内容为空，且迁移过程中目标库会被设置为只读，不能对其进行写入操作。
- 相互关联的数据对象需要同时迁移，否则会导致迁移失败。常见的关联关系：视图引用表、视图引用视图、存储过程/函数/触发器引用视图/表、主外键关联表等。

## 操作限制
- 迁移过程中请勿进行如下操作，否则会导致迁移任务失败。
  - 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
  - 在库表结构迁移和全量迁移阶段，请勿执行库或表结构变更的 DDL 操作。 
- 如果仅执行全量数据迁移，请勿在迁移过程中向源实例中写入新的数据，否则会导致源和目标数据不一致。针对有数据写入的场景，为实时保持数据一致性，建议选择全量+增量数据迁移。

## 支持的 SQL 操作
| 操作类型 | 支持的 SQL 操作                                              |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE、REPLACE                              |
| DDL      | TABLE：CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE <br>VIEW：CREATE VIEW、DROP VIEW<br>INDEX：CREATE INDEX、DROP INDEX <br>DATABASE：CREATE DATABASE、ALTER DATABASE、DROP DATABASE |

## 环境要求
>?如下环境要求，系统会在启动迁移任务前自动进行校验，不符合要求的系统会报错。如果用户能够识别出来，可以参考 [校验项检查要求](https://cloud.tencent.com/document/product/571/58685) 自行修改，如果不能则等系统校验完成，按照报错提示修改。

<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td>
<li>源库和目标库网络能够连通。</li>
<li>源库所在的服务器需具备足够的出口带宽，否则将影响迁移速率。</li>
<li>待补充</li>
</td></tr>
<tr> 
<td>目标数据库要求</td>
<td>
<li>目标库的版本必须大于等于源库的版本。</li>
<li>目标库的空间大小须是源库待迁移库表空间的1.2倍以上。</li>
<li>待补充</li></td></tr>
<tr> 
<td>其他要求</td>
<td>环境变量 innodb_stats_on_metadataw 必须设置为 OFF。</td></tr>
</table>

## 操作步骤【待环境ok待适配】
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/migration)，在左侧导航选择**数据迁移**页，单击**新建迁移任务**，进入新建迁移任务页面。
2. 在新建迁移任务页面，选择迁移的目标实例所属地域，单击**0元购买**，目前 DTS 数据迁移功能免费使用。
![](https://main.qcloudimg.com/raw/7cde8ece6d819a89800e2fccfafc4010.png)
3. 在设置源和目标数据库页面，完成任务设置、源库设置和目标库设置，测试源库和目标库连通性通过后，单击**新建**。
>?如果连通性测试失败，请根据提示和 [修复指导](https://cloud.tencent.com/document/product/571/58685) 进行排查和解决，然后再次重试。

![](https://qcloudimg.tencent-cloud.cn/raw/ec7829ac6cd56989488982765bbb4734.png)
![](https://qcloudimg.tencent-cloud.cn/raw/665f1c340b41bf328684f9b4a27f36c6.png)
**因源数据库部署形态和接入类型的交叉场景较多，各场景迁移步骤类似，如下仅提供典型场景的配置示例，其他场景请用户参考配置。**

- [**示例一**：本地自建数据库通过专线/VPN方式迁移至腾讯云数据库](#1)

- [<b>示例二</b>：腾讯云数据库迁移至腾讯云数据库](#2)

- [<b>示例三</b>：阿里云 RDS 通过公网方式迁移至腾讯云数据库](#3)

[**示例一**：本地自建数据库通过专线/VPN方式迁移至腾讯云数据库](id:1)

<table>
<thead><tr><th width="10%">设置类型</th><th width="20%">配置项</th><th width="70%">说明</th></tr></thead>
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
<td rowspan=10>源库设置</td>
<td>源库类型</td><td>根据您的源数据库类型选择，本场景选择“MySQL”。</td></tr>
<tr>
<td>服务提供商</td><td>自建数据库（包括云服务器上的自建）或者腾讯云数据库，请选择“普通”；第三方云厂商数据库，请选择对应的服务商。<br>本场景选择“普通”。</td></tr>
<tr>
<td>接入类型</td><td>请根据您的场景选择，本场景选择“专线接入”或“VPN接入”，该场景需要 <a href="https://cloud.tencent.com/document/product/571/60604">配置 VPN 和 IDC 之间的互通</a>，其他接入类型的准备工作请参考 <a href="https://cloud.tencent.com/document/product/571/59968">准备工作概述</a>。
<ul><li>公网：源数据库可以通过公网 IP 访问。</li>
<li>云主机自建：源数据库部署在 <a href="https://cloud.tencent.com/document/product/213">腾讯云服务器 CVM</a> 上。</li>
<li>专线接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/216">专线接入</a> 方式与腾讯云私有网络打通。</li>
<li>VPN接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/554">VPN 连接</a> 方式与腾讯云私有网络打通。</li>
<li>云数据库：源数据库属于腾讯云数据库实例。</li>
<li>云联网：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877">云联网</a> 与腾讯云私有网络打通。</li></ul></td></tr>
<tr>
<td>所属地域</td><td>选择离自建数据库最近的一个地域即可。</td></tr>
<tr>
<td>私有网络专线网关/VPN 网关</td><td>专线接入时只支持私有网络专线网关，请确认网关关联网络类型。<br>VPN 网关，请选择通过 VPN 网关接入的 VPN 网关实例。</td></tr>
<tr>
<td>私有网络</td><td>选择私有网络专线网关和 VPN 网关关联的私有网络和子网。</td></tr>
<tr>
<td>主机地址</td><td>源库 MySQL 访问 IP 地址或域名。</td></tr>
<tr>
<td>端口</td><td>源库 MySQL 访问端口。</td></tr>
<tr>
<td>帐号</td><td>源库 MySQL 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库 MySQL 的数据库帐号的密码。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>选择“MySQL”。</td></tr>
<tr>
<td>接入类型</td><td>根据您的场景选择，本场景选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>选择目标库所属地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标库的实例 ID。</td></tr>
<tr>
<td>帐号</td><td>目标库的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>目标库的数据库帐号的密码。</td></tr>
</tbody></table>
[<b>示例二</b>：腾讯云数据库迁移至腾讯云数据库](id:2)

<table>
<thead><tr><th width="10%">设置类型</th><th width="20%">配置项</th><th width="70%">说明</th></tr></thead>
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
<td rowspan=8>源库设置</td>
<td>源库类型</td><td>根据您的源数据库类型选择，本场景选择“MySQL”。</td></tr>
<tr>
<td>服务提供商</td><td>自建数据库（包括云服务器上的自建）或者腾讯云数据库，请选择“普通”；第三方云厂商数据库，请选择对应的服务商。<br>本场景选择“普通”。</td></tr>
<tr>
<td>接入类型</td><td>请根据您的场景选择，本场景选择“云数据库”，不同接入类型的准备工作请参考 <a href="https://cloud.tencent.com/document/product/571/59968">准备工作概述</a>。
<ul><li>公网：源数据库可以通过公网 IP 访问。</li>
<li>云主机自建：源数据库部署在 <a href="https://cloud.tencent.com/document/product/213">腾讯云服务器 CVM</a> 上。</li>
<li>专线接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/216">专线接入</a> 方式与腾讯云私有网络打通。</li>
<li>VPN接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/554">VPN 连接</a> 方式与腾讯云私有网络打通。</li>
<li>云数据库：源数据库属于腾讯云数据库实例。</li>
<li>云联网：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877">云联网</a> 与腾讯云私有网络打通。</li></ul></td></tr>
<tr>
<td>是否跨账号</td><td><ul><li>本账号：源数据库实例和目标数据库实例所属的主账号为同一个腾讯云主账号。</li><li>跨账号：源数据库实例和目标数据库实例所属的主账号为不同的腾讯云主账号。<br>如下以同账号之间的迁移为例，跨账号操作指导请参见 <a href="https://cloud.tencent.com/document/product/571/54117">云数据库跨账号实例间迁移</a>。</li></ul></td></tr>
<tr>
<td>所属地域</td><td>源库所属地域。</td></tr>
<tr>
<td>数据库实例</td><td>源库 MySQL 实例 ID。</td></tr>
<tr>
<td>帐号</td><td>源库 MySQL 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库 MySQL 的数据库帐号的密码。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>选择“MySQL”。</td></tr>
<tr>
<td>接入类型</td><td>根据您的场景选择，本场景选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>选择目标库所属地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标库的实例 ID。</td></tr>
<tr>
<td>帐号</td><td>目标库的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>目标库的数据库帐号的密码。</td></tr>
</tbody></table>

[<b>示例三</b>：阿里云 RDS 通过公网方式迁移至腾讯云数据库](id:3)

目前 DTS 仅支持迁移阿里云数据库 Redis，华为云分布式缓存服务 Redis、华为云数据库 GaussDB(for Redis)，其他第三方云厂商迁移至腾讯云请参见 [使用redis-port进行迁移](https://cloud.tencent.com/document/product/239/33786)。

<table>
<thead><tr><th width="10%">设置类型</th><th width="20%">配置项</th><th width="70%">说明</th></tr></thead>
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
<td rowspan=8>源库设置</td>
<td>源库类型</td><td>根据您的源数据库类型选择，本场景选择“MySQL”。</td></tr>
<tr>
<td>服务提供商</td><td>自建数据库（包括云服务器上的自建）或者腾讯云数据库，请选择“普通”；第三方云厂商数据库，请选择对应的服务商。<br>本场景选择“阿里云”。</td></tr>
<tr>
<td>接入类型</td><td>对于第三方云厂商数据库，一般可以选择公网方式，也可以选择 VPN 接入，专线或者云联网的方式，需要根据实际的网络情况选择。<br>本场景选择“公网”，不同接入类型的准备工作请参考 <a href="https://cloud.tencent.com/document/product/571/59968">准备工作概述</a>。
<ul><li>公网：源数据库可以通过公网 IP 访问。</li>
<li>云主机自建：源数据库部署在 <a href="https://cloud.tencent.com/document/product/213">腾讯云服务器 CVM</a> 上。</li>
<li>专线接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/216">专线接入</a> 方式与腾讯云私有网络打通。</li>
<li>VPN接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/554">VPN 连接</a> 方式与腾讯云私有网络打通。</li>
<li>云数据库：源数据库属于腾讯云数据库实例。</li>
<li>云联网：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877">云联网</a> 与腾讯云私有网络打通。</li></ul></td></tr>
<tr>
<td>所属地域</td><td>源库所属地域。</td></tr>
<tr>
<td>主机地址</td><td>源库 MySQL 访问 IP 地址或域名。</td></tr>
<tr>
<td>端口</td><td>源库 MySQL 访问端口。</td></tr>
<tr>
<td>帐号</td><td>源库 MySQL 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库 MySQL 的数据库帐号的密码。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>选择“MySQL”。</td></tr>
<tr>
<td>接入类型</td><td>根据您的场景选择，本场景选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>选择目标库所属地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标库的实例 ID。</td></tr>
<tr>
<td>帐号</td><td>目标库的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>目标库的数据库帐号的密码。</td></tr>
</tbody></table>
4. 在设置迁移选项及选择迁移对象页面，设置迁移类型、对象，单击**保存**。
>?
>- 如果用户在迁移过程中确定会使用 gh-ost、pt-osc 等工具对某张表做 Online DDL，则**迁移对象**需要选择这个表所在的整个库（或者整个实例），不能仅选择这个表，否则无法迁移 Online DDL 变更产生的临时表数据到目标数据库。
>- 如果用户在迁移过程中确定会对某张表使用 rename 操作（例如将 table A rename 为 table B），则**迁移对象**需要选择 table A 所在的整个库（或者整个实例），不能仅选择 table A，否则系统会报错。 
>
![](https://qcloudimg.tencent-cloud.cn/raw/59f84553fab9fd963d7db2a6ec272ef5.png)
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>迁移类型</td>
<td>请根据您的场景选择。<ul><li>结构迁移：迁移数据库中的库、表等结构化的数据。</li><li>全量迁移：迁移整个数据库，迁移数据仅针对任务发起时，源数据库已有的内容，不包括任务发起后源库实时新增的数据写入。</li><li>全量 + 增量迁移：迁移数据包括任务发起时源库的已有内容，也包括任务发起后源库实时新增的数据写入。如果迁移过程中源库有数据写入，需要不停机平滑迁移，请选择此场景。</li></ul></td></tr>
<tr>
<td>迁移对象</td>
<td><ul><li>整个实例：迁移整个实例，但不包括系统库，如information_schema、mysql、performance_schema、sys。</li>
<li>指定对象：迁移指定对象。</li></ul> </td></tr>
<tr>
<td>指定对象</td>
<td>在源库对象中选择待迁移的对象，然后将其移到已选对象框中。</td></tr>
<tr>
<td>是否迁移账号</td>
<td>如果需要迁移源库的账号信息，则勾选此功能。</td></tr>
</tbody></table>

5. 在校验任务页面，进行校验，校验任务通过后，单击**启动任务**。
 - 如果校验任务不通过，可以参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/58685) 修复问题后重新发起校验任务。
    - 失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。  
    - 警告：表示检验项检查不完全符合要求，可以继续任务，但对业务有一定的影响，用户需要根据提示自行评估是忽略警告项还是修复问题再继续。
 - 如果勾选了账号迁移，则校验任务会对源库的账号信息进行检查，对满足要求的账号进行迁移，不满足的不迁移或者降权迁移，检查详情请参见[迁移账号](https://cloud.tencent.com/document/product/571/65702)。
![](https://qcloudimg.tencent-cloud.cn/raw/32ae94770e6ce95b75295586d1d13e82.png)
6. 返回数据迁移任务列表，任务进入准备运行状态，运行1分钟 - 2分钟后，数据迁移任务开始正式启动。
   - 选择**结构迁移**或者**全量迁移**：任务完成后会自动结束，不需要手动结束。
   - 选择**全量 + 增量迁移**：全量迁移完成后会自动进入增量数据同步阶段，增量数据同步不会自动结束，需要您手动单击**完成**结束增量数据同步。
      - 请选择合适时间手动完成增量数据同步，并完成业务切换。
      - 观察迁移阶段为增量同步，并显示无延迟状态，将源库停写几分钟。
      - 目标与源库数据差距为0MB及目标与源库时间延迟为0秒时，手动完成增量同步。
   ![](https://main.qcloudimg.com/raw/e2b9ed2f2a63a0fdf28a557aa5f7aaf2.png)
7. （可选）如果您需要进行查看任务、删除任务等操作，请单击对应的任务，在**操作**列进行操作，详情可参考 [任务管理](https://cloud.tencent.com/document/product/571/58674)。
8. 当迁移任务状态变为**任务成功**时，即可对业务进行正式割接，更多详情可参考 [割接说明](https://cloud.tencent.com/document/product/571/58660)。
