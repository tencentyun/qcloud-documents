
本文为您介绍 Oracle 增量同步至 TBase 的相关配置操作。

## 配置 Oracle 源端
### 数据库版本
Oracle 数据库须为11.2.0.4、12.1.0.2或以上版本。
Oracle 数据库需启用 XStream 功能，通过 v$option 命令查询，若 parameter 下 XStream 的 value 值是 true，即为已启用。

### 步骤1：启用 XStream 功能
1. 在命令行工具中执行以下命令，以数据库管理员连接到数据库。
```
#登录数据库系统用户，设置 SID
export  ORACLE_SID=orcl
#登录数据库
sqlplus / as sysdba 
```
2. 执行以下命令开启 XStream。
```
alter  system set  enable_goldengate_replication=true;
```   
 
### 步骤2：配置 Oracle Stream Pool
Oracle Streams Pool 是 Oracle Streams 使用的 System Global Area（SGA）的一部分内存。此部分内存用于 capture，apply，XStream outbound server，也用于缓存缓冲队列的信息。如果使用自动内存管理机制，系统将根据负载自动调整 stream_pool_size 大小，建议手动指定大小，参考如下:
- SGA 小于32GB：stream_pool_size = 4G
- SGA 为32GB - 64GB：stream_pool_size = 8G
- SGA 大于64GB：stream_pool_size = 5%SGA - 20%SGA

### 步骤3：开启数据库归档
1. 设置数据归档路径（如已开启，可忽略此操作）。
```
alter system set db_recovery_file_dest_size=100G; #设置归档区域大小（假设归档存放在闪回区）
alter system set db_recovery_file_dest='/arch’scope=spfile;   #设置归档路径
```
2. 开启日志归档（需重启数据库）。
```
SHUTDOWN IMMEDIATE    #停止数据库
STARTUP MOUNT   #启动到 mount 状态
ALTER DATABASE ARCHIVELOG; #开启数据库归档
ALTER DATABASE OPEN;    #打开数据库
```
3. 检查归档是否开启。
```
SQL> ARCHIVE LOG LIST   #检查归档是否开启
Database log mode              Archive Mode
Automatic archival             Enabled
```
当回显打印“Database log  mode:ArchiveMode”，即说明日志归档已开启。

### 步骤4：创建用户并授权
  1. 创建 XStream 管理员用户并配置权限。
    - 非 CDB 环境
```
 #创建表空间，指定大小
CREATE TABLESPACE xstream_tbs DATAFILE '/usr/oracle/dbs/xstream_tbs.dbf'   SIZE 25M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED;

#创建用户并指定表空间
CREATE USER xstrmadmin IDENTIFIED BY password   DEFAULT TABLESPACE xstream_tbs  QUOTA UNLIMITED ON xstream_tbs;

#授予连接权限
GRANT CREATE SESSION TO xstrmadmin; 

#授予 XStream 管理员权限
BEGIN 
DBMS_XSTREAM_AUTH.GRANT_ADMIN_PRIVILEGE( 
grantee => 'xstrmadmin', 
privilege_type => 'CAPTURE', 
grant_select_privileges => TRUE); 
END;

#授予对象访问权限
GRANT CREATE SESSION TO  xstrmadmin;
GRANT SELECT ON V_$DATABASE to xstrmadmin;
GRANT FLASHBACK ANY TABLE TO xstrmadmin;
GRANT SELECT ANY TABLE to xstrmadmin;
GRANT LOCK ANY TABLE TO xstrmadmin;
Grant select_catalog_role to xstrmadmin;
```
    - CDB 环境
    ```
#登录数据库
sqlplus / as sysdba

#切换到 cdb 下
alter session set container=CDB$ROOT;

#创建表空间，指定大小
CREATE TABLESPACE xstream_tbs DATAFILE '/usr/oracle/dbs/xstream_tbs.dbf'   SIZE 25M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED;

#创建用户并指定表空间
CREATE USER c##xstrmadmin IDENTIFIED BY password DEFAULT TABLESPACE xstream_tbs QUOTA UNLIMITED ON xstream_tbs CONTAINER=ALL;

#授予连接权限
GRANT CREATE SESSION, SET CONTAINER TO c##xstrmadmin CONTAINER=ALL; 

#授予 XStream 管理员权限
BEGIN 
DBMS_XSTREAM_AUTH.GRANT_ADMIN_PRIVILEGE( 
grantee => 'c##xstrmadmin', 
privilege_type => 'CAPTURE', 
grant_select_privileges => TRUE, 
container => 'ALL'); 
END

#授予对象访问权限
GRANT CREATE SESSION TO  c##xstrmadmin;
GRANT SELECT ON V_$DATABASE to c##xstrmadmin;
GRANT FLASHBACK ANY TABLE TO c##xstrmadmin;
GRANT SELECT ANY TABLE to c##xstrmadmin;
GRANT LOCKANYTABLE TO c##xstrmadmin;
Grant select_catalog_role to c##xstrmadmin;
    ```
  2. 修改日志记录参数。
    ```
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY, UNIQUE, FOREIGN KEY) COLUMNS;
```


## 配置 TBase 目标端
创建同步的用户名和模式。   
```
#创建用户
create user dbbridge password  ‘dbbridge';
#创建模式
create schema dbbridge;
#将模式归属于新建用户
alter schema dbbridge owner to dbbridge;
#授权用户在该模式下所有表的所有操作权限
grant all privileges on all tables  in schema dbbridge to dbbridge;
```
  
## Oracle 数据同步至 TBase
Oracle 源端和 TBase 目标端配置完成后，可参考 [DTS-DBbridge 使用流程](https://cloud.tencent.com/document/product/571/45866#.E4.BD.BF.E7.94.A8.E6.B5.81.E7.A8.8B) 进行后续数据同步操作。
