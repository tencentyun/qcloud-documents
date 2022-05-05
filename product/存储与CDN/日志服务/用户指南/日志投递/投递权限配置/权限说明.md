日志服务（Cloud Log Service，CLS）将日志投递至对象存储（Cloud Object Storage，COS）或 Ckafka 的过程中，需要用户确认授予日志服务具有写 COS 或 Ckafka 的权限。用户需要为日志服务的唯一服务角色 `CLS_QcsRole` 授权 `QcloudCOSAccessForCLSRole` 或 `QcloudCKAFKAAccessForCLSRole` 策略权限。

若您需授予协作者或子账号配置投递任务权限，则请参考本文进行操作。



## 通过控制台为协作者或子账号配置投递任务

协作者或子账号在日志服务控制台上进行投递任务配置时，需要主账号授权必要的权限，否则无法顺利进行投递配置。协作者或子账号在配置投递任务时，会依赖以下权限：

| 权限名称                                                     | 描述说明                                    | 应用场景                                                     |
| ------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------ |
| CLS 预设策略：QcloudCLSFullAccess                            | 协作者或子账号可以操作日志服务的权限        | 协作者或子账号需要此权限才能<br>操作日志服务进行投递任务的配置   |
| CAM 预设策略：QcloudCamSubaccountsAuthorizeRoleFullAccess    | 协作者或子账号可以授权服务角色的权限        | 日志投递至 COS 或 Ckafka 时，需要<br>协作者或子账号确认角色授权，使 CLS 具有写 COS 或写 Ckafka 的权限，即为服务角色 CLS_QcsRole 授权 QcloudCOSAccessForCLSRole 或 QcloudCKAFKAAccessForCLSRole 策略权限 |
| COS 接口权限：GetService<br>（或预设策略：QcloudCOSReadOnlyAccess） | 协作者或子账号可以获取 COS 存储桶列表的权限  | 控制台配置投递至 COS 任务的过程<br>中，需要拉取 COS 存储桶列表，然后选择投递的目标存储桶 |
| CKafka 接口权限：ListInstance，ListTopic<br>(或预设策略：QcloudCkafkaReadOnlyAccess) | 协作者或子账号可以获取 CKafka 资源列表的权限 | 控制台配置投递至 Ckafka 任务的过程<br>中，需要拉取 CKafka 的资源列表，然后选择投递的目标 Ckafka 实例的主题 |

### 主账号授权步骤

1. 使用主账号登录访问管理控制台，选择左侧导航栏中的**用户** > **[用户列表](https://console.cloud.tencent.com/cam)**。
2. 在“用户列表”页面中，单击需操作的用户名称，进入用户详情页。
3. 在用户详情页面中，选择**关联策略**。
4. 在“添加策略”页面的“设置用户权限”中，选择**从策略列表中选取策略关联**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3434ebc9faabe6b1de93d6f940b9928d.png)
5. 为协作者或子账号关联预设策略：`QcloudCLSFullAccess`、`QcloudCamSubaccountsAuthorizeRoleFullAccess`、`QcloudCOSReadOnlyAccess`、`QcloudCkafkaReadOnlyAccess`。
<dx-alert infotype="notice" title="">
主账号必须完成授权操作，否则协作者或子账号无法正常进行投递配置。
</dx-alert>
6. 单击**下一步**。
7. 在“审阅”中确认配置，并单击**确定**即可完成授权。




