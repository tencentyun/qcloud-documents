## HTTPDNS 的全读写策略
- 为子用户或协作者授权完全读写权限（创建、管理等全部操作）。
- 策略名称：QcloudHTTPDNSFullAccess
```
{
"version": "2.0",
"statement": [
   {
     "effect": "allow",
     "action": [
     "httpdns:*"
     ],
    "resource": "*"
  }
]
}
```

## HTTPDNS 的只读策略
- 授权一个子用户只读访问 HTTPDNS 的权限（即可以查看所有 HTTPDNS 下面所有资源的权限），但用户无法创建、更新或删除它们。 在控制台，操作一个资源的前提是可以查看该资源，所以建议您为子账户开通 HTTPDNS 全读权限。
- 策略名称： QcloudHTTPDNSReadOnlyAccess
```
{
"version": "2.0",
"statement": [
   {
      "effect": "allow",
      "action": [
      "httpdns:Describe*"
      ],
      "resource": "*"
    }
]
}
```




