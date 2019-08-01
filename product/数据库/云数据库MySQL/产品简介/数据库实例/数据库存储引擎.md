存储引擎是指表的类型，数据库的存储引擎决定了表在计算机中的存储方式。虽然 MySQL 数据库支持功能不同的多种存储引擎，但并非所有引擎都为恢复和数据耐久性而进行了优化。时间点还原和快照还原等腾讯云数据库 MySQL 功能需要可恢复的存储引擎，并且只有 InnoDB 存储引擎支持这些功能。

腾讯云数据库 MySQL 默认支持 InnoDB 存储引擎，并在 MySQL 5.6 及以上的版本中，不再支持 MyISAM 存储引擎。主要原因如下：
- 在目前的 MySQL 版本中，TencentDB 对 InnoDB 做了很多内核优化，已经具有明显的性能优势。
- MyISAM 采用的是表级锁机制，而 InnoDB 是行级锁机制，通常情况下 InnoDB 具有更高的写入效率。
>?
>- 表级锁是 MySQL 中锁定粒度最大的一种锁，表示对当前操作的整张表加锁。
>- 行级锁是 MySQL 中锁定粒度最细的一种锁，表示只针对当前操作的行进行加锁。
- MyISAM 对数据完整性的保护存在缺陷，且这些缺陷会导致数据库数据的损坏甚至丢失。另外，这些缺陷很多是设计问题，无法在不破坏兼容性的前提下修复。
- MyISAM 向 InnoDB 的迁移代价低，大多数应用仅需要改动建表的代码即可完成迁移。
- MyISAM 的发展在向 InnoDB 转移，在最新的官方 MySQL  8.0 版本中，系统表均已采用 InnoDB。

更多信息请参见 [InnoDB 简介](https://dev.mysql.com/doc/refman/5.7/en/innodb-introduction.html) 和 [MyISAM 简介](https://dev.mysql.com/doc/refman/5.7/en/myisam-storage-engine.html)。
