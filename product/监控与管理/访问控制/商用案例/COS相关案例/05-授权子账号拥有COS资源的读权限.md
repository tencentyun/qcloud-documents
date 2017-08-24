### 授权子账号拥有该账号下COS资源的读权限

企业帐号CompanyExample（ownerUin为12345678）下有一个子账号Developer，该子账号需要拥有对企业帐号CompanyExample的COS服务的只读访问权限（访问COS的存储桶或者对象及对象列表等）。

方案A：

企业帐号CompanyExample直接将预设策略QcloudCOSReadOnlyAccess授权给子账号Developer。授权方式请参考[授权管理](https://www.qcloud.com/document/product/378/8961)。

方案B：

step1：通过策略语法方式创建以下策略
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action":  [
                    "cos:List*",
                    "cos:Get*",
                    "cos:Head*",
                    "cos:OptionsObject"
                ],
         "resource": "*"
     }
}
```
step2：将该策略授权给子账号。授权方式请参考[授权管理](https://www.qcloud.com/document/product/378/8961)。
