TDSQL can view history data using rollback feature. If you want to restore the data in your machine, please follow the steps described in this document.
## 1. Prepare Environment Required to Restore Data
*Note: Make sure to use a CVM that resides in the same basic network or VPC to ensure the normal network connection*
Recommendation on basic configurations: CPU: 2-core or above; memory: 4 GB or above; disk space: it must exceed the space actually used by the database; operating system: the latest version of centos
Requirement for basic environment: **Mariadb 10.0.10**
Example of installation:

- Add yum source 
```
vi /etc/yum.repos.d/mariadb-10.0.10.repo):
# MariaDB 10.0 CentOS repository list - created 2016-05-30 02:16 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
# baseurl = http://yum.mariadb.org/10.0/centos7-amd64
baseurl = http://archive.mariadb.org/mariadb-10.0.10/yum/centos6-amd64/
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=0
```

- Check whether the mariadb version is 10.0.10 when configuring yum source
```
yum makecache
yum info MariaDB-server
```
- Install MariaDB-server
```
yum install MariaDB-server
```
*Note: If you are prompted that installation failed because previous version exists, you may need to remove it first, for example: `yum remove mariadb-libs`*

- Install Mariadb client
```
yum install MariaDB-client
```
- Install LZ4 decompression software
```
yum install -y lz4
percona-xtrabackup
yum install http://www.percona.com/downloads/percona-release/redhat/0.1-3/percona-release-0.1-3.noarch.rpm
yum install percona-xtrabackup
```


## 2. Download Backup
First, acquire the download address of a backup in **"Tencent Cloud Console -> Cloud Database -> Console -> Backup and Recovery"**
![](//mccdn.qcloud.com/static/img/c3d9a2815d8039c37af9dd31ff7c0853/image.png)

**Example of download command**
```
wget --content-disposition ' http://169.254.0.27:8083/2/noshard1/set_1464144850_587/1464552298xxxxxxxx'
```

## 3. Restore Backup File
- 1) Go to the download directory of the backup file and decompress the cold backup file using LZ4
```
lz4 -d set_1464144850_587.1464552298.xtrabackup.lz4
```
- 2) Decompress the file to a temporary directory "xtrabackuptmp" with xbstream tool
```
mkdir xtrabackuptmp/
mv set_1464144850_587.1464552298.xtrabackup xtrabackuptmp/
xbstream -x < set_1464144850_587.1464552298.xtrabackup
```
After decompression, the information about the directory and file is as follows:
 ![](//mccdn.qcloud.com/static/img/6f1d1aaf1ce9061cba0e09e4e47c271d/image.png)
- 3) Apply log
Use innobackupex to apply log
```
mkdir /root/dblogs_tmp
innobackupex --apply-log --use-memory=1G --tmpdir='/root/dblogs_tmp/' /root/xtrabackuptmp/
```
The operation is successful if you see "completed OK!", as shown below:
![](//mccdn.qcloud.com/static/img/4f43de6b03bf4456975105a8567d81a9/image.png)

- 4) Stop database and clear data file
Stop database
```
service mysql stop
```
Clear data file
```
mkdir /var/lib/mysql-backup
mv /var/lib/mysql/* /var/lib/mysql-backup
```

- 5) Modify database parameter file `(/etc/my.cnf.d/server.cnf)`. For more information about the specific parameter value, please see **the parameter of decompressed backup-my.cnf**:
*Note: You cannot replace the parameter file directly with backup-my.cnf.*
```
[mysqld]
skip-name-resolve
datadir=/var/lib/mysql
innodb_checksum_algorithm=innodb
innodb_log_checksum_algorithm=innodb
innodb_data_file_path=ibdata1:2G:autoextend
innodb_log_files_in_group=4
innodb_log_file_size=1073741824
innodb_page_size=4096
innodb_log_block_size=512
innodb_undo_tablespaces=0
```
- 6) Load image with innobackupex
```
innobackupex --defaults-file=/etc/my.cnf --move-back /root/xtrabackuptmp/
```
The image is successfully loaded if you see "completed OK!", as shown below:
 ![](//mccdn.qcloud.com/static/img/f109ca176fe161dc145863fa4808d93f/image.png)
- 7) Start Database
```
chmod 777 -R /var/lib/mysql
service start mysql
```
*Note: If you fail to start the database, you need to check and fix the error, and then try again*

- 8) Connect the database to check data
After starting the database, you may need to connect the database with the original account and password to view data.

