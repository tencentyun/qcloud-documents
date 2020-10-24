
企业账号 CompanyExample 下有一个子账号 Developer，该子账号需要具备访问内嵌腾讯云日志服务控制台页面的权限。

>?日志服务提供 [日志服务控制台](https://console.cloud.tencent.com/cls) 内嵌到其他系统的能力，客户可以在外部系统服务中（例如公司内部运维或运营系统）快速集成日志服务控制台，满足不需要登录腾讯云控制台即可检索分析日志的诉求。

## 准备工作

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam)。创建子账号 Developer，详细操作请参考 [自定义创建子用户](https://cloud.tencent.com/document/product/598/13674)。
2. 在新建用户页面，单击【自定义创建】，进入选择用户类型页面，单击 **【可访问资源并接收消息】**。
3. 单击【下一步】，进入填写用户信息页面，选中**【编程访问】**及【**腾讯云控制台访问**】。

## 操作步骤

分为三个步骤：主账号 CompanyExample 创建自定义角色、主账号 CompanyExample 创建自定义策略、主账号关联策略到子账号。

1. 主账号 CompanyExample 创建自定义角色
 1. 在角色列表页面，单击**【新建角色】**。
 1. 在弹出的选择角色载体窗口，选择**【腾讯云账户】**作为角色载体，进入角色信息填写页面。
 1. 在角色信息填写页面，使用**【当前主账号】**，同时勾选**【允许当前角色访问控制台】**。
   <img src="https://main.qcloudimg.com/raw/b7c545d85043790e0ca0cfb119298d84.png" alt="image-20200819165703476" style="zoom:80%;" />
 1. 在策略列表内勾选您想要给当前创建角色赋予的策略为角色完成权限配置（可不选择直接进入下一步）。
 1. 输入您的角色名称（如 ClsBuildInRole），审阅您即将创建角色的相关信息，单击【完成】后即完成自定义角色创建。
   <img src="https://main.qcloudimg.com/raw/2d914510bd70a67cd6655ca12606be17.png" alt="image-20200819165703476" style="zoom:80%;" />

2. 主账号 CompanyExample 创建支持内嵌控制台权限的自定义策略
 1. 在策略页面，单击**【新建自定义策略】**。
 1. 在弹出的选择创建策略方式窗口，选择**【按策略语法创建】**，进入策略语法填写页面。
 1. 在**【按策略语法创建】**页面，选择**【空白模板】**。
 1. 在编辑策略页面，填写【策略名称】（如 ClsBuildInStrategy），【策略描述】以及**【策略内容】**，单击完成。
>?策略内容参考以下语法例子，用户根据实际信息修改使用。**其中 uin 和 roleName 根据实际信息修改**。uin 为主账号 uin，rolename 为步骤1创建的角色，如 ClsBuildInRole。

   ```
   {
       "version": "2.0",
       "statement": [
           {
               "effect": "allow",
               "action": [
                   "name/sts:AssumeRole"
               ],
               "resource": [
                   "qcs::cam::uin/100001234567:roleName/ClsBuildInRole"
               ]
           }
       ]
   }
   ```

3. 主账号关联策略到子账号
 1. 在策略页面，在搜索框搜索需要关联子用户的**【策略名称】**（如ClsBuildInStrategy）。
 1. 在搜索到的策略的右侧操作栏，选择**【关联用户/组】**。
   <img src="https://main.qcloudimg.com/raw/3b8d312b18eab5ab50b389d70e2f9409.png" alt="image-20200819165949371" style="zoom:80%;" />
 1. 在弹框选择该策略需要关联的子账号 Developer，单击【确定】。也可以在用户页面，从用户关联到策略，此处不赘述。详细操作请参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)。
