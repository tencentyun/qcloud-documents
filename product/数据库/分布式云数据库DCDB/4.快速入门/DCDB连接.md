以下为通过MySQL命令行连接DCDB的相关操作流程。
## 连接步骤
### 新建用户权限
1. 在 [DCDB控制台](https://console.cloud.tencent.com/dcdb) 中，单击需要操作的实例最右方的【管理】，进入实例详情页面。
![](https://mc.qcloudimg.com/static/img/e1220243ef39496cd62c0f5982fc87fe/r1.png)
2. 在实例详情页面单击【账号管理】，进入帐号管理页面。
![](https://mc.qcloudimg.com/static/img/4e60badccaa63bf1632dbe1ed948793f/r2.png)
3. 单击创建帐号，依次输入用户名、主机、密码、备注，检查无误后单击【确定】，进入设置权限页面。
	> 主机名实际是网络出口地址。这里支持%这样的匹配方式，代表所有IP均可访问。
	
	![](https://mc.qcloudimg.com/static/img/00f4abaa96562c16f0aa3a3af0e30c00/r3.png)
4. 在设置权限页面，根据需求分配权限后，单击【保存设置】即可完成权限分配。若需要稍后设置权限，单击【之后设置】即可。
	> 通过左边的导航栏，我们提供了完全兼容MySQL管理方式的图形化界面，权限管理可以细化到列级。

	![](https://mc.qcloudimg.com/static/img/9029ee57e3892fe92ac0c3a5ead80dbb/r4.png)

5. 完成创建后，单击【修改权限】可以修改用户权限，单击【克隆帐号】可以完全复制当前帐号权限来新建一个帐号。单击【更多】可以重置密码和删除帐号。
	![](https://mc.qcloudimg.com/static/img/5f87261b43fc058adbd66b486a69e571/r5.png)

### 获取外网地址
1. 进入实例详情页面，在基本信息中找到外网地址，单击【打开】。

	![](https://mc.qcloudimg.com/static/img/fc3d50322e3547722a8d3e29e479b2e5/r6.png)	

2. 稍等片刻后，即可获得外网地址以及端口号。
	> DCDB提供了唯一的IP，端口供用户访问和使用。

	![](https://mc.qcloudimg.com/static/img/234c21d6897515b6623055301771dd24/r7.png)

### 完成连接命令
- 在创建用户和获取外网地址后，可通过第三方工具进行连接，这里以MySQL命令行连接为例。

		mysql -h外网地址 -P端口号 -u用户名  -p
		Enter password: **********（输入密码）

- 将相关代码正确输入后，显示如下信息，成功连接数据库，下一步即可进行数据库内相关操作。

		Welcome to the MySQL monitor.  Commands end with ; or \g.
