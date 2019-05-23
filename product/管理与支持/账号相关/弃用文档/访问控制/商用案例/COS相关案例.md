### 授权子帐号拥有COS资源的所有权限

企业帐号CompanyExample下有一个子账号Developer，该子账号需要拥有对企业帐号CompanyExample名下的COS资源的所有权限

方案A：

企业帐号CompanyExample直接将预设策略QcloudCOSFullAccess授权给子账号Developer。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

方案B：

step1：通过策略语法方式创建以下策略

```
{
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": "name/cos:*"
         "resource": "*"
     }
}
```

step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

### 跨帐号访问权限和公有读写权限

请参考COS文档说明。