# 7.1 Oracle到Tbase增量同步配置
## 7.1.1 Oracle源端配置
### 7.1.1.1 数据库版本要求
    Oracle数据库为11.2.0.4/12.1.0.2或以上版本。
    Oracle数据库需启用xstream功能，通过v$option查询到parameter为XStream的value值是true即为已启用。
### 7.1.1.2 启用Xstream功能
    1) 在命令行工具中执行以下命令以DBA管理用户连接到数据库。
			  #登陆数据库系统用户,设置SID
          export  ORACLE_SID=orcl
        #登陆数据库
         sqlplus / as sysdba 
				 
    2)	执行以下命令开启Xstream
        alter  system set  enable_goldengate_replication=true;
 
### 7.1.1.3 配置Oracle Stream Pool
       Oracle Streams Pool是Oracle Streams 使用的System Global Area(SGA) 的一部分内存。此部分内存用于capture，apply，XStream outbound server，也用于缓存缓冲队列的信息。如果使用自动内存管理机制,系统根据负载自动调整stream_pool_size大小,建议手工指定大小.参考如下:

          SGA<32G	           stream_pool_size=4G
					32G<SGA<64G	       stream_pool_size=4G
          SGA>64G	           stream_pool_size=5%~20%SGA

### 7.1.1.4  开启数据库归档
    1)	设置数据归档路径(如已开启，忽略操作)
          alter system set db_recovery_file_dest_size=100G; #设置归档区域大小(假设归档存放在闪回区)
		      alter system set db_recovery_file_dest='/arch’scope=spfile;   #设置归档路径
 
    2)	开启日志归档(需重启数据库)
          SHUTDOWN IMMEDIATE         #停止数据库
          STARTUP MOUNT              #启动到mount状态
          ALTER DATABASE ARCHIVELOG; #开启数据库归档
          ALTER DATABASE OPEN;       #打开数据库
    
         SQL> ARCHIVE LOG LIST         #检查归档是否开启
                 Database log mode              Archive Mode
                 Automatic archival             Enabled

         当回显打印“Database log  mode:ArchiveMode”,说明日志归档已开启。

### 7.1.1.5  创建用户并授权
    1)	创建XStream管理员用户并配置权限。
       非CDB环境
		      #创建表空间，指定大小
           CREATE TABLESPACE xstream_tbs DATAFILE '/usr/oracle/dbs/xstream_tbs.dbf'   SIZE 25M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED;

          #创建用户并指定表空间
           CREATE USER xstrmadmin IDENTIFIED BY password   DEFAULT TABLESPACE xstream_tbs  QUOTA UNLIMITED ON xstream_tbs;

          #授予连接权限
           GRANT CREATE SESSION TO xstrmadmin; 

          #授予xstream管理员权限
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
           GRANT select_catalog_role to xstrmadmin;

 
     CDB环境
         #登陆数据库
           sqlplus / as sysdba

         #切换到cdb下
           alter session set container=CDB$ROOT;

         #创建表空间，指定大小
           CREATE TABLESPACE xstream_tbs DATAFILE '/usr/oracle/dbs/xstream_tbs.dbf'   SIZE 25M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED;

         #创建用户并指定表空间
          CREATE USER c##xstrmadmin IDENTIFIED BY password DEFAULT TABLESPACE xstream_tbs QUOTA UNLIMITED ON xstream_tbs CONTAINER=ALL;

         #授予连接权限
          GRANT CREATE SESSION, SET CONTAINER TO c##xstrmadmin CONTAINER=ALL; 

         #授予xstream管理员权限
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
           GRANT select_catalog_role to c##xstrmadmin;

    2)	修改日志记录参数。
          ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY, UNIQUE, FOREIGN KEY) COLUMNS;

## 7.1.2 Tbase目标端配置
### 7.1.2.1  用户配置
      创建同步的用户名和模式
          
      #创建用户
        create user dbbridge password  'dbbridge';
        create schema dbbridge;
        alter schema dbbridge owner to dbbridge
      #授权限
        grant all privileges on all tables  in schema dbbridge to dbbridge;

