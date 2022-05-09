当权限策略中同时包含允许（allow）和拒绝（deny）的授权语句时，需要根据具体的场景判断 deny 是否生效。

本文通过查询资源列表类的 API、COS 权限 deny 所有用户（匿名用户 anonymous）、计费权限三个典型场景，帮助您理解 deny 不生效的原因。

## 查询资源列表类的 API
###  不生效场景说明
各产品的 API 可以简单划分为增、删、改、查4类，其中查询可以分为查询单个资源详情 API 和查询某类资源列表 API。查询某类资源列表 API 时可能 deny 不生效，建议您避免对这类 action 使用 deny，避免使用 string_not_equal、string_like 等条件键。

### 不生效场景示例
**场景1：**用户授权了允许资源 a、b、c，拒绝了资源 d，又授予了标签 T，其中资源 d 属于标签 T，拒绝资源 d 无法实现。
示例：授权以下策略，用户在查看资源列表的时候仍然能够查看到资源 d。
```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "*"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&T"  //标签 T
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "*"
            ],
            "resource": [
                "qcs::cvm:ap-guangzhou::instanceid/a",  //资源 a
                "qcs::cvm:ap-guangzhou::instanceid/b",  //资源 b
                "qcs::cvm:ap-guangzhou::instanceid/c"   //资源 c
            ]
        },
        {
            "effect": "deny",
            "action": [
                "*"
            ],
            "resource": [
                "qcs::cvm:ap-guangzhou::instanceid/d"   //资源 d
            ]
        }
    ]
}
```

**场景2：**用户授权了允许标签 T1，拒绝标签 T2，其中资源 a 既关联了标签 T1，又关联了标签 T2，拒绝资源 a 无法实现。
例如：授权以下策略，仍然可以在查看资源列表的时候查看到资源 a。
```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "*"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&T1"  //标签 T1
                    ]
                }
            }
        },
        {
            "effect": "deny",
            "action": [
                "*"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&T2"  //标签 T2
                    ]
                }
            }
        }
    ]
}
```

**场景3：**对于包含资源的自定义策略（如标签等场景下的使用和鉴权），有 condition 的情况下，只支持精确匹配的策略条件键，支持 string_equal、ip_equal、ip_not_equal。其他类型条件键（例如 string_not_equal）不支持。
例如：授权以下策略，用户仍然可能看到关联了标签 T 的资源。
```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "*"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_not_equal": {
                    "qcs:resource_tag": [
                        "key&T"  //标签 T
                    ]
                }
            }
        }
    ]
}
```

**场景4：**同时授权了 allow 所有 resource，以及 deny 指定标签，deny 可能无法生效，即仍然能查看到关联了该标签的资源。
例如：授权以下策略，用户在查看资源列表的时候仍然可能查看到主账号下所有的资源。
```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "*"
            ],
            "resource": "*"
        },
        {
            "effect": "deny",
            "action": [
                "*"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&T"  //标签 T
                    ]
                }
            }
        }
    ]
}
```

## COS 权限 deny 所有用户（匿名用户 anonymous）
在 COS 的 Bucket ACL 或 Bucket Policy 中配置 deny 所有用户（匿名用户 anonymous）访问，但如果同时还有另外指定 allow 某个用户，被 allow 的用户仍然可以访问 COS 存储桶。

## 计费权限
如果一个子用户关联了 AdministratorAccess 或 QCloudFinanceFullAccess 策略，同时还关联了一个 deny action finance:xx 的策略，这个子用户在 action finance:xx 仍然可以鉴权通过，不会被拒绝访问。
