With database rollback feature, the losses of system can be minimized. The full backups and log backups of CDB for SQLServer are kept for **7 days**, so the data can be rolled back to any time point within 7 days.
Use the following steps:
1.	Enter the instance details page, and click Rollback button
![](//mccdn.qcloud.com/static/img/6e9523611eb2bb6574c23bb78f2ed3c3/image.png)
2.	Select a database to be rolled back, set the rollback time, choose whether to overwrite the source database, and click "Next" to continue
![](//mccdn.qcloud.com/static/img/71e6e919e84f6c38e396daed4ea1c7fd/image.png)
3.	After the configured parameters are confirmed, click "Rollback" button to start the rollback task
![](//mccdn.qcloud.com/static/img/43835ee5e83586111988a40b2c77d346/image.png)
4.	The instance status becomes "In progress", and you can view the rollback progress in the task list
![](//mccdn.qcloud.com/static/img/6745a9fe2877d953d07de00cfaade272/image.png)
5.	Rollback is successful. Since you choose not to overwrite the source database, so you can see a generated clone database in the Database Management page
![](//mccdn.qcloud.com/static/img/5e8c765027e5acea83a52f4b7e8203d2/image.png)
Note: Currently, only local instances can be rolled back. You can choose to overwrite the source database or generate a clone database. If you generate a clone database, the disk space after rollback cannot exceed available space for instance, otherwise the rollback will fail.

