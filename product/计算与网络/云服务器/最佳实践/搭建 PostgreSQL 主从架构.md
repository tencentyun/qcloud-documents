## 操作场景

PostgreSQL 是一个开源对象关系型数据库管理系统，并侧重于可扩展性和标准的符合性。PostgreSQL 面向企业复杂 SQL 处理的 OLTP 在线事务处理场景，支持 NoSQL 数据类型（JSON/XML/hstore），支持 GIS（Geographic Information System 或 Geo－Information system）地理信息处理，在可靠性、数据完整性方面有良好声誉，适用于互联网网站、位置应用系统、复杂数据对象处理等应用场景。

本文指导您在 CentOS 7 操作系统的云服务器实例上搭建 PostgreSQL。

## 示例软件版本
本文搭建的 PostgreSQL 组成及版本使用说明如下：
- Linux：Linux 操作系统，本文以 CentOS 7.6 为例。
- PostgreSQL：关系型数据库管理系统，本文以 PostgreSQL 9.6 为例。


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
3. 依次执行以下命令，安装 PostgreSQL。
本文以使用 PostgreSQL 9.6 版本为例，您可按需选择其他版本。
```
wget --no-check-certificate https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```
```
rpm -ivh pgdg-redhat-repo-latest.noarch.rpm
```
```
yum install postgresql96-server postgresql96-contrib -y
```
```
/usr/pgsql-9.6/bin/postgresql96-setup initdb
```
4. 执行以下命令，启动服务。
```
systemctl start postgresql-9.6.service
```
5. 执行以下命令，设置服务开机自启动。
```
systemctl enable postgresql-9.6.service 
```
6. 执行以下命令，登录 postgres 用户。
```
su - postgres
```
7. 执行以下命令，进入 PostgreSQL 交互终端。
```
psql
```
8. 执行以下命令，为用户 postgres 设置密码，增强安全性。
```
ALTER USER postgres WITH PASSWORD '自定义密码';
```
9. 执行以下命令，创建数据库账号，并设置密码及登录权限和备份权限。
```
create role 账户名 login replication encrypted password '自定义密码';
```
本文以创建数据库帐号 `replica`，密码 `123456` 为例，则执行以下命令。
```
create role replica login replication encrypted password '123456';
```
10. 执行以下命令，查询账号是否创建成功。
```
SELECT usename from pg_user;
```
返回如下结果，表示已创建成功。
```
usename  
----------
postgres
replica
(2 rows)
```
11. 执行以下命令，查询权限是否创建成功。
```
SELECT rolname from pg_roles;
```
返回如下结果，表示已创建成功。
```
rolname      
-------------------
pg_signal_backend
postgres
replica
(3 rows)
```
12. 输入 **\q**，按 **Enter**，退出 SQL 终端。
13. 输入 **exit**，按 **Enter**，退出 PostgreSQL。
14. 执行以下命令，打开 `pg_hba.conf` 配置文件，设置 `replica` 用户白名单。
```
vim /var/lib/pgsql/9.6/data/pg_hba.conf
```
15. 按 **i** 切换至编辑模式，在 `IPv4 local connections` 段添加如下两行内容：
```
host    all             all             <从节点的VPC IPv4网段>          md5     #允许 VPC 网段中 md5 密码认证连接
host    replication     replica         <从节点的VPC IPv4网段>          md5     #允许用户从 replication 数据库进行数据同步
```
例如，数据库账号为 `replica`，从节点的 VPC IPv4 网段为 `xx.xx.xx.xx/16`，则在 `IPv4 local connections` 段添加如下内容：
```
host    all             all             xx.xx.xx.xx/16         md5
host    replication     replica         xx.xx.xx.xx/16         md5
```
16. 按 **Esc**，输入 **:wq**，保存文件返回。
17. 执行以下命令，打开 `postgresql.conf` 文件。
```
vim /var/lib/pgsql/9.6/data/postgresql.conf
```
18. 按 **i** 进入编辑模式，分别找到以下参数，并将参数修改为以下内容：
```
listen_addresses = '*'   #监听的内网 IP 地址
max_connections = 100    #最大连接数，从库的 max_connections 必须要大于主库的
wal_level = hot_standby  #启用热备模式
synchronous_commit = on  #开启同步复制
max_wal_senders = 32     #同步最大的进程数量
wal_sender_timeout = 60s #流复制主机发送数据的超时时间
```
19. 按 **Esc**，输入 **:wq**，保存文件返回。
20. 执行以下命令，重启服务。
```
systemctl restart postgresql-9.6.service
```

### 配置从节点

1. 登录从节点实例。
2. 执行以下命令，升级所有包、系统版本和内核。
```
yum update -y
```
3. 依次执行以下命令，安装 PostgreSQL。
```
wget --no-check-certificate https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```
```
rpm -ivh pgdg-redhat-repo-latest.noarch.rpm
```
```
yum install postgresql96-server postgresql96-contrib -y
```
4. 执行以下命令，使用 pg_basebackup 基础备份工具制定备份目录。
```
pg_basebackup -D /var/lib/pgsql/9.6/data -h <主节点公网 IP> -p 5432 -U replica -X stream -P
```
根据提示，输入数据库账号对应的密码，按 **Enter**。返回如下结果，表示备份成功。
```
Password: 
24526/24526 kB (100%), 1/1 tablespace
```
5. 执行以下命令，拷贝 master 配置相关文件。
```
cp /usr/pgsql-9.6/share/recovery.conf.sample /var/lib/pgsql/9.6/data/recovery.conf
```
6. 执行以下命令，打开 `recovery.conf` 文件。
```
vim /var/lib/pgsql/9.6/data/recovery.conf
```
7. 按 **i** 切换至编辑模式，分别找到如下参数，并修改为如下内容：
```
standby_mode = on     #声明此节点为从库
primary_conninfo = 'host=<主节点公网 IP> port=5432 user=数据库账号 password=数据库密码' #对应主库的连接信息
recovery_target_timeline = 'latest' #流复制同步到最新的数据
```
8. 按 **Esc**，输入 **:wq**，保存文件返回。
9. 执行以下命令，打开 `postgresql.conf` 文件。
```
vim /var/lib/pgsql/9.6/data/postgresql.conf
```
10. 按 **i** 切换至编辑模式，分别找到如下参数，并修改为如下内容：
```
max_connections = 1000             # 最大连接数，从库的 max_connections 必须要大于主库的
hot_standby = on                   # 开启热备
max_standby_streaming_delay = 30s  # 数据流备份的最大延迟时间
wal_receiver_status_interval = 1s  # 从节点向主节点报告自身状态的最长间隔时间
hot_standby_feedback = on          # 如果有错误的数据复制向主进行反馈
```
11. 按 **Esc**，输入 **:wq**，保存文件返回。
12. 执行以下命令，修改数据目录的属组和属主。
```
chown -R postgres.postgres /var/lib/pgsql/9.6/data
```
13. 执行以下命令，启动服务。
```
systemctl start postgresql-9.6.service
```
14. 执行以下命令，设置服务开机自启动。
```
systemctl enable postgresql-9.6.service
```

### 验证部署
您可以通过如下操作验证是否部署成功：
1. 执行以下命令，从节点备份目录。
```
pg_basebackup -D /var/lib/pgsql/96/data -h <主节点公网 IP> -p 5432 -U replica -X stream -P
```
输入数据库密码并按 **Enter**，返回如下结果，则表示已备份成功。
```
Password: 
24526/24526 kB (100%), 1/1 tablespace
```
2. 在主节点中，执行以下命令，查看 sender 进程。
```
ps aux |grep sender
```
![](https://qcloudimg.tencent-cloud.cn/raw/bc610cf837b18158a8d0ddd89d5d87ae.png)
3. 在从节点中，执行以下命令，查看 receiver 进程。
```
ps aux |grep receiver
```
返回如下结果，即表示可成功查看到 receiver 进程。
![](https://qcloudimg.tencent-cloud.cn/raw/13c908ae7d83ff8d5099f2c488b40046.png)
4. 在主节点中，依次执行以下命令，进入 PostgreSQL 交互终端，在主库中查看从库状态。
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
![](https://qcloudimg.tencent-cloud.cn/raw/c38c6faf64af66188df0e944b335353a.png)

