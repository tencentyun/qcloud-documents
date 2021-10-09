## CAM 简介

### 基本概念
根账户通过给子账户绑定策略实现授权，策略设置可精确到 **[API，资源，用户/用户组，允许/拒绝，条件]** 维度。

#### 账户

- **根账号**：腾讯云资源归属、资源使用计量计费的基本主体，可登录腾讯云服务。
- **子账号**：由根账号创建账号，有确定的身份 ID 和身份凭证，且能登录到腾讯云控制台。根账号可以创建多个子账号(用户)。**子账号默认不拥有资源，必须由所属根账号进行授权。**
- **身份凭证**：包括登录凭证和访问证书两种，**登录凭证** 指用户登录名和密码，**访问证书** 指云 API 密钥（SecretId 和 SecretKey）。

#### 资源与权限
- **资源**：资源是云服务中被操作的对象，如一个云服务器实例、COS 存储桶、VPC 实例等。
- **权限**：权限是指允许或拒绝某些用户执行某些操作。默认情况下，**根账号拥有其名下所有资源的访问权限**，而**子账号没有根账号下任何资源的访问权限**。
- **策略**：策略是定义和描述一条或多条权限的语法规范。**根账号**通过将**策略关联**到用户/用户组完成授权。

### 相关文档
| 阅读目的                     | 链接                                                         |
| ------------------------ | ------------------------------------------------------------ |
| 了解策略和用户之间关系   | [策略管理](https://cloud.tencent.com/document/product/598/10601) |
| 了解策略的基本结构       | [策略语法](https://cloud.tencent.com/document/product/598/10603) |
| 了解还有哪些产品支持 CAM | [支持 CAM 的产品](https://cloud.tencent.com/document/product/598/10588) |

[单击查看更多 CAM 文档 >>](https://cloud.tencent.com/document/product/378)

## API 网关资源
```
- qcs::APIgateway:_`region`_:uin/_`uin—id`_:service/_`serviceid`_
- qcs::APIgateway:_`region`_:uin/_`uin—id`_:service/_`serviceid`_/API/_`apiid`_
- qcs::APIgateway:_`region`_:uin/_`uin—id`_:usagePlan/_`usagePlanid`_
- qcs::APIgateway:_`region`_:uin/_`uin—id`_:secret/_`secretid`_
- qcs::APIgateway:_`region`_:uin/_`uin—id`_:IPStrategy/_`IPStrategyId`_
- qcs::APIgateway:_`region`_:uin/_`uin—id`_:logRule/_`logRuleId`_
```
所有的创建接口为账户级别，而其他接口均为资源级别。

## 访问控制策略示例 

### API 网关全读写策略
授权一个子用户以 API 服务的完全管理权限（创建、管理等全部操作）。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "apigw:*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

也可以通过设置系统的 [全读写策略](https://console.cloud.tencent.com/cam/policy/createV2) 支持。
![](https://main.qcloudimg.com/raw/0d537a59ff25d11c33990dfff506d1ab.png)

### API 网关单个服务完全管理策略
授权一个子用户某个特定 API 服务的完全管理权限（创建、管理等全部操作）：
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "apigw:*"
            ],
            "resource":"qcs::apigw:ap-guangzhou:uin/{ownerUin}:service/service-id/API/api-id",
            "effect": "allow"
        }
    ]
}
```

### API 网关单个服务只读策略
1. 按照策略生成器创建，授权列表类权限和产品监控权限，这里是对账户下的所有资源授予只读权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "apigw:Describe*",
                "apigw:GenerateApiDocument"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

2. 授权单 API 只读权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "ckafka:Get*",
                "ckafka:List*"
            ],
            "resource": "qcs::apigw:ap-guangzhou:uin/{ownerUin}:service/service-id/API/api-id",
            "effect": "allow"
        }
    ]
}
```

