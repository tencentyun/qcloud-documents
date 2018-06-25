
策略是用于定义和描述一条或多条权限的语法规范。CAM 支持两种类型的策略，预设策略和自定义策略。
	
## 预设策略
	
预设策略是由腾讯云创建和管理的一些常见的权限集合，如超级管理权限和资源管理权限等，粒度比较粗。这类策略不可以编辑。
在预设策略的界面中，我们可以通过服务类型还有关键字来进行搜索（如服务类型为全部服务，关键字为 ad）。
![](https://mc.qcloudimg.com/static/img/e47f92362e4eaa7474e1c0809eca10f4/image.png)


		
## 自定义策略

由用户创建的策略，允许作细粒度的权限划分。为某DBA关联一条策略，使其有权管理 CDB 实例，而无权管理 CVM 实例。自定义策略根据创建方式的不同分为按策略生成器创建的策略、按业务权限创建的策略和按语法创建的策略。
按策略生成器创建的策略,通过从策略向导中选择服务和操作，并定义资源，自动生成策略语法，简单灵活，优先推荐使用；
按业务权限创建的策略，由用户设置，权限粒度可由业务接入时控制，解决对权限划分有一定要求，但并不复杂的用户诉求；
按语法创建的策略，由用户设置，权限粒度灵活，由用户把控，解决对权限精细划分有较高要求的用户诉求。
	
	
## 创建自定义策略
### 按策略生成器创建

1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/)>单击右上角帐号名称>单击【访问管理】，进入 [访问管理](https://console.cloud.tencent.com/cam)页面。
![](https://mc.qcloudimg.com/static/img/70f40a3945e8491f98bad1e86bb13add/ff+%281%29.png)

2. 单击【策略管理】>【自定义策略】>【按策略生成器创建】，进入创建页面。
![](https://mc.qcloudimg.com/static/img/81536116ca7d59290890583b48e0b642/image.png)

3. 选择访问管理的效果（如允许）、想要管理的服务（如归档存储）以及操作，填写资源描述（需要关联对象的服务要求填写资源描述，资源描述的具体定义和示例可参考【说明】链接），单击【添加声明】>【下一步】，进入编辑策略步骤。
![](https://mc.qcloudimg.com/static/img/7eaa529adf79788dd71921800275ca52/image.png)
	部分服务的操作无需关联对象，不需要填写资源描述。
![](https://mc.qcloudimg.com/static/img/8ee4cdbe52f3ca285a5e6f7618e60c94/g+%281%29.png)
	用户可以在一条策略中添加多条声明（如下图添加的是归档存储的 AboutVaultLock 和短信的 SmsQcloudcom）。
![](https://mc.qcloudimg.com/static/img/1e02503f7caaeab2a13f1a81998f35d1/image.png)
4. 单击【创建策略】即可。其中策略名称和策略内容是自动生成的，策略名称中的前缀 "policygen" 是固定的，后面的数字是根据创建的时间生成的，策略内容与第 3 步的服务和操作对应，用户可对其进行微调。
![](https://mc.qcloudimg.com/static/img/e544dff9d49760af82f582a169583710/image.png)


### 按业务权限创建

1. 登录腾讯云控制台，进入 [策略管理](https://console.cloud.tencent.com/cam/policy)页面，单击【自定义策略】>【按业务权限创建】，进入创建页面。
![](https://mc.qcloudimg.com/static/img/33495c7cc0cf33b0c1c63784b0ab475b/image.png)

2. 勾选出需要的业务至策略中并命名，单击【下一步】。
![](https://mc.qcloudimg.com/static/img/3dd92d1bd3ac368fa5930eff581aafed/image.png)

3. 将某些功能的权限开关置为【开】，并单击【下一步】。
![](https://mc.qcloudimg.com/static/img/a8268e994ab28579b349ebed30c7bd6b/image.png)

4. 单击【关联对象】，选出您想要关联的对象，单击【确认】>【完成】。
![](https://mc.qcloudimg.com/static/img/23885b53e01350406669cf2e98863108/image.png)

### 按策略语法创建

1. 登录腾讯云控制台，进入 [策略管理](https://console.cloud.tencent.com/cam/policy)页面，单击【自定义策略】>并单击【按策略语法创建】，进入创建页面。
![](https://mc.qcloudimg.com/static/img/e44addd7134cb52966ece2ba9e66c0b2/image.png)

2. 选择模版类型，并输入关键字进行搜索（如模版类型为全部模版，关键字为 a ），选择AdministratorAccess模版。
![](https://mc.qcloudimg.com/static/img/4a3abf6b7ed48f1dc78360db6cad4e1d/image.png)

3. 编辑策略内容，单击【创建策略】即可。其中策略名称和策略内容是自动生成的，策略名称中前缀 "policygen" 是固定的，后面的数字是根据创建的时间生成的。
![](https://mc.qcloudimg.com/static/img/b86a9a381cd252b515f9bec0ba5a720c/image.png)







