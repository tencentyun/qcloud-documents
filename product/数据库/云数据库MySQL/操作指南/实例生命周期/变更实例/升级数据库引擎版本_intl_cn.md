CDB 支持MySQL 数据库引擎的以下主要版本就地升级：
* MySQL 5.5 到 MySQL 5.6
* MySQL 5.6 到 MySQL 5.7

CDB for MySQL 不允许跨主要版本升级，例如若要将 CDB 上的 MySQL 5.1 数据库实例的主要版本升级到 MySQL 5.6 或更高版本，您必须首先将数据库实例升级到 MySQL 5.5。

MySQL 的主要版本升级期间，CDB 会清空 slow\_log  表。如果要保留日志信息，请在升级主要版本之前保存日志内容。CDB for MySQL 主要版本升级通常需要较长时间。

#### 注意事项
CDB for MySQL 5.6/5.7 主从同步基于 GTID 实现，默认仅支持 InnoDB 引擎，因此升级有如下注意事项：
* 升级过程中会将 MyISAM 引擎的表转换为 InnoDB。
* 不支持`create table …  as select …`语法。
* 升级前建议您先完成 MyISAM 到 InnoDB 的转换。

#### 控制台升级
1. 在实例详情中，单击您所需要升级的实例数据库版本其后的【升级】（MySQL 5.7 无法升级到更高版本，无【升级】按钮）。
![][image-1]
2. 在【数据库版本】选项中选择需要的数据库版本，单击【升级】。数据库版本升级涉及到数据搬迁，所以在升级完成时会发生秒级的 MySQL 数据库连接闪断。可在发起升级时选择切换时间为【维护时间内】，会在实例升级完成后的下一个【维护时间】内发起切换。
需要注意的是，选择切换时间为【维护时间内】时，数据库规格升级完成时不会立即切换，会保持同步直到实例的【维护时间】内发起切换，因此可能会延长整个实例升级所需时间。
更详细的切换时间设置说明请查看：[升级数据库规格中的切换时间说明部分](https://cloud.tencent.com/document/product/236/7271)。
![][image-2]

[image-1]:	//mc.qcloudimg.com/static/img/30eb65a62102eea61a48422a404df814/4.png
[image-2]:	//mc.qcloudimg.com/static/img/a4b395e9a85a4a289b016cf2ae1c4a14/5.png
