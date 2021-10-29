## 操作场景

PostgreSQL 是一个开源对象关系型数据库管理系统，并侧重于可扩展性和标准的符合性。PostgreSQL 面向企业复杂 SQL 处理的 OLTP 在线事务处理场景，支持 NoSQL 数据类型（JSON/XML/hstore），支持 GIS（Geographic Information System 或 Geo－Information system）地理信息处理，在可靠性、数据完整性方面有良好声誉，适用于互联网网站、位置应用系统、复杂数据对象处理等应用场景。

本文指导您在 CentOS 7 操作系统的云服务器实例上搭建 PostgreSQL。

## 示例软件版本
本文搭建的 PostgreSQL 组成及版本使用说明如下：
Linux：Linux 操作系统，本文以 CentOS 7.6 为例。
PostgreSQL：关系型数据库管理系统，本文以 PostgreSQL 11.2 为例。


## 前提条件
- 已创建两台云服务器实例（一台云服务器实例作为主节点，另一台云服务器实例作为从节点）。
具体步骤请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 新建的两台云服务器实例已配置安全组规则：放通5432端口。
具体步骤请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。

## 操作步骤

### 配置主节点

1. 登录主节点实例。
2. 执行以下命令，升级所有包、系统版本和内核。
```
yum update -y
```
3. 执行以下命令，安装 PostgreSQL 存储库。
```
yum install https://download.postgresql.org/pub/repos/yum/reporpms/EL-6-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```
4. 执行以下命令，安装客户端包。
```
yum install postgresql11
```
5. 执行以下命令，安装服务器包。
```
yum install postgresql11-server
```
6. 执行以下命令，初始化数据库。
```
/usr/pgsql-11/bin/postgresql-11-setup initdb
```
7. 执行以下命令，启动服务。
```
systemctl start postgresql-11
```
8. 执行以下命令，设置服务开机自启动。
```
systemctl enable postgresql-11
```
9. 执行以下命令，登录 postgres 用户。
```
su - postgres
```
10. 执行以下命令，进入 PostgreSQL 交互终端。
```
psql
```
11. 执行以下命令，为用户 postgres 设置密码，增强安全性。
```
ALTER USER postgres WITH PASSWORD '自定义密码';
```
12. 执行以下命令，创建数据库账号（例如 `postuser`），并设置密码及登录权限和备份权限。
```
create role 账户名 login replication encrypted password '自定义密码';
```
例如，创建一个数据库账号，其账户名为 `postuser`，密码为 `postuser`，则执行以下命令：
```
create role postuser login replication encrypted password 'postuser';
```
13. 执行以下命令，查询账号是否创建成功。
```
SELECT usename from pg_user;
```
返回如下结果，表示已创建成功。
```
usename  
 ----------
postgres
postuser
(2 rows)
```
14. 执行以下命令，查询权限是否创建成功。
```
SELECT rolname from pg_roles;
```
返回如下结果，表示已创建成功。
```
rolname  
 ----------
postgres
postuser
(2 rows)
```
15. 输入 **\q**，按 **Enter**，退出 SQL 终端。
16. 输入 **exit**，按 **Enter**，退出 PostgreSQL。
17. 执行以下命令，打开 `pg_hba.conf` 配置文件。
```
vim /var/lib/pgsql/11/data/pg_hba.conf
```
18. 按 **i** 切换至编辑模式，在 `IPv4 local connections` 段添加如下两行内容：
```
host    all             all             <从节点的 VPC IPv4 网段>          md5     #允许 VPC 网段中 md5 密码认证连接
host    replication     数据库账号        <从节点的 VPC IPv4 网段>        md5     #允许用户从 replication 数据库进行数据同步
```
例如，数据库账号为 `postuser`，从节点的 VPC IPv4 网段为 `192.10.0.0/16`，则在 `IPv4 local connections` 段添加如下内容：
```
host    all             all             192.10.0.0/16          md5
host    replication     postuser        192.10.0.0/16          md5
```
19. 按 **Esc**，输入 **:wq**，保存文件返回。
20. 执行以下命令，打开 `postgresql.conf` 文件。
```
vim /var/lib/pgsql/11/data/postgresql.conf
```
21. 按 **i** 进入编辑模式，分别找到以下参数，并将参数修改为以下内容：
```
listen_addresses = 'xxx.xxx.xxx.xxx'   #监听的内网 IP 地址
max_connections = 100    #最大连接数，从库的 max_connections 必须要大于主库的
wal_level = hot_standby  #启用热备模式
synchronous_commit = on  #开启同步复制
max_wal_senders = 32     #同步最大的进程数量
wal_sender_timeout = 60s #流复制主机发送数据的超时时间
```
22. 按 **Esc**，输入 **:wq**，保存文件返回。
23. 执行以下命令，重启服务。
```
systemctl restart postgresql-11
```

### 配置从节点

1. 登录从节点实例。
2. 执行以下命令，升级所有包、系统版本和内核。
```
yum update -y
```
3. 执行以下命令，安装 PostgreSQL 存储库。
```
yum install https://download.postgresql.org/pub/repos/yum/reporpms/EL-6-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```
4. 执行以下命令，安装客户端包。
```
yum install postgresql11
```
5. 执行以下命令，安装服务器包。
```
yum install postgresql11-server
```
6. 执行以下命令，使用 pg_basebackup 基础备份工具制定备份目录。
```
pg_basebackup -D /var/lib/pgsql/11/data -h 主节点的内网 IP -p 5432 -U 数据库账号 -X stream -P
```
例如，主节点的内网 IP 为 `192.10.123.321`，数据库账号为 `postuser`，则执行以下命令：
```
pg_basebackup -D /var/lib/pgsql/11/data -h 192.10.123.321 -p 5432 -U postuser -X stream -P
```
根据提示，输入数据库账号对应的密码，按 **Enter**。返回如下结果，表示备份成功。
```
Password: 
24526/24526 kB (100%), 1/1 tablespace
```
7. 执行以下命令，拷贝 master 配置相关文件。
```
cp /usr/pgsql-11/share/recovery.conf.sample /var/lib/pgsql/11/data/recovery.conf
```
8. 执行以下命令，打开 `recovery.conf` 文件。
```
vim /var/lib/pgsql/11/data/recovery.conf
```
9. 按 **i** 切换至编辑模式，分别找到如下参数，并修改为如下内容：
```
standby_mode = on     #声明此节点为从库
primary_conninfo = ‘host=<主节点内网 IP> port=5432 user=数据库账号 password=数据库密码’ #对应主库的连接信息
recovery_target_timeline = ‘latest’ #流复制同步到最新的数据
```
10. 按 **Esc**，输入 **:wq**，保存文件返回。
11. 执行以下命令，打开 `postgresql.conf` 文件。
```
vim /var/lib/pgsql/11/data/postgresql.conf
```
12. 按 **i** 切换至编辑模式，分别找到如下参数，并修改为如下内容：
```
listen_addresses= 'xxx.xx.xx.xx'   #监听的内网 IP 地址
max_connections = 1000             # 最大连接数，从库的 max_connections 必须要大于主库的
hot_standby = on                   # 开启热备
max_standby_streaming_delay = 30s  # 数据流备份的最大延迟时间
wal_receiver_status_interval = 1s  # 从节点向主节点报告自身状态的最长间隔时间
hot_standby_feedback = on          # 如果有错误的数据复制向主进行反馈
```
13. 按 **Esc**，输入 **:wq**，保存文件返回。
14. 执行以下命令，修改数据目录的属组和属主。
```
chown -R postgres.postgres /var/lib/pgsql/11/data
```
15. 执行以下命令，启动服务。
```
systemctl start postgresql-11
```
16. 执行以下命令，设置服务开机自启动。
```
systemctl enable postgresql-11
```

### 验证部署
您可以通过如下操作验证是否部署成功：
1. 在主节点中，执行以下命令，查看 sender 进程。
```
ps aux |grep receiver
```
返回如下结果，即表示可成功查看到 sender 进程。
![](https://main.qcloudimg.com/raw/d25daabc3d32c58237dd20d871e6852a.png)
2. 在从节点中，执行以下命令，查看 receiver 进程。
```
ps aux | grep receiver
```
返回如下结果，即表示可成功查看到 receiver 进程。
![](https://main.qcloudimg.com/raw/961283ed95a9640ba2121f5fafba2a7b.png)
3. 在主节点中，依次执行以下命令，进入 PostgreSQL 交互终端，在主库中查看从库状态。
```
su - postgres
```
```
psql
```
```
select * from pg_stat_replication;
```
返回如下结果，即表示可成功查看到从库状态。
![](https://main.qcloudimg.com/raw/c85b5324929a4bffddd92c9dce906d56.png)
4. 验证备库是否可以同步主库数据。
 1. 在主节点中，依次执行以下命令，进入 PostgreSQL 交互终端，在主库中创建一个库（如 `testdb` ）。
```
su - postgres
```
```
psql
```
```
create database testdb;
```
 2. 在从节点中，依次执行以下命令，进入 PostgreSQL 交互终端，查看备库是否可以同步。
```
su - postgres
```
```
psql
```
```
\l
```
返回如下结果，即表示可备库同步成功。
![](https://main.qcloudimg.com/raw/2912a3d9892665469bff1768c76c7ae9.png)


