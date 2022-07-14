当需要将已有 OLTP 数据库实例数据同步至 TDSQL-H LibraDB 数据库实例时，可通过添加 CDC 任务建立 OLTP 到 LibraSQL 分析引擎的数据同步链路，已有 OLTP 即可拥有 HTAP 能力。

## 背景信息
- 一个 TDSQL-H LibraDB 实例支持创建一个或多个数据同步链路（即 CDC 任务）。
- TDSQL-H LibraDB 支持的源端 OLTP 数据库包括自建数据库、云数据库和第三方云厂商数据库，数据库类型当前仅支持 MySQL。
支持的源数据库网络接入类型说明如下：
<table class="table-striped">
<thead><tr><th>接入类型</th><th>说明</th></tr></thead>
<tbody>
<tr>
<td>公网</td>
<td>源数据库可通过公网 IP 访问。</td></tr>
<tr>
<td>云主机自建</td>
<td>源数据库部署在 <a href="https://cloud.tencent.com/document/product/213" target="_blank">腾讯云服务器 CVM</a> 上。</td></tr>
<tr>
<td>专线接入</td>
<td>源数据库可通过 <a href="https://cloud.tencent.com/document/product/216" target="_blank">专线接入</a> 方式与腾讯云私有网络打通。</td></tr>
<tr>
<td>VPN 接入</td>
<td>源数据库可通过 <a href="https://cloud.tencent.com/document/product/554" target="_blank">VPN 连接</a> 方式与腾讯云私有网络打通。</td></tr>
<tr>
<td>云数据库</td>
<td>源数据库属于腾讯云数据库实例。</td></tr>
<td>云联网</td>
<td>源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877" target="_blank">云联网</a> 与腾讯云私有网络打通。</td></tr>
</tbody></table>
  对于第三方云厂商数据库，一般可以选择公网方式，也可以选择 VPN 接入，专线或者云联网的方式，需要根据实际的网络情况选择。 
- 数据同步支持整个实例同步和指定对象同步。
支持的数据同步类型及使用场景说明如下：
<table>
<thead><tr><th>初始结构</th><th>初始全量数据</th><th>增量数据</th><th>功能</th><th>场景</th></tr></thead>
<tbody>
<tr>
<td>&#10003;</td><td>-</td><td>-</td><td>只将源数据库表结构同步到 LibraSQL 分析引擎。</td><td>做结构验证。</td></tr>
<tr>
<td>&#10003;</td><td>&#10003;</td><td>-</td><td>将源数据库表结构和全量数据同步到 LibraSQL 分析引擎。</td><td>开发测试环境做测试验证。</td></tr>
<tr>
<td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>将源数据库表结构、全量数据同步到 LibraSQL 分析引擎后继续保持数据同步。将源数据库在同步过程中的数据，实时同步到目标。</td><td>同步的信息最多，适用于所有场景。</td></tr>
<tr>
<td>&#10003;</td><td>-</td><td>&#10003;</td><td>只做结构同步和增量数据同步。</td><td>日志场景，流式分析等只关注增量数据的场景。</td></tr>
<tr>
<td>-</td><td>-</td><td>&#10003;</td><td>只将增量数据同步到目标端。</td><td>用户需要定制化的目标表结构，且只需要流式的增量数据。</td></tr>
</tbody></table>      

## 使用限制
- 源表必须包含主键或者不可为 NULL 的唯一键。
- 源实例不可只读。
- 若选择增量同步。
  - 要求 MySQL 开启 GTID。
  - 要求开启 Binlog，且要求为 ROW 和 FULL 格式。
  - 支持高频 DDL 同步。
- 同步过程中请勿进行如下操作，否则会导致同步任务失败。
  - 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
  - 请勿在源库上执行分布式事务。
  - 请勿在源库写入 Binlog 格式为 `STATEMENT` 的数据。
  - 增量导入追上前请勿在源库上执行清除 Binlog 的操作。
  - 在同步增量阶段，请勿删除系统库表 `__tencentdb__`。

## DDL 支持
<table>
<thead><tr><th>对象</th><th>DDL</th><th>备注</th></tr></thead>
<tbody>
<tr><td>Database</td><td>create、drop</td><td>drop 操作转义为重命名操作：将库名修改为 “deleted_unix时间戳_原库名”</td></tr>
<tr>
<td rowspan="3">Table</td><td rowspan="3">create、rename、drop、truncate、alter</td><td>drop 操作转义为重命名操作：将表名修改为 “deleted_unix时间戳_原表名” </td></tr>
<tr>
<td>truncate 操作转义为：将表名修改为 “deleted_unix时间戳_原表名”并新建本地表</td></tr><tr><td>rename 操作不支持移动表：`RENAME TABLE current_db.tbl_name TO other_db.tbl_name;`</td></tr>
<tr>
<td>Column</td><td>add、drop、rename、change、modify、alter</td><td>-</td></tr>
</tbody></table>

<dx-alert infotype="explain" title="说明">
- 当分析引擎是 LibraSQL 10.3.203 及更早期版本时，由于 Database Engine 不支持 [atomic engine](https://clickhouse.com/docs/en/engines/database-engines/atomic/)，下述 DDL 不支持：rename、drop、truncate、alter rename table、drop database。
- 对于删除类操作，为保障数据安全，我们会转义为改名操作。
- 库表 DDL 同步说明：
  - “同步对象”选择“整个实例”，在 CDC 任务启动后：OLTP 新增的对象及其修改均能同步到分析引擎。
  - “同步对象”选择“指定对象”，且指定对象为整库时，在 CDC 任务启动后：OLTP 指定库中新增的表及其修改会同步到分析引擎，但不会同步其他库的变化。
</dx-alert>

## 环境要求
<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td>
<li>源库和目标库网络能够连通。</li>
<ul>
<li>实例参数要求：
<ul>
<li>源库 server_id 参数需要手动设置，且值不能设置为0。</li>
<li>源库表的 row_format 不能设置为 FIXDE。</li>
<li>源库和目标库 lower_case_table_names 变量必须设置一致。</li>
<li>源库变量 connect_timeout 设置数值必须大于10。</li></ul>
<li>Binlog 参数要求：
<ul>
<li>源端 log_bin 变量必须设置为 ON。</li>
<li>源端 binlog_format 变量必须设置为 ROW。</li>
<li>源端 binlog_row_image 变量必须设置为 FULL。</li>
<li>MySQL 5.6 及以上版本 gtid_mode 变量不为 ON 时会报警告，建议打开 gtid_mode。</li>
<li>不允许设置 do_db, ignore_db。</li>
<li>源实例为从库时，log_slave_updates 变量必须设置为 ON。</li></ul></li>
<li>外键依赖：
<ul>
<li>外键依赖只能设置为 NO ACTION，RESTRICT 两种类型。</li>
<li>部分库表同步时，有外键依赖的表必须齐全。</li></ul></li></td></tr>
</table>

## 注意事项
- CDC 在执行全量数据同步时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。
- 数据同步时，CDC 会使用执行同步任务的账号在源库中写入系统库 `__tencentdb__`，用于记录同步任务过程中的数据对比信息。
  - 为保证后续数据对比问题可定位，同步任务结束后不会删除源库中的 `__tencentdb__`。
  - `__tencentdb__` 系统库占用空间非常小，约为源库存储空间的千分之一到万分之一（例如源库为50GB，则 `__tencentdb__` 系统库约为5KB - 50KB） ，并且采用单线程，等待连接机制，所以对源库的性能几乎无影响，也不会抢占资源。
- 为了让服务对您的源端实例影响降到最小。CDC 限制了源实例帐号的权限。建议您在源数据库为 CDC 任务单独增加帐号，并赋予以下权限。
  - **整个实例**同步，需要的源端帐号权限如下：
```sql
CREATE USER 'CDC帐号'@'%' IDENTIFIED BY 'CDC密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO 'CDC帐号'@'%';  
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO 'CDC帐号'@'%';  
GRANT SELECT ON *.* TO 'CDC帐号';
```
  - **指定对象**同步，需要的源端帐号权限如下：
```sql
CREATE USER 'CDC帐号'@'%' IDENTIFIED BY 'CDC密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO 'CDC帐号'@'%';  
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO 'CDC帐号'@'%';  
GRANT SELECT ON `mysql`.* TO 'CDC帐号'@'%';
GRANT SELECT ON 待同步的库.* TO 'CDC帐号';
```
如需了解更多 MySQL 相关权限，请参见 [Privileges Provided by MySQL](https://dev.mysql.com/doc/mysql-security-excerpt/8.0/en/privileges-provided.html)。

## 前提条件
- 已创建源端 OLTP 数据库实例。
- 已 [创建 TDSQL-H LibraDB 实例](https://cloud.tencent.com/document/product/1488/63927)。

## 操作步骤
1. 登录 [TDSQL-H LibraDB 控制台](https://console.cloud.tencent.com/libradb/instance)。
2. 在实例列表，单击实例 ID 或在**操作**列单击**详情**。
3. 通过以下两种方式进入**新建CDC**页面。
   - 方式一：在实例管理页面，单击**CDC**页签。
   - 方式二：在架构图区域，单击**添加OLTP**。
4. 设置数据源：根据以下参数说明设置数据源。
![](https://qcloudimg.tencent-cloud.cn/raw/cc17befc59f95b50a739e3813d5a7dc1.png)
设置数据源时选择的服务提供商、接入类型不同，配置的参数项不同，请根据实际配置。
<table class="table-striped">
<thead><tr><th>区域</th><th>参数</th><th>说明</th></tr></thead>
<tbody>
<tr>
<td rowspan="2"><b>任务设置</b></td>
<td><b>任务名称</b></td>
<td>自定义 CDC 任务名称。</td></tr>
<tr>
<td><b>标签</b></td>
<td>标签用于从不同维度对资源分类管理。如果需要添加标签，请单击<b>添加</b>。</td></tr>
<tr>
<td rowspan="11"><b>源库设置</b></td>
<td><b>源库类型</b></td>
<td>源数据库类型。目前 TDSQL-H LibraDB 仅支持同步数据库类型为 MySQL 的 OLTP 数据库。</td>
<tr>
<td><b>服务提供商</b></td>
<td>源数据库所属服务提供商。包括普通、AWS、阿里云。其中，普通表示非 AWS、非阿里云的源数据库。</td>
<tr>
<td><b>数据库版本</b></td>
<td>源数据库版本，仅服务提供商选择 AWS 或阿里云时需要选择。</td>
<tr>
<td><b>接入类型</b></td>
<td>包括公网、云主机自建、专线接入、VPN接入、云数据库、云联网。具体接入类型说明请参见本文中的背景信息。</td></tr>
<tr>
<td><b>是否跨账号</b></td>
<td>源数据库账是否与当前登录账号一致，如果一致请选择本账号，否则请选择跨账号。</td></tr>
<tr>
<td><b>所属地域</b></td>
<td>源数据库实例所属地域。</td></tr>
<tr>
<td><b>主机地址</b></td>
<td>源数据库实例访问 IP 地址或域名。</td></tr>
<tr>
<td><b>端口</b></td>
<td>源数据库实例对应的端口号。</td></tr>
<tr>
<td><b>帐号</b></td>
<td>源数据库实例的帐号。根据整个实例或指定对象同步，该帐号需要具备权限不同，具体请参见本文中的注意事项。</td></tr>
<tr>
<td><b>密码</b></td>
<td>源数据库实例帐号对应的密码。</td></tr>
<tr>
<td><b>私有网络云联网</b></td>
<td>云联网接入时只支持私有网络云联网，请选择 VPC 类型的云联网。</td></tr>
</tbody></table>
5. 设置完成后，在页面下方单击**测试连通性**，测试通过后在页面下方单击**下一步**。
如果测试连通性失败，请根据提示修改源库设置信息后，继续单击**测试连通性**，直至测试通过后在页面下方单击**下一步**。
6. 设置数据同步对象：选择数据同步类型和同步对象。
   - **整个实例**：选择整个实例后，根据已选同步类型，同步整个实例的对应数据。
   - **指定对象**：支持库级别、表级别同步。指定对象时还支持多表归并和修改库表名映射。
多表归并说明及操作请参见 [多表归并（数据合并）](https://cloud.tencent.com/document/product/1488/74331)，修改库表名映射说明及操作请参见 [修改库表名映射](https://cloud.tencent.com/document/product/1488/63694)。
7. 设置完成后，单击**下一步**。
8. 高级设置：可[设置排序键](https://cloud.tencent.com/document/product/1488/76363)、 [设置分区键](https://cloud.tencent.com/document/product/1488/63692) 和 [自定义字段类型映射](https://cloud.tencent.com/document/product/1488/63691#.E8.87.AA.E5.AE.9A.E4.B9.89.E6.95.B0.E6.8D.AE.E7.B1.BB.E5.9E.8B.E8.BD.AC.E6.8D.A2)。
9. 设置完成后，单击**下一步**。
10. 在校验任务页面，完成校验并各项校验通过后，单击**启动任务**或**稍后启动**。
>?CDC 任务正式启动数据同步前，会检查源实例和目标实例。查询检查结果中会显示各项检查结果是否通过。
>如果查询结果中有检查项校验结果为失败或告警，请在对应检查项后单击**查看详情**，查看错误原因并修复问题，修复后请在页面左下方单击**重新校验**，直至校验通过。
> - 失败：不能启动 CDC 任务。
> - 告警：可启动 CDC 任务，根据错误原因评估是否对业务有影响，如果有请修复问题后重新校验。</li></ul>
>
页面返回至 CDC 列表页面，显示当前 CDC 任务的状态、进度等相关信息。

## 后续操作
- CDC 任务创建成功后，如果未立即启动，支持立即启动任务、查看任务详情、修改任务配置参数、终止任务和创建类似任务等操作。
- CDC 任务启动后，支持完成准备工作、查看任务详情、数据对比、终止任务和创建类似任务等操作。

