## 物理备份恢复数据库
#### 1 下载备份文件
具体步骤请参考：[具体的下载说明](https://cloud.tencent.com/doc/product/236/7123)
下载文件成功后，如下图：
![](https://mc.qcloudimg.com/static/img/d02b20501dd1c42a95f2b7a74c266b98/1.png)

#### 2 解压备份文件
解压备份文件：
```
tar   xfv  backup.tgz
```
查询解压后生成的文件，其中蓝色字体的目录文件为备份生成时 CDB 存在的数据库
![](https://mc.qcloudimg.com/static/img/62a64dc648edb040b9bbd9f2bbd65491/2.png)


#### 3 配置文件修改
由于存在的版本问题，请将解压文件 backup-my.cnf 中的
innodb_checksum_algorithm、
innodb_log_checksum_algorithm、
innodb_fast_checksum、
innodb_page_size 、
innodb_log_block_size、
redo_log_version 注释掉，如下图：
![](https://mc.qcloudimg.com/static/img/10113311b33e398ce0df96ca419f7f45/3.png)

#### 4 修改文件属主
修改文件属主，并检查文件所属为mysql用户
```
chown -R mysql:mysql /home/mysql/backup/data
```
![](https://mc.qcloudimg.com/static/img/efbdeb20e1b699295c6a4321943908b2/4.png)

#### 5 启动mysqld进程并且登录验证
启动mysqld进程，并验证启动成功
```
mysqld_safe --defaults-file=/home/mysql/backup/data/backup-my.cnf --user=mysql --datadir=/home/mysql/backup/data &
```
客户端登录mysql验证
mysql  -uroot
![](https://mc.qcloudimg.com/static/img/346346626997b85385408ac728bf82ff/5.png)

注意：
1.恢复完成后，表 mysql.user 中是不包含 CDB 中创建的用户，需要新建。
2.新建用户前请执行如下 SQL：
```
delete from mysql.db where user<>'root' and char_length(user)>0;
delete from mysql.tables_priv where user<>'root' and char_length(user)>0;
flush privileges;
```





