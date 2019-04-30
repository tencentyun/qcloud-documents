
企业帐号CompanyExample（ownerUin为12345678）下有一个子账号Developer，该子账号需要拥有对企业帐号CompanyExample的指定CVM机器（id为ins-1,广州地域）的操作权限。

步骤1：通过策略语法方式创建以下策略
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
步骤2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。
