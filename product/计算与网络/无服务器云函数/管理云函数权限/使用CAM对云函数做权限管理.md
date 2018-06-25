[访问控制（Cloud Access Management，CAM）](https://cloud.tencent.com/document/product/598?)是腾讯云提供的Web服务，主要用于帮助客户安全管理腾讯云账户下的资源的访问权限。用户可以通过 CAM 创建、管理和销毁用户(组)，并使用身份管理和策略管理控制其他用户使用腾讯云资源的权限。

腾讯云无服务器云函数已经和访问控制（Cloud Access Management，CAM）进行了对接，用户可以通过主账号给子账号或者协作者赋予不同的权限。当前 SCF 支持的权限力度如下:

| 服务 | 策略语法 |  云API | 控制台 | 授权粒度 | 临时证书| 
| ---------| ---------| ---------| ---------|
| 无服务器云函数 | ✔ | ✔ | ✔ | 资源级 | ✔|

当前SCF支持的接口如下：

| 接口名称  | 描述 | 级别 |
|---------|---------|
| ListFunctions | 获取账号下的函数列表|账号级 |
| GetAccountSettings| 获取账号下的限额配置|账号级 |
| CreateFunction| 新建一个新函数| 资源级|
| DeleteFunction| 删除指定的函数| 资源级|
| InvokeFunction| 触发函数，分为同步和异步触发| 资源级|
| UpdateFunction| 更新函数，包括配置和/或代码| 资源级|
| SetTrigger    | 对指定函数配置触发器| 资源级|
| DeleteTrigger | 删除指定函数的触发器| 资源级|
| GetFunction   | 获取指定函数的配置信息| 资源级|
| ListVersion   | 获取指定函数的版本信息| 资源级|
| GetFunctionLogs | 获取指定函数的日志信息| 资源级|
>**注意：**
在配置策略语法时，还需要配合使用 monitor 相关的接口以获得账号下的监控信息，使用方法请参考下面的策略样例。

SCF 的策略语法遵循 CAM 的[语法结构](https://cloud.tencent.com/document/product/598/10604)和[资源描述方式](https://cloud.tencent.com/document/product/598/10606)，策略语法以 JSON 格式为基础，所有资源均可采用下述的六段式描述方式，示例如下：
```
qcs: :scf:region:uin/uin—id:function/function-name
```
策略样例
```
{	 
        "version":"2.0", 
        "statement": 
        [ 
           { 
              "effect":"allow", 
              "action":
              [
                "scf:ListFunctions",
                "scf:GetAccountSettings"，
                "monitor:*"
              ], 
              "resource":["*"]  
           }, 
          { 
             "effect": "allow",
             "action": 
             [
                "scf:DeleteFunction",
                "scf:CreateFunction",
                "scf:InvokeFunction",
                "scf:UpdateFunction",
                "scf:GetFunctionLogs",
                "scf:SetTrigger",
                "scf:DeleteTrigger",
                "scf:GetFunction",
                "scf:ListVersion"
            ],
            "resource": 
            [
                "qcs::scf:gz:uin/******:function/Test1",
                "qcs::scf:gz:uin/******:function/Test2"
            ]
         }
      ] 
} 
```
* 操作(action)是需要关联资源的操作时，resource定义为"*"，表示关联所有资源。

* 操作(action)是不需要关联资源的操作时，resource都需要定义为"*"。

* 该样例可以实现子账号拥有主账号下某些函数的操作权限，resource中的资源描述为主账号下的某个函数



## 示例一 ：创建子用户并对其赋予 SCF 的所有操作权限
1. 使用主账号[创建子用户](https://cloud.tencent.com/document/product/598/13674)。登录腾讯云控制台，进入 用户管理 页面，单击【新建用户】 > 【子用户】,如下图所示：
![](https://main.qcloudimg.com/raw/74da3e5cecca08b3012789f307fac05a/%E5%88%9B%E5%BB%BA%E5%AD%90%E7%94%A8%E6%88%B7%E6%88%AA%E5%9B%BE.png)
![](https://main.qcloudimg.com/raw/e096e14bd1eef8fc1dcf1ba3faf931a8/%E5%88%9B%E5%BB%BA%E5%AD%90%E7%94%A8%E6%88%B7.png)
2. 填写用户信息。在此过程中，可批量创建子用户，设置访问类型和控制台密码等，如下图所示：
![](https://main.qcloudimg.com/raw/388c1df7b498d0fee2c640fed505ceb8/%E5%A1%AB%E5%86%99%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF.png)
3. 设定权限。将子用户添加到现有用户组或新建用户组(必选），如下图所示：
![](https://main.qcloudimg.com/raw/eea4b2e2bc6362734b8fb3c3be6bde4a/%E5%85%B3%E8%81%94%E7%94%A8%E6%88%B7%E7%BB%84.png)
4. 创建自定义策略。在左侧的导航栏中单击【策略管理】进入策略管理页面，【新建自定义策略】>【按策略生成器创建】，进入创建页面:
![](https://main.qcloudimg.com/raw/7788eb317107f6752146741dcc96f07e/%E5%88%9B%E5%BB%BA%E7%AD%96%E7%95%A5.png)
   按照下图的选择，单击【添加声明】>【下一步】，进入编辑策略步骤：
![](https://main.qcloudimg.com/raw/9db1e6d30d8ac9ce192d3b952f0d7cb7/%E5%88%9B%E5%BB%BASCF%E7%AD%96%E7%95%A5.png)
   点击【创建策略】完成策略创建：
![](https://main.qcloudimg.com/raw/107468780b8417f4b5e319122fa403dc/%E7%AD%96%E7%95%A5%E7%BC%96%E8%BE%91-all.png)
5. 把策略关联到用户/用户组。如下图所示：
![](https://main.qcloudimg.com/raw/efc1301717d483b6265b1af6b545aaa6/%E5%85%B3%E8%81%94%E7%94%A8%E6%88%B7.png)
  可以选择切换用户或用户组，点击【确定】完成关联操作:
![](https://main.qcloudimg.com/raw/e52ee8a97b4b914ec44a1cb4265af073/%E5%85%B3%E8%81%94%E7%94%A8%E6%88%B72.png)
6. 登录子账号查看权限。在左侧的导航栏中单击【用户管理】进入用户管理页面，可以查看到子用户登录地址：
![](https://main.qcloudimg.com/raw/684a6ef92fed293c4c03146e36cff658/%E6%9D%83%E9%99%90%E6%9F%A5%E7%9C%8B.png)

## 示例二 ：创建子用户并对其赋予部分函数的操作权限
1. 完成子用户创建，同示例一中的步骤1到步骤3。
2. 创建自定义策略，同示例一中的步骤4，在进入编辑策略步骤后，对策略内容进行修改，可替换成上文“策略样例”中的代码，如下图所示：
![](https://main.qcloudimg.com/raw/8967d3afdbc8ea6f07d0cd5ae83e96c9/%E7%AD%96%E7%95%A5%E7%BC%96%E8%BE%912.png)
>**注意：**
>resource中的资源描述，需要替换成主账号的ID和主账号下函数名，region需要和函数保持一致。
3. 把策略关联到用户/用户组，登录子账号查看权限，同示例一种的步骤5和步骤6。
>**注意：**
>策略生效后，当前子账号可以看到所有的函数名，但是只能对resource中的函数进行操作和查看。