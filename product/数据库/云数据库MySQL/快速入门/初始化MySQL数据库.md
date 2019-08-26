## 操作场景
本文为您介绍对已经购买的 MySQL 数据库执行初始化操作。

## 前提条件
已购买 MySQL 数据库，请参见 [购买指引](https://cloud.tencent.com/document/product/236/5160)。

## 操作步骤
1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)。
2. 在左侧导航选择【实例列表】页签。
3. 选择状态为【未初始化】的 MySQL 实例，在操作列单击【初始化】。
![](https://main.qcloudimg.com/raw/5161cf5c35bf952ba6b1f0ba77cc6f07.png)
4. 在弹出的初始化对话框中，配置初始化相关参数，单击【确定】开始初始化。
 - **支持字符集**：选择 MySQL 数据库支持的字符集。
 - **表名大小写敏感**：表名是否大小写敏感，默认为是。
 - **自定义端口**：数据库的访问端口，默认为3306。
 - **设置root帐号密码**：新创建的 MySQL 数据库的用户名默认为 root，此处用来设置此 root 帐号的密码。
 - **确认密码**：再次输入密码。
![](https://main.qcloudimg.com/raw/6cf4875a39cb614d83fd90b70ef8f617.png)
5. 返回实例列表，目标 MySQL 实例的状态变为【运行中】，说明已初始化成功。
![](https://main.qcloudimg.com/raw/67bc351b68283f9b9c0b163f95d8d783.png)
