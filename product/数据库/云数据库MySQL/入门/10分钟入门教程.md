您可以通过本教程了解，如何创建环境（我们将此环境称为“实例”）来运行 MySQL 数据库、连接数据库以及删除数据库实例。

### 步骤 1 ：创建 MySQL 数据库实例
在此步骤中，我们将创建一个 CDB for MySQL 数据库实例，该实例将采用按量计费的付费方式，1000 MB 的内存规格以及 50 GB 的硬盘规格。
1. 登录 [腾讯云控制台][1]，单击导航条中的【云产品】>【基础产品】>【数据库】>【关系型数据库】，或直接点击进入 [云数据库控制台][2]。
![][image-1]
2. 单击【新建】按钮，进入云数据库 MySQL 购买界面。
![][image-2]
3. 您现在可配置数据库实例。下面的列表显示了可在本教程中使用的示例设置：
	* 计费模式：选择按量计费。有关计费模式的更多信息，请参阅 [按量计费说明](https://www.qcloud.com/document/product/555/9617) 和 [预付费计费说明](https://www.qcloud.com/document/product/555/9618)。
	* 地域和可用区：建议选择最靠近您客户的地域。有关地域和可用区的更多信息，请参阅 [地域和可用区](https://www.qcloud.com/document/product/236/8458)。
	* 网络：本例中选择基础网络。有关网络环境的更多信息请参阅 [网络环境](https://www.qcloud.com/document/product/213/5227)。
	* 数据库版本：本例中选择 MySQL5.6。
	* 实例规格和硬盘：本例中选择 内存 1,000 MB 和 硬盘 50GB。您最多可以扩展至内存 488,000 MB 和硬盘 6,000 GB。
	* 数据复制方式：本例中选择异步复制。有关数据复制方式的更多信息，请参阅 [数据实例复制](https://www.qcloud.com/document/product/236/7913)。
	* 指定项目：本例中选择默认项目。
单击 【开通】。
![](//mc.qcloudimg.com/static/img/fe92ec47b00bf083295a9079acf09d87/image.png)
4. 等待 1 -2 分钟，（系统）完成数据库创建。创建过程中，数据库实例的状态将保持为 **发货中**，直至数据库实例创建完成，状态转换为 **初始化**。新的数据库实例会显示在 CDB 控制台上的数据库实例列表中。
![](//mc.qcloudimg.com/static/img/096e4e8126e37d2247f29bb217fc6573/image.png)
5. 初始化数据库实例。新购买的实例需要初始化后方可使用，单击 **操作** 栏目的【初始化】按钮，进入初始化设置页面。
![](//mc.qcloudimg.com/static/img/ee4847572a1c29f29aac3b42130c1cbf/image.png)
6. 配置初始化相关参数，然后单击【确定】开始初始化。
	- 支持的字符集：本例中选择 UTF8。
	- 表名大小写敏感：默认为是。
	- 自定义端口：默认为 3306。
	- root账户密码：设置 root 账户的密码。
	- 确认密码：再次输入密码。
![](//mc.qcloudimg.com/static/img/a1b69801dc18d284ef8b0f3ea777265b/image.png)
7. 目标 MySQL 实例的状态变为“**运行中**”，说明已初始化成功。
![](//mc.qcloudimg.com/static/img/74d297059388f2ad3de8ee1158c87409/image.png)

### 步骤 2： 登录 MySQL 数据库实例
在此步骤中，我们将登录到刚才创建的 MySQL 数据库实例。
1. 在 [云数据库控制台][2] ，在刚才创建的实例的 **操作** 栏目中单击【登录】。
![](//mc.qcloudimg.com/static/img/ac3c4021591c4af5f0d218d0ab03f167/image.png)
2. 在数据管理控制台的登录界面，帐号输入 root，密码为之前在初始化选项中配置的 root 账户的密码，单击【登录】。
![](//mc.qcloudimg.com/static/img/b5538d93dc27d99af6fed9f0e5c9b798/image.png)
3. 在数据管理页面可以查看实例的状态和基本信息。
![](//mc.qcloudimg.com/static/img/0bf7a42b20c6d701f572d5c48de93e4e/image.png)

### 步骤 3： 连接 MySQL 数据库实例
在此步骤中，我们将通过 phpMyAdmin 连接到刚才创建的 MySQL 数据库实例。
1. 在数据管理页面单击【返回PMA】，进入 phpMyAdmin。
![](//mc.qcloudimg.com/static/img/8a33f0b349c501cad1d3508c90246827/image.png)
2. 您现在已经通过 phpMyAdmin 成功连接到 MySQL 数据库，在此页面上您可以看到 MySQL 数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](//mc.qcloudimg.com/static/img/c8f60117f5aec772663d3c7890c96b1e/image.png)

### 步骤 4： 销毁 MySQL 数据库实例
在此步骤中，我们将通过 CDB 控制台轻松删除 MySQL 数据库实例。建议删除不再使用的实例，以免继续为其付费。
1. 返回 [云数据库控制台][2] ，在刚才创建的实例的 **操作** 栏目中单击【更多】 > 【销毁】。![](//mc.qcloudimg.com/static/img/281136fa83efaeb10d68b41127bbdab1/image.png)
2. 单击【立即销毁】即可销毁 MySQL 数据库实例，您将无需再为其付费。
![](//mc.qcloudimg.com/static/img/1431f9c680738c534f03985f46b62830/image.png)

### 后续步骤
您已通过 CDB for MySQL 创建、连接和删除 MySQL 数据库实例。借助 CDB for MySQL，您能够在云中轻松设置、操作和扩展关系型数据库。
现在，您已经了解了如何通过 CDB 创建和连接 MySQL 数据库，您可以继续学习下一个教程，以了解如何在 phpMyAdmin 上创建数据库和数据表。[建立数据库和表](https://www.qcloud.com/document/product/236/8465)。

[1]:	https://console.qcloud.com/
[2]:	https://console.qcloud.com/cdb
[3]:	https://www.qcloud.com/document/product/378/3629
[4]:	https://www.qcloud.com/document/product/236/8458
[5]:    https://www.qcloud.com/document/product/213/5227
[6]:    https://www.qcloud.com/document/product/236/7913

[image-1]:  https://mc.qcloudimg.com/static/img/c5a7e2e50a04631d861d899c1e71598b/step1.png
[image-2]:  https://mc.qcloudimg.com/static/img/c8d25b4002230535f28dbc59ae58318b/step2.png
[image-3]:  https://mc.qcloudimg.com/static/img/876e8649c8f1b41fe792fd86e08d993a/step3.png
[image-4]:	https://mc.qcloudimg.com/static/img/745bffd1e06ffd5e7c7bb8f87766050b/step4.png
[image-5]:	https://mc.qcloudimg.com/static/img/1f4c68979c718e4a75734ca91f37c4ac/step5.png
[image-6]:	https://mc.qcloudimg.com/static/img/a4403f63257ebe96b62867f22417d356/step6.png
