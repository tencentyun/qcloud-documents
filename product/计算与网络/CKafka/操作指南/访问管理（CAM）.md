
##  CAM 基本概念
主账号通过给子账号绑定策略实现授权，策略设置可精确到 **[API，资源，用户/用户组，允许/拒绝，条件]** 维度。

#### 账户
- **主账号**：拥有腾讯云所有资源，可以任意访问其任何资源。
- **子账号**：包括子用户和协作者。
 - **子用户**： 由主账号创建，完全归属于创建该子用户的主账号。
 - **协作者**：本身拥有主账号身份，被添加作为当前主账号的协作者，则为当前主账号的子账号之一，可切换回主账号身份。
- **身份凭证**：包括登录凭证和访问证书两种，**登录凭证** 指用户登录名和密码，**访问证书** 指云 API 密钥（SecretId 和 SecretKey）。

#### 资源与权限

- **资源**：资源是云服务中被操作的对象，如一个云服务器实例、COS 存储桶、VPC 实例等。
- **权限**：权限是指允许或拒绝某些用户执行某些操作。默认情况下，**主账号拥有其名下所有资源的访问权限**，而**子账号没有主账号下任何资源的访问权限**。
- **策略**：策略是定义和描述一条或多条权限的语法规范。**主账号**通过将**策略关联**到用户/用户组完成授权。

[单击查看更多 CAM 文档>>](https://cloud.tencent.com/document/product/598/10583)

##  相关文档
| 目标 | 链接 | 
|---------|---------|
|了解策略和用户之间关系| [策略管理](https://cloud.tencent.com/document/product/598/10601)|
|了解策略的基本结构| [策略语法](https://cloud.tencent.com/document/product/598/10603) | 
|了解还有哪些产品支持 CAM|[支持 CAM 的产品](https://cloud.tencent.com/document/product/598/10588)|


##  访问控制策略示例 

### CKafka 全读写策略
授权一个子用户以 CKafka 服务的完全管理权限（创建、管理等全部操作）。
```json
{
  "version": "2.0",
  "statement": [
    {
      "action": [
            "name/ckafka:*",
            "name/monitor:GetMonitorData"
      ],
      "resource": "*",
      "effect": "allow"
    }
  ]
}
```

您也可以通过设置系统的 [全读写策略](https://console.cloud.tencent.com/cam/policy/createV2) 支持。
1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 
2. 在左侧菜单栏中，单击 **[策略](https://console.cloud.tencent.com/cam/policy)**。
3. 在策略列表中，单击**新建自定义策略**。
4. 在选择创建策略方式的弹窗中，选择**按策略语法创建**。
5. 在模板类型中，搜索“CKafka”，选择消息服务（CKafka）全读写访问权限 [QcloudCKafkaFullAccess]，单击**下一步**。
6. 单击**创建策略**。



### CKafka 实例只读策略
1. 按照策略生成器创建，授权列表类权限和产品监控权限。
```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "name/ckafka:ListInstance",
                "name/monitor:GetMonitorData"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

2. 授权单实例只读权限
>!List* 接口不支持资源粒度的鉴权。

 ```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "name/monitor:GetMonitorData",
                "name/ckafka:Get*"
            ],
            "resource": [
                "qcs::ckafka:gz::ckafkaId/uin/$createUin/$instanceId" 
            ]
        }
    ]
}
```

您也可以通过设置系统的 [只读策略](https://console.cloud.tencent.com/cam/policy/createV2) 支持。
1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 
2. 在左侧菜单栏中，单击 **[策略](https://console.cloud.tencent.com/cam/policy)**。
3. 在策略列表中，单击**新建自定义策略**。
4. 在选择创建策略方式的弹窗中，选择**按策略语法创建**。
5. 在模板类型中，搜索“CKafka”，选择消息服务（CKafka）只读访问策略 [QcloudCkafkaReadOnlyAccess]，单击**下一步**。
6. 单击**创建策略**。


