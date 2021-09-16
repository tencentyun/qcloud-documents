由于分布式数据库到分布式数据库的数据导入方案与一般情况不同，使用 mysqldump 对分布式实例导入数据到分布式实例的步骤如下：

## 1. 安装 MariaDB 版本的 mysqldump
购买 Linux 版的云服务器，使用`yum install mariadb-server`即可安装。

## 2. 导出表结构
```
mysqldump --compact --single-transaction -d -uxxx -pxxx  -hxxx.xxx.xxx.xxx -Pxxxx  db_name table_name   >  schema.sql
```
>?db_name 和 table_name 参数根据实际情况选择。

## 3. 导出数据
mysqldump 导出数据：
在 [TDSQL MySQL版 控制台](https://console.cloud.tencent.com/dcdb) 的参数设置中设置 net_write_timeout 参数：set global net_write_timeout=28800
```
mysqldump --compact --single-transaction --no-create-info -c -uxxx  -pxxx -hxxx.xxx.xxx.xxx -Pxxxx db_name table_name  > data.sql
```
>?db_name 和 table_name 参数根据实际情况选择，如果导出的数据要导⼊到另外⼀套 TDSQL MySQL版 环境的话，必须加上 -c 选项，-c 与 db_name 之间需添加空格。
>
![](https://main.qcloudimg.com/raw/567f47f17939e809a7e0aa2f06627353.png)

## 4. 在目标库创建 db
```
mysql --default-character-set=utf8 -uxxx -pxxx -hxxx.xxx.xxx.xxx -Pxxxx -e "create database dbname;";
```
- --default-character-set=utf8：根据您目标表实际情况设定。
- -uxxx：有权限的帐号（-u 是关键字）。
- -pxxx：密码（-p 是关键字）。
- -hxxx.xxx.xxx.xxx -Pxxxx：数据库实例的 IP 和端口。
- dbname：代表 db 的名字。

## 5. 在目标库上导入表结构
```
mysql --default-character-set=utf8 -uxxx -pxxx -hxxx.xxx.xxx.xxx -Pxxxx dbname < schema.sql
```
- --default-character-set=utf8：根据您目标表实际情况设定。
- -uxxx：有权限的帐号（-u 是关键字）。
- -pxxx：密码（-p 是关键字）。
- -hxxx.xxx.xxx.xxx -Pxxxx：数据库实例的 IP 和端口。
- dbname：代表 db 的名字。

## 6. 在目标库上导入表数据
```
mysql --default-character-set=utf8 -uxxx -pxxx -hxxx.xxx.xxx.xxx -Pxxxx dbname < data.sql
```
>?如果源表中使用了自增字段，并且导入的时候出现“Column 'xx' specified twice”的错误，则需要对 schema.sql 做处理。
   去掉自增字段的反引号(cat schema.sql | tr "`" " " > schema_tr.sql )，然后 drop database，使用处理后的 schema_tr.sql 重复步骤3 - 5的操作。
	 
![](https://main.qcloudimg.com/raw/b55fe0763f4e8fd1795fec478e9dc0c1.png)
