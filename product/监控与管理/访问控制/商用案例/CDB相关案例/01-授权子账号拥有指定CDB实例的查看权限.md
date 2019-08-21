
企业帐号CompanyExample（ownerUin为12345678）下有一个子账号Developer，该子账号需要拥有对企业帐号CompanyExample名下的两个cdb实例（实例id分别是cdb-1和cdb-2）的查看权限，

步骤1：通过策略语法方式创建以下策略
```
 {
    "version": "2.0",
    "statement":[
     {
         "effect": "allow",
         "action": "cdb:*",
         "resource": ["qcs::cdb::uin/12345678:instanceId/cdb-1", "qcs::cdb::uin/12345678:instanceId/cdb-2"]
     }
   ]
}
```
步骤2：将该策略授权给子账号。授权方式请参考[授权管理](https://cloud.tencent.com/document/product/378/8961)。

注：子账号Developer在CDB的查询列表页同样仅能查看到实例id为cdb-1和cdb-2的资源。

