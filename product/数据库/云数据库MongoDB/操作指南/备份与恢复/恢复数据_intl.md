You can recover data in TencentDB for MongoDB by following the steps below<br>
1. In the backup recovery list, click **Rollback** for a backup file to go to the rollback page, where you can select the time point and type for the rollback. The rollback includes the entire instance rollback and the database table rollback. The specific operations are shown as below:<br>
![](https://main.qcloudimg.com/raw/465f02c986bd98eb401ac4ef2aa19025.png)
![](https://main.qcloudimg.com/raw/9b1edc4f0626c1e1b3d8c15298cecff7.png)
![](https://main.qcloudimg.com/raw/b5dc990e9bc750dc5a1871fb599470dd.png)
2. The system creates a temporary instance free of charge to store the rollback data. The user name and password of the temporary instance are the same as those of the original instance. The original instance remains unchanged and the business will not be affected.<br>
3. Access the temporary instance to confirm rollback data within 48 hours after the completion of rollback.<br>
For the temporary instance generated in the rollback, you can perform any of the following:<br> 
(1) Conversion: Convert the temporary instance to a formal business instance independent of the original instance.<br>
(2) Replacement: Replace the original instance with the temporary instance (bind the private IP of the original instance to the temporary instance).<br> 
If no action is performed within 48 hours, the temporary instance will be terminated.
![](https://mc.qcloudimg.com/static/img/4729ddc8384362dfb9a601343e928807/huifu2.png)

