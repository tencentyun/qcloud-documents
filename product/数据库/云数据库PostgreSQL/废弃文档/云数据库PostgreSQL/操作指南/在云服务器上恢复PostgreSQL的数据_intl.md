### 1. Create a recovery directory
mkdir recovery
Note: recovery is only a sample directory, which can be replaced with your own directory.

### 2. Download the full backup file
Go to PostgreSQL management page - **Tencent Cloud Console** -> **Cloud Products** -> **Relational Database** -> **PostgreSQL Instance List** -> **Management** -> **Backup Management**, and click **Download** to get the download address of the backup file you need. (The server and the database must be in the same network)

![](https://mc.qcloudimg.com/static/img/a5de09aeecb4bf1d9ce20423c0c8ddd5/1.png)

### 3. Decompress the full backup file

Enter the command
```
tar zxf 20170905010143.tar.gz -C recovery
```
After decompressing, you get
![](https://mc.qcloudimg.com/static/img/c946fa0b44be183d6fcdfbffb1815d33/2.png)

### 4. Install posgresql of the same version (skip this step if it is already installed)
For example, in case of yum source installation, you can find an appropriate yum source in https://yum.postgresql.org/:

```
yum install http://yum.postgresql.org/9.3/RedHat/rhel-6-x86_64/pgdg-redhat93-9.3-1.noarch.rpm
 yum install postgresql93-server postgresql93-contrib
 
//Initialize
 service postgresql-9.3 initdb
 
Enable
 service postgresql-9.3 startor
 
/etc/init.d/postgresql-9.3 start
 
View the installation result
 
rpm -aq| grep postgres
 
You can see
 
[root@i-87-575-VM vmuser]# rpm -aq| grep postgres
 postgresql93-libs-9.3.4-1PGDG.rhel6.x86_64
 postgresql93-contrib-9.3.4-1PGDG.rhel6.x86_64
 postgresql93-9.3.4-1PGDG.rhel6.x86_64
 postgresql93-server-9.3.4-1PGDG.rhel6.x86_64
```

### 5. Modify the configuration file
Comment out the following options in the `postgresql.conf` configuration file (comment method: use # at the beginning of the line)
Comment all out if there is more than one such option.
```
shared_preload_libraries
local_preload_libraries
rds_extension_list.names
pg_stat_statements.max
pg_stat_statements.track
archive_mode
archive_command
Add the configuration to the end of the postgresql.conf file (indicating that strongsync mode is no longer used)
synchronous_commit = local
synchronous_standby_names = ''
```

### 6. Change folder permission
```
chmod 0700 recovery
 ```
It is modified as shown below
![](https://mc.qcloudimg.com/static/img/a0322a623ad657307be8a88ab54fd7b9/3.png)


### 7. Apply the incremental backup file [optional]
This is an optional step. If this step is skipped, the data of the database when the full backup starts will be used.
Note: If xlog file is put under the pg_xlog folder, pg will automatically replay xlog log. For example, if the full backup is done at 12:00 and all xlogs between 12:00 and 13:00 are put under the pg_xlog folder, the database can be restored to the one at 13:00.
Download the incremental backup file (xlog)
![](https://mc.qcloudimg.com/static/img/775b3a63d1fa37e1815ab13c100f8b40/4.png)


Decompress it to the pg_xlog folder
```tar zxf 20170904010214_20170905010205.tar.gz```
![](https://mc.qcloudimg.com/static/img/751212c370c884d1510651c257517760/8.png)

 
### 8. Start the database
```pg_ctl start -D ~/recovery```

![](https://mc.qcloudimg.com/static/img/88a7a4e59cf9e349aca7212c78799461/9.png)



### 9. Log in for verification

Log in

 ![](https://mc.qcloudimg.com/static/img/54440cf9ce9f77672b27a0e4a71a1bd7/10.png)

Verify whether the database is running

 ![](https://mc.qcloudimg.com/static/img/475867ab40e84bba76ba175d396c7670/11.png)



