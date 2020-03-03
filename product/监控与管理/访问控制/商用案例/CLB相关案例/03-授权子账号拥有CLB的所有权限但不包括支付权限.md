
企业帐号 CompanyExample（ownerUin 为 12345678）下有一个子账号 Developer，该子账号需要拥有对企业帐号 CompanyExample 的 CLB 服务的所有权限管理权限（创建、管理等全部操作），但不包括支付权限，可以下单但无法支付。

方案A：

企业帐号 CompanyExample 直接将预设策略 QcloudCLBFullAccess 授权给子账号 Developer。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/378/8961)。

方案B：

步骤1：通过策略语法方式创建以下策略。
```
 {
    "version": "2.0",
    "statement":[
         {
             "effect": "allow",
             "action": "clb:*",
             "resource": "*"
         }
    ]
}
```
步骤2：将该策略授权给子账号。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/378/8961)。

