FDW (FOREIGN DATA WRAPPER) is a kind of extension provided by PostgreSQL for accessing external data sources, including data from other databases of the instance in question or that from other instances. Depending on the type of the destination database instance, FDW extensions can take different forms, including postgres_fdw, mysql_fdw, and mongo_fdw. How to use an FDW extension:

 1. Install the FDW extension using CREATE EXTENSION.
 2. Create a foreign server object, using "CREATE SERVER" to represent each remote database you want to connect to. Specify connection information, except user and password, as options of the server object.
 3. Create a user mapping, using CREATE USER MAPPING, for each database user you want to allow to access each foreign server. Specify the remote user name and password to use as user and password options of the user mapping.
 4. Create a foreign table, using CREATE FOREIGN TABLE, for each remote table you want to access. The columns of the foreign table must match the referenced remote table. You can, however, use table and/or column names different from the remote table's, if you specify the correct remote names as options of the foreign table object.

FDW extensions allow direct access to data across instances. For security reasons, TencentDB for PostgreSQL is optimized for permission control while creating a foreign server object, enabling classified management based on the environment where the destination instance is located. Additional auxiliary parameters are added to the open source version to verify user identities and adjust network policies.

## Auxiliary Parameters for CREATE SERVER
#### Auxiliary parameters for such extensions as postgres_fdw and mysql_fdw    

 - host
    Required. The private IP of the destination instance, which is used for postgres_fdw.
 - address
    Required. The private IP of the destination instance, which is used for mysql_fdw.
 - port
    Required. The private port of the destination instance.
 - instanceid
    Required. The resource ID of the destination instance.
     1. If the destination instance type is CDB, it is the instance ID, in a format like postgres-xxxxx and mysql-xxxxx, and it can be found in the instance console. The figure below shows an example for PostgreSQL:
![](https://main.qcloudimg.com/raw/da92d46f8b152ffda53300fa577e9399.png)
     2. If the destination instance is on a Tencent Cloud CVM, it is the instance ID of the CVM, in a format like ins-xxxxx.
![](https://main.qcloudimg.com/raw/9dd32f99dfb6ea8b3d1f39a89944aab1.png)

 - access_type
    Optional. The destination instance type:
    1. The destination instance is a CDB instance, such as TencentDB for PostgreSQL and TencentDB for MySQL. If the parameter is not specified, this type is used by default.
    2. The destination instance is on a Tencent Cloud CVM.
    3. The destination instance is self-built in a Tencent Cloud public network.
    4. The destination instance is connected via Tencent Cloud VPN.
    5. The destination instance connected via a self-built VPN.
    6. The destination instance is connected via Direct Connect.
    7. The destination instance is Tencent Cloud COS data.
 - uin
    Optional. The ID of the account to which the instance belongs, which is required for user authentication. This information can be found in [query uin](https://console.cloud.tencent.com/developer).
 - own_uin
    Optional. The ID of the main account to which the instance belongs, which is also required for user authentication.
 - vpcid
    Optional. VPC ID. This parameter is required if the destination instance is in the VPC of Tencent Cloud CVM. It can be found in [VPC Console](https://console.cloud.tencent.com/vpc/vpc).
 - subnetid
    Optional. VPC subnet ID. This parameter is required if the destination instance is in the VPC of Tencent Cloud CVM. It can be found in the Subnet of [VPC Console](https://console.cloud.tencent.com/vpc/subnet).
 - dcgid
    Optional. Direct connect ID. This parameter is required if the destination instance needs to be connected through a direct connect network.
 - vpngwid
    Optional. VPN gateway ID. This parameter is required if the destination instance needs to be connected through a VPN.
 - region
    Optional. The region where the destination instance resides. For example, "ap-guangzhou" indicates Guangzhou. This parameter is required if the FDW extension accesses cross-region data.

### Auxiliary parameters for COS_FDW
  - host
    Required. The access domain name of Tencent Cloud COS, such as: `https://xxxx-xxxxxx.cos.ap-beijing.myqcloud.com. `
  - bucket
    Required. The name of the bucket in Tencent Cloud COS.
  - id
    Required. The SecretId value of a Tencent Cloud API key, which can be found in the Cloud API Key of [CAM Console](https://console.cloud.tencent.com/capi).
  - key
    Required. The SecretKey value of a Tencent Cloud API key, which can be found in the Cloud API Key of [CAM Console](https://console.cloud.tencent.com/capi).

### FDW availability

| Name | Available directly | Available across regions |
| - 			| :-: 						| -: 						|
| postgres_fdw | It can used for instances created before April 26, 2018 after they restart, and can be used directly for new instances. | Not supported by default. You can [submit a ticket] for application. |
| mysql_fdw | It can used for instances created before April 26, 2018 after they restart, and can be used directly for new instances. | Not supported by default. You can [submit a ticket] for application. |
| cos_fdw | In beta test. You can [submit a ticket] for trial use. | Not supported by default. You can [submit a ticket] for application. |



### Reference Links

[CREATE SERVER in version 9.3](https://www.postgresql.org/docs/9.3/static/sql-createserver.html)
[CREATE SERVER in version 9.5](https://www.postgresql.org/docs/9.5/static/sql-createserver.html)

## An Example of Using postgres_fdw
The postgres_fdw extension can be used to access data from other databases of the instance or that from other instances.

### Preconditions
1. Create test data in the instance.
```
postgres=>create role user1 with LOGIN  CREATEDB PASSWORD 'password1';
postgres=>create database testdb1;
CREATE DATABASE
```

2. Create test data in the destination instance.
```
postgres=>create role user2 with LOGIN  CREATEDB PASSWORD 'password2';
postgres=> create database testdb2;
CREATE DATABASE
postgres=> \c testdb2 user2
You are now connected to database "testdb2" as user "user2".
testdb2=> create table test_table2(id integer);
CREATE TABLE
testdb2=> insert into test_table2 values (1);
INSERT 0 1
```


## Create the postgres_fdw Extension
```
    #Create
    postgres=> \c testdb1
    You are now connected to database "testdb1" as user "user1".
    testdb1=> create extension postgres_fdw;
    CREATE EXTENSION
    #View
    testdb1=> \dx
                               List of installed extensions
         Name     | Version |   Schema   |                    Description
    --------------+---------+------------+----------------------------------------------------
     plpgsql      | 1.0     | pg_catalog | PL/pgSQL procedural language
     postgres_fdw | 1.0     | public     | foreign-data wrapper for remote PostgreSQL servers
    (2 rows)

```

### Create SERVER

1. The destination instance is a TencentDB instance.
```
    #Access the data of the destination instance testdb2 from the instance testdb1
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', instanceid 'postgres-xxxxx');
    CREATE SERVER
```
2. The destination instance is on a Tencent Cloud CVM and the network is a basic network.
```
    testdb1=>create server srv_test foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx', dbname 'testdb2', port '5432', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou',uin 'xxxxxx',own_uin 'xxxxxx');
    CREATE SERVER
```
3. The destination instance is on a Tencent Cloud CVM and the network is a VPC.
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpcid 'vpc-xxxxxx', subnetid 'subnet-xxxxx');
    CREATE SERVER
```

4. The destination instance is self-built in a Tencent Cloud public network.
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '3', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx');
    CREATE SERVER 
```

5. The destination instance is connected via Tencent Cloud VPN.
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '4', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');
```

6. The destination instance is connected via a self-built VPN.
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '5', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');   
```

7. The destination instance is connected via Tencent Cloud direct connect.
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '6', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', dcgid 'xxxxxx');    
    CREATE SERVER       
```


### Create a user mapping
```
    testdb1=> create user mapping for user1 server srv_test1 options (user 'user2',password 'password2');
    CREATE USER MAPPING
```
### Create a foreign table
```
    testdb1=> create foreign table foreign_table1(id integer) server srv_test1 options(table_name 'test_table2');
    CREATE FOREIGN TABLE
```
### Access foreign data
```
    testdb1=> select * from foreign_table1;
     id
    ----
      1
    (1 row)
```
### Notes on Using postgres_fdw
If the destination instance is on a CVM, note the following:
 1. Lift the hba constraint for PostgreSQL to allow the created mapping user (e.g., user2) to access data in MD5 mode. For more information on how to modify hba, see [PostgreSQL Documentation](https://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html).
 2. If the destination instance is not a CDB instance and the hot backup mode is set up for it, you must update the server connection address or recreate the server after the master/slave switch.

### Reference documentation

[Introduction to postgres_fdw](http://www.postgres.cn/docs/9.5/postgres-fdw.html)

[CREATE SERVER in version 9.3](https://www.postgresql.org/docs/9.3/static/sql-createserver.html)

[CREATE SERVER in version 9.5](https://www.postgresql.org/docs/9.5/static/sql-createserver.html)

[Introduction to pg_hba in version 9.3](https://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html)

[Introduction to pg_hba in version 9.5](https://www.postgresql.org/docs/9.5/static/auth-pg-hba-conf.html)

## An Example of Using mysql_fdw
The mysql_fdw extension can be used to access data from other MySQL instances.

### Preconditions

1. Create test data in the instance.
```
    postgres=>create role user1 with LOGIN  CREATEDB PASSWORD 'password1';
    postgres=>create database testdb1;
    CREATE DATABASE
```
2. Create test data in the destination instance.
```
    postgres=>create role user2 with LOGIN  CREATEDB PASSWORD 'password2';
    postgres=> create database testdb2;
    CREATE DATABASE
    postgres=> \c testdb2 user2
    You are now connected to database "testdb2" as user "user2".
    testdb2=> create table test_table2(id integer);
    CREATE TABLE
    testdb2=> insert into test_table2 values (1);
    INSERT 0 1
```

### Create the mysql_fdw extension
```
    #Create
    postgres=> \c testdb1
    You are now connected to database "testdb1" as user "user1".
    testdb1=> create extension mysql_fdw;
    CREATE EXTENSION
    #View
    testdb1=> \dx
                               List of installed extensions
         Name     | Version |   Schema   |                    Description
    --------------+---------+------------+----------------------------------------------------
     plpgsql      | 1.0     | pg_catalog | PL/pgSQL procedural language
     mysql_fdw    | 1.0     | public     | Foreign data wrapper for querying a MySQL server
    (2 rows)
```

### Create SERVER
1. The destination instance is a TencentDB instance.
 ```
    #Access the data of the destination instance testdb2 from the instance testdb1
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', instanceid 'cdb-xxxxx', uin 'xxxxxx', region 'ap-guangzhou');
    CREATE SERVER
 ```
2. The destination instance is on a Tencent Cloud CVM and the network is a basic network.
```
    testdb1=>create server srv_test foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou',uin 'xxxxxx',own_uin 'xxxxxx');
    CREATE SERVER
```
3. The destination instance is on a Tencent Cloud CVM and the network is a VPC.
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpcid 'vpc-xxxxxx', subnetid 'subnet-xxxxx');
    CREATE SERVER
```
4. The destination instance is self-built instance in a Tencent Cloud public network.
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', access_type '3', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx');
    CREATE SERVER   
```
5. The destination instance is connected via Tencent Cloud VPN.
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', access_type '4', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');
```
6. The destination instance is connected via a self-built VPN.
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', access_type '5', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');   
```
7. The destination instance is connected via Tencent Cloud direct connect.
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', access_type '6', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', dcgid 'xxxxxx');    
    CREATE SERVER       
```


### Create a user mapping
```
    testdb1=> create user mapping for user1 server srv_test1 options (user 'user2',password 'password2');
    CREATE USER MAPPING
```
### Create a foreign table
```
    testdb1=> create foreign table foreign_table1(id integer) server srv_test1 options(dbname 'testdb2', table_name 'test_table2');
    CREATE FOREIGN TABLE
```
### Access foreign data
```
    testdb1=> select * from foreign_table1;
     id
    ----
      1
    (1 row)
```

### Reference Links

[CREATE SERVER in version 9.3](https://www.postgresql.org/docs/9.3/static/sql-createserver.html)
[CREATE SERVER in version 9.5](https://www.postgresql.org/docs/9.5/static/sql-createserver.html)

## An Example of Using cos_fdw
The cos_fdw extension can be used to obtain the text data in Tencent Cloud COS from a TencentDB for PostgreSQL instance.

### Preconditions
1. Create test data in the instance.
```
    postgres=>create role user1 with LOGIN  CREATEDB PASSWORD 'password1';
    postgres=>create database testdb1;
    CREATE DATABASE
```

2. Create a bucket "test1" in [COS Console](https://console.cloud.tencent.com/cos5/bucket), and upload a text file to "/testdir/test.txt" in the bucket.


 ### Create the cos_fdw extension
```
    #Create
    postgres=> \c testdb1
    You are now connected to database "testdb1" as user "user1".
    testdb1=> create extension cos_fdw;
    CREATE EXTENSION
    #View
    testdb1=> \dx
                               List of installed extensions
         Name     | Version |   Schema   |                    Description
    --------------+---------+------------+----------------------------------------------------
     plpgsql      | 1.0     | pg_catalog | PL/pgSQL procedural language
     cos_fdw      | 1.0     | public     | foreign-data wrapper for flat qcloud cos access
    (2 rows)
```

### Create SERVER
```
    #Access the data of the COS test1 from the instance testdb1
    testdb1=>create server srv_cos foreign data wrapper cos_fdw options(host 'test11-xxxxxx.cos.ap-chengdu.myqcloud.com', bucket 'test1', id 'xxxxxx', key 'xxxxxx');
    CREATE SERVER
```

### Create a foreign table
Parameter: filepath, the relative path to the text file in the bucket
```
    testdb1=> create foreign table test_cos(id integer) server srv_cos options(filepath '/testdir/test.txt');
    CREATE FOREIGN TABLE
```
### Access foreign data
```
    testdb1=> select * from test_cos;
     id
    ----
      1
    (1 row)

```
### Reference Links

[COS Documentation](https://intl.cloud.tencent.com/document/product/436).


