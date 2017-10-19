### 03-授权子账号对特定目录内文件的读权限

企业帐号 CompanyExample（ownerUin为12345678,appId为8000001）下有一个子账号 Developer，该子账号需要拥有对企业帐号CompanyExample 的 COS 服务的上海地域名为 Bucket1 的存储桶的 dir1 目录下文件的读权限。

方案A：

step1：通过策略语法方式创建以下策略
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": "cos:*",
         "resource": ["qcs::cos:cn-east:uid/8000001:prefix//8000001/Bucket1/dir1/*",
                    "qcs::cos:cn-east:uid/8000001:prefix//8000001/Bucket1/dir1"]
     }
}
```
step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

方案B：

通过 COS 控制台进行 Policy 和 ACL 设置。具体请参考 COS 文档。