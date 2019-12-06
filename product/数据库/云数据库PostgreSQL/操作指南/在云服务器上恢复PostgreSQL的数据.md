## 通过控制台下载备份进行恢复
### 1. 创建恢复目录
```
mkdir recovery
```
>?recovery 为示例目录，用户可自行修改恢复目录。

### 2. 下载全量备份文件
登录 [PostgreSQL 控制台](https://console.cloud.tencent.com/pgsql)，在实例列表单击操作列的【管理】进入管理页面，选择【备份管理】页，获取您所需的备份文件下载地址。（服务器需与数据库处于同一网络中）
![](https://mc.qcloudimg.com/static/img/a5de09aeecb4bf1d9ce20423c0c8ddd5/1.png)

### 3. 解压全量备份文件
执行如下命令解压全量备份文件：
```
tar zxf 20170905010143.tar.gz –C recovery
```
解压后如下图：
![](https://mc.qcloudimg.com/static/img/c946fa0b44be183d6fcdfbffb1815d33/2.png)

### 4.（可选）安装相同版本的 PostgreSQL
如已安装可跳过此步骤，本示例采用 yum 源的安装方式，yum 源可至 [该地址](https://yum.postgresql.org/) 查找您所需要的版本。
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

### 5. 修改配置文件
将配置文件`postgresql.conf`中的以下选项注释掉，注释方法：在行首使用#。
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

### 6. 更改文件夹权限
```
chmod 0700 recovery
```
修改后如下图：
![](https://mc.qcloudimg.com/static/img/a0322a623ad657307be8a88ab54fd7b9/3.png)

### 7.（可选）应用增量备份文件
如果跳过该步骤，则数据库的内容为开始做全量备份时数据库的内容。
>?将 xlog 文件放入 pg_xlog 文件夹下，pg 会自动重放 xlog 日志。例如12:00时做的全量备份，如果在该全量备份的基础上，在 pg_xlog 文件夹下放置12:00至13:00的所有 xlog，则数据库能恢复到13:00时的数据内容。
>
下载增量备份文件（xlog）：
![](https://mc.qcloudimg.com/static/img/775b3a63d1fa37e1815ab13c100f8b40/4.png)
解压在 pg_xlog 文件夹下：
```
tar zxf 20170904010214_20170905010205.tar.gz
```
![](https://mc.qcloudimg.com/static/img/751212c370c884d1510651c257517760/8.png)

### 8. 启动数据库
```
pg_ctl start -D ~/recovery
```
![](https://mc.qcloudimg.com/static/img/88a7a4e59cf9e349aca7212c78799461/9.png)

### 9.	登录验证
登录数据库：
![](https://mc.qcloudimg.com/static/img/54440cf9ce9f77672b27a0e4a71a1bd7/10.png)
验证数据库是否运行：
![](https://mc.qcloudimg.com/static/img/475867ab40e84bba76ba175d396c7670/11.png)


## 通过手动导出数据进行恢复
您也可以手动导出备份数据，然后在腾讯云云服务器上进行恢复操作，该方案在 Windows 和 Linux 下同样适用，与物理文件所在的文件系统无关。

1. 在云服务器下 dump 出数据，多个库时使用 pg_dumpall，示例如下：
```
pg_dump -h 10.20.3.7 -p 5432 -Utera   -f tera.sql -c -C postgres
```
 - 不指定文件格式时，默认导出的文件为文本文件，文件形式如下：
```
-- PostgreSQL database dump
--
-- Dumped from database version 9.5.4
-- Dumped by pg_dump version 9.5.19
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;
```
 - 若数据较大，可通过 -Fc 指定为二进制文件。
2. 在云服务器上恢复数据。
 - 文本文件，可直接通过执行 sql 语句恢复，示例如下：
```
psql -U postgres <./tera.sql
```
>?因为有 pg_stat_error 等插件，可能会导致报错，但不影响数据导入。
 - 二进制文件，需要用 pg_restore 还原。
