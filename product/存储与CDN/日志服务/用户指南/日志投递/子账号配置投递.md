## 简介

日志服务 CLS 具备 **COS 投递功能**，该功能可以实现操作同一账号的资源（不支持多个账户下的资源）。默认情况下，子账号没有权限使用投递配置功能，需要主账号为子账号添加授权，才能正常使用该功能。下面将为您详细介绍如何为子账号添加授权。

### 相关说明

假设主账号下拥有 CLS 资源 TopicA 和 COS 资源 BucketA（公有读写）、BucketB（公有读私有写）、BucketC（私有读写）。不同账号下，被允许的操作如下：

| 操作者         | 描述                                             | 是否支持 |
| -------------- | ------------------------------------------------ | -------- |
| 主账号         | 配置 TopicA 日志数据投递 BucketA（公有读写）     | 是       |
| 主账号         | 配置 TopicA 日志数据投递 BucketB（公有读私有写） | 是       |
| 主账号         | 配置 TopicA 日志数据投递 BucketC（私有读写）     | 是       |
| 子账号或协作者 | 配置 TopicA 日志数据投递 BucketA（公有读写）     | 是       |
| 子账号或协作者 | 配置 TopicA 日志数据投递 BucketB（公有读私有写） | 是       |
| 子账号或协作者 | 配置 TopicA 日志数据投递 BucketC（私有读写）     | 是       |

子账号（或协作者）在配置日志投递前，需要确保主账号已在[ CAM 管理控制台](https://console.cloud.tencent.com/cam/overview) 上为子账号配置了以下相关的权限策略：

- 访问主账号 CLS 资源的权限：QcloudCLSFullAccess。
- 访问主账号 COS 存储桶列表的权限：QcloudCOSGetServiceAccess。
- 创建策略及绑定策略的权限：CreateRole、AttachRolePolicy。

## 操作步骤

### 创建策略

1. 登录 [访问管理](https://console.cloud.tencent.com/cam/overview) 控制台。
2. 在左侧导航中，单击【策略】。
3. 在**策略**界面中，单击【新建自定义策略】。
4. 创建策略方式选择【按策略生成器创建】，如下图所示。
![](https://main.qcloudimg.com/raw/c2278683630ddcf9c05add8fc454f2b7.png)
5. 在弹窗界面中，配置如下选项：
 - 服务（Service）：选择**用户与权限**。
 - 操作(Action)：勾选 CreateRole（创建角色）、AttachRolePolicy（绑定策略到角色）。
 - 资源（Resource）：填写 `*` 。
   ![](https://main.qcloudimg.com/raw/d6be535c0499155faa2bb08365f1e7d5.png)
6. 单击【添加声明】，确认配置的权限无误后，单击【下一步】。
   ![](https://main.qcloudimg.com/raw/bc014cb48d1bb2544d77ad434476ef57.png)
7. 策略名称可根据需要进行自定义修改，单击【创建策略】，完成创建。

### 关联策略

对相应的子账号（协作者）进行策略授权，需要添加 QcloudCLSFullAccess、QcloudCOSGetServiceAccess 以及刚才创建的策略。

1. 登录 [访问管理](https://console.cloud.tencent.com/cam/overview) 控制台。
2. 在左侧导航中，单击【用户】。
3. 在**用户**界面中，找到需要关联策略的 **子账号（协作者）**，在其右侧单击【授权】。
   ![](https://main.qcloudimg.com/raw/a03444f6e038450afa309ceb3faf5a18.png)
4. 在关联策略界面中，勾选对应策略 **QcloudCLSFullAccess**、**QcloudCOSGetServiceAccess** 以及刚才创建的策略 ，单击【确认】，完成策略关联。
![](https://main.qcloudimg.com/raw/4e84f8aa5571b9e01df0e2dc431e99e3.png)
5. 完成以上步骤后，即可使用子账号（协作者）添加投递配置功能。



