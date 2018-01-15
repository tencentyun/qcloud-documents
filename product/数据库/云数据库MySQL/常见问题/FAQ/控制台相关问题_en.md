### 1. How to reset MySQL password?
For more information on on how to reset password, please see [Reset Password](https://cloud.tencent.com/document/product/236/10305).

### 2. How large is the MySQL instance storage space?
You can view the instance storage space in the instance details page in console.
**Step 1:** Log in to Tencent Cloud [Console](https://console.cloud.tencent.com/), and click "Cloud Database" in "Cloud Products" to go to the relational database page.
![](//mc.qcloudimg.com/static/img/00ff8ac563c02a5f661a1b47284f92dc/image.png)
**Step 2:** On the relational database page, click "Instance List" under "MySQL", and locate the MySQL database instance for which you want to reset password in the target region (in this example, it is Guangzhou). Click the instance name or "Manage" button to go to the MySQL database management page.
![](//mc.qcloudimg.com/static/img/62b1e4ab9953e54eab6c53da62ad6436/image.png)
**Step 3:** In the MySQL database management page, you can view the instance's storage space in the configuration information of instance details.
![](//mc.qcloudimg.com/static/img/6572eabefce378b96a06f983dea04d0e/image.png)

### 3. How to view the MySQL data sheet?
You can view and modify the data sheet via PMA.
![](//mc.qcloudimg.com/static/img/ce1c2957c302e865ac453e111bf3f0e9/image.png)
   
### 4. Why the max_connections value of MySQL always displays as 1,000 in the instance monitor, instead of the actual maximum number of connections?
In the instance monitor, the value of max_connections is fixed, but you can modify it. You can view the number of currently open connections as shown in the figure below:
![](//mc.qcloudimg.com/static/img/46ef7ad72797eb8115819a3a56fd01a1/image.png)

### 5. How to know the count of accesses to an MySQL instance?
You can view the count of accesses to an MySQL instance in the instance details page in console.
Step 1: Log in to Tencent Cloud [Console](https://console.cloud.tencent.com/), and click "Cloud Database" in "Cloud Products" to go to the relational database page.
![](//mc.qcloudimg.com/static/img/00ff8ac563c02a5f661a1b47284f92dc/image.png)
Step 2: On the relational database page, click "Instance List" under "MySQL", and locate the MySQL database instance for which you want to reset password in the target region (in this example, it is Guangzhou). Click the instance name or "Manage" button to go to the MySQL database management page.
![](//mc.qcloudimg.com/static/img/62b1e4ab9953e54eab6c53da62ad6436/image.png)
Step 3: In the MySQL database management page, you can view the count of accesses to the instance in the configuration information of instance details.
![](//mc.qcloudimg.com/static/img/2bfa1b9d421be3cc1e83dbd5a7a26d0c/image.png)
### 6. When will MySQL temporary instances be available?
Tencent Cloud will notify you of the availability of temporary instances by publish a notice. Please visit [Tencent Cloud website](https://cloud.tencent.com/) from time to time for updates.

### 7. How to get informed of insufficient disk space?
The monitoring center monitors the disk space of cloud databases. When over 90% of the cloud database space is occupied, text message and e-mail alarms are triggered. You simply need to configure the alarm recipient in Cloud Monitoring, who will receive the alarms in case of insufficient disk space. For more information on how to configure alarm recipient, please see [Alarm](https://cloud.tencent.com/document/product/236/8457).
