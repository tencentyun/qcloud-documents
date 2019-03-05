# Restoring a Database Instance to a Specified Time

You can use the rollback tool at console to roll back a database or table on Tencent Cloud platform. Based on cold backup and binlog, the tool can be used to roll back data in real time.

The CDB rollback tool can roll back the cloud database or table to the specified time by rebuilding images and real-time logs regularly, and ensure that all data have the same time slice. During the rollback, the access to the original database or table is not affected.
Currently, a rollback operation can generate a new database or table. After the rollback is finished, you can see the original database or table, as well as the new database or table.

> Note:
>
> CDB will not change any user data. The data damage due to personal reasons can be automatically repaired through rollback.
> * A rollback cannot be initiated until the database goes through cold backup successfully at least once.

## CDB Management Console
** To restore a database instance to the specified time, please proceed as follows:**

### Performing Rollback on a Single Instance:
1. Log in to Tencent Cloud CDB Management Console and open CDB Console via the URL [https://console.cloud.tencent.com/cdb](https://console.cloud.tencent.com/cdb)
2. In the instance list, select the instance to be rolled back, and select "Manage" in "Operation".
3. Click "Rollback" at the upper right corner of instance details page, and the rollback operation page will be displayed.
4. Select the database table to be rolled back. You can select some of the database tables or all the database tables, and set the time to roll back to. To specify the name of new database table created after the rollback, enter the custom name in "Set name of the new database table" column. After finishing the setting, click "Batch Rollback".
![](https://mc.qcloudimg.com/static/img/0337bf681fe69b9c05bf97040f8188a9/image.png)
5. After the rollback submission succeeds, you can view the progress in "Rollback Log".
![](https://mc.qcloudimg.com/static/img/eae743ae57be74cc901b398ceea75665/image.png)

### Batch Rollback:
For more information on batch rollback, refer to "Batch Operation": [Click to view "Batch Rollback"](https://cloud.tencent.com/document/product/236/7262#2.E6.89.B9.E9 .87.8F.E5.9B.9E.E6.A1.A3 "点击查看【批量回档】")
