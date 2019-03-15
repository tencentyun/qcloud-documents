### 1. 创建恢复目录
mkdir recovery
注: recovery 只是示例目录，用户可以自行修改为自己的目录。

### 2.	下载全量备份文件
进入 PostgreSQL 的管理页面——“腾讯云控制台>云产品>关系型数据库>PostgreSQL 实例列表>管理>备份管理”单击下载，获取您所需的备份文件下周地址。（服务器需与数据库处于同一网络中）

![](https://mc.qcloudimg.com/static/img/a5de09aeecb4bf1d9ce20423c0c8ddd5/1.png)

### 3.	解压全量备份文件

输入命令
```
tar zxf 20170905010143.tar.gz –C recovery
```
解压后得到
![](https://mc.qcloudimg.com/static/img/c946fa0b44be183d6fcdfbffb1815d33/2.png)

### 4. 安装相同版本的 posgresql（如已安装可跳过此步骤）
例如采用 yum 源的安装方式，yum 源可到 https://yum.postgresql.org/ 查找您所需要的版本：

```
yum install http://yum.postgresql.org/9.3/RedHat/rhel-6-x86_64/pgdg-redhat93-9.3-1.noarch.rpm
 yum install postgresql93-server postgresql93-contrib
 
//初始化
 service postgresql-9.3 initdb
 
开启
 service postgresql-9.3 start或者
 
/etc/init.d/postgresql-9.3 start
 
查看安装结果
 
rpm -aq| grep postgres
 
可以看到
 
[root@i-87-575-VM vmuser]# rpm -aq| grep postgres
 postgresql93-libs-9.3.4-1PGDG.rhel6.x86_64
 postgresql93-contrib-9.3.4-1PGDG.rhel6.x86_64
 postgresql93-9.3.4-1PGDG.rhel6.x86_64
 postgresql93-server-9.3.4-1PGDG.rhel6.x86_64
```

### 5.	配置文件修改
将配置文件`postgresql.conf`中的以下选项注释掉（注释方法：在行首使用#）
如有多个该选项，则全部注释掉。
```
shared_preload_libraries
local_preload_libraries
rds_extension_list.names
pg_stat_statements.max
pg_stat_statements.track
archive_mode
archive_command
在postgresql.conf文件末尾追加配置 （表示不再使用强同步模式）
synchronous_commit = local
synchronous_standby_names = ''
```

### 6.	更改文件夹权限
```
chmod 0700 recovery
 ```
修改后如下图
![](https://mc.qcloudimg.com/static/img/a0322a623ad657307be8a88ab54fd7b9/3.png)


### 7.	应用增量备份文件[可选]
该步骤为可选步骤，如果跳过该步骤，则数据库的内容为开始做全量备份时数据库的内容。
说明：将 xlog 文件放入 pg_xlog 文件夹下，pg 会自动重放 xlog 日志。例如12：00时做的全量备份，如果在该全量备份的基础上，在 pg_xlog 文件夹下放置 12：00 至 13：00 的所有 xlog，则数据库能恢复到 13：00 时的数据内容。
下载增量备份文件（xlog）
![](https://mc.qcloudimg.com/static/img/775b3a63d1fa37e1815ab13c100f8b40/4.png)


解压在 pg_xlog 文件夹下
```tar zxf 20170904010214_20170905010205.tar.gz```
![](https://mc.qcloudimg.com/static/img/751212c370c884d1510651c257517760/8.png)

 
### 8.	启动数据库
```pg_ctl start -D ~/recovery```

![](https://mc.qcloudimg.com/static/img/88a7a4e59cf9e349aca7212c78799461/9.png)



### 9.	登录验证

登录

 ![](https://mc.qcloudimg.com/static/img/54440cf9ce9f77672b27a0e4a71a1bd7/10.png)

数据库是否运行

 ![](https://mc.qcloudimg.com/static/img/475867ab40e84bba76ba175d396c7670/11.png)


