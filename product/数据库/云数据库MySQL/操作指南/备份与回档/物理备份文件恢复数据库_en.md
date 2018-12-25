## Recovering Database Using Physical Backup
#### 1. Downloading Backup File
For detailed steps, refer to the [download instructions](https://cloud.tencent.com/doc/product/236/7123)
After the file is downloaded, the result will be shown as follows:
![](https://mc.qcloudimg.com/static/img/d02b20501dd1c42a95f2b7a74c266b98/1.png)

#### 2. Decompressing Backup File
Decompress the backup file:
```
tar   xfv  backup.tgz
```
Query the files generated after decompression. The directory file in blue is the database in which CDB resides when the backup is generated.
![](https://mc.qcloudimg.com/static/img/62a64dc648edb040b9bbd9f2bbd65491/2.png)


### 3. Modifying Configuration File
Due to version problems, please comment out
innodb_checksum_algorithm,
innodb_log_checksum_algorithm,
innodb_fast_checksum,
innodb_page_size,
innodb_log_block_size, and
redo_log_version in the decompressed file "backup-my.cnf", as shown below:
![](https://mc.qcloudimg.com/static/img/10113311b33e398ce0df96ca419f7f45/3.png)

#### 4. Modifying File Owner
Modify the file owner, and check whether the file belongs to a mysql user
```
chown -R mysql:mysql /home/mysql/backup/data
```
![](https://mc.qcloudimg.com/static/img/efbdeb20e1b699295c6a4321943908b2/4.png)

#### 5. Starting mysql Process and Logging in for Verification
Start the mysql process, and verify whether it is successfully started
```
mysqld_safe --defaults-file=/home/mysql/backup/data/backup-my.cnf --user=mysql --datadir=/home/mysql/backup/data &
```
Log in to mysql for verification at the client
mysql  -uroot
![](https://mc.qcloudimg.com/static/img/346346626997b85385408ac728bf82ff/5.png)

Note:
1. After recovery, the table "mysql.user" does not contain the user created in the CDB, and you need to create one.
2. Execute the following SQL before creating a new user:
```
delete from mysql.db where user<>'root' and char_length(user)>0;
delete from mysql.tables_priv where user<>'root' and char_length(user)>0;
flush privileges;
```






