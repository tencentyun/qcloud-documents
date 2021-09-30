


Oracle 中的 PROFILE 可以用于对用户所能使用的数据库资源进行限制。

TDSQL PostgreSQL版（Oracle 兼容）兼容 PROFILE 用法。

## 语法
创建 PROFILE：
```
CREATE PROFILE profile
LIMIT { resource_parameters
  | password_parameters
  }
    [ resource_parameters
    | password_parameters
    ]... ;
     
<resource_parameters> 
{ { SESSIONS_PER_USER
  | CPU_PER_SESSION
  | CPU_PER_CALL
  | CONNECT_TIME
  | IDLE_TIME
  | LOGICAL_READS_PER_SESSION
  | LOGICAL_READS_PER_CALL
  | COMPOSITE_LIMIT
  }
  { integer | UNLIMITED | DEFAULT }
| PRIVATE_SGA
  { integer [ K | M ] | UNLIMITED | DEFAULT }
}
     
< password_parameters >
{ { FAILED_LOGIN_ATTEMPTS
  | PASSWORD_LIFE_TIME
  | PASSWORD_REUSE_TIME
  | PASSWORD_REUSE_MAX
  | PASSWORD_LOCK_TIME
  | PASSWORD_GRACE_TIME
  }
  { expr | UNLIMITED | DEFAULT }
| PASSWORD_VERIFY_FUNCTION
  { function | NULL | DEFAULT }
}
```
    
profile 分配给用户：
```
ALTER USER user_name PROFILE profile_name;
```
    
删除 profile：
```
DROP PROFILE profile_name;
```
    
## 示例
```
cpu_per_call limit
postgres=# create profile app_user limit
   sessions_per_user 10
   cpu_per_session 1000
   cpu_per_call 100
   connect_time 100
   logical_reads_per_session 1000
   logical_reads_per_call 1000
   composite_limit 5000000
   Idle_Time 1000
   private_sga 1000
   failed_login_attempts 5 
   password_life_time 1 
   password_reuse_time 2 
   password_reuse_max 5 
   password_lock_time 0.042 
   password_grace_time 0.042;
CREATE PROFILE
postgres=# ALTER RESOURCE COST CPU_PER_SESSION 3 CONNECT_TIME 3 private_sga 2 LOGICAL_READS_PER_SESSION 2; 
ALTER RESOURCE COST
postgres=# create user cpu_call password '123';
CREATE ROLE
postgres=# create profile profile_cpu_call limit cpu_per_call 10;
CREATE PROFILE
postgres=# alter user cpu_call profile profile_cpu_call;
ALTER ROLE
postgres=# \c - cpu_call
You are now connected to database "postgres" as user "cpu_call".
postgres=> create table bb(id int,name varchar(20));
ERROR:  node:dn001, backend_pid:13359, nodename:dn002,backend_pid:20303,message:exceeded call limit on CPU usage
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user cpu_call;
drop profile profile_cpu_call;DROP ROLE
postgres=# drop profile profile_cpu_call;
DROP PROFILE
    
cpu_per_session limit
postgres=# create user cpu_session password '123';
CREATE ROLE
postgres=# create profile profile_cpu_session limit cpu_per_session 10;
CREATE PROFILE
postgres=# alter user cpu_session profile profile_cpu_session;
ALTER ROLE
postgres=# \c - cpu_session
You are now connected to database "postgres" as user "cpu_session".
postgres=> create table bb(id int,name varchar(20));
\c - tbase
drop user cpu_session;
drop profile profile_cpu_session;
FATAL:  node:dn002, backend_pid:21503, nodename:dn001,backend_pid:14480,message:exceeded session limit on CPU usage, you are being logged off
server closed the connection unexpectedly
This probably means the server terminated abnormally
before or while processing the request.
The connection to the server was lost. Attempting reset: Succeeded.
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user cpu_session;
DROP ROLE
postgres=# drop profile profile_cpu_session;
DROP PROFILE
postgres=# 
    
logical_reads_per_session limit
postgres=# \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# create user blk_session password '123';
alter user blk_session profile profile_blk_session;
CREATE ROLE
postgres=# create profile profile_blk_session limit logical_reads_per_session 10;
\c - blk_session
CREATE PROFILE
postgres=# alter user blk_session profile profile_blk_session;
create table bb(id int,name varchar(20));
ALTER ROLE
postgres=# \c - blk_session
You are now connected to database "postgres" as user "blk_session".
postgres=> create table bb(id int,name varchar(20));
\c - tbase
drop user blk_session;
drop profile profile_blk_session;
FATAL:  node:dn002, backend_pid:25880, nodename:dn001,backend_pid:18543,message:exceeded session limit on IO usage, you are being logged off
server closed the connection unexpectedly
This probably means the server terminated abnormally
before or while processing the request.
The connection to the server was lost. Attempting reset: Succeeded.
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user blk_session;
DROP ROLE
postgres=# drop profile profile_blk_session;
DROP PROFILE
postgres=# 
    
logical_reads_per_call limit
postgres=# \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# create user blk_call password '123';
alter user blk_call profile profile_blk_call;
CREATE ROLE
postgres=# create profile profile_blk_call limit logical_reads_per_call 10;
CREATE PROFILE
postgres=# alter user blk_call profile profile_blk_call;
\c - blk_call
create table bb(id int,name varchar(20));
ALTER ROLE
postgres=# \c - blk_call
You are now connected to database "postgres" as user "blk_call".
postgres=> create table bb(id int,name varchar(20));
\c - tbase
drop user blk_call;
drop profile profile_blk_call;ERROR:  node:dn001, backend_pid:19447, nodename:dn002,backend_pid:26821,message:exceeded call limit on IO usage
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user blk_call;
DROP ROLE
postgres=# drop profile profile_blk_call;
DROP PROFILE
    
composite_limit limit
postgres=# \c - tbase
create user composite password '123';
create profile profile_composite limit composite_limit 10;
You are now connected to database "postgres" as user "tbase".
postgres=# create user composite password '123';
alter user composite profile profile_composite;
CREATE ROLE
postgres=# create profile profile_composite limit composite_limit 10;
\c - composite
create table bb(id int,name varchar(20));
CREATE PROFILE
postgres=# alter user composite profile profile_composite;
ALTER ROLE
postgres=# \c - composite
\c - tbase
drop user composite;
You are now connected to database "postgres" as user "composite".
postgres=> create table bb(id int,name varchar(20));
drop profile profile_composite;
FATAL:  node:dn002, backend_pid:27700, nodename:dn001,backend_pid:20266,message:exceeded COMPOSITE_LIMIT, you are being logged off
server closed the connection unexpectedly
This probably means the server terminated abnormally
before or while processing the request.
The connection to the server was lost. Attempting reset: Succeeded.
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user composite;
DROP ROLE
postgres=# drop profile profile_composite;
DROP PROFILE
    
private_sga limit
postgres=# \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# create user sga password '123';
create profile profile_private_sga limit private_sga 10;
alter user sga profile profile_private_sga;
\c - sga
CREATE ROLE
postgres=# create profile profile_private_sga limit private_sga 10;
create table bb(id int,name varchar(20));
CREATE PROFILE
postgres=# alter user sga profile profile_private_sga;
\c - tbase
drop user sga;
ALTER ROLE
postgres=# \c - sga
You are now connected to database "postgres" as user "sga".
postgres=> create table bb(id int,name varchar(20));
drop profile profile_private_sga;FATAL:  node:dn001, backend_pid:21253, nodename:dn002,backend_pid:28723,message:exceeded private_sga, you are being logged off
server closed the connection unexpectedly
This probably means the server terminated abnormally
before or while processing the request.
The connection to the server was lost. Attempting reset: Succeeded.
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user sga;
DROP ROLE
postgres=# drop profile profile_private_sga;
DROP PROFILE
```
    
