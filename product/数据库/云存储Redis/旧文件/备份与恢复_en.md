## 1 Automatic Backup of Instance

An instance can be automatically backed up once a day, and the backup method is follows:

  1)	Enter instance details page, click "Backup and Recovery" tab, select "Auto Backup Settings", and click the  "Settings" button.
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/beifenhuifu-1.png)

  2)	Select a day to create a backup and specify the time period of starting the backup, and then click "Save".
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/beifenhuifu-2.png)

  3) The backup will start within the specified time period. When the backup is in progress, you can check the task status in the task center. When the backup is finished, you can check the generated backup in "Backup and Recovery".
	
  <span style = "color:#F00">Note: If affected by any relevant process, the backup may be delayed.
	
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/beifenhuifu-3.png)
## 2	Recovery from Backup

  You can recover an entire instance or a specified Key from a backup.
	
 <span style = "color:#F00"> Note: Recovering the entire instance will interrupt the service provided by it.</span>
	
### 2.1	Recovering an Instance

  1)	Select the backup to be rolled back in "Backup and Recovery", and click "Recover Instance".
  
  2)	In the pop-up box for confirming instance recovery, enter the password for the instance, and click "Recover".
  
  <span style = "color:#F00">Note: The password here is the instance password set by the user, rather than the<instance ID: instance password>link password for accessing the instance.</span>
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/beifenhuifu-4.png)

  3)	When the instance goes into "Recovering Backup by Backup ID" status, you can check the task status in the task center. When the instance goes into a "Running" status, it can work normally.
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/beifenhuifu-5.png)

### 2.2	Recovering a Specified Key

  1)	Select the backup to be rolled back in "Backup and Recovery", and click "Recover Instance".
	
  2)	In the pop-up box for confirming instance recovery, enter the password for the instance, and click "Next".
	
  <span style = "color:#F00">Note: The password here is the instance password set by the user, rather than the<instance ID: instance password>link password for accessing the instance.</span>
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/beifenhuifu-6.png)

  3)	Enter the key to be recovered from the backup (For multiple keys, they need to be separated by semicolons). Then click "Finish". When the instance goes into "Recovering Backup by Key" status, you can check the task status in the task center. When the instance goes into a "Running" status, it can be put into use.
  
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/beifenhuifu-7.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/beifenhuifu-8.png)
