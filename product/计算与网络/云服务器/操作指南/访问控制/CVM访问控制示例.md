## CVM 访问管理策略示例

您可以通过使用 CAM （Cloud Access Management，访问管理）策略让用户拥有在 CVM （Cloud Virtual Machine，云服务器）控制台中查看和使用特定资源的权限。该部分的示例能够使用户使用控制台的特定部分的策略。
### CVM 的全读写策略
若您想让用户拥有创建和管理 CVM 实例的权限，您可以对该用户使用名称为：QcloudCVMFullAccess 的策略。
您可以进入 [策略管理界面](https://console.cloud.tencent.com/cam/policy)，在右边的全部服务中选择【云服务器】，即可在图中位置找到该策略。

![Alt text](https://mc.qcloudimg.com/static/img/ac676b0e8f27c0759ad602c5fe383d3c/1500033749808.png)
策略语法如下：

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/vpc:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/clb:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": "name/monitor:*",
            "resource": "*"
        }
    ]
}
```
以上策略是通过让用户分别对 CVM、VPC（Virtual Private Cloud）、CLB（Cloud Load Balance）和 MONITOR 中所有资源都具有操作的权限来达到目的。

### CVM 的只读策略
若您只想让用户拥有查询 CVM 实例的权限，但是不具有创建、删除、开关机的权限，您可以对该用户使用名称为：QcloudCVMInnerReadOnlyAccess 的策略。

您可以进入 [策略管理界面](https://console.cloud.tencent.com/cam/policy) ，并在右侧的全部服务中选择【云服务器】，即可在图中位置找到该策略。
![Alt text](https://mc.qcloudimg.com/static/img/c3a3537c24dde34054a590c3fe7eccc8/1500033727016.png)

策略语法如下：

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:Describe*",
                "name/cvm:Inquiry*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
以上策略是通过让用户分别对如下操作 CVM 中所有以单词 “Describe” 开头的所有操作和所有以单词 “Inquiry” 开头的所有操作具有操作的权限来达到目的。

### CVM 相关资源的只读策略
如果您想要让用户只拥有查询 CVM 实例及相关资源（VPC 、CLB）的权限，但不允许该用户拥有创建、删除、开关机等操作的权限，您可以对该用户使用名称为：QcloudCVMReadOnlyAccess 的策略。

您可以进入 [策略管理界面](https://console.cloud.tencent.com/cam/policy), 并在右边的全部服务中选择【云服务器】，即可在图中位置找到该策略。
![Alt text](https://mc.qcloudimg.com/static/img/17c3e2be396ea544b7d4ca425e5049c5/1500033915369.png)
策略语法如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:Describe*",
                "name/cvm:Inquiry*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/vpc:Describe*",
                "name/vpc:Inquiry*",
                "name/vpc:Get*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/clb:Describe*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": "name/monitor:*",
            "resource": "*"
        }
    ]
}
```
以上策略是通过让用户分别对如下操作具有操作权限来达到目的：
- CVM 中以单词 “Describe” 开头的所有操作和所有以单词 “Inquiry” 开头的所有操作。
- VPC 中以单词 “Describe ”开头的所有操作、以单词 “Inquiry” 开头的所有操作和以单词 “Get” 开头的所有操作。
- CLB 中以单词 “Describe” 开头的所有操作。
- Monitor 中所有的的操作。

### 弹性云盘的相关策略

若您想要让用户能够查看 CVM 控制台中的云硬盘信息，创建云硬盘，使用云硬盘，可先将以下操作添加到您策略中，再将该策略关联到该用户。

- **CreateCbsStorages ：**创建云硬盘。
- **AttachCbsStorages ：**挂载指定的弹性云盘到指定的云服务器上。
- **DetachCbsStorages ：**解挂指定的弹性云盘。
- **ModifyCbsStorageAttributes ：**修改指定云硬盘的名称或项目 ID。
- **DescribeCbsStorages ：**查询云硬盘的详细信息性。
- **DescribeInstancesCbsNum ：**查询云服务器已挂载的弹性云盘数量和可挂载的弹性云盘的总数。
- **RenewCbsStorage ：**续费指定的弹性云盘。
- **ResizeCbsStorage ：**扩容指定的弹性云盘。

以下策略不允许用户修改云硬盘属性。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:ModifyCbsStorageAttributes"
            ],
            "resource": [
                "qcs::cvm::uin/1410643447:*"
            ],
            "effect": "deny"
        }
    ]
}

```
### 安全组的相关策略

若您想要让用户能够查看并使用 CVM 控制台中的安全组，可将以下操作添加到您策略中，再将该策略关联到该用户。

- **DeleteSecurityGroup ：**删除安全组。
- **ModifySecurityGroupPolicys ：**替换安全组所有策略。
- **ModifySingleSecurityGroupPolicy ：**修改安全组单条策略。
- **CreateSecurityGroupPolicy ：**创建安全组策略。
- **DeleteSecurityGroupPolicy ：**删除安全组策略。
- **ModifySecurityGroupAttributes ：**修改安全组属性。

以下策略允许用户在 CVM 控制台中具有创建，删除安全组的权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:DeleteSecurityGroup",
                "name/cvm:CreateSecurityGroup"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
以下策略可以让用户在 CVM 控制台中具有创建、删除修改安全组策略的权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:ModifySecurityGroupPolicys",
                "name/cvm:ModifySingleSecurityGroupPolicy",
                "name/cvm:CreateSecurityGroupPolicy",
                "name/cvm:DeleteSecurityGroupPolicy"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

### 弹性 IP 地址的相关策略

若您想要让用户能够查看并使用 CVM 控制台中的弹性 IP 地址，可先将以下操作添加到您策略中，再将该策略关联到该用户。

- **AllocateAddresses ：**分配地址给 VPC 或者 CVM。
- **AssociateAddress ：**将弹性 IP 地址与实例或者与网络接口关联。
- **DescribeAddresses ：**查看 CVM 控制台中的弹性 IP 地址。
- **DisassociateAddress ：**取消弹性 IP 地址与实例或者与网络接口关联。
- **ModifyAddressAttribute ：**修改弹性 IP 地址的属性。
- **ReleaseAddresses ：**解除弹性 IP 地址。

以下策略允许用户查看弹性 IP 地址并可以将其分配给实例并与之相关联。用户不可以修改弹性 IP 地址的属性、取消弹性 IP 地址的关联或释放弹性 IP 地址。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cvm:DescribeAddresses",
                "name/cvm:AllocateAddresses",
                "name/cvm:AssociateAddress"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
### 授权用户拥有特定 CVM 的操作权限策略
若您想要授权用户拥有特定 CVM 操作权限，可将以下策略关联到该用户。
以下策略允许用户拥有对 ID 为 ins-1, 广州地域的 CVM 机器的操作权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cvm:*",
            "resource": "qcs::cvm:gz::instance/ins-1",
            "effect": "allow"
        }
    ]
}
```


### 授权用户拥有特定地域 CVM 的操作权限策略
若您想要授权用户拥有特定地域的 CVM 的操作权限，可将以下策略关联到该用户。
以下策略允许用户拥有对广州地域的 CVM 机器的操作权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cvm:*",
            "resource": "qcs::cvm:gz::*",
            "effect": "allow"
        }
    ]
}
```

### 授权子账号拥有 CVM 的所有权限但不包括支付权限

企业帐号 CompanyExample（ownerUin 为12345678）下有一个子账号 Developer，该子账号需要拥有对企业帐号 CompanyExample 的 CVM 服务的所有权限管理权限（创建、管理等全部操作），但不包括支付权限，可下单但无法支付。

方案A：

企业帐号 CompanyExample 直接将预设策略 QcloudCVMFullAccess 授权给子账号 Developer。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)。

方案B：

1. 通过策略语法方式创建以下策略
```
 {
    "version": "2.0",
    "statement":[
         {
             "effect": "allow",
             "action": "cvm:*",
             "resource": "*"
         }
    ]
}
```
2. 将该策略授权给子账号。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)。


### 授予子账号拥有项目管理的操作权限
企业帐号 CompanyExample（ownerUin 为12345678）下有一个子账号 Developer，需要基于项目授权子账号在控制台管理资源。


1. 按业务权限创建项目管理自定义策略，请参考 [策略](https://cloud.tencent.com/document/product/598/10601)。
2. 给子账号关联创建好的自定义策略，请参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)。
子账号做项目管理时如遇到无权限提示，例如：查看快照、镜像、VPC、弹性公网 IP 等产品时提示无权限，可授权子账号 QcloudCVMAccessForNullProject、QcloudCVMOrderAccess 和 QcloudCVMLaunchToVPC 预设策略。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)。


### 自定义策略

若您觉得预设策略不能满足您所想要的要求，您可以创建自定义策略。
自定义的策略语法如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "Action"
            ],
            "resource": "Resource",
            "effect": "Effect"
        }
    ]
}
```
- Action 中换成您要进行允许或拒绝的操作。
- Resource 中换成您要授权的具体资源。
- Effect 中换成允许或者拒绝。


