## 操作场景
本文为您介绍对已经购买的 MySQL 数据库执行初始化操作。

## 前提条件
已购买 MySQL 数据库，请参见 [购买指引](https://cloud.tencent.com/document/product/236/5160) 购买 MySQL 数据库。

## 操作步骤
1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)。
2. 在左侧导航选择【实例列表】页签。
3. 选择状态为【未初始化】的 MySQL 实例，在【操作】列，单击【初始化】。
![](https://main.qcloudimg.com/raw/a5d701f0c9d0ae6b78f0a22959dbe1a1.png)
4. 在弹出的初始化页中，配置初始化相关参数，单击【确定】开始初始化。
 - **支持字符集**：选择 MySQL 数据库支持的字符集。
 - **表名大小写敏感**：表名是否大小写敏感，默认为是。
 - **自定义端口**：数据库的访问端口，默认为3306。
 - **设置root帐号密码**：新创建的 MySQL 数据库的用户名默认为 root，此处用来设置此 root 帐号的密码。
 - **确认密码**：再次输入密码。
 ![初始化实例](https://main.qcloudimg.com/raw/b9e2635a5e83618bb5bb48a6e40fcd5f.png)
5. 返回实例列表，目标 MySQL 实例的状态变为【运行中】，说明已初始化成功。
![](https://main.qcloudimg.com/raw/1fe665a25b68e24a043039da9f6916db.png)
