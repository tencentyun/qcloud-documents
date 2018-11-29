## Batch Renewal
1. Log in to the [Cloud Database Console](https://console.cloud.tencent.com/cdb), select one or more instances to be renewed, and click "Renewal".
![](https://mc.qcloudimg.com/static/img/83008284f2d39df398d2cce0cc3eb706/check_one.png)
2. Select the renewal period, click "OK" to go to the next step.
![](https://mc.qcloudimg.com/static/img/2e4a806ce72aeacfc9fd0ca2d4446bfb/check_two.png)
3. Confirm the order information before you click "Confirm Purchase".
![](https://mc.qcloudimg.com/static/img/6a6ca027e73ae123bef06cbc443bcf9d/check_three.png)
4. After the order is paid, you can continue to view the order or jump to the console.
![](https://mccdn.qcloud.com/img56825d7c5d5ea.png)

## Batch Rollback

You can roll back a database or table on Tencent Cloud platform. Based on cold backup and binlog, rollback feature can be used to roll back data in real time. The cloud database rollback tool can roll back the cloud database or table to the specified time by rebuilding images and real-time logs regularly, and ensure that all data have the same time slice. During the rollback, the access to the original database or table is not affected. A rollback operation can generate a new database/table. After the rollback is finished, you can see the original database/table and the new database/table.

>**Note:**  
>Cloud database does not change any user data. The data damaged due to personal reasons can be automatically recovered through rollback.

### Detailed Procedure of Batch Rollback

1. Log in to the [Cloud Database Console](https://console.cloud.tencent.com/cdb), select one or more instances to be rolled back, and click "More Operations" -> "Rollback".
![](https://mc.qcloudimg.com/static/img/38b5002d8b4d158a5c57c150b50277ad/reback_one.png)
2. Select the rollback method, specify the database/table to be rolled back and the rollback time, and then click "Batch Rollback".
>**Note:**  
>Each instance can be specified with only one rollback time.</blockquote>
![](https://mc.qcloudimg.com/static/img/7a01be7903fd592133ea40b88b1b399c/reback_two.png)
3. After the submission is successful, the list of tasks performed on the cloud database is displayed, and you can view the rollback progress.
![](https://mc.qcloudimg.com/static/img/0a0cd866d319f103dc452fc39c9e7a54/reback_three.png)
4. Find the rollback instance and click "Manage" in "Operation". In the instance page, click "Operation Log" and select "Rollback Log" to view rollback history and current progress.
![](https://mc.qcloudimg.com/static/img/3faa954178e5e2e1b4a3e99b6597fd89/reback_four.png)

## Batch SQL Operation

This feature allows you to execute SQL statements on multiple instances or databases selected. You can also use this feature to create database/table and change table structure in batches to complete initialization or modification of multiple instances. To use this feature, make sure that the user name and password of the selected instance are consistent.

### Procedure of Batch SQL Operation

1. Log in to the [Cloud Database Console](https://console.cloud.tencent.com/cdb), select one or more instances on which the SQL operation is performed and click "More Operations" -> "SQL Operation".
![](https://mc.qcloudimg.com/static/img/e404ae00352e6118163f7a6701edd228/sql_one.png)
2. Select the instance or database to be operated on, and click "Next" to continue.
![](https://mc.qcloudimg.com/static/img/2301e2abe6a5486c4764aa1d75227565/sql_two.png)
3. Select the SQL file. If you cannot find the required SQL file, click "Add File" to upload one.
![](https://mc.qcloudimg.com/static/img/81a527221f924a30907f21bc79f07993/sql_three.png)
4. Confirm the instance or database to be operated on and the SQL file. Then, enter the password if all information is correct, and click "Start".
![](https://mc.qcloudimg.com/static/img/cbf17bc5623e08a61bcd0235a20cf3d7/sql_four.png)
5. After the operation is submitted, you can view the task information in "Task List".
![](https://mc.qcloudimg.com/static/img/1a3e03af04e2c2703a94aef948dede24/sql_five.png)

