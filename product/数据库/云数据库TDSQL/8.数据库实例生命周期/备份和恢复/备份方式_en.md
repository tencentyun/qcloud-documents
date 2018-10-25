## Backup Methods
Currently, the cloud database supports full backup and incremental backup.

#### 1. Full Backup

(1) You can set the start time and storage period for full backup. By default, the backup starts at 00: 00 - 05: 00 in the morning, during which the performance is relatively low, and the storage period is 7 days (30 days by default for finance cloud).

### 2. Incremental Backup by Binlog
Binlog is generated in real time which occupies certain disk space, and regularly uploaded to the backup system of the cloud database.

### 3. Backup by LZ4 compression 
For more information, please see [How to Decompress Backup and Log Files](https://cloud.tencent.com/document/product/237/2088).

