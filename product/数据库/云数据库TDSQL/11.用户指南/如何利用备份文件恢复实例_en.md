MariaDB (TDSQL) can check the historical data using rollback feature. You can recover the historical data on your CVM as needed by following the steps in this document.
## 1. Prepare recovery environment
*Note: Make sure to use the CVM in the same basic network or VPC, to ensure the connectivity of network*
Basic configurations: CPU: 2-core or above; memory: 4 GB or above; disk space: it must exceed the space actually used by the database; operating system: the latest version of centos
Required basic environment: **For example, Mariadb 10.0.10**
Example of installation process:

- Add YUM source 
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

- Check whether the version of MariaDB for configuration of YUM source is 10.0.10
```
yum makecache
yum info MariaDB-server
```
- Install MariaDB-server
```
yum install MariaDB-server
```
*Note: If prompted that there is a conflict with the previous version, you need to delete the previous installation package, for example: `yum remove mariadb-libs`*

- Install MariaDB client
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


## 2. Download backup
First, acquire the download address of a backup in **"Tencent Cloud Console -> Cloud Database -> Console -> Backup and Recovery"**
![](//mccdn.qcloud.com/static/img/c3d9a2815d8039c37af9dd31ff7c0853/image.png)

**Download command example**
```
wget  --content-disposition ' http://169.254.0.27:8083/2/noshard1/set_1464144850_587/1464552298xxxxxxxx'
```

## 3. Recover backup file
- 1) Enter the download directory of a backup file, and decompress the cold backup file using LZ4
```
lz4 -d set_1464144850_587.1464552298.xtrabackup.lz4
```
- 2) Use xbstream tool to decompress the file to a temporary directory "xtrabackuptmp"
```
mkdir xtrabackuptmp/
mv set_1464144850_587.1464552298.xtrabackup xtrabackuptmp/
xbstream -x < set_1464144850_587.1464552298.xtrabackup
```
After the decompression, the directory and files are shown below:
 ![](//mccdn.qcloud.com/static/img/6f1d1aaf1ce9061cba0e09e4e47c271d/image.png)
- 3) Apply log
Use innobackupex for log application
```
mkdir /root/dblogs_tmp
innobackupex --apply-log  --use-memory=1G --tmpdir='/root/dblogs_tmp/' /root/xtrabackuptmp/
```
When the operation is successful, a message indicating "completed OK!" is shown as follows:
![](//mccdn.qcloud.com/static/img/4f43de6b03bf4456975105a8567d81a9/image.png)

- 4) Stop the database, and clear up the data files
Stop the database
```
service mysql stop
```
Clear up the data files
```
mkdir /var/lib/mysql-backup
mv /var/lib/mysql/* /var/lib/mysql-backup
```

- 5) Modify the database's parameter file `(/etc/my.cnf.d/server.cnf)`. Specific parameters can be found in the step "Parameters of decompressed backup-my.cnf":
*Note: The parameter file cannot be directly replaced with backup-my.cnf.*
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
- 6) Use innobackupex to load image
```
innobackupex --defaults-file=/etc/my.cnf --move-back /root/xtrabackuptmp/
```
When the operation is successful, a message indicating "completed OK!" is shown as follows:
 ![](//mccdn.qcloud.com/static/img/f109ca176fe161dc145863fa4808d93f/image.png)
- 7) Launch the database
```
chmod 777 -R /var/lib/mysql
service start mysql
```
*Note: In case of a launch failure, you need to check the error message and re-launch the database after restoring*

- 8) Connect the database to check data
After database startup, you need to view the data by connecting the database with the original account name and password.

