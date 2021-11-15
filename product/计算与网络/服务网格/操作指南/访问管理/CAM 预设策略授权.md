您可以把 CAM 中的 TCM 相关预设策略关联至子账号，快速完成 TCM 的 CAM 授权。

##  TCM 相关预设策略

您可以使用以下预设策略为您的子账号授予相关权限：

| 策略 | 描述 |
|------- |--------|
|`QcloudTCMFullAccess` | 服务网格（TCM）全读写访问权限（创建、删除等全部操作） |
|`QcloudTCMReadOnlyAccess`| 服务网格（TCM）只读访问权限（可以查看TCM下所有资源，但无法创建、更新或删除它们） |

### 服务网格全读写预设策略

策略名：QcloudTCMFullAccess，策略内容：

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "tcm:*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

### 服务网格只读预设策略

策略名：QcloudTCMReadOnlyAccess，策略内容：

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "tcm:List*",
                "tcm:Describe*",
                "tcm:ForwardRequestRead"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

## TCM 相关产品的 CAM 权限

使用 TCM 还涉及到关联的 VPC、CCN、CLB、TKE等产品的 CAM 权限，您可以参考相应产品的 CAM 授权文档，为子账号授予合适的权限：

| TCM 相关产品 | 授权指南文档 |
|------- |--------|
| 私有网络（VPC） | [VPC 访问管理概述](https://cloud.tencent.com/document/product/215/39265) |
| 负载均衡（CLB） | [CLB 访问管理概述](https://cloud.tencent.com/document/product/214/9777) |
| 容器服务（TKE） | [TKE 权限管理概述](https://cloud.tencent.com/document/product/457/11542) |

## 子账号关联预设策略

您可在创建子账号的“设置用户权限”步骤中，通过 [直接关联](#direct) 或 [随组关联](#byGroup) 方式，为该子账户关联预设策略。

### 直接关联[](id:direct)

您可以直接为子账号关联策略以获取策略包含的权限。

1. 登录访问管理控制台，选择左侧导航栏中的**用户** > **[用户列表](https://console.cloud.tencent.com/cam)**。
2. 在“用户列表”管理页面，选择需要设置权限的子账号所在行右侧的**授权**。
3. 在弹出的“关联策略”窗口中，勾选需授权的策略。
4. 单击**确定**即可。

### 随组关联[](id:byGroup)

您可以将子账号添加至用户组，该子账号将自动获取该用户组所关联策略的权限。如需解除随组关联策略，仅需将子账号移出相应用户组即可。

1. 登录访问管理控制台，选择左侧导航栏中的**用户** > **[用户列表](https://console.cloud.tencent.com/cam)**。
2. 在“用户列表”管理页面，选择需要设置权限的子账号所在行右侧的**更多操作** > **添加到组**。
3. 在弹出的“添加到组”窗口中，勾选需加入的用户组。
4. 单击**确定**即可。

### 登录子账号验证

登录 [腾讯云服务网格控制台](https://console.cloud.tencent.com/tke2/mesh)，验证可使用所授权策略对应功能，则表示子账号授权成功。
   
