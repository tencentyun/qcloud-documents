### 1. 如何自己手动设置 MySQL 备份？
您可以通过离线迁移到本地来备份 MySQL 数据，请参考 [离线迁移数据](https://cloud.tencent.com/document/product/236/8464)。

### 2.开发者自己如何备份数据？
云数据库实例每天会进行全量备份，开发者也可以采用云数据库提供的多线程快速导入导出工具进行备份，详见 [手动备份与恢复云数据库](https://cloud.tencent.com/document/product/236/7275?!preview&lang=cn)，或者通过 mysqldump 工具自己备份数据。

### 3. MySQL 怎么设置备份方式？
在实例列表页，单击实例，进入【备份管理】，再单击【自动备份设置】，即可进行设置备份方式。
![](//mc.qcloudimg.com/static/img/61eec4f474762057d6956dc61ecc1214/image.png)
![](//mc.qcloudimg.com/static/img/d67376cc5c98175d31fd29ae55499cb9/image.png)

### 4. MySQL 支持什么方式的备份？
1. 逻辑备份支持实例级和库表级下载，物理备份仅支持实例级的下载。
2. MySQL 低于 5.6 版本的仅支持逻辑备份。

### 5. MySQL 异步复制模式有备份库，备份库在哪里？
云数据库实例每天会进行全量备份，开发者可以在控制台外网或者内网下载备份数据，也可以在 phpMyAdmin 中手动备份数据库。

### 6. MySQL如何查看 binlog 日志？
1. 控制台下载 binlog 到本地，比如下载到云服务器。
2. 使用 mysqlbinlog 命令查看。mysql5.6 需要安装 3.4 或以上版本的 mysqlbinlog 方支持本地服务器查看 binlog。

### 7.云数据库的 binlog 保存时间是多久？
由于 MySQL binlog 会占用大量的存储空间，所以云数据库只保存最近 5 天的 binlog。另外，如果 binlog 数据量增加太快，服务器磁盘存储不下 5 天的 binlog，需要人工删除 binlog，释放空间，详见 <a href="https://cloud.tencent.com/document/product/236/7269#5-.E4.BA.91.E6.95.B0.E6.8D.AE.E5.BA.93.E7.9A.84binlog.E4.BF.9D.E5.AD.98.E6.97.B6.E9.97.B4.E8.AF.B4.E6.98.8E5" target="_blank">云数据库的binlog保存时间说明</a>。
