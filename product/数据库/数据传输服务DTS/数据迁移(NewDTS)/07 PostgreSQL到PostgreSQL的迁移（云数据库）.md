本文介绍使用 DTS 数据迁移功能从 PostgreSQL 迁移数据至腾讯云数据库 PostgreSQL 的操作指导。

## 注意事项 
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您的数据库配置过低，建议您在业务低峰期进行迁移。
- 外网实例迁移时，请确保源实例服务在外网环境下可访问，并且要保持外网连接的稳定性，当网络出现波动或者故障时会导致迁移失败，迁移一旦失败，就需要重新发起迁移任务。
- 除腾讯云数据库 PostgreSQL 之外的其他 PostgreSQL 作为源端时，必须要求源端库具有 replication 权限，否则迁移前校验步骤将不通过。

## 前提条件
- 已 [创建云数据库 PostgreSQL](https://cloud.tencent.com/document/product/409/56961)。
- 源数据库和目标数据库符合迁移功能和版本要求，请参见 [数据迁移支持的数据库](https://cloud.tencent.com/document/product/571/58686) 进行核对。
- 已完成 [准备工作](https://cloud.tencent.com/document/product/571/59968)。
- 源数据库需要具备的权限如下：
  - 源库为腾讯云数据库 PostgreSQL 之外的其他 PostgreSQL 时，要求源端库必须具有 replication 权限。  
  - 源库腾讯云数据库 PostgreSQL，要求源数据库必须为创建云数据库实例时的初始化用户。  
  - 如果部分表或者对象无权限，可使用高权限用户执行如下示例语句，对无权限的对象分别授予权限：  
```
grant select on table 表名 to 用户名;
grant select on SEQUENCE 序列名 to 用户名;
grant connect on database 库名 to 用户名;
grant select on large object 大对象oid to 用户名;
GRANT USAGE ON SCHEMA 模式名 to 用户名;
```
- 目标数据库必须为创建云数据库实例时的初始化用户。 
   - 如果目标实例中包含待迁移的 database，且 database 的 owner 非当前迁移用户，可执行以下语句将 database 授予迁移用户：
```
alter database 库名 owner to 迁移用户;
```
   - 如果目标迁移账户为非 `pg_tencentdb_superuser` 角色用户，在校验时，会提示“目标实例权限检查失败，无法获取Schema列表”，请使用如下语句为迁移用户赋予初始化用户权限：
```
grant pg_tencentdb_superuser to 迁移用户;
```

## 应用限制
- 相互关联的数据对象需要同时迁移，否则会导致迁移失败。常见的关联关系：视图引用表、视图引用视图、存储过程/函数/触发器引用视图/表、主外键关联表等。
- 为保障迁移效率，CVM 自建实例迁移不支持跨地域迁移。如需要跨地域迁移，请选择公网接入方式。
- 如果进行整个实例迁移，目标库中不能存在与源库同名的用户和角色。

## 操作限制
- 迁移过程中请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
- 在结构迁移、全量迁移和增量迁移阶段，请勿执行 DDL 操作，大对象操作，否则会导致迁移数据不一致。
- 如果仅执行全量数据迁移，仅会迁移在发起迁移这一刻之前的数据，如果在迁移过程中向源实例中写入新的数据，源库和目标库的数据会出现不一致。针对有数据写入的场景，为实时保持数据一致性，建议选择全量 + 增量数据迁移。

## 环境要求
>?如下环境要求，系统会在启动迁移任务前自动进行校验，不符合要求的系统会报错。如果用户能够识别出来，可以 参考 [校验项检查要求](https://cloud.tencent.com/document/product/571/58685) 自行修改，如果不能则等系统校验完成，按照报错提示修改。

<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td><ul>
<li>源库和目标库网络能够连通。</li>
<li>源库所在的服务器需具备足够的出口带宽，否则将影响迁移速率。</li>
<li>实例参数要求：
<ul>
<li>增量迁移时源库 wal_level 参数值必须为 logical。</li>
<li>增量迁移时源库 max_replication_slots 值必须大于待迁移的 database 数量。</li>
<li>增量迁移时源库 max_wal_senders 值必须大于待迁移的 database 数量。</li></ul>
</ul></td>
<tr> 
<td>目标数据库要求</td>
<td>
<li>仅全量迁移时，目标数据库实例版本必须大于源库实例版本；增量迁移时，支持10.x以上的版本互相迁移。</li>
<li>目标库的可用空间大小须是源库待迁移实例的1.2倍以上。（数据增量迁移会执行 update，delete 操作，导致数据库的表产生碎片，因此迁移完成后目标数据库的表存储空间很可能会比源实例的表存储空间大，这主要是因为源端和目标端不同的 autovcauum 触发条件导致。）</li>
<li>目标库不能有和源库同名的迁移对象。如用户名不能相同，不能存在相同名的表。</li>
<li>增量迁移时目标库 max_worker_processes 值必须大于 max_logical_replication_workers。</li>
</tr>
</table>

## 操作步骤
1. （可选）PostgreSQL 9.4、9.5、9.6 版本作为源数据库进行“全量 + 增量迁移”时，需要参考如下指导安装 tencent_decoding 插件，其他场景请跳过该步骤。
 1. 根据源数据库所在服务器的系统架构，下载对应的插件。  
    - 只支持系统架构为 x86_64 和 aarch64。
    - 插件版本需要和 PostgreSQL 版本保持一致。
    - Glibc 版本需要满足要求：x86_64 系统不低于 2.17 - 323 版本，aarch64 系统不低于 2.17 - 260 版本。 
       - 在 Linux 系统上查看 Glibc 版本：
```
RHEL/CentOS: rpm -q glibc
```
       - 在其他操作系统（Debian/Ubuntu/SUSE 等）上查看 Glibc 版本：
```
ldd --version | grep -i libc
```
下载地址：  [x86_64 9.4](https://postgresql-1258344699.cos.ap-shanghai.myqcloud.com/tencent_decoding/9.4/tencent_decoding.so)、[x86_64 9.5](https://postgresql-1258344699.cos.ap-shanghai.myqcloud.com/tencent_decoding/9.5/tencent_decoding.so)、[x86_64 9.6](https://postgresql-1258344699.cos.ap-shanghai.myqcloud.com/tencent_decoding/9.6/tencent_decoding.so)、[aarch64 9.4](https://postgresql-1258344699.cos.ap-shanghai.myqcloud.com/tencent_decoding_aarch64/9.4/tencent_decoding.so)、[aarch64 9.5](https://postgresql-1258344699.cos.ap-shanghai.myqcloud.com/tencent_decoding_aarch64/9.5/tencent_decoding.so)、[aarch64 9.6](https://postgresql-1258344699.cos.ap-shanghai.myqcloud.com/tencent_decoding_aarch64/9.6/tencent_decoding.so)。    
 2. 将下载得到的 tencent_decoding.so 文件放置于 Postgres 进程目录的 lib 文件夹下，无需重启实例。 
2. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/migration)，在左侧导航选择**数据迁移**页，单击**新建迁移任务**，进入新建迁移任务页面。
3. 在新建迁移任务页面，选择迁移的目标实例所属地域，单击**0元购买**，目前 DTS 数据迁移功能免费使用。
>?迁移任务订购后不支持更换地域，请谨慎选择。
3. 在设置源和目标数据库页面，完成任务设置、源库设置和目标库设置，测试源库和目标库连通性通过后，单击**新建**。
>?如果连通性测试失败，请根据提示和 [修复指导](https://cloud.tencent.com/document/product/571/58685) 进行排查和解决，然后再次重试。
>
<img src="https://main.qcloudimg.com/raw/414b9b3caf06c106ce894dea9a0ddf2a.png"  style="zoom:50%;">
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
<td>源库类型</td><td>根据您的源数据库类型选择，本场景选择“PostgreSQL”。</td></tr>
<tr>
<td>接入类型</td><td>请根据您的场景选择，本场景选择“云数据库”。<br>为保障迁移效率，CVM 自建实例迁移不支持跨地域迁移。如需要跨地域迁移，请选择公网接入方式。
<ul><li>公网：源数据库可以通过公网 IP 访问。</li>
<li>云主机自建：源数据库部署在 <a href="https://cloud.tencent.com/document/product/213">腾讯云服务器 CVM</a> 上。</li>
<li>专线接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/216">专线接入</a> 方式与腾讯云私有网络打通。</li>
<li>VPN接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/554">VPN 连接</a> 方式与腾讯云私有网络打通。</li>
<li>云数据库：源数据库属于腾讯云数据库实例。</li>
<li>云联网：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877">云联网</a> 与腾讯云私有网络打通。</li></ul>不同接入类型的准备工作请参考 <a href="https://cloud.tencent.com/document/product/571/59968">准备工作概述</a>。</td></tr>
<tr>
<td>所属地域</td><td>源库 PostgreSQL 所属地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标库的实例 ID。</td></tr>
<tr>
<td>帐号</td><td>源库 PostgreSQL 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库 PostgreSQL 的数据库帐号的密码。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>选择“PostgreSQL”。</td></tr>
<tr>
<td>接入类型</td><td>根据您的场景选择，本场景默认选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>源库中已选择的地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标库的实例 ID。</td></tr>
<tr>
<td>帐号</td><td>目标库的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>目标库的数据库帐号的密码。</td></tr>
</tbody></table>
4. 在设置迁移选项及选择迁移对象页面，设置迁移类型、对象，单击**保存**。
<img src="https://main.qcloudimg.com/raw/aadd11ed6a095813fa767690e6857276.png"  style="zoom:60%;">
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>迁移类型</td>
<td>请根据您的场景选择。<ul><li>结构迁移：迁移数据库中的库、表等结构化的数据。</li><li>全量迁移：迁移整个数据库。</li><li>全量 + 增量迁移：迁移整个数据库和后续增量数据，如果迁移过程中有数据写入，需要不停机平滑迁移，请选择此场景。</li></ul></td></tr>
<tr>
<td>迁移对象</td>
<td><ul><li>整个实例：迁移整个实例，但不包括系统库，如postgres中的系统对象，但是会迁移role与用户元数据定义。</li>
<li>指定对象：迁移指定对象。</li></ul> </td></tr>
<tr>
<td>指定对象</td>
<td>在源库对象中选择待迁移的对象，然后将其移到已选对象框中。</td></tr>
</tbody></table>
5. 在校验任务页面，进行校验，校验任务通过后，单击**启动任务**。
    如果校验任务不通过，可以参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/58685) 修复问题后重新发起校验任务。
  - 失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。
  - 警告：表示检验项检查不完全符合要求，可以继续任务，但对业务有一定的影响，用户需要根据提示自行评估是忽略警告项还是修复问题再继续。
 ![](https://main.qcloudimg.com/raw/5ed72bfbcaefe3234e5c08114a2761f3.png)
6. 返回数据迁移任务列表，任务进入准备运行状态，运行1分钟 - 2分钟后，数据迁移任务开始正式启动。
   - 选择**结构迁移**或者**全量迁移**：任务完成后会自动结束，不需要手动结束。
   - 选择**全量 + 增量迁移**：全量迁移完成后会自动进入增量数据同步阶段，增量数据同步不会自动结束，需要您手动单击**完成**结束增量数据同步。单击完成后任务进入**完成中**的状态。请不要对源端和目标端进行任何修改，此时后端将自动的将部分对象与源端进行对齐。
      - 请选择合适时间手动完成增量数据同步，并完成业务切换。
      - 观察迁移阶段为增量同步，并显示无延迟状态，将源库停写几分钟。
      - 目标与源库数据差距为0MB及目标与源库时间延迟为0秒时，手动完成增量同步。
   ![](https://main.qcloudimg.com/raw/d3cbe3342e2fe2f7627b66dae31703e9.png)
7. （可选）如果您需要进行查看任务、删除任务等操作，请单击对应的任务，在**操作**列进行操作，详情可参考 [任务管理](https://cloud.tencent.com/document/product/571/58674)。
8. 当迁移任务状态变为**任务成功**时，即可对业务进行正式割接，更多详情可参考 [割接说明](https://cloud.tencent.com/document/product/571/58660)。
