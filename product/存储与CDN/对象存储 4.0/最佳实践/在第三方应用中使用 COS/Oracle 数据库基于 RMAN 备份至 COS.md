对象存储（Cloud Object Storage，COS）海量容量无上限，自动沉降归档存储类型和深度归档存储类型，媲美磁带的成本，特别适合备份归档场景。

当前，越来越多客户选择备份上云；而 Oracle 备份模块实现了和对象存储 COS 的对接，基于 COS 来实现低成本的数据库备份和恢复成为优选。

## OSB 对接腾讯云 COS

Oracle 的 Oracle Secure Backup Cloud Module 模块，是 Oracle Secure Backup（OSB） 产品家族的一员，实现与对象存储 COS 的对接，将 Oracle 数据库备份上云，直接备份到腾讯云存储COS；Oracle Secure Backup Cloud Module 模块并与 RMAN 功能实现整合，用户可以自定义 RMAN 脚本，高效将 Oracle 数据库直接备份到腾讯云 COS。

Oracle 9i 或以上版本，支持 Oracle Secure Backup Cloud Module，详见 [Oracle 官方文档](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/oracle-secure-backup-osb-cloud-module.html#GUID-6FCF4FD8-861C-4D52-BB41-32E6EF03789F)。

## 安装 OSB

1. 若您未安装 OSB，可从 [Oracle 官网](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/oracle-secure-backup-osb-cloud-module.html#GUID-964AADD2-3405-4476-8698-E9F2133CB5B7) 获取最新版本。
2. 将下载的 osbws_installer.zip 压缩包解压。用户根据自己 COS 服务的 SecretId、SecretKey、地域和 endpoint 参数配置，执行 OBS 的安装命令：
```
java -jar osbws_install.jar -AWSID <SecretId> -AWSKey <SecretKey> -walletDir $ORACLE_HOME/osbws_wallet -libDir $ORACLE_HOME/lib -location <地域> -awsEndPoint <endpoint>

// 根据压缩包的存放目录进行替换
```
例如：
```
java -jar osbws_install.jar -AWSID AKIDxxxx -AWSKey XXXX -walletDir $ORACLE_HOME/osbws_wallet -libDir $ORACLE_HOME/lib -location ap-guangzhou -awsEndPoint cos.ap-guangzhou.myqcloud.com
```
oracle12以上的版本中自带了 osb 模块，如果安装时长时间 download 无反应，建议在官网下载最新 osb 模块进行安装，或使用代理服务器进行安装。

## RMAN 进行数据库备份到 COS

1. 首先登录数据库，连接 RMAN，连接命令：`rman target / `。
2. 接着执行如下命令，将数据库备份到 COS 存储桶，其中标红的部分与数据库名有关，根据实际值进行修改。
```
run {
allocate channel ch1 type
sbt parms='SBT_LIBRARY=/u01/app/oracle/product/11.2.0/dbhome_1/lib/libcos.so,
SBT_PARMS=(OSB_WS_PFILE=/u01/app/oracle/product/11.2.0/dbhome_1/dbs/cosorcl.ora)';
backup channel=ch1 database format='ora_%d_%I_%T_%s_%t_%c_%p.dbf' plus archivelog;
backup channel=ch1  current controlfile  format='%d_%I_%T_%s_%t_%c_%p.conf';
backup channel=ch1 spfile format='ora_%d_%I_%T_%s_%t_%c_%p.spf' ;
release channel ch1;
}
```

## RMAN 从 COS 恢复数据库

1. 关闭数据库，并置于非挂载状态。
	- 执行命令关闭数据库：
	```
	shutdown immediate;
	```

	- 执行命令使数据库至 nomount 状态：
	```
	startup nomount;
	```

2. 选择要恢复的备份文件，通过 rman 命令 list backup 列举出所有的备份文件，记录下所选备份问卷的句柄 Handle 名称和标记 TAG 值。
3. 关联备份问卷，执行如下 restore 命令，关联句柄为“ORACLE_1880733115_20190507_5_1007656283_1_1.conf”的备份文件，通过 list backup 获取；其中`lib/libcos.so`和`cosorcl.ora`部分与数据库名有关，可根据实际值进行修改，与备份时一致。
```
run {
allocate channel ch1 type
sbt parms='SBT_LIBRARY=/u01/app/oracle/product/11.2.0/dbhome_1/lib/libcos.so,
SBT_PARMS=(OSB_WS_PFILE=/u01/app/oracle/product/11.2.0/dbhome_1/dbs/cosorcl.ora)';
restore controlfile from '**ORACLE_1880733115_20190507_5_1007656283_1_1.conf**';
release channel ch1;
}
```

4. 切换数据库至 mount 状态 alter database mount。执行如下 restore 命令：
```
run {

allocate channel ch1 type
sbt parms='SBT_LIBRARY=/u01/app/oracle/product/11.2.0/dbhome_1/lib/libcos.so,
SBT_PARMS=(OSB_WS_PFILE=/u01/app/oracle/product/11.2.0/dbhome_1/dbs/cosorcl.ora)';
restore database from tag='**TAG20190507T163102**';
recover database from tag='**TAG20190507T163102**';
release channel ch1;
}
```
其中 **TAG20190507T163102** 的 tag 值相当于每个备份的 ID 号，通过 list backup 获取，需要确保与前面恢复的控制文件是一致的，即是句柄为“**ORACLE_1880733115_20190507_5_1007656283_1_1.conf**”备份文件的tag；其中标红（非加粗）的部分与数据库名有关，根据实际值进行修改；与备份时一致。

5. 打开数据库，即可看到从 COS 上恢复的数据。



## RMAN 默认无并发，需要手动修改

登录 rman，修改并发参数配置，此处以并发数15为例：

```
run {
configure channel device type sbt parms='SBT_LIBRARY=/u01/app/oracle/product/11.2.0/dbhome_1/lib/libcos.so ENV=(OSB_WS_PFILE=/u01/app/oracle/product/11.2.0/dbhome_1/dbs/cosorcl.ora)';
configure default device type to SBT;
configure device type SBT parallelism 15;
}
```

## 相关参考

更多帮助信息，请参见 [Oracle 官方文档](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/oracle-secure-backup-osb-cloud-module.html#GUID-6FCF4FD8-861C-4D52-BB41-32E6EF03789F)。
