Apache Superset 是一个数据浏览和可视化 Web 应用程序。

Superset 特性：
- 支持几乎所有主流的数据库，包括 MySQL、PostgresSQL、Oracle、SQL Server、SQLite、SparkSQL 等，并深度支持 [Druid](http://druid.io/)。
- 丰富的可视化展示，支持自定义创建 dashboard。
- 数据的展示完全可控，可自定义展示字段、聚合数据、数据源等。

EMR 上的 Superset，原装了对 Mysql、Hive、Presto、Impala、Kylin、Druid、Clickhouse 的支持。

## 准备工作
1. 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。
2. 创建集群时，可选组件中勾选了 Superset。
3. Superset 默认安装在集群的 master 节点上。
4. 打开 master 节点的安全组策略，确保您的网络可以访问 master 节点的18088端口。
5. 添加初始化操作。
```
export PYTHONPATH=/usr/local/service/superset/conf
/usr/local/service/superset/bin/superset db upgrade
/usr/local/service/superset/bin/superset fab create-admin   设置用户名admin及密码
/usr/local/service/superset/bin/superset init
```

## 登录
在浏览器地址栏中输入`http://${master_ip}:18088`（或者通过 **[EMR 控制台](https://console.cloud.tencent.com/emr) > 集群服务**）, 打开 Supserset 登录界面，默认用户名为 admin，密码为您创建集群时的密码。
![](https://main.qcloudimg.com/raw/d250be3123fb3e7da47d69b73ef6343a.png)

## 添加 DataBase
进入 **Sources > Databases** 界面，单击 **Filter List**。
![](https://main.qcloudimg.com/raw/c98760953f38fc23d27abcbf5208bd83.png)
进入如下页面，在 SQLAlchemy URI 中加入您需要添加的组件的 URI。
![](https://main.qcloudimg.com/raw/57b69ecbd6f5c2ac0ca4adde380325ae.png)
 
各个数据库的链接 SQLAlchemy URI 如下：

| **名称** | **SQLAlchemy   URI**                                         | **备注**                                                     |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Mysql    | `mysql+pymysql://<mysqlname>:<password>@<mysql_ip>:<mysql_port>/<your_database>` | <li>mysqlname：连接 mysql 使用的用户名<li>password：mysql 密码<li>your_database：需要连接的 mysql 数据库 |
		| Hive     | `hive://hadoop@<master_ip>:7001/default?auth=NONE`             | Master_ip：EMR 集群的 master_ip          |
| presto   | `presto://hive@<master_ip>:9000/hive/<hive_db_name>`           | <li/>Master_ip：EMR 集群的 master_ip<li/>hive_db_name：hive 中的数据库名称，不填默认为 default |
| impala   | `impala://<core_ip>:27000`                                     | core_ip：EMR 集群中的 core ip     |
| kylin    | `kylin://<kylin_user>:<password>@<master_ip>:16500/<kylin_project>` | <li/>kylin_user：kylin 的用户名<li/>password：kylin 的密码<li/>master_ip：EMR 集群的 master_ip<li/>kylin_project：kylin 的项目 |
|Clickhouse  |`clickhouse://<user_name>:<password>@<clickhouse-server-endpoint>:8123/<database_name>`| `clickhouse://default:password@localhost:8123/default`<li/>user_name：用户名</li>password：密码<li/>clickhouse-server-endpoint：ch 服务的服务 endpoint<li/>database_name：需要访问的 DB 名字


## 自行添加新 Database
Superset 支持 Database。如果您需要安装其他的数据库，可通过如下操作进行：
1. 登录 EMR 集群 master 所在机器。
2. 执行命令`source /usr/local/service/superset/bin/activate`。
3. pip3 install 对应的 Python 库。
4. 重启 Superset。

