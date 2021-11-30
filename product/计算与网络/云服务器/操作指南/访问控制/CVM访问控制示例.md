## 操作场景

您可以通过使用访问管理（Cloud Access Management，CAM）策略让用户拥有在云服务器（Cloud Virtual Machine，CVM）控制台中查看和使用特定资源的权限。本文档提供了查看和使用特定资源的权限示例，指导用户如何使用控制台的特定部分的策略。

## 操作示例
### CVM 的全读写策略
如果您希望用户拥有创建和管理 CVM 实例的权限，您可以对该用户使用名称为：QcloudCVMFullAccess 的策略。该策略是通过让用户分别对 CVM、VPC（Virtual Private Cloud）、CLB（Cloud Load Balance）和 MONITOR 中所有资源都具有操作的权限来达到目的。
具体操作步骤如下：
参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)，将预设策略 QcloudCVMFullAccess 授权给用户。

### CVM 的只读策略
如果您希望用户拥有查询 CVM 实例的权限，但是不具有创建、删除、开关机的权限，您可以对该用户使用名称为：QcloudCVMInnerReadOnlyAccess 的策略。该策略是通过让用户分别对如下操作 CVM 中所有以单词 “Describe” 开头的所有操作和所有以单词 “Inquiry” 开头的所有操作具有操作的权限来达到目的。具体操作步骤如下：
参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)，将预设策略 QcloudCVMInnerReadOnlyAccess 授权给用户。

### CVM 相关资源的只读策略
如果您希望用户只拥有查询 CVM 实例及相关资源（VPC 、CLB）的权限，但不允许该用户拥有创建、删除、开关机等操作的权限，您可以对该用户使用名称为：QcloudCVMReadOnlyAccess 的策略。该策略是通过让用户分别对如下操作具有操作权限来达到目的：
- CVM 中以单词 “Describe” 开头的所有操作和所有以单词 “Inquiry” 开头的所有操作。
- VPC 中以单词 “Describe ”开头的所有操作、以单词 “Inquiry” 开头的所有操作和以单词 “Get” 开头的所有操作。
- CLB 中以单词 “Describe” 开头的所有操作。
- Monitor 中所有的操作。

具体操作步骤如下：
参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)，将预设策略 QcloudCVMReadOnlyAccess 授权给用户。

### 弹性云盘的相关策略

如果您希望用户可以查看 CVM 控制台中的云硬盘信息，并具有创建云硬盘，使用云硬盘等的权限，可先将以下操作添加到您策略中，再将该策略关联到该用户。
- **CreateCbsStorages：**创建云硬盘。
- **AttachCbsStorages：**挂载指定的弹性云盘到指定的云服务器上。
- **DetachCbsStorages：**解挂指定的弹性云盘。
- **ModifyCbsStorageAttributes：**修改指定云硬盘的名称或项目 ID。
- **DescribeCbsStorages：**查询云硬盘的详细信息。
- **DescribeInstancesCbsNum：**查询云服务器已挂载的弹性云盘数量和可挂载的弹性云盘的总数。
- **RenewCbsStorage：**续费指定的弹性云盘。
- **ResizeCbsStorage：**扩容指定的弹性云盘。

具体操作步骤如下：
1. 根据 [策略](https://cloud.tencent.com/document/product/598/10601)，创建一个可以查看 CVM 控制台中的云硬盘信息，具有创建云硬盘，使用云硬盘等其他权限的自定义策略。
策略内容可参考以下策略语法进行设置：
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "name/cvm:CreateCbsStorages",
                "name/cvm:AttachCbsStorages",
                "name/cvm:DetachCbsStorages",
                "name/cvm:ModifyCbsStorageAttributes",
                "name/cvm:DescribeCbsStorages"
            ],
            "resource": [
                "qcs::cvm::uin/1410643447:*"
            ]
        }
    ]
}
```
2. 找到创建的策略，在该策略行的 “操作” 列中，单击**关联用户/组**。
3. 在弹出的 “关联用户/用户组” 窗口中，选择您需要授权的用户/组，单击**确定**。


### 安全组的相关策略

如果您希望用户可以查看并使用 CVM 控制台中的安全组，可将以下操作添加到您策略中，再将该策略关联到该用户。
- **DeleteSecurityGroup：**删除安全组。
- **ModifySecurityGroupPolicys：**替换安全组所有策略。
- **ModifySingleSecurityGroupPolicy：**修改安全组单条策略。
- **CreateSecurityGroupPolicy：**创建安全组策略。
- **DeleteSecurityGroupPolicy：**删除安全组策略。
- **ModifySecurityGroupAttributes：**修改安全组属性。

具体操作步骤如下：
1. 根据 [策略](https://cloud.tencent.com/document/product/598/10601)，创建一个允许用户在 CVM 控制台中具有创建、删除、修改安全组等其他权限的自定义策略。
策略内容可参考以下策略语法进行设置：
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
2. 找到创建的策略，在该策略行的 “操作” 列中，单击**关联用户/组**。
3. 在弹出的 “关联用户/用户组” 窗口中，选择您需要授权的用户/组，单击**确定**。


### 弹性 IP 地址的相关策略

如果您希望用户可以查看并使用 CVM 控制台中的弹性 IP 地址，可先将以下操作添加到您策略中，再将该策略关联到该用户。
- **AllocateAddresses：**分配地址给 VPC 或者 CVM。
- **AssociateAddress：**将弹性 IP 地址与实例或者与网络接口关联。
- **DescribeAddresses：**查看 CVM 控制台中的弹性 IP 地址。
- **DisassociateAddress：**取消弹性 IP 地址与实例或者与网络接口关联。
- **ModifyAddressAttribute：**修改弹性 IP 地址的属性。
- **ReleaseAddresses：**解除弹性 IP 地址。

具体操作步骤如下：
1. 根据 [策略](https://cloud.tencent.com/document/product/598/10601)，创建一个自定义策略。
该策略允许用户在 CVM 控制台中具有查看弹性 IP 地址并可以将其分配给实例并与之相关联，但不可以修改弹性 IP 地址的属性、取消弹性 IP 地址的关联或释放弹性 IP 地址的权限。策略内容可参考以下策略语法进行设置：
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
2. 找到创建的策略，在该策略行的 “操作” 列中，单击**关联用户/组**。
3. 在弹出的 “关联用户/用户组” 窗口中，选择您需要授权的用户/组，单击**确定**。

### 授权用户拥有特定 CVM 的操作权限策略
如果您希望授权用户拥有特定 CVM 操作权限，可将以下策略关联到该用户。具体操作步骤如下：
1. 根据 [策略](https://cloud.tencent.com/document/product/598/10601)，创建一个自定义策略。
该策略允许用户用于对 ID 为 ins-1，地域为广州的 CVM 实例的操作权限，策略内容可参考以下策略语法进行设置：
```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cvm:*",
            "resource": "qcs::cvm:ap-guangzhou::instance/ins-1",
            "effect": "allow"
        }
    ]
}
```
2. 找到创建的策略，在该策略行的 “操作” 列中，单击**关联用户/组**。
3. 在弹出的 “关联用户/用户组” 窗口中，选择您需要授权的用户/组，单击**确定**。


### 授权用户拥有特定地域 CVM 的操作权限策略
如果您希望授权用户拥有特定地域的 CVM 的操作权限，可将以下策略关联到该用户。具体操作步骤如下：
1. 根据 [策略](https://cloud.tencent.com/document/product/598/10601)，创建一个自定义策略。
该策略允许用户拥有对广州地域的 CVM 机器的操作权限，策略内容可参考以下策略语法进行设置：
```
{
    "version": "2.0",
    "statement": [
        {
            "action": "cvm:*",
            "resource": "qcs::cvm:ap-guangzhou::*",
            "effect": "allow"
        }
    ]
}
```
2. 找到创建的策略，在该策略行的 “操作” 列中，单击**关联用户/组**。
3. 在弹出的 “关联用户/用户组” 窗口中，选择您需要授权的用户/组，单击**确定**。


### 授权子账号拥有 CVM 的所有权限但不包括支付权限

假设，企业账号（CompanyExample，ownerUin 为12345678）下有一个子账号（Developer），该子账号需要对企业帐号的 CVM 服务拥有所有管理权限（例如创建、管理等全部操作），但不包括支付权限（可下单但无法支付）。
我们可通过以下两种方案进行实现：
- **方案 A**
企业账号 CompanyExample 直接将预设策略 QcloudCVMFullAccess 授权给子账号 Developer。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)。
- **方案 B**
 1. 根据以下策略语法，创建一个 [自定义策略](#CAMCustomPolicy)。
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
假设，企业账号（CompanyExample，ownerUin 为12345678）下有一个子账号（Developer），需要基于项目授权子账号在控制台管理资源。
具体操作步骤如下：
1. 根据业务权限创建一个项目管理的自定义策略。
详情请参考 [策略](https://cloud.tencent.com/document/product/598/10601)。
2. 参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)，将创建好的自定义策略授权给子账号。
子账号做项目管理时如遇到无权限提示，例如查看快照、镜像、VPC、弹性公网 IP 等产品时提示无权限，可授权子账号 QcloudCVMAccessForNullProject、QcloudCVMOrderAccess 和 QcloudCVMLaunchToVPC 预设策略。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)。


### 自定义策略[](id:CAMCustomPolicy)

如果您觉得预设策略不能满足您的要求，您可以通过创建自定义策略达到目的。
具体操作步骤请参考 [策略](https://cloud.tencent.com/document/product/598/10601)。
更多 CVM 相关的策略语法请参考 [授权策略语法](https://cloud.tencent.com/document/product/213/10313)。


