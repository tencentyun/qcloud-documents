当权限策略中同时包含允许（allow）和拒绝（deny）的授权语句时，需要根据具体的场景判断 deny 是否生效。

本文通过查询资源列表类的操作、COS 权限 deny 所有用户（匿名用户 anonymous）、计费相关操作三类典型场景，帮助您理解 deny 不生效的逻辑。

## 查询资源列表类的操作

腾讯云各个服务的操作（action）可以简单划分为增、删、改、查 4 类，其中查询类又可以分为查询单个资源详情和查询某类资源列表，查询某类资源列表的操作。在以下场景中可能存在 deny 不生效，**建议对这类操作避免使用 deny，避免使用 string_not_equal、string_like 等条件键**。


#### 不生效场景列举：
**场景1：**授权允许（allow）子用户访问 CVM 实例 a、b、c，拒绝（deny）访问实例 d，同时又授予子用户访问绑定标签 T 的资源，其中实例 d 绑定了标签T，此时“拒绝（deny）访问实例 d”的策略不会生效。

例如：授权以下策略，用户在查看 CVM 实例列表的时候仍然能够查看到实例 d。
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
                "qcs::cvm:ap-guangzhou::instanceid/a",  //实例 a
                "qcs::cvm:ap-guangzhou::instanceid/b",  //实例 b
                "qcs::cvm:ap-guangzhou::instanceid/c"   //实例 c
            ]
        },
        {
            "effect": "deny",
            "action": [
                "*"
            ],
            "resource": [
                "qcs::cvm:ap-guangzhou::instanceid/d"   //实例 d
            ]
        }
    ]
}
```

**场景2：**授权允许子用户访问绑定标签 T1 的资源，拒绝访问绑定标签 T2 的资源，其中资源 a 既绑定了标签 T1，又绑定了标签 T2，则拒绝访问 a 资源的策略不会生效。

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

**场景3：**权限策略包含 condition 时，支持精确匹配的策略条件键使用 string_equal、ip_equal、ip_not_equal 等才会生效，其他类型条件键（例如 string_not_equal 等）不会生效。

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

**场景4：**同时授权允许访问所有 resource，以及拒绝访问绑定指定标签的资源时，拒绝访问可能无法生效，即仍然能查看到关联了该标签的资源。

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

## 计费相关操作

如果一个子用户关联了 AdministratorAccess 或 QCloudFinanceFullAccess 策略，同时还关联了一个 deny action finance:xx 的策略，这个子用户在 action finance:xx 仍然可以鉴权通过，不会被拒绝访问。
