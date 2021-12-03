
## 通过控制台下载备份进行恢复
### 1. 安装 PostgreSQL 数据库
在待恢复数据的云服务器 CVM 中，安装与备份数据相同版本的 PostgreSQL 数据库，如已安装可跳过此步骤。
>?本文以在 CentOS 7 操作系统的云服务器中，安装 PostgreSQL 10 版本数据库并恢复数据为例。
>
1. 登录 Linux 系统的云服务器，请参见 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 安装 PostgreSQL 数据库，本文采用 yum 源的安装方式，yum 源可至 [该地址](https://yum.postgresql.org/) 查找所需版本。
>?如果您需要恢复 11.8 或者 12.4 版本，建议安装同版本的数据库，请更改安装包中的版本号，如`postgresql10-server`修改为`postgresql11-server`或者`postgresql12-server`。
>
执行如下命令，安装 PostgreSQL 10 版本。
```
yum install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
yum install postgresql10-server postgresql10-contrib postgresql10 postgresql10.x86_64
```
>?PostgreSQL 9.5 版本安装命令如下：
>```
yum install https://yum.postgresql.org/9.5/redhat/rhel-7.6-x86_64/pgdg-centos95-9.5-3.noarch.rpm
yum install postgresql95-server postgresql95-contrib postgresql95
```
3. 执行如下命令，查看安装结果。
```
rpm -aq| grep postgres
```
可返回如下类似信息：
```
[root@i-87-575-VM vmuser]# rpm -aq| grep postgres
postgresql10-libs-10.11-2PGDG.rhel7.x86_64
postgresql10-server-10.11-2PGDG.rhel7.x86_64
postgresql10-contrib-10.11-2PGDG.rhel7.x86_64
postgresql10-10.11-2PGDG.rhel7.x86_64
```

### 2. 使用 postgres 用户创建恢复目录
切换为 postgres 用户，在云服务器中创建恢复目录。
```
mkdir /var/lib/pgsql/10/recovery
```
其中，recovery 为示例目录，用户可自行修改恢复目录。后续示例中不同版本目录名将不再区分描述，请以实际为准，如PostgreSQL 10.x 均为`/var/lib/pgsql/10`，PostgreSQL 9.5.x 均为`/var/lib/pgsql/9.5`。
>?PostgreSQL 9.5 版本命令如下：
```
mkdir /var/lib/pgsql/9.5/recovery
```

### 3. 下载全量备份文件
1. 登录 [PostgreSQL 控制台](https://console.cloud.tencent.com/pgsql)，在实例列表，单击**操作**列的**管理**进入管理页面。
2. 选择**备份管理**页，在备份列表中，根据备份时间选择需要恢复的备份版本，单击**操作**列的**下载**。
3. 根据提供的 VPC 网络地址或外网地址链接下载备份文件。
>?
>- 使用 VPC 网络地址下载备份时，云数据库须与云服务器处于同一 VPC，备份需下载至`/var/lib/pgsql/10/recovery`目录。
>- 使用外网地址下载备份时，下载后需将备份文件上传至云服务器中的`/var/lib/pgsql/10/recovery`目录，请参见 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
>
上传完示例如下：
![](https://main.qcloudimg.com/raw/e450c3acbab7f0c18560accbe7085184.png)

### 4. 解压全量备份文件
执行如下命令，解压全量备份文件。
```
cd /var/lib/pgsql/10/recovery
tar -xf 20191221010146.tar.gz
```
解压后如下图：
![](https://main.qcloudimg.com/raw/c5849130653dbf20598fc2edc75703a2.png)

### 5. 删除多余的临时文件
执行如下命令，删除多余的临时文件。
```
rm -rf backup_label
```

### 6. 修改配置文件
1. 将配置文件`postgresql.conf`中的以下选项注释掉，注释方法：在行首使用#。
如有多个该选项，则全部注释掉。
```
shared_preload_libraries
local_preload_libraries
pg_stat_statements.max
pg_stat_statements.track
archive_mode
archive_command
synchronous_commit
synchronous_standby_names
```
>?如果恢复版本为 PostgreSQL 12.4，还需要注释 `include = 'standby.conf'` 这一行。
2. 修改配置文件`postgresql.conf`。
```
port = '5432'    ##将port参数的值修改为5432
unix_socket_directories = '/var/run/postgresql/'  ##将unix_socket_directories的值修改为/var/run/postgresql/，如未设置此值，可跳过此项
```
3. 在`postgresql.conf`文件末尾追加配置，表示不再使用强同步模式。
```
synchronous_commit = local
synchronous_standby_names = ''
```

### 7. 使用 root 用户更改文件夹权限
```
chmod 0700 /var/lib/pgsql/10/recovery
chown postgres:postgres /var/lib/pgsql/10/recovery -R
```
修改后如下图：
![](https://main.qcloudimg.com/raw/ad8fe68e68c55f9b3165cbd9744656a7.png)

### 8.（可选）应用增量备份文件
如跳过该步骤，则数据库的内容为开始做全量备份时数据库的内容。
将 xlog 文件放入`/var/lib/pgsql/10/recovery/pg_wal`文件夹下，如下载的备份中不包含`pg_wal`目录，请将`pg_xlog`目录修改为`pg_wal`，pg 会自动重放 xlog 日志。
例如12:00时做的全量备份，如果在该全量备份的基础上，在`pg_wal`文件夹下放置12:00至13:00的所有 xlog，则数据库能恢复到13:00时的数据内容。
>?PostgreSQL 版本为 9.x 时，则为`/var/lib/pgsql/9.x/recovery/pg_xlog`文件夹。
>

1. 在控制台【备份管理】页，获取 xlog 下载地址，下载增量备份文件（xlog）。
下载后如下图：
![](https://main.qcloudimg.com/raw/2f7bc19401dc01363de4df37d9624536.png)
2. 解压日志至`pg_wal`文件夹。
```
tar -xf 20170904010214_20170905010205.tar.gz
```
![](https://main.qcloudimg.com/raw/acd7311a8434305dc252e8fe4475c600.png)

### 9. 使用 postgres 用户启动数据库
```
/usr/pgsql-10/bin/pg_ctl start -D /var/lib/pgsql/10/recovery
```
![](https://main.qcloudimg.com/raw/33f99c711355ecb9c400b80a27214e66.png)

### 10.	登录数据库验证
1. 登录 PostgreSQL  数据库。
```
export PGDATA=/var/lib/pgsql/10/recovery
psql
```
![](https://main.qcloudimg.com/raw/bcc5757ce2bca7246601e22d3714d3af.png)
2. 验证数据库是否运行。
```
/usr/pgsql-10/bin/pg_ctl status -D /var/lib/pgsql/10/recovery
```
如提示"server is running"，则代表数据库正在运行。
![](https://main.qcloudimg.com/raw/52466f7ac534d4d27863868a739a1647.png)

## 通过手动导出数据进行恢复
您也可以手动导出备份数据，然后在腾讯云云服务器上进行恢复操作，该方案在 Windows 和 Linux 下同样适用，与物理文件所在的文件系统无关。

1. 在云服务器下 dump 出数据，示例如下：
```
命令格式为：pg_dump -h <访问IP> -U <访问用户> -f <备份文件全路径> -c -C <导出的数据库名>
Example:
/usr/pgsql-10/bin/pg_dump -h 192.168.0.16 -U testroot -f backup.sql -c -C postgres
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
psql -U postgres <./backup.sql
```
>?因为有 pg_stat_error 等插件，可能会导致报错，但不影响数据导入。
 - 二进制文件，需要用 pg_restore 还原。
