1. 登录腾讯云 [管理控制台](https://console.cloud.tencent.com/)，进入管理中心后，在【云产品】模块找到【云数据库 TencentDB】，单击关系型数据库进入云数据库管理页面；也可以通过最近访问中单击关系型数据库快速进入。
![](https://main.qcloudimg.com/raw/dd64658acc7a9dd50163f14b101bdf7b.png)
2. 在关系型数据库页面，单击【MySQL】下的【实例列表】，找到目标地域（此例中以广州为例）中待重置密码的 MySQL 数据库实例，单击【实例名】或者【管理】按钮，进入 MySQL 数据库管理页面。
![](https://main.qcloudimg.com/raw/e8bb2676a5f71e72bdc3823d50f09a85.png)
3. 在 MySQL 数据库管理页面，单击【数据库管理】下的【账号管理】进入帐号管理页面后，找到需要重置密码的帐号，单击【更多】 > 【重置密码】。
![](https://main.qcloudimg.com/raw/808962974f71c45fb6cb7c69ae8a08e4.png)
4. 在重置密码页面，输入新密码和确认密码等信息，单击【确定】即可完成密码重置。
![](https://main.qcloudimg.com/raw/013d7804bff33787e900ea7977b28d10.png)

> **注意**
> 
> 1. 云数据库 MySQL 的重置密码功能已接入[CAM](https://cloud.tencent.com/document/product/236/14469)权限管理，强烈建议对此接口（重置密码）或敏感资源（此指云数据库 MySQL实例）权限收紧，只授权给应该授权的人员。
> 2. 数据库密码建议定期更换，最长间隔不超过3个月
> 3. 数据库密码规格需要8-64个字符，至少包含英文、数字和符号 _+-&=!@#$%^*() 中的2种
