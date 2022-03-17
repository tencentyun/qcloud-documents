### 预设策略为何出现新的策略版本？
预设策略由腾讯云创建和管理，是被用户高频使用的一些常见权限集合。

预设策略与云服务的功能关系密切，若云服务做了功能升级或调整，腾讯云可能配合云服务对预设策略进行升级或调整，此时会新增一个策略版本，以保证覆盖新的功能权限。
可能会被调整的预设策略，将会包括一般的预设策略以及与服务角色关联的预设策略。

### 如何授予主账号权限？

主账号默认拥有所有权限，不需要授权。

### 如何授予子账号某些产品的某些操作权限？

您可以通过 [策略生成器创建](https://cloud.tencent.com/document/product/598/37739#.E6.8C.89.E7.AD.96.E7.95.A5.E7.94.9F.E6.88.90.E5.99.A8.E5.88.9B.E5.BB.BA) 创建一条自定义策略，勾选您需要的产品及操作。通过 [策略关联用户](https://cloud.tencent.com/document/product/598/10602#.E9.80.9A.E8.BF.87.E7.AD.96.E7.95.A5.E5.85.B3.E8.81.94.E7.94.A8.E6.88.B7.2F.E7.94.A8.E6.88.B7.E7.BB.84) 即可。关联成功后，您的子账号将在您设置的权限范围内管理主账号下的资源。

### 为子账号授权后，子账号购买的资源属于哪个账号？

使用子账号身份购买的资源，资源归属于所属主账号。

### 子账号密码如何重置？

子用户修改密码请参阅 [为子用户重置登录密码](https://cloud.tencent.com/document/product/598/36260)，协作者修改密码请参阅 [修改账号密码](https://cloud.tencent.com/document/product/378/14623)。

### 子账号购买资源产生的费用从哪里扣除？

使用子账号身份产生的费用，从所属主账号余额扣除。

 

### 为什么创建策略时提示不在白名单内？

目前有不少产品是灰度期间，个别产品暂不支持 CAM 管理。您可以查看 [支持 CAM 的产品](https://cloud.tencent.com/document/product/598/10588) 来确定是否能够在 CAM 里以及何种粒度对产品服务权限进行管理。

如需要对处于灰度期的产品使用 CAM 进行管理，请通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行操作。

### 如何对项目内资源进行精细化权限管理？

您可以通过基于 [标签](https://cloud.tencent.com/document/product/651) 的方式对项目内资源进行精细化的权限管理。

### 为什么给子账号授权了云产品只读策略（ReadOnlyAccess）却依然存在部分云产品无访问权限？

您好，云产品只读策略（ReadOnlyAccess）仅包含授权粒度为操作级或资源级云产品的读接口，如果您访问服务级云产品或操作级/资源级云产品的写接口就会出现无权限提示。云产品的授权粒度请参阅 [支持 CAM 的产品](https://cloud.tencent.com/document/product/598/10588)。

### 如何授予子账号查看有限的资源列表权限？

以下示例介绍如何授予子账号查看有限的资源列表权限。详细信息：

企业账号 CompanyExample（ownerUin 为 12345678）下有一个子账号 Developer，要求该子账号在控制台仅能查看企业账号 CompanyExample 的部分资源。

以 CVM 云服务器实例为例，授予子账号仅能在控制台查看 gz 地域 ID 为 ins-xxx1 和 ins-xxx2 的云服务器实例：

1. 通过策略语法方式创建以下策略：
```json
{
"version": "2.0",
"statement": [
{
"action": [
    "cvm:DescribeInstances"
],
"resource": ["qcs::cvm:gz::instance/ins-xxx1",
    "qcs::cvm:gz::instance/ins-xxx2"
],
"effect": "allow"
}
  ]
}
```
也可以根据需要设置更高的权限，如全读写权限。若需要拥有广州地域所有云服务器实例的全读写权限，可以将策略语法写成如下形式：
```json
{
  "version": "2.0",
  "statement": [
      {
          "action": [
              "cvm:*"
              ],
          "resource": "qcs::cvm:gz::*",
          "effect": "allow"
      }
  ]
}
```

2. 将该策略授权给子账号。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)。
目前，**支持**只读操作这种资源粒度权限控制的产品有：云服务器 CVM，云数据库 TencentDB for MySQL，容器服务 TKE。
 对于其他产品，暂不支持对具体资源授权只读权限，只能授予子账号查看所有资源的权限，或无法查看所有资源。

 
