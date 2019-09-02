### 1. 如何重置 MySQL 的密码？
如何重置密码请参考 [密码重置](https://cloud.tencent.com/document/product/236/10305)。

### 2. MySQL 实例的存储空间是多少？
您可以在控制台的实例详情中查看实例的存储空间。
**步骤1：**登录腾讯云 [管理控制台](https://console.cloud.tencent.com/) ，进入管理中心后，在【云产品】模块单击【云数据库】，进入关系型数据库页面。
![](//mc.qcloudimg.com/static/img/00ff8ac563c02a5f661a1b47284f92dc/image.png)
**步骤2：**在关系型数据库页面，单击【MySQL】下的【实例列表】，找到目标地域（此例中以广州为例）中待重置密码的 MySQL 数据库实例，单击【实例名】或者【管理】按钮，进入 MySQL 数据库管理页面。
![](//mc.qcloudimg.com/static/img/62b1e4ab9953e54eab6c53da62ad6436/image.png)
**步骤3：**在 MySQL 数据库管理页面，实例详情中的配置信息，可以查看到实例的存储空间。
![](//mc.qcloudimg.com/static/img/6572eabefce378b96a06f983dea04d0e/image.png)

### 3. 怎样查看 MySQL 数据表?
您可以通过 PMA 查看数据表，修改数据表。
![](//mc.qcloudimg.com/static/img/ce1c2957c302e865ac453e111bf3f0e9/image.png)
   
### 4. MySQL 的 max_connections 实例监控中这个数值始终显示为 1000，而不是实际的当前最大连接数。
实例监控中 max_connections 这个数值是个定值来的，这个值也可以修改。要看现在的链接数可以查看当前打开链接数，如下图：
![](//mc.qcloudimg.com/static/img/46ef7ad72797eb8115819a3a56fd01a1/image.png)

### 5. 怎样才能知道 MySQL 实例的访问次数？
您可以在控制台的实例详情中查看实例的访问次数。
步骤1：登录腾讯云 [管理控制台](https://console.cloud.tencent.com/) ，进入管理中心后，在【云产品】模块单击【云数据库】，进入关系型数据库页面。
![](//mc.qcloudimg.com/static/img/00ff8ac563c02a5f661a1b47284f92dc/image.png)
步骤2：在关系型数据库页面，单击【MySQL】下的【实例列表】，找到目标地域（此例中以广州为例）中待重置密码的 MySQL 数据库实例，单击【实例名】或者【管理】按钮，进入 MySQL 数据库管理页面。
![](//mc.qcloudimg.com/static/img/62b1e4ab9953e54eab6c53da62ad6436/image.png)
步骤3：在 MySQL 数据库管理页面，实例详情中的配置信息，可以查看到实例的访问次数。
![](//mc.qcloudimg.com/static/img/2bfa1b9d421be3cc1e83dbd5a7a26d0c/image.png)
### 6. MySQL 的临时实例什么时间会有？
临时实例有上线的话，腾讯云会有公告通知的，您可以关注 [腾讯云官网](https://cloud.tencent.com/) 。

### 7. 如何获知磁盘空间不足？
监控中心对云数据库的磁盘空间进行了监控，当云数据库的使用空间超过 90% 的时候就会触发短信和邮件告警，这里只需要在云监控中配置好对应的告警接收人（如何配置请参考[告警功能](https://cloud.tencent.com/document/product/236/8457)），当空间不足的时候就能收到告警。
