### 授权子账号拥有CLB的所有权限

企业帐号CompanyExample（ownerUin为12345678）下有一个子账号Developer，该子账号需要拥有对企业帐号CompanyExample的CLB服务的完全管理权限（创建、管理、CLB下单支付等等全部操作）。

方案A：

企业帐号CompanyExample直接将预设策略QcloudCLBFullAccess、QcloudCLBFinanceAccess授权给子账号Developer。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

方案B：

step1：通过策略语法方式创建以下策略
```
{
    "version": "2.0",
    "statement":[
         {
             "effect": "allow",
             "action": "clb:*",
             "resource": "*"
         },
         {
                "effect": "allow",
                "action": "finance:*",
                "resource": "qcs::clb:::*"
         }
    ]
}
```
step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

