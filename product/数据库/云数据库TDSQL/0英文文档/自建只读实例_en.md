> This capacity is supported for MariaDB (TDSQL) instances applied after April 1, 2017 in default. Instances applied before April 1, 2017 need to be upgraded by submitting a ticket. There will be a brief disconnection (about one minute) during the upgrade process, please make adjustment to the lows of business.

## 1. Overview
### 1.1 Overview
If you only need to achieve [Read-write Separation](https://cloud.tencent.com/document/product/237/2081), all the slaves on MariaDB (TDSQL) support read-only capability currently. For more information, please see the document of [Read-write Separation](https://cloud.tencent.com/document/product/237/2081) technique.

However, you may still need additional read-only instances, to control in a more flexible way and build complicated business systems. Therefore, MariaDB (TDSQL) supports the scheme of **using self-built CVM read-only instances**.

### 1.2 Architecture of self-built read-only instance
As shown in the figure below, self-built read-only instances locate outside of the MariaDB (TDSQL) cluster. You can "sync" the data to one or more self-built read-only instances using master-slave synchronization feature and TProxy's Binlog synchronization feature. So, you can install any software or work with any data on the self-control CVM.

![](https://mc.qcloudimg.com/static/img/a347c4d64a22c6b3f08c115c9e51c490/image.png)

To ensure the performance and stability of MariaDB (TDSQL) cluster, we only provide "async" synchronization under this scheme, and increase the delay time of data synchronization in case of cluster overload, to reduce the performance consumption on MariaDB (TDSQL) master cluster. This means, the data delay of your self-built read-only instances may range from few seconds to few minutes. If you have any stringent requirements for delay, it is recommended to use [Read-write Separation](https://cloud.tencent.com/document/product/237/2081) technique of MariaDB (TDSQL).

## 2. Creation scheme
### 2.1 Determine kernel version of MariaDB (TDSQL)
Generally, you can view the kernel version of TDSQL in the list of instances or instance details. Currently, MariaDB 10.0.10 and MariaDB 10.1.9 are supported (more versions will be supported in the future, but the basic scheme remains the same);
 
### 2.2 Create a CVM with supported specifications
Create a CVM based on the memory and disk specification information of an existing instance.
	
- **CVM configuration**: Compared to MariaDB (TDSQL) instance, your CVM is about 20% larger in configuration, 50 GB larger in data disk size , and at least 2 GB larger in memory size. If you want to install other software in the CVM, you can expand the CVM configuration as required
- **Computing system**: Centos 6/Centos 7 is recommended
- **Data disk formatting**: EXT3 file system is required and mounted under the directory "/data".
- **Installation of MariaDB**: You must install MariaDB with same version as MariaDB (TDSQL).

### 2.3 Example of MariaDB installation
On Centos, for example, install MariaDB with a version of `mariadb 10.0.10` by following the steps below:
	
- 1. Configure and add YUM source file (`vi /etc/yum.repos.d/mariadb.repo`):

> The official YUM source of 10.0.10 version is:
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
> The official YUM source of 10.1.9 version is:
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

- 2. Check whether the version of MariaDB for configuration of YUM source is correct

```
	yum makecache
	yum info MariaDB-server
```

- 3. Install MariaDB-server and Client


```
	yum install MariaDB-server MariaDB-client MariaDB-devel -y
	Note: If prompted that there is a conflict with the previous version, you need to delete the previous installation package, for example: yum remove mariadb-libs.
```

### 2.4 Install Mydumper

Download address: https://launchpad.net/mydumper
Compile and install: `yum install make cmake pcre-devel glib2-devel zlib-devel gcc-c++`
Decompress `mydumper-0.9.1.tar.gz` to enter the directory and install:
	cmake. 
	make && make install
After installation, run `mydumper -V` to view the version information

### 2.5 Configure and launch MariaDB on CVM

Delete the file `/etc/my.cnf.d/enable_encryption.preset`
	rm -f /etc/my.cnf.d/enable_encryption.preset
Create directory:
	mkdir -p /data/dbdata/{data,tmpdir}
	mkdir -p /data/dblogs/relay
Modify the configuration file `/etc/my.cnf.d/server.cnf`:
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

>		Note:
			During the configuration of these parameters, you can use "show gloabl variabels like xxx" on the original instance to view parameters for reference. In this case:
			The parameters such as character-set-server, lower_case_table_names, innodb_page_size need to be the same as that in the original TDSQL instance.
			The value of innodb_buffer_pool_size can be set by referring to TDSQL parameters.
			The server-id shall be different from that of original TDSQL instance
		Run "mysql_install_db" and install DB
		Modify the file owner:
	chown -R mysql:mysql /data/dbdata/  /data/dblogs/
		Launch MariaDB:
			service mysql start
		Modify Root password and test login:
			mysqladmin -u root password 'root';
	mysql -uroot -proot -hlocalhost -P3306


### 2.6 Create a database account for synchronization

You can create a regular account for synchronization on master, and a read-only account for synchronization on slave (it is recommended to sync on slave to avoid the impact on master).
The permissions of a database account are set to include at least the global permissions `SELECT, REPLICATION SLAVE, REPLICATION CLIENT, RELOAD`. **If the configuration of permissions on the console fails, or there is no desired permission, please contact the customer service to add required permissions for your synchronization account by submitting a ticket**.

### 2.7 Export TDSQL data using Mydumper

>Note: You need to lock table in the process of first export, please evaluate whether the business is acceptable. It is recommended to operate during off-peak business hours.
Export TDSQL data using Mydumper (-B is followed by the database to be synced):
	`mydumper -t 4 --host 10.66.183.239 --port 3306 --user=user --password=password001 --outputdir=./export_tdsql -B syncdb`
	Import data using Myloader (-B is followed by the database to be synced):
`myloader --host localhost --port 3306 --user=root --password=root -d ./export_tdsql -o -B syncdb`


### 2.8 Build master-slave synchronization relationship
View the information of Metadata file exported in 2.7:
	`cat export_tdsql/metadata`
The file must contain Binlog location and GTID information, otherwise the synchronization relationship cannot be built:
	```
	SHOW MASTER STATUS:
	Log: binlog.000003
	Pos: 64233211
		GTID:0-2694363359-883267
Log into CVM's DB to configure the master/slave:
		Configure the DB to be synced:
			set global replicate_do_db='syncdb';
		Set "gtid_slave_pos" point:
	SET GLOBAL gtid_slave_pos = "0-2694363359-883267";
	Configure master-slave relationship:
	CHANGE MASTER TO 	MASTER_HOST='10.66.183.239',MASTER_PORT=3306,MASTER_USER='user',MASTER_PASSWORD='password111',master_use_gtid=slave_pos;
	Launch slave:
	START SLAVE;
	View slave status:
	show slave status\G
	```
The configuration is successful if both Slave_IO_Running and Slave_SQL_Running are running.

## 5. Considerations and service limits

- The read-only instance deployed based on CVM cannot be added to MariaDB (TDSQL) for management. This means, if a node in the MariaDB (TDSQL) cluster fails, the read-only instance deployed under the scheme will never be switched to master, so it cannot improve the availability of system.

- You can mount multiple self-build read-only instances. However, it is recommended to limit the quantity to 4 to ensure the business performance.

- Currently, the feature of self-built read-only instance is provided free of charge.


