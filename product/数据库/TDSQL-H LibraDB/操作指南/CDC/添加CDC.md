
本文为您介绍如何通过控制台创建将 OLTP 同步到分析引擎的 CDC 数据链路。

## 操作步骤
1. 登录 [TDSQL-H LibraDB 控制台](https://console.cloud.tencent.com/libradb/instance)，在实例列表，单击实例 ID 或**操作**列的**详情**，进入实例管理页面。
2. 在实例管理页面，选择 **CDC** 页，单击**添加CDC**，可创建将 OLTP 同步到分析引擎的数据链路。
或在实例详情页的架构图中，选择**添加OLTP**创建链路。
3. 在新建页面，填写源端 MySQL 实例的信息。**测试连通性**通过后，即可单击**下一步**，进入**设置对象**。
为了让服务对您的源端实例影响降到最小。CDC 限制了源实例帐号的权限。建议您为 CDC 任务单独增加用户和帐号信息。所需权限如下：
  - “整个实例”同步，需要的源端帐号权限如下：
```sql
CREATE USER 'CDC帐号'@'%' IDENTIFIED BY 'CDC密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO 'CDC帐号'@'%';  
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO 'CDC帐号'@'%';  
GRANT SELECT ON *.* TO 'CDC帐号';
```
  - “指定对象”同步，需要的源端帐号权限如下：
```sql
CREATE USER 'CDC帐号'@'%' IDENTIFIED BY 'CDC密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO 'CDC帐号'@'%';  
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO 'CDC帐号'@'%';  
GRANT SELECT ON `mysql`.* TO 'CDC帐号'@'%';
GRANT SELECT ON 待同步的库.* TO 'CDC帐号';
```
  - 授权语句中，有对\_\_tencentdb\_\_库的授权，腾讯云需要该库记录位点等元数据信息。
>?对\_\_tencentdb\_\_授权前，无需创建\_\_tencentdb\_\_。
>
<img src="https://qcloudimg.tencent-cloud.cn/raw/cc3c9fd2e81933459bcffdbfb182ae57.png" style="zoom:80%;" />
4. 在**设置对象**页面，选择同步类型和对象，单击**保存**。
- CDC 提供了如下同步类型选择，以适用于用户多种场景。  
<table>
<thead><tr><th>初始结构</th><th>初始全量数据</th><th>增量数据</th><th>功能</th><th>场景</th></tr></thead>
<tbody><tr>
<td>&#10003;</td><td>-</td><td>-</td>
<td>只将库表结构同步到 LibraSQL 分析引擎。</td>
<td>做结构验证。</td></tr>
<tr>
<td>&#10003;</td><td>&#10003;</td><td>-</td>
<td>将库表结构和全量数据同步到 LibraSQL 分析引擎。</td>
<td>开发测试环境做测试验证。</td></tr>
<tr>
<td>&#10003;</td><td>&#10003;</td><td>&#10003;</td>
<td>将库表结构、全量数据同步到 LibraSQL 分析引擎后继续保持数据同步。将源端在同步过程中的数据，实时同步到目标。</td>
<td>同步的信息最多，适用于所有场景。</td></tr>
<tr>
<td>&#10003;</td><td>-</td><td>&#10003;</td>
<td>只做结构同步和增量数据同步。</td>
<td>日志场景，流式分析等只关注增量数据的场景。</td></tr>
<tr>
<td>-</td><td>-</td><td>&#10003;</td>
<td>只将增量数据同步到目标端。</td>
<td>用户需要定制化的目标表结构，且只需要流式的增量数据。</td></tr>
</tbody></table>	  
- 同步对象可选择**整个实例**或**指定对象**。当选择指定对象时，可 [修改库表名映射](https://cloud.tencent.com/document/product/1488/63694)。
5. 在**高级设置**页面，可 [设置分区键](https://cloud.tencent.com/document/product/1488/63692) 和 [自定义字段类型映射](https://cloud.tencent.com/document/product/1488/63691#.E8.87.AA.E5.AE.9A.E4.B9.89.E6.95.B0.E6.8D.AE.E7.B1.BB.E5.9E.8B.E8.BD.AC.E6.8D.A2)。完成设置后，单击**保存**。
6. CDC 正式启动数据同步前，需要检查用户的各项设定是否能满足启动的要求，**校验任务**页即是将检查结果汇总报告。若校验通过，则可正式启动任务。可关闭该页，在任务列表页修改、重新校验或是启动任务。
   - 若有“失败”类校验结果，则不能启动任务。
   - 若有“警告”类校验结果，虽可以启动任务，但需用户仔细核对警告信息。
7. **校验任务**通过校验后，即可**启动任务**。任务启动后会返回任务列表。显示当前任务的进度和信息。

