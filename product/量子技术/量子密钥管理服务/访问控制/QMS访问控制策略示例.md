### QMS 的全读写策略
以下策略允许子账号拥有所有操作的权限。Action 元素指定所有 QMS 相关 API。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/kms:*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
### QMS 的只读策略
以下策略允许子账号查询您的 QMS 资源。但子账号无法创建、更新或删除它们。
在控制台，操作一个资源的前提是可以查看该资源，所以建议您为用户开通 QMS 全读权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/kms:ListKey",
                "name/kms:GetKeyAttributes"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

### 允许子账号做管理类操作


```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/kms:CreateKey",
                "name/kms:ListKey",
                "name/kms:GetKeyAttributes",
                "name/kms:SetKeyAttributes"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```

### 允许子账号做数据类操作，但不允许其做管理类操作



```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/kms:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "action": [
                "name/kms:CreateKey",
                "name/kms:ListKey",
                "name/kms:GetKeyAttributes",
                "name/kms:SetKeyAttributes"
            ],
            "resource": "*",
            "effect": "deny"
        }
    ]
}
```
