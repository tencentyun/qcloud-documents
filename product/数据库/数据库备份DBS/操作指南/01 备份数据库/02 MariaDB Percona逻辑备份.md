## 操作场景
本章节介绍通过 DBS 对 MariaDB、Percona 数据库进行逻辑备份。

## 前提条件
- 源数源数据库符合备份功能和版本要求，请参见 [备份和恢复能力汇总](https://cloud.tencent.com/document/product/1513/64026) 进行核对。
- 已完成 [准备工作](https://cloud.tencent.com/document/product/1513/64040)。
- 备份帐号需要具备源数据库的相关权限，如下为全量和增量备份的授权，如果仅全量，无增量备份，则不需要 REPLICATION CLIENT、REPLICATION SLAVE 授权。
  - “整个实例”备份：
```
CREATE USER '帐号'@'%' IDENTIFIED BY '密码';  
GRANT LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO '帐号'@'%';  
使用只读帐号对腾讯云 MariaDB 的从库进行备份时，只读帐号缺少`lock table`权限，需要提交工单https://console.cloud.tencent.com/workorder/category申请
GRANT SELECT ON *.* TO '帐号';
```
  - “指定对象”备份：
```
CREATE USER '帐号'@'%' IDENTIFIED BY '密码';  
GRANT LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO '帐号'@'%';  
GRANT SELECT ON `mysql`.* TO '帐号'@'%';
GRANT SELECT ON 待备份的库.* TO '帐号';
```

## 约束限制
- 逻辑备份的对象仅支持库、表、索引、视图，不支持用户数据、存储过程、Function 等。
- 不支持 GIS 地理类型的数据备份。
- 源库为 MariaDB 10.0.X 版本时，不支持 Decimal 数据类型的备份。 
- 只支持备份 InnoDB、MyISAM、TokuDB 三种数据库引擎，如果存在这三种以外的数据引擎表则默认跳过不进行备份。
- 全量备份阶段，源库不能进行 DDL 操作，否则任务报错，增量备份阶段可以进行 DDL 操作。 

## 支持的 SQL 操作

| 操作类型 | 支持的 SQL 操作                                              |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE、REPLACE                              |
| DDL      | TABLE：CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE  VIEW：CREATE VIEW、DROP VIEW INDEX：CREATE INDEX、DROP INDEX  DATABASE：CREATE DATABASE、ALTER DATABASE、DROP DATABASE |

## 操作步骤
### 购买备份计划
登录 [DBS 控制台](https://console.cloud.tencent.com/dbs)，在左侧导航选择**备份计划**页，单击**新建备份计划**，跳转到购买备份计划页面，根据实际需求选择各项配置信息，确认无误后，单击**立即购买**。
- **商品类型**：备份计划实例。
- **计费模式**：包年包月。
- **备份计划地域**：该地域为数据库备份存储和恢复所属地域，购买后不可修改。
- **数据库类型**：选择源端的数据库类型。
- **规格**：选择备份计划的规格，规格越高，性能越好，请根据您的数据量选择，不同规格计费详情请参考 [计费概述](https://cloud.tencent.com/document/product/1513/64028)。
- **备份方式**：当前仅支持逻辑备份。
- **标签**：设置标签，当备份实例较多时，用于区分。

### 配置备份计划
1. 登录 [DBS 控制台](https://console.cloud.tencent.com/dbs)，在左侧导航选择**备份计划**页，然后在右侧选择已购买的备份计划，单击**配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/020d9771d050e2bf1d9942458c7d853c.png)
2. 在**设置备份源**页面配置备份计划和数据源，单击**测试连通性**，通过后进入**下一步**。
如果连通性测试失败，请参考 [连通性测试不通过处理方法](https://cloud.tencent.com/document/product/1513/64057) 进行处理。
![](https://qcloudimg.tencent-cloud.cn/raw/ab0602611ea3ee9a6270f98fe27332f3.png)
<table>
<thead><tr><th width="10%">设置类型</th><th width="20%">配置项</th><th width="70%">说明</th></tr></thead>
<tbody>
<tr>
<td rowspan=2>备份计划设置</td>
<td>计划名称</td>
<td>设置一个具有业务意义的名称，便于识别。</td></tr>
<tr>
<td>全量备份并行数上限</td>
<td>该上限与用户购买的备份计划规格中的上限一致。</td></tr>
<tr>
<td rowspan=9>源实例设置</td>
<td>数据库类型</td><td>购买计划中设置的数据库类型，不可修改。</td></tr>
<tr>
<td>接入类型</td><td>请根据您的场景选择，本场景选择“公网”。
<ul><li>公网：源数据库可以通过公网 IP 访问。</li>
<li>云主机自建：源数据库部署在 <a href="https://cloud.tencent.com/document/product/213">腾讯云服务器 CVM</a> 上。</li>
<li>专线接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/216">专线接入</a> 方式与腾讯云私有网络打通。</li>
<li>VPN接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/554">VPN 连接</a> 方式与腾讯云私有网络打通。</li>
<li>云数据库：源数据库属于腾讯云数据库实例。</li>
<li>云联网：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877">云联网</a> 与腾讯云私有网络打通。</li>
<li>私有网络 VPC：源数据部署在腾讯云上，且有<a href="https://cloud.tencent.com/document/product/215">私有网络</a>。</li></ul></td></tr>
<tr>
<td>所属地域</td><td>备份计划中的地域，该地域为备份数据存储和恢复所在地域。</td></tr> 
<tr>
<td>主机地址</td><td>源库访问 IP 地址或域名。</td></tr>
<tr>
<td>端口</td><td>源库访问端口。</td></tr>
<tr>
<td>帐号</td><td>源库的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库的数据库帐号的密码。</td></tr>
<tr>
<td>连接方式</td><td><ul><li>非加密方式：DBS 与源数据库的连接不加密。</li><li>SSL 安全连接：DBS 与源数据库通过 SSL（Secure socket layer）安全连接，对传输链路进行加密。</li></ul><dx-alert infotype="explain" title="说明">选择 SSL 安全连接可能会增加源库的连接响应时间，一般腾讯云内网链路相对较安全，无需开启 SSL 安全连接，采用公网/专线等传输方式，并且对数据安全要求较高的场景，需要开启 SSL 安全连接。<br>选择<b> SSL 安全连接</b> 前，请先在源数据库中开启 SSL 加密。如果源库为腾讯云数据库，可参考 <a href="https://cloud.tencent.com/document/product/237/33944">开启 SSL 加密</a>。</dx-alert></td></tr>
<tr>
<td>CA 根证书</td><td>可选，上传 CA 证书后，DBS 会校验传输目标服务器的身份，使传输链路更加安全。</td></tr></tbody></table>
3. 在**设置备份对象**页面，选择备份对象后，单击**下一步**。
备份对象：
   - 整个实例：备份整个实例，当前仅支持备份库、表和视图，暂不支持备份用户权限、存储过程、Function等。选择整个实例，后续源库新增的对象会同步到备份集中，恢复任务中可以恢复新增的对象。 
   - 指定对象：备份指定对象，然后在下面的界面中选择需要备份的指定库、表等。选择指定对象，则仅同步指定对象到备份集中，后续恢复任务中不能恢复新增的对象。
   ![](https://qcloudimg.tencent-cloud.cn/raw/069c3df7c09a9b5f97a2c597053176b0.png)
4. 在**选择备份策略**页面，选择策略模板、备份方式、备份频率、备份周期等，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/2e55da1199d1137fbb9f73b3f1d8e328.png)
<table>
<thead><tr><th width="20%">配置项</th><th width="80%">说明</th></tr></thead>
<tbody>
<tr>
<td>导入策略模板配置</td>
<td>勾选该参数时，如下参数将按照模板中的内容导入，用户可以在模板的基础上进行修改。</td></tr>
<tr>
<td>备份类型</td>
<td>当前仅支持逻辑备份。</td></tr>
<tr>
<td>全量备份方式</td>
<td><ul>
<li>周期备份：根据用户设置的频率（每星期）、周期、全量备份开始时间进行备份。周期备份支持勾选增量备份。</li>
<li>单次备份：根据用户设置的时间进行一次全量备份。单次备份不支持增量备份。</li>
</ul>当一次全量备份所需时间大于备份间隔时，将会跳过一下次备份时间点。</td></tr>
<tr>
<td>存储类型</td>
<td>DBS 内置存储。</td></tr>
<tr>
<td>存储池</td>
<td>选择该备份计划地域的存储池。</td></tr>
<tr>
<td>存储方式</td>
<td><ul><li>非存储加密：数据保存在 DBS 内置存储中，不加密。</li><li>内置加密存储：数据以加密的方式保存在 DBS 内置存储中，加密方式为存储系统自身的加密方式，数据上传到存储系统时加密，从存储系统获取数据即解密。</li><li>KMS 加密存储：数据以 KMS （<a href="https://cloud.tencent.com/document/product/573">密钥管理系统</a>）加密方式保存在 DBS 内置存储中，加密密钥为  <a href="https://console.cloud.tencent.com/kms2">KMS 中设置的密钥</a>。</li></ul></td></tr>
<tr>
<td>保留时间</td>
<td>可设置范围为7天到3650天（10年）。</td></tr>
<tr>
<td>保存为策略模板</td>
<td>支持将当前配置的策略保存为模板，方便后续直接使用。</td></tr>
</tbody></table>
5. 在**预检查及启动**页面，执行校验任务通过后，单击**立即启动**。
   如果校验任务不通过，可以参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/1513/65196) 修复问题后重新发起校验任务。
   - 失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。
   - 警告：表示检验项检查不完全符合要求，用户需要根据警告评估对业务的影响，确认影响可接受，则可以忽略警告继续任务。
![](https://qcloudimg.tencent-cloud.cn/raw/7e3d527a2f3d8113734223e4748dd0cb.png)
6. 备份计划会在后续按系统指示启动备份任务。
7. （可选）用户如果需要对备份计划进行修改、暂停等操作，请参考 [备份任务管理](https://cloud.tencent.com/document/product/1513/64046)。

