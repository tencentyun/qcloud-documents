
## 概述

当一个主账号下有多个子账号或者协作者时，主账号希望子账号/协作者登录时，可以看到和操作的资源不同。针对该场景，您可以通过对子账号按照资源 ID 进行授权来实现资源的隔离访问。

## 场景说明

TI-ONE 的主要资源已完成接入资源级权限控制，具体所有支持资源级的业务接口清单请查看 [支持 CAM 的业务接口](https://cloud.tencent.com/document/product/598/70050)。下面以 Notebook 为例，假设主账号用户在 TI-ONE 上有两个 Notebook 实例，分别信息如下：

| 名称  | 资源 ID                 |
| ----- | ---------------------- |
| test1 | nb-1513712596279328768 |
| test2 | nb-542850099662357632  |

接下来，主账号需要创建两个 CAM 自用户，分别为 tioneuser1 和 tioneuser2，通过资源级控制授权，保证 tioneuser1 只能访问 test1，tioneuser2 只能访问 test2。

## 操作步骤

### 第一步：确定主账号Uin和需要授权的NotebookID

1.授权语法中需要填写主账号的账号ID（Uin）
![](https://qcloudimg.tencent-cloud.cn/raw/a9c577fa40e34c64ef090c9ec9f72c78.png)
2.找到需要授权的 Notebook 实例对应的实例ID（进入TI-ONE 控制台 Notebook 列表，单击 Notebook 名称，在详情页中找到实例 ID）
![](https://qcloudimg.tencent-cloud.cn/raw/1526fc2c6f83b91731a7874a3bc68304.png)

### 第二步：确定自定义策略内容

下面的自定义策略表达的意思为：被授予了这个策略的子账号，将拥有实例ID为nb-15303\*\*\*\*\*08621312的 Notebook 的访问权限（但是无法编辑和修改）。该子账号无法访问主账号下其他 Notebook 实例。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "tione:*"
            ],
            "resource": [
                "qcs::tione:ap-guangzhou:uin/100*****6610:notebook/nb-15303******08621312"
                 ## uin为主账号的uin, notebook为实例ID,
            ]
        },
        {
            "effect": "deny", ##如果需要保证notebook实例不被修改和删除，可添加这一部分deny的策略控制，此部分为可选
            "action": [
                "tione:DeleteNotebook",
                "tione:ModifyNotebook"
            ],
            "resource": [
                "qcs::tione:ap-guangzhou:uin/100*****6610:notebook/nb-1530380051508621312"
            ]
        },
        {
            "effect": "allow", ##这一部分为保证子账号可以获得TIONE角色服务授权，不能删除
            "action": [
                "cam:GetRole",
                "cam:ListAttachedRolePolicies"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}

```

### 第三步，使用主账号创建策略并授权
1. 创建自定义策略
进入[访问管理控制台](https://console.cloud.tencent.com/cam/policy)，单击**新建自定义策略**
![](https://qcloudimg.tencent-cloud.cn/raw/2471baeb414e475a6703e214b806552d.png)
在弹出的对话框中，选择按策略语法创建
![](https://qcloudimg.tencent-cloud.cn/raw/a8935e01034f1e261770decb06940670.png)
选择模板类型为自定义-空白模板，将上述策略语法粘贴，完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/a0a743dc46c0ab28d71e065166fe4331.png)
2. 给子账号授权
进入[用户列表](https://console.cloud.tencent.com/cam)，确定需要授权的子账号，单击**授权**，将刚刚创建的自定义策略授予给该子账号，即可完成授权。
![](https://qcloudimg.tencent-cloud.cn/raw/bf2573fd2df2a678087f71f8e3270364.png)
针对其他子账号的授权也可以参考上述的授权方法。
