### 授权子账号拥有CVM的所有权限但不包括支付权限

企业帐号CompanyExample（ownerUin为12345678）下有一个子账号Developer，该子账号需要拥有对企业帐号CompanyExample的CVM服务的所有权限管理权限（创建、管理等全部操作），但不包括支付权限，可以下单但无法支付。

方案A：

企业帐号CompanyExample直接将预设策略QcloudCVMFullAccess授权给子账号Developer。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

方案B：

step1：通过策略语法方式创建以下策略
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
step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

