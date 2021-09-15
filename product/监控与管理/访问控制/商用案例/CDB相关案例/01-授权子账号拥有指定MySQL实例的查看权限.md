
企业帐号 CompanyExample（ownerUin 为 12345678）下有一个子账号 Developer，该子账号需要拥有对企业帐号 CompanyExample 名下的两个 MySQL 实例（实例 ID 分别是 cdb-1 和 cdb-2）的查看权限。

步骤1：通过策略语法方式创建以下策略。
```json
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
步骤2：将该策略授权给子账号。授权方式请参考 [授权管理](https://cloud.tencent.com/document/product/378/8961)。

>?子账号 Developer 在 MySQL 的查询列表页同样仅能查看到实例 ID 为 cdb-1 和 cdb-2 的资源。


