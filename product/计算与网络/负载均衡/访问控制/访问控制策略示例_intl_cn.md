### CLB的全读写策略
授权一个子用户以CLB服务的完全管理权限（创建、管理等全部操作）。
> 策略名称：CLBResourceFullAccess
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
            "name/clb:*",
      ],
      "resource": "*",
      "effect": "allow"
    }
  ]
}
```
### CLB的只读策略
授权一个子用户只读访问CLB的权限（即可以查看所有LB下面所有资源的权限），但用户无法创建、更新或删除它们。 在控制台，操作一个资源的前提是可以查看该资源，所以建议您为子账户开通CLB全读权限。
> 策略名称： CLBResourceReadOnlyAccess

```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
            "name/clb:Describe*",
      ],
      "resource": "*",
      "effect": "allow"
    }
  ]
}
```
