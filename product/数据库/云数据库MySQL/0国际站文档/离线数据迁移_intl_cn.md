## 控制台迁移数据
1. 通过 [云数据库数据控制台](https://console.cloud.tencent.com/cdb) 下载备份文件。（详见：<a href="https://cloud.tencent.com/document/product/236/7274" target="_blank">下载备份文件<a/>）
2. 还原数据库时，可以通过 MySQL 命令行工具进行还原，方式如下：
```
shell > mysql -h hostname -P port -u username -p < bak_pathname
```
其中，hostname 为还原数据的目标主机，port 为目标主机的端口，username 为目标主机的数据库用户名，bak_pathname 为备份文件的完整路径。  
3. 还原数据表时，先登录到 MySQL 数据库，再通过 `shell > source bak_pathname` 进行数据表还原。
其中，bak_pathname 为备份文件的完整路径名。

### Windows 迁移数据库
1. 以 db_blog 这个数据库为例。进入 [云数据库数据控制台](https://console.cloud.tencent.com/cdb) 找到需要导出数据的实例，单击【管理】 > 【备份管理】进入备份管理页面，在【备份列表】中找到需要下载的备份文件，单击【下载】 > 【部分下载】。
![](//mc.qcloudimg.com/static/img/067a823712584842fc983ab34fa79b55/image.png)
![][image-7]
2. 选中需要导出的数据库，单击【下一步】。
![][image-8]
3. 单击 **本地下载** 中的【下载】按钮，将备份文件下载至本地。
![][image-9]
4. 记录完整的路径名称。
本例中的完整路径为： F:\download\cdb147691_backup_20170717050142
![][image-1]
5. 进入命令提示符，通过 MySQL 命令行工具进行还原。
![][image-2]
6. 登录 MySQL 数据库可以查看到备份的数据库已经还原到服务器内。
![][image-10]

### Windows 迁移数据表
1. 以 db_blog 下的 t_blog 数据表为例，从云数据库数据控制台下载备份文件。
![][image-11]
2. 从云数据库数据控制台下载备份文件，记录完整的路径名称。
本例中的完整路径为 F:\download\cdb147691_backup_20170718050146
![][image-3]
3. 进入命令提示符，通过 MySQL 命令行工具进行还原。
![][image-4]
4. 登录 MySQL 数据库可以查看到备份的数据表已经还原到服务器内。
![][image-12]

## 命令行工具迁移数据
1. 使用 MySQL 命令行工具 mysqldump 生成待导入的 SQL 文件，方式如下：
>**注意：**
>使用 mysqldump 导出的数据文件必须兼容所购买的云数据库 MySQL 版本的 SQL 规范，可登录云数据库通过 `select version();` 获取相应的 MySQL 版本信息。生成的 SQL 文件名称允许英文/数字/下划线，但不能包含 “test” 字符。</blockquote>
```
shell > mysqldump [options] db_name [tbl_name ...] > bak_pathname
```
其中，options 为导出选项，db_name 为数据库名称，tbl_name 为表名称，bak_pathname 为导出路径名。
更多 mysqldump 导出数据说明，请参考 [MySQL官方手册](https://dev.mysql.com/doc/refman/5.6/en/mysqldump.html)。

2. 还原数据库时，可以通过 MySQL 命令行工具进行还原，方式如下：
```
shell > mysql -h hostname -P port -u username -p < bak_pathname
```
其中，hostname 为还原数据的目标主机，port 为目标主机的端口，username 为目标主机的数据库用户名，bak_pathname 为备份文件的完整路径。

### 通过 CVM 主机 Linux 系统迁移数据
CVM 主机访问数据库请参考 <a href="https://cloud.tencent.com/document/product/236/3130" target="_blank">访问MySQL数据库</a>。
1. 以云数据库上的 db_blog 数据库为例。登录 CVM 主机，使用 MySQL 命令行工具 mysqldump 生成待导入的 SQL 文件。
![][image-5]
2. 通过 MySQL 命令行工具进行还原，本例将数据还原到 CVM 服务器上。可以查看到备份的数据库已导入到目标服务器对应的数据库中。
![][image-6]

## 导入数据文件字符集编码问题
1. 云数据库导入数据文件如果没有指定字符集编码，以云数据库设置的字符集编码执行。
2. 如果导入数据文件中有指定的字符集编码，则以指定的字符集编码执行。
3. 如果导入的数据文件的字符集编码与云数据库当前字符集编码不同，会造成乱码。

更多字符集编码问题，请参考 <a href="https://cloud.tencent.com/document/product/236/7259#6-.E5.AD.97.E7.AC.A6.E9.9B.86.E8.AF.B4.E6.98.8E6" target="_blank">使用限制</a>，字符集说明。

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
