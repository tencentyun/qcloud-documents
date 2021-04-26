管理员和子用户仅能够由 **创建者** 或其他 **超级管理员** 进行设置。

## 注意事项
+ 可以直接为存量子用户关联策略，进行权限划分。
+ 预设管理员高于项目管理员，项目管理员高于普通子用户，当同时关联预设管理员策略、项目管理类策略、CDN 策略时，最终结果为所有权限的并集。

## 预设管理员配置示例
超级管理员设置步骤如下。
1. 登录 [访问管理](https://console.cloud.tencent.com/cam) 控制台，单击左侧【用户管理】，在页面内单击【新建用户】。
![](https://mc.qcloudimg.com/static/img/3d8ddebadc422c6a19be0f0a04ee2f21/create_user.png)
2. 输入管理员姓名、设置 **允许登录腾讯云**，输入 QQ 号、联系手机、联系邮箱等信息,单击【下一步】。
![](https://mc.qcloudimg.com/static/img/7aa429ae0459a5103278cc4921f6e759/create_child.png)
3. 勾选 **AdministratorAccess** 策略，单击【完成】，即完成超级管理员的创建。
![](https://mc.qcloudimg.com/static/img/2177ce9b753b67e9c41563f45a45aab2/child_policy.png)
超级管理员设置完成后，管理员使用其 QQ 号码及对应的 QQ 密码即可登录腾讯云官网进行管理操作。云资源管理员(策略名：QCloudResourceFullAccess)和财务管理员(策略名：QCloudFinanceFullAccess)的设置与此流程一致，在此不做介绍。

## 项目管理员配置示例
项目管理员能够管理指定项目下所有云资源。
### 创建项目管理员策略
1. 登录 [访问管理](https://console.cloud.tencent.com/cam) 控制台，单击左侧【策略管理】。
![](https://mc.qcloudimg.com/static/img/6f3cd3c38bdf918931010a4a9d12a3d8/policy_manage.png)
2. 进入【自定义策略】页面，单击【新建自定义策略】。
![](https://mc.qcloudimg.com/static/img/a29b5becbaec002762acb0a304712fc4/create_policy.png)
3. 在弹出的窗口中单击【按业务权限创建】创建策略。
![](https://mc.qcloudimg.com/static/img/b6a6e011879dde16de7eede6af3f11f4/policy_way.png)
4. 输入策略名，勾选服务类型为【项目管理】,单击【下一步】。
![](https://mc.qcloudimg.com/static/img/c4318a01a3d1304c7422a95b427b093e/service_type.png)
5. 开启【管理 CDN 业务项目内云资源】和【管理其他业务项目内云资源】功能，完成后单击【下一步】。
![](https://mc.qcloudimg.com/static/img/dfebfd2e913daef94444793c249ca8aa/policy_function.png)
6. 单击【关联对象】，为您的两项功能关联指定项目下的资源对象。
![](https://mc.qcloudimg.com/static/img/fc8846208269614856b381bfbe797a18/policy_link.png)
不同功能与对象的关联是互不干扰的，可以将【管理CDN业务项目内云资源】功能关联项目 A 和 B，【管理其他业务内云资源】功能关联项目 B。
![](https://mc.qcloudimg.com/static/img/bb3e54ed615a3b3acb79f2ca4e236a35/policy_link2.png)
7. 单击【完成】，可在自定义策略列表看到创建的策略。
![](https://mc.qcloudimg.com/static/img/bb1b980a2048e775d55b924112b6fdbf/create_policy_done.png)

### 创建项目管理员
1. 登录 [访问管理](https://console.cloud.tencent.com/cam) 控制台，单击左侧【用户管理】，在页面内单击【新建用户】。
![](https://mc.qcloudimg.com/static/img/3d8ddebadc422c6a19be0f0a04ee2f21/create_user.png)
2. 输入管理员姓名、设置 **允许登录腾讯云**，输入 QQ 号、联系手机、联系邮箱等信息，单击【下一步】。
![](https://mc.qcloudimg.com/static/img/c75f0ccb3c9ce66b65931332f239894b/create_projecet_manager.png)
3. 勾选已经创建好的项目管理员策略 **project_manage** 策略，单击【完成】，即完成项目管理员的创建。
![](https://mc.qcloudimg.com/static/img/14a35505579ef55fe56afca5fba09b1b/connect_policy.png)

## 子用户配置示例
假设您要配置某子用户，允许其查询【测试项目】中域名的消耗统计信息、管理【测试二项目】中域名的配置信息、刷新【测试项目三】中的 URL 资源。
### 创建子用户 CDN 策略
1. 登录 [访问管理](https://console.cloud.tencent.com/cam) 控制台，单击左侧【策略管理】。
![](https://mc.qcloudimg.com/static/img/6f3cd3c38bdf918931010a4a9d12a3d8/policy_manage.png)
2. 进入【自定义策略】页面，单击【新建自定义策略】。
![](https://mc.qcloudimg.com/static/img/a29b5becbaec002762acb0a304712fc4/create_policy.png)
3. 在弹出的窗口中单击【按业务权限创建】创建策略。
![](https://mc.qcloudimg.com/static/img/b6a6e011879dde16de7eede6af3f11f4/policy_way.png)
4. 输入策略名，勾选服务类型为【内容分发网络】,单击【下一步】。
![](https://mc.qcloudimg.com/static/img/8271a16f69d90b5950a81e42ba73e666/policy_cdn.png)
5. 开启【查看消耗数据及统计量】、【查询域名信息】和【刷新预热】功能，完成后单击【下一步】。
![](https://mc.qcloudimg.com/static/img/56f4130ada2854e5f20c400341135e62/cdn_policy_function.png)
6. 将各个功能关联对应对象，选择指定项目。
![](https://mc.qcloudimg.com/static/img/b207167ccab51a249d72c8d9edf106ed/connect_object.png)
如图，为【查看消耗数据及统计量】关联【测试项目】。
![](https://mc.qcloudimg.com/static/img/e84d64ac3cba90d856fc7a66f7e3c6b6/test_project.png)
7. 单击【完成】，可在自定义策略列表看到创建的策略。
![](https://mc.qcloudimg.com/static/img/7488f8fe1eda8d8c8d135b6938699697/cdn_policy_done.png)

### 创建子用户
1. 登录 [访问管理](https://console.cloud.tencent.com/cam) 控制台，单击左侧【用户管理】，在页面内单击【新建用户】。
![](https://mc.qcloudimg.com/static/img/3d8ddebadc422c6a19be0f0a04ee2f21/create_user.png)
2. 输入管理员姓名、设置 **允许登录腾讯云**，输入 QQ 号、联系手机、联系邮箱等信息,单击【下一步】。
![](https://mc.qcloudimg.com/static/img/338c331b34378f9de8b38f8afc0c9554/subuser_info.png)
3. 勾选已经创建好的子用户 CDN 策略 **cdn_policy** 策略，单击【完成】，即完成有指定权限的子用户的创建。
![](https://mc.qcloudimg.com/static/img/cf548004a888e0bd098b25e04a77dad3/connect_subuser_policy.png)










