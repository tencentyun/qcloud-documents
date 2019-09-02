## Migrating Data via Console
1. Log in to the [Cloud Database console](https://console.cloud.tencent.com/cdb) to download backup files. (For more information, please see Downloading Backup Files)
2. A database can be recovered with MySQL command line tool, as shown below:
```
shell > mysql -h hostname -P port -u username -p < bak_pathname
```
The "hostname" is the destination server to be recovered. The "port" is the port of destination server. The "username" is the user name for the database on the destination server. The "bak_pathname" is the full path for backup files.  
3. Log in to the MySQL database to recover the database table with `shell > source bak_pathname`.
The "bak_pathname" is the full path for backup files.

### Migrate data on Windows
1. Take the database "db_blog" as an example. Log in to the [Cloud Database console](https://console.cloud.tencent.com/cdb) and locate the instance of which you need to export data. Click **Management** -> **Backup Management** to enter the backup management page. Find the backup files to be downloaded and click **Download** -> **Partial Download**.
![](//mc.qcloudimg.com/static/img/067a823712584842fc983ab34fa79b55/image.png)
![][image-7]
2. Select the database to be exported and click **Next**.
![][image-8]
3. Click **Download** in **Download Locally** to download backup files to the local computer.
![][image-9]
4. Record the full path.
The full path for this example is as follows: F:\download\cdb147691_backup_20170717050142
![][image-1]
5. Enter the command prompt to recover the database with MySQL command line tool.
![][image-2]
6. Log in to the MySQL database, and you can find that the backup database has already been recovered to the server.
![][image-10]

### Migrate database table on Windows
1. Take the database table "t_blog" under "db_blog" as an example. Download backup files from the Cloud Database console.
![][image-11]
2. Download backup files from the Cloud Database console and record the full path.
The full path for this example is F:\download\cdb147691_backup_20170718050146.
![][image-3]
3. Enter the command prompt to recover the database with MySQL command line tool.
![][image-4]
4. Log in to the MySQL database, and you can find that the backup database table has already been recovered to the server.
![][image-12]

## Migrating Data with Command Line Tool
1. Generate the SQL files to be imported using MySQL command line tool mysqldump, as shown below:
>**Note:**
> The data files exported by mysqldump must be compatible with the SQL standard of the purchased cloud database's MySQL version. You can log in to the cloud database via `select version ();` to obtain corresponding MySQL version information. The generated SQL file name can contain English letters/numbers/underscores, but cannot contain "test" characters.
```
shell > mysqldump [options] db_name [tbl_name ...] > bak_pathname
```
The "options" is the export option. The "db_name" is the database name. The "tbl_name" is the table name, and the "bak_pathname" is the export path.
For more information on how to export data with mysqldump, please see [official MySQL manual](https://dev.mysql.com/doc/refman/5.6/en/mysqldump.html).

2. A database can be recovered with MySQL command line tool, as shown below:
```
shell > mysql -h hostname -P port -u username -p < bak_pathname
```
The "hostname" is the destination server to be recovered. The "port" is the port of destination server. The "username" is the user name for the database on the destination server. The "bak_pathname" is the full path for backup files.

### Migrate data on CVM Linux system
For more information on accessing the database on CVMs, please see Assess MySQL Database.
1. Take the db_blog database on Cloud Database as an example. Log in to the CVM and generate the SQL files to be imported using MySQL command line tool mysqldump, as shown below:
![][image-5]
2. Recover the data with MySQL command line tool. In this example, the data is recovered to a CVM. You can find that the backup database has already been recovered to the corresponding database on the destination server.
![][image-6]

## Character Set Encoding Issues of Imported Data Files
1. If the imported data files do not specify a character set encoding, the one set by the cloud database will be executed.
2. If the imported data files have specified a character set encoding, the specified one will be executed.
3. If the character set encoding of imported data files is different from those of the cloud database, it will display unreadable codes.

For more information on character set encoding, please see Character Set in [Use limits](https://cloud.tencent.com/document/product/236/7259)

[image-1]:  https://mc.qcloudimg.com/static/img/ec1530d76dab094cfc76a49e05e34d3c/step11.png
[image-2]:  https://mc.qcloudimg.com/static/img/bb37805c3fa523664ea427923f79c747/step12.png
[image-3]:  https://mc.qcloudimg.com/static/img/42f282cf218253ba16ec51eb715ac76f/step13.png
[image-4]:  https://mc.qcloudimg.com/static/img/ec52232b7fab6e9d44b95ab1f774a0c1/step14.png
[image-5]:  https://mc.qcloudimg.com/static/img/2eb987a5a0a3d1b5b889970e67d66840/step15.png
[image-6]:  https://mc.qcloudimg.com/static/img/58d60e0df9def342ee8344d68e5d6558/step16.png
[image-7]:  https://mc.qcloudimg.com/static/img/93e534bb662bd93cd1cc33f3e7e01fd8/step1.png
[image-8]:  https://mc.qcloudimg.com/static/img/85c72e3d044155342ec9375b42d7d597/step2.png
[image-9]:  https://mc.qcloudimg.com/static/img/fbd4f81256f71264d8616916673c3383/step3.png
[image-10]: https://mc.qcloudimg.com/static/img/3bae3de9bd92e262bcfc2d0ae73a85bf/step4.png
[image-11]: https://mc.qcloudimg.com/static/img/189a5828548563144959c91482b91694/step5.png
[image-12]: https://mc.qcloudimg.com/static/img/4f03808a5f93d2b2731431c12c1684ee/step6.png

