Storage engines refer to table types. The storage engine of a database determines how the table is stored in the computer. Although MySQL supports multiple storage engines with varying capabilities, not all of them are optimized for recovery and data durability. Tencent Cloud database for MySQL features such as Point-In-Time restore and snapshot restore require a recoverable storage engine and are supported for the InnoDB storage engine only. Tencent Cloud database for MySQL supports InnoDB storage engine by default and no longer supports MyISAM engine from version 5.6 or later. For more information on InnoDB and MyISAM engines, please see [About InnoDB](https://dev.mysql.com/doc/refman/5.7/en/innodb-introduction.html) and [About MyISAM](https://dev.mysql.com/doc/refman/5.7/en/myisam-storage-engine.html).

The reasons why CDB for MySQL does not support MyISAM engine are as follows:
- CDB for MySQL greatly optimizes the kernels for InnoDB and achieves high performance.
- MyISAM uses the table-level locking (locking at the largest granularity (table) in MySQL), while InnoDB uses the row-level locking (locking at the smallest granularity (row) in MySQL, ). Generally, InnoDB has higher write efficiency.
- Defects are found in MyISAM's protection for data integrity, which may lead to data corruption or even loss. In addition, most of the defects are design errors, which cannot be fixed without breaking the compatibility.
- You do not need to spend much to move MyISAM to InnoDB. In most cases, this can be made by simply changing the code of the created table.
- MyISAM is developing towards InnoDB. The system tables in the latest MySQL 5.7 have adopted InnoDB.


