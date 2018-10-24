 在此步骤中，我们将对已经购买的 MySQL 数据库执行初始化操作。
 ### 1. 登录 MySQL 控制台

在 [腾讯云控制台](https://console.cloud.tencent.com/) 的左上角，单击【云产品】菜单下的【关系型数据库】，进入 MySQL 数据库产品页面。
![](https://main.qcloudimg.com/raw/9605667d15d3d7ea2bd535cc644dc9a8.png)
### 2. 初始化实例
在关系型数据库页面中，单击【MySQL】下的【实例列表】，找到目标地域（此例中以广州为例）中要操作的状态为“**未初始化**” MySQL 数据库实例。
![](https://mc.qcloudimg.com/static/img/bc6f4a538ac4bf614e3a270338a7be4c/image.png)
单击【初始化】对要操作的 MySQL 实例执行初始化。
![](https://mc.qcloudimg.com/static/img/fe0ebd9776b6f920338e9436b82024a3/image.png)

### 3. 配置初始化参数
在【初始化】弹框中，配置初始化相关参数，然后单击【确定】开始初始化。
- **支持的字符集**：选择 MySQL 数据库支持的字符集。
- **表名大小写敏感**：表名是否大小写敏感，默认为是。
- **自定义端口**：数据库的访问端口，默认为 3306。
- **root 账户密码**：新创建的 MySQL 数据库的用户名默认为 root，此处用来设置此 root 账户的密码。
- **确认密码**：再次输入密码。
![](https://mc.qcloudimg.com/static/img/a1b69801dc18d284ef8b0f3ea777265b/image.png)

### 4. 实例初始化完成
目标 MySQL 实例的状态变为“**运行中**”，说明已初始化成功。
![](https://mc.qcloudimg.com/static/img/81234ad724b600506564d920b051ce3f/image.png)
