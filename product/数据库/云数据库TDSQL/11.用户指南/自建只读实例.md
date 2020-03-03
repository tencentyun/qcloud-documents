## 1. 概述
### 1.1 概述
如果您仅需要实现[读写分离](https://cloud.tencent.com/document/product/237/2081)，目前MariaDB所有从机都支持只读，详情可查看文档[读写分离](https://cloud.tencent.com/document/product/237/2081)技术。

然而，您可能仍然需要额外只读实例，以实现更灵活的控制，并实现构建一些复杂业务系统。因此，MariaDB支持**利用CVM自建只读实例**的方案。

### 1.2 自建只读实例的架构
如下图所示，自建只读实例是在MariaDB集群外，利用主从同步功能和TProxy的binlog同步功能，将数据“同步”到一个或多个自建只读实例。这样，您可以在自主控制的CVM服务器上，安装任何软件或做任何数据操作。

![](https://mc.qcloudimg.com/static/img/a347c4d64a22c6b3f08c115c9e51c490/image.png)

为保证性能和MariaDB集群的稳定性，我们在此方案下，仅提供**异步**同步方案，且在集群压力过大时提高数据同步延迟以减少对MariaDB主集群的性能消耗；这意味着，您自建的只读实例的数据延迟可能在几秒到几分钟不等。对延迟有苛刻要求的情况下，建议您使用MariaDB的[读写分离](https://cloud.tencent.com/document/product/237/2081)技术。

## 2. 建设方案
### 2.1 明确MariaDB内核版本
通常您可以在实例列表或实例详情中，查看MariaDB的内核版本；目前已经支持MariaDB 10.0.10，MariaDB 10.1.9；（未来可支持更多版本，但基本方案不变）
 
### 2.2 创建适当规格的CVM
根据您现有实例内存、磁盘规格信息，创建CVM。
	
- **CVM配置**：我们建议您的CVM配置比MariaDB实例的大约20%，且数据盘至少大50GB，内存至少大2GiB。如果您还要在CVM上安装其他软件，再根据软件需要适当加大CVM配置
- **操作系统**：推荐CentOS 6/CentOS 7
- **数据盘格式化**：要求ext3文件系统，且挂载在/data目录下。
- **安装MariaDB**：必须安装与MariaDB相同的版本。

### 2.3 安装MariaDB举例
以CentOS为例，安装(`mariadb 10.0.10`)版本的步骤如下：
	
- 1.配置添加yum源文件(`vi /etc/yum.repos.d/mariadb.repo`):

> 10.0.10版本的官网yum源为：
	```
	# MariaDB 10.0 CentOS repository list - created 2016-05-30 02:16 UTC
	# http://downloads.mariadb.org/mariadb/repositories/
	[mariadb]
	name = MariaDB
	#baseurl = http://yum.mariadb.org/10.0/centos7-amd64
	baseurl = http://archive.mariadb.org/mariadb-10.0.10/yum/centos6-amd64/
	gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
	gpgcheck=0
	```
> 10.1.9版本的官网yum源为：
	```
	# MariaDB 10.1 CentOS repository list - created 2016-05-30 02:16 UTC
	# http://downloads.mariadb.org/mariadb/repositories/
	[mariadb]
	name = MariaDB
	#baseurl = http://yum.mariadb.org/10.1/centos7-amd64
	baseurl = http://archive.mariadb.org/mariadb-10.1.9/yum/centos6-amd64/
	gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
	gpgcheck=0
	```

- 2.检查配置yum源对应的mariadb版本是否正确

```
	yum makecache
	yum info MariaDB-server
```

- 3.安装MariaDB-server和Client


```
	yum install MariaDB-server MariaDB-client MariaDB-devel -y
	注：如果有提示和以前安装的版本冲突，您可能需要先移除以前安装的包，例如: yum remove mariadb-libs.
```

### 2.4 安装mydumper

下载地址：https://launchpad.net/mydumper
编译安装：`yum install make cmake pcre-devel glib2-devel zlib-devel gcc-c++`
解压`mydumper-0.9.1.tar.gz`进入目录并安装:
	cmake . 
	make && make install
安装完后运行`mydumper –V`可以看到版本信息

### 2.5 配置CVM上的MariaDB并启动

删除文件`/etc/my.cnf.d/enable_encryption.preset`
	rm -f /etc/my.cnf.d/enable_encryption.preset
创建目录:
	mkdir -p /data/dbdata/{data,tmpdir}
	mkdir -p /data/dblogs/relay
修改配置文件`/etc/my.cnf.d/server.cnf:`
```
	[mysqld]
	character-set-server = utf8
	collation-server = utf8_general_ci
	innodb_page_size=16384
	lower_case_table_names=1
	server-id=10
	innodb_buffer_pool_size=2097152000
	skip-name-resolve
	datadir = /data/dbdata/data/
	relay-log = /data/dblogs/relay/relay.log
	log-error = /data/dblogs/mysqld.err
	tmpdir = /data/dbdata/tmpdir
```

>		注意事项：
			在配置这些参数时，可以在原实例上使用show gloabl variabels like xxx来查看原实例的参数做参考。其中：
			character-set-server、lower_case_table_names、innodb_page_size等参数要和原TDSQL实例一样
			innodb_buffer_pool_size的值可以参考tdsql的参数。
			server-id要和原TDSQL实例不同
		运行mysql_install_db 安装db
		修改文件所有者：
	chown -R mysql:mysql /data/dbdata/  /data/dblogs/
		启动mariadb：
			service mysql start
		修改root密码并测试登录：
			mysqladmin -u root password 'root';
	mysql -uroot -proot -hlocalhost -P3306


### 2.6 创建用于同步的数据库账号

如果准备从主机上同步，创建普通账号，如果从备机上同步，则创建只读账号（建议从备机上进行同步，避免影响主机）。
设置数据库账号的权限至少包含全局`SELECT, REPLICATION SLAVE,REPLICATION CLIENT, RELOAD`的权限（**如果在控制台进行设置权限失败，或者没有所需的权限，请建工单联系客服为您的同步账号添加所需的权限**）。

### 2.7 使用mydumper导出TDSQL数据

>注意：第一次导出过程中会有锁表操作，请评估业务是否可以接受，建议在业务低峰期操作。
使用mydumper导出tdsql数据(-B后面跟着的是要进行同步的数据库)：
	`mydumper -t 4 --host 10.66.183.239 --port 3306 --user=user --password=password001 --outputdir=./export_tdsql -B syncdb`
	使用myloader导入数据(-B后面跟着的是要进行同步的数据库)：
`myloader --host localhost --port 3306 --user=root --password=root -d ./export_tdsql -o -B syncdb`


### 2.8 建立主从同步关系
查看7中导出的metadata文件信息：
	`cat export_tdsql/metadata`
里面应该要有binlog位置和gtid的信息，否则无法进行建主从同步关系：
	```
	SHOW MASTER STATUS:
	Log: binlog.000003
	Pos: 64233211
		GTID:0-2694363359-883267
登录CVM的db配置主从：
		配置要进行同步的db：
			set global replicate_do_db='syncdb';
		设置gtid_slave_pos点：
	SET GLOBAL gtid_slave_pos = "0-2694363359-883267";
	配置主从关系：
	CHANGE MASTER TO 	MASTER_HOST='10.66.183.239',MASTER_PORT=3306,MASTER_USER='user',MASTER_PASSWORD='password111',master_use_gtid=slave_pos;
	启动备机：
	START SLAVE;
	查看slave状态：
	show slave status\G
	```
其中Slave_IO_Running和Slave_SQL_Running为running状态，则配置成功。

## 5. 使用注意事项及功能限制

- 此处基于CVM部署的只读实例，并不会被纳入MariaDB集群进行管理，这意味着如果MariaDB集群中节点故障，该方案部署的只读实例（永远）不会被切换为主机，所以他不会提升系统可用性。

- 您可以挂在多个自建只读实例，但从业务性能建议您不超过4个。

- 自建只读实例功能当前免费。

