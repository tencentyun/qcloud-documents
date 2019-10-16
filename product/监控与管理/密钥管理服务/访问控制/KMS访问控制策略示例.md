## 概述
本文为您详细介绍在访问管理控制台在，创建 KMS 策略。

## 操作步骤
1. 登录 [访问管理](https://console.cloud.tencent.com/cam/overview) 控制台。
2. 在左侧菜单中，现在【策略】>【新建自定义策略】>【按策略语法创建】，进入策略创建页面。
3. 选择策略模板，例如空白模板或 KMS 策略模板，单击【下一步】。
4. 输入策略名称和策略内容，策略内容可参见下方示例。
![](https://main.qcloudimg.com/raw/a95eacce7b1727ce61e8fc9308355d45.jpg)
5. 单击【创建策略】，即可创建。





## 示例
#### KMS 的全读写策略
以下策略允许子账号有所有操作的权限。Action 元素指定所有 KMS 相关 API。
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
#### KMS 的只读策略
以下策略允许子账号查询您的 KMS 资源。但子账号无法创建、更新或删除它们。
在控制台，操作一个资源的前提是可以查看该资源，所以建议您为用户开通 KMS 全读权限。

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

#### 允许子账号做管理类操作

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

#### 允许子账号做数据类操作，但不允许其做管理类操作

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
