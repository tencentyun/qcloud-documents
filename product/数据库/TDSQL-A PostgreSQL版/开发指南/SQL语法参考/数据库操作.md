## 数据库创建
要创建一个数据库，必须是一个超级用户或者具有特殊的 CREATEDB 特权，默认情况下，新数据库将通过克隆标准系统数据库 template1 被创建。可以通过写 TEMPLATE name 指定一个不同的模板。通过写 TEMPLATE template0 您可以创建一个干净的数据库，它将只包含您的 TDSQL-A PostgreSQL版 所预定义的标准对象。

### 默认参数创建数据库
```
postgres=# CREATE DATABASE tdapg_db;
CREATE DATABASE
```

### 指定克隆库
```
postgres=# CREATE DATABASE tdapg_db_template TEMPLATE template0;
CREATE DATABASE
```

### 指定所有者
```
postgres=# CREATE ROLE pgxz WITH LOGIN;
CREATE ROLE
postgres=# CREATE DATABASE tdapg_db_owner OWNER pgxz;
CREATE DATABASE
postgres=# \l+ tdapg_db_owner
                         List of databases
   Name   | Owner | Encoding | Collate  |  Ctype  | Access privileges | Size | Tablespace | Description 
----------------+-------+----------+------------+------------+-------------------+-------+------------+-------------
 tdapg_db_owner | pgxz | UTF8   | en_US.utf8 | en_US.utf8 |          | 18 MB | pg_default | 
(1 row)
```

### 指定编码
```
postgres=# CREATE DATABASE tdapg_db_encoding ENCODING UTF8;  
CREATE DATABASE
postgres=# \l+ tdapg_db_encoding
                          List of databases
    Name    | Owner | Encoding | Collate  |  Ctype  | Access privileges | Size | Tablespace | Description 
-------------------+-------+----------+------------+------------+-------------------+-------+------------+-------------
 tdapg_db_encoding | dbadmin | UTF8   | en_US.utf8 | en_US.utf8 |          | 18 MB | pg_default | 
(1 row)
```

### 指定排序规则
```
postgres=# CREATE DATABASE tdapg_db_lc_collate LC_COLLATE 'zh_CN.utf8';
CREATE DATABASE
postgres=# \l+ tdapg_db_lc_collate
                          List of databases
    Name     | Owner | Encoding | Collate  |  Ctype  | Access privileges | Size | Tablespace | Description 
---------------------+-------+----------+------------+------------+-------------------+-------+------------+-------------
 tdapg_db_lc_collate | dbadmin | UTF8   | zh_CN.utf8 | zh_CN.utf8 |          | 18 MB | pg_default |
```

### 指定分组规则
```
postgres=# CREATE DATABASE tdapg_db_lc_ctype LC_CTYPE 'zh_CN.utf8';
CREATE DATABASE
postgres=# \l+ tdapg_db_lc_ctype
                          List of databases
    Name    | Owner | Encoding | Collate  |  Ctype  | Access privileges | Size | Tablespace | Description 
-------------------+-------+----------+------------+------------+-------------------+-------+------------+-------------
 tdapg_db_lc_ctype | dbadmin | UTF8   | zh_CN.utf8 | zh_CN.utf8 |          | 18 MB | pg_default | 
(1 row)
```

### 配置数据可连接
```
postgres=# CREATE DATABASE tdapg_db_allow_connections ALLOW_CONNECTIONS true;

CREATE DATABASE
postgres=# SELECT datallowconn FROM pg_database WHERE datname='tdapg_db_allow_connections'; 
 datallowconn 
--------------
 t
(1 row)
```

### 配置连接数
```
postgres=# CREATE DATABASE tdapg_db_connlimit CONNECTION LIMIT 100;
CREATE DATABASE
postgres=# SELECT datconnlimit FROM pg_database WHERE datname='tdapg_db_connlimit';            
 datconnlimit 
--------------
     100
(1 row)
```

### 配置数据库可以被复制
```
postgres=# CREATE DATABASE tdapg_db_istemplate IS_TEMPLATE true;
CREATE DATABASE
postgres=# SELECT datistemplate FROM pg_database WHERE datname='tdapg_db_istemplate';      
 datistemplate 
---------------
 t
(1 row)
```

### 多个参数一起配置
```
postgres=# CREATE DATABASE tdapg_db_mul OWNER pgxz CONNECTION LIMIT 50 TEMPLATE template0 ENCODING 'utf8' LC_COLLATE 'C';
CREATE DATABASE
```

## 数据库修改
### 修改数据库名称
```
postgres=# ALTER DATABASE tdapg_db RENAME TO tdapg_db_new;
ALTER DATABASE
```

修改数据库时，如果该数据库已经有 session 连接上来，则会提示如下错误：
```
ERROR: database "tdapg_db" is being accessed by other users
DETAIL: There are 6 other sessions using the database.
```

使用下面方法可以把 session 断开，然后再修改：
```
postgres=# SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname='tdapg_db_template';  
 pg_terminate_backend 
----------------------
 t
(1 row)
```

### 修改连接数
```
postgres=# ALTER DATABASE tdapg_db_new CONNECTION LIMIT 50;
ALTER DATABASE
```

### 修改数据库所有者
```
postgres=# ALTER DATABASE tdapg_db_new OWNER TO dbadmin;
ALTER DATABASE
```

### 配置数据默认运行参行
```
postgres=# ALTER DATABASE tdapg_db_new SET search_path TO public,pg_catalog,pg_oracle;   
ALTER DATABASE
```

ALTER DATABASE 不支持的项目：

| **项目**   | **备注** |
| ---------- | -------- |
| encoding   | 编码     |
| lc_collate | 排序规则 |
| lc_ctype   | 分组规则 |

## 数据库删除
```
postgres=# DROP DATABASE tdapg_db_new;
DROP DATABASE
```

删除数据库时，如果该数据库已经有session连接上来，则会提示如下错误：
```
postgres=# DROP DATABASE tdapg_db_template;
ERROR: database "tdapg_db_template" is being accessed by other users
DETAIL: There is 1 other session using the database.
```
使用下面方法可以把 session 断开，然后再删除：
```
postgres=# SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname='tdapg_db_template';  
 pg_terminate_backend 
----------------------
 t
(1 row)
postgres=# DROP DATABASE tdapg_db_template;
DROP DATABASE
```

