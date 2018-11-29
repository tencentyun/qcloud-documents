### 授权子账号拥有特定地域的CVM的操作权限

企业帐号CompanyExample（ownerUin为12345678）下有一个子账号Developer，该子账号需要拥有对企业帐号CompanyExample的广州地域所有机器的操作权限。

step1：企业帐号CompanyExample直接将预设策略QcloudCVMReadOnlyAccess授权给子账号Developer。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

step2：通过策略语法方式创建以下策略
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
step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。
