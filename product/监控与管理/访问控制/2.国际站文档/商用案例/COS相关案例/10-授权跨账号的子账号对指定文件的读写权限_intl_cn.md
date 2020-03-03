### 授权跨账号的子账号对指定文件的读写权限

企业帐号 CompanyGranter（ownerUin为12345678,appId为8000001）,该账号拥有一个对象 Object1，在广州地域名为 Bucket1 的存储桶的dir1 目录下。另外一个企业帐号 CompanyGrantee（ownerUin为87654321）,其子账号需要拥有上述对象的读写权限。

这里涉及权限传递。

step1：企业帐号 CompanyGrantee 通过策略语法方式创建以下策略
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": "cos:*",
         "resource": "qcs::gz:cvm:uid/8000001:prefix//8000001/Bucket1/dir1/Object1"
     }
}
```
step2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

step3：企业帐号 CompanyGranter 通过 COS 控制台进行 Policy 和 ACL 设置，将对象 Object1 授权给企业帐号 CompanyGrantee，具体请参考 COS 文档。
