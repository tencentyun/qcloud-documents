### 1. Will the current table data be overwritten or a new table be created when a table is rolled back?
A rollback operation can generate a new database/table in the original instance. After the rollback is finished, you can see both the original database/table and the new database/table. The database table name after rollback is "original database table name _bak".
### 2. How to perform rollback operations in batch for MySQL?
See [Batch Rollback](https://cloud.tencent.com/document/product/236/8466#.E6.89.B9.E9.87.8F.E5.9B.9E.E6.A1.A3).
### 3. Some of the data is accidentally deleted during the storage procedure which was just executed for MySQL and no backup was created for these data - Can the lost data be restored?
You can use the rollback feature in console.
You can restore the data generated at any time point in the last three days.
![](//mc.qcloudimg.com/static/img/06dc8e407e02ea57a9754f07a92118f3/image.png)
