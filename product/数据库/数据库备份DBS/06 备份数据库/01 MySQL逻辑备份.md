## 操作场景
本章节介绍通过 DBS 对自建、第三方厂商、腾讯云 MySQL 数据库进行逻辑备份。

## 前提条件
- 源数据库符合备份功能和版本要求，请参见 [支持的备份能力](https://cloud.tencent.com/document/product/1513/64026) 进行核对。
- 备份账号需要具备源数据库的对应权限，请参考如下指导进行授权。
  - “整个实例”备份：
```
CREATE USER '帐号'@'%' IDENTIFIED BY '密码';  
GRANT RELOAD,LOCK TABLES,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO '帐号'@'%';  //源库为阿里云数据库时，不需要授权 SHOW DATABASES，其他场景则需要授权。阿里云数据库授权，请参考 https://help.aliyun.com/document_detail/96101.html 
GRANT SELECT ON *.* TO '帐号';
```
  - “指定对象”备份：
```
CREATE USER '帐号'@'%' IDENTIFIED BY '密码';  
GRANT RELOAD,LOCK TABLES,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO '帐号'@'%';  //源库为阿里云数据库时，不需要授权 SHOW DATABASES，其他场景则需要授权。阿里云数据库授权，请参考 https://help.aliyun.com/document_detail/96101.html  
GRANT SELECT ON `mysql`.* TO '帐号'@'%';
GRANT SELECT ON 待备份的库.* TO '帐号';
```

## 约束限制
逻辑备份的对象仅支持库、表、索引、视图，不支持用户数据、存储过程、Function 等。

## 操作步骤
### 购买备份计划
登录 DBS 控制台，在左侧导航选择**备份计划**页，单击**新建备份计划**，跳转到购买备份计划页面，根据实际需求选择各项配置信息，确认无误后，单击**立即购买**。
- **商品类型**：备份计划实例。
- **计费模式**：包年包月。
- **备份计划地域**：该地域为数据库备份存储和恢复所属地域，购买后不可修改。
- **数据库类型**：选择源端的数据库类型。
- **规格**：选择备份计划的规格，规格越高，性能越好，请根据您的数据量选择，不同规格计费详情请参考 [计费概述](https://cloud.tencent.com/document/product/1513/64028)。
- **备份方式**：当前仅支持逻辑备份。
- **标签**：设置标签，当备份实例较多时，用于区分。

### 配置备份计划
1. 登录 DBS 控制台，在左侧导航选择**备份计划**页，然后在右侧选择已购买的备份计划，单击**配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/c8febe50a84a788546ca461860150b34.png)
2. 在**设置备份源**页面配置备份计划和数据源，单击**测试连通性**，通过后进入**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/ad89d7899a6fa05f7c2680e8b3548a17.png)
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
<td rowspan=8>源实例设置</td>
<td>数据库类型</td><td>选择“MySQL”。</td></tr>
<tr>
<td>服务提供商</td><td>如果源数据库为自建数据库（包括腾讯云 CVM 上自建）、腾讯云数据库，请选择“普通”，如果是第三方云厂商，选择对应的服务提供商。</td></tr>
<tr>
<td>接入类型</td><td>请根据您的场景选择，本场景选择“公网”。
<ul><li>公网：源数据库可以通过公网 IP 访问。</li>
<li>云主机自建：源数据库部署在 <a href="https://cloud.tencent.com/document/product/213">腾讯云服务器 CVM</a> 上。</li>
<li>专线接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/216">专线接入</a> 方式与腾讯云私有网络打通。</li>
<li>VPN接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/554">VPN 连接</a> 方式与腾讯云私有网络打通。</li>
<li>云数据库：源数据库属于腾讯云数据库实例。</li>
<li>云联网：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877">云联网</a> 与腾讯云私有网络打通。</li>
<li>私用网络 VPC：源数据部署在腾讯云上，且有<a href"https://cloud.tencent.com/document/product/215">私有网络</a>。</li></ul>对于第三方云厂商数据库，一般可以选择公网方式，也可以选择 VPN 接入，专线或者云联网的方式，需要根据实际的网络情况选择。</td></tr>
<tr>
<td>所属地域</td><td>备份计划中的地域，该地域为备份数据存储和恢复所在的地域。</td></tr> 
<tr>
<td>主机地址</td><td>源库 MySQL 访问 IP 地址或域名。</td></tr>
<tr>
<td>端口</td><td>源库 MySQL 访问端口。</td></tr>
<tr>
<td>帐号</td><td>源库 MySQL 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库 MySQL 的数据库帐号的密码。</td></tr></tbody></table>

3. 在**设置备份对象**页面，选择备份对象后，单击**下一步**。
备份对象：
  - 整个实例：备份整个实例，当前仅支持备份库、表和视图，暂不支持备份用户权限、存储过程、Function等。  
  - 指定对象：备份指定对象，然后在下面的界面中选择需要备份的指定库、表等。
![](https://qcloudimg.tencent-cloud.cn/raw/069c3df7c09a9b5f97a2c597053176b0.png)
4. 在**选择备份策略**页面，选择策略模板、备份方式、备份频率、备份周期等，单击**下一步**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/2e034676dcd755a7795c6ffb32512832.png" style="zoom:67%;" />
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
<td>保留时间</td>
<td>可设置范围为7天到3650天（10年）。</td></tr>
<tr>
<td>保存为策略模板</td>
<td>支持将当前配置的策略保存为模板，方便后续直接使用。</td></tr>
</tbody></table>
5. 在**预检查及启动**页面，执行校验任务通过后，单击**立即启动**。
 - 失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。
 - 警告：表示检验项检查不完全符合要求，用户需要根据警告评估对业务的影响，确认影响可接受，则可以忽略警告继续任务。
![](https://qcloudimg.tencent-cloud.cn/raw/7e3d527a2f3d8113734223e4748dd0cb.png)
6. 备份计划会在后续按系统指示启动备份任务。

