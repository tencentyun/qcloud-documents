## 支持的版本

| 节点 | 版本 | Driver|
|---------|---------|	---------|	
|MySQL-CDC 	|MySQL：5.6，5.7，8.0.x<br>RDS MySQL：5.6，5.7， 8.0.x<br>PolarDB MySQL：5.6，5.7，8.0.x<br>Aurora MySQL：5.6，5.7，8.0.x<br>MariaDB：10.x<br>PolarDB X：2.0.1	|JDBC Driver：8.0.21|

## 创建 MySQL 节点
1. 在数据集成页面左侧目录栏单击**实时同步**。
2. 在实时同步页面上方选择**单表同步**新建（可选择表单和画布模式）并进入配置页面。
3. 单击左侧**读取**，单击选择 MySQL 节点并配置节点信息。
![](https://qcloudimg.tencent-cloud.cn/raw/8f7635438de658e3d26cb74d62da060b.png)
4. 参数信息：
<table>
<thead>
<tr>
<th>参数</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>节点名称</td>
<td>输入 MySQL 节点名称</td>
</tr>
<tr>
<td>数据源</td>
<td>选择需要同步的表所在数据源</td>
</tr>
<tr>
<td>库</td>
<td>选择需要同步的表所在数据库</td>
</tr>
<tr>
<td>表</td>
<td>支持选择多个表，请保证多表 schema 一致</td>
</tr>
<tr>
<td>表主键</td>
<td>分库分表模式下默认表 schema 一致。系统将使用拉去第一张表的主键，请选择或输入表主键字段名称</td>
</tr>
<tr>
<td>格式</td>
<td>指定 mysql 日志编码格式（utf-8、gbk、Latin1、utf8mb4）</td>
</tr>
<tr>
<td>读取模式</td>
<td>支持全量和增量两种模式</td>
</tr>
<tr>
<td>过滤操作</td>
<td>设置后将不同步指定操作类型的数据，支持插入、更新和删除</td>
</tr>
</tbody></table>
5. 预览数据字段，单击**保存**。

## 注意事项
1. 为每个 Reader 设置一个不同的 SERVER ID。
每一个读取 Binlog 的 MySQL 数据库客户端都应该有一个唯一的 ID，称为 SERVER ID。 MySQL 服务器将使用此 ID 来维护网络连接和 Binlog 位置。因此，如果不同的作业共享相同的服务器 ID，可能会导致从错误的 Binlog 位置读取。 因此，建议通过 [SQL Hints](https://nightlies.apache.org/flink/flink-docs-release-1.11/dev/table/sql/hints.html) ，例如假设源并行度为 4，那么我们可以使用 `SELECT * FROM source_table /*+ OPTIONS('server-id'='5401-5404') */` ; 为 4 个 Source Reader 中的每一个分配唯一的服务器 ID。
2. 设置 MySQL 会话超时。
当为大型数据库制作初始一致快照时，您建立的连接可能会在读取表时超时。您可以通过在 MySQL 配置文件中配置 interactive_timeout 和 wait_timeout 来防止这种行为。
	- interactive_timeout：服务器在关闭交互式连接之前等待其活动的秒数。请参阅 [MySQL :: MySQL 8.0 Reference Manual :: 5.1.8 Server System Variables](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_interactive_timeout)。
	- wait_timeout：服务器在关闭非交互式连接之前等待其活动的秒数。请参阅 [MySQL :: MySQL 8.0 Reference Manual :: 5.1.8 Server System Variables](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_wait_timeout)。
