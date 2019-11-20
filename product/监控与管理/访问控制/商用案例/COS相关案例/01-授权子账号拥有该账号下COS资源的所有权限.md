企业帐号 CompanyExample（ownerUin 为 12345678）下有一个子账号 Developer，该子账号需要拥有对企业帐号 CompanyExample 的 COS 服务的完全管理权限（创建、管理、访问 COS 的存储桶或者对象）。

方案 A：

企业帐号 CompanyExample 直接将预设策略 QcloudCOSFullAccess 授权给子账号 Developer。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/378/8961)。

方案 B：

步骤 1：通过策略语法方式创建以下策略。
```
 {
    "version": "2.0",
    "statement":[
     {
         "effect": "allow",
         "action": "cos:*",
         "resource": "*"
     }
   ]
}
```
步骤 2：将该策略授权给子账号。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/378/8961)。
