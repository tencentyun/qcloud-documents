## CDB for MySQL 存储引擎
CDB for MySQL默认支持InnoDB存储引擎，并在MySQL 5.6以上的版本中，不再支持MyISAM存储引擎。

## 为什么CDB不支持MyISAM
CDB for MySQL 不支持 MyISAM 引擎的主要原因有如下几个：

* 在目前的MySQL版本中，CDB对InnoDB做了很多内核优化，已经具有明显的性能优势。

* MyISAM采用的是表锁的锁机制，而Innodb是行锁锁机制，通常情况下InnoDB具有更高的写入效率。

* MyISAM 对数据完整性的保护存在缺陷，且这些缺陷会导致数据库数据的损坏甚至丢失。另外，这些缺陷很多是设计问题，无法在不破坏兼容性的前提下修复。

* MyISAM 向 InnoDB 的迁移代价低，大多数应用仅需要改动建表的代码即可完成迁移。

* MyISAM 的发展在向 InnoDB 转移，在最新的 5.7 版本中 MySQL 系统表均已采用InnoDB。

