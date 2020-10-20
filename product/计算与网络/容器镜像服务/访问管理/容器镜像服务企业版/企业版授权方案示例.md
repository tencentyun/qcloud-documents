
## 预设策略配置
- **QcloudTCRFullAccess**：容器镜像服务（TCR）全读写权限。
子账号绑定该策略后，将具有 TCR 全部资源的全部操作权限，包含企业版及容器服务 TKE 内的个人版。
```
	{
		"version": "2.0",
		"statement": [{
			"action": [
				"tcr:*"
			],
			"resource": "*",
			"effect": "allow"
		}]
	}
```
- **QcloudTCRReadOnlyAccess**：TCR 只读权限。
子账号绑定该策略后，将具有容器镜像服务全部资源的只读权限，包含企业版及容器服务 TKE 内的个人版。
```
	{
		"version": "2.0",
		"statement": [{
			"action": [
				"tcr:Describe*",
				"tcr:PullRepository*"
			],
			"resource": "*",
			"effect": "allow"
		}]
	}
```

## 典型场景策略配置
>!以下场景策略均只面向企业版使用场景。
>
- 授予子账号 TCR 企业版内全部资源的全读写操作权限。
```
	{
		"version": "2.0",
		"statement": [{
			"action": [
				"tcr:*"
			],
			"resource": [
				"qcs::tcr:::instance/*",
				"qcs::tcr:::repository/*"
			],
			"effect": "allow"
		}]
	}
```
- 授予子账号 TCR 企业版内全部资源的只读操作权限。
```
	{
		"version": "2.0",
		"statement": [{
			"action": [
				"tcr:Describe*",
				"tcr:PullRepository*"
			],
			"resource": [
				"qcs::tcr:::instance/*",
				"qcs::tcr:::repository/*"
			],
			"effect": "allow"
		}]
	}
```
- 授权子账号管理指定实例，例如 dev-guangzhou，其实例 ID 为 ins-xxxxxxxx。
```
	{
		"version": "2.0",
		"statement": [{
			"action": [
				"tcr:*"
			],
			"resource": [
				"qcs::tcr:::instance/ins-xxxxxxxx/*"
			],
			"effect": "allow"
		}]
	}
```
- 授权子账号管理指定实例内的指定命名空间，例如实例 ins-xxxxxxxx 下 team-01。
```
	{
		"version": "2.0",
		"statement": [{
				"action": [
					"tcr:*"
				],
				"resource": [
					"qcs::tcr:::repository/ins-xxxxxxxx/team-01/*"
				],
				"effect": "allow"
			},
			{
				"action": [
					"tcr:DescribeInstances",
					"tcr:DescribeInstanceStatus"
				],
				"resource": [
					"qcs::tcr:::repository/ins-xxxxxxxx/*"
				],
				"effect": "allow"
			}
		]
	}
```
- 授权子账号只读某个镜像仓库，仅能拉取该仓库内镜像，无法删除仓库、修改仓库属性及推送镜像。例如实例 ins-xxxxxxxx 下 team-01 命名空间内的 repo-demo。
```
	{
		"version": "2.0",
		"statement": [{
				"action": [
					"tcr:DescribeRepository",
					"tcr:PullRepository"
				],
				"resource": [
					"qcs::tcr:::repository/ins-xxxxxxxx/team-01/repo-demo/*"
				],
				"effect": "allow"
			},
			{
				"action": [
					"tcr:DescribeInstances",
					"tcr:DescribeInstanceStatus",
					"tcr:DescribeNamespace"
				],
				"resource": [
					"qcs::tcr:::repository/ins-xxxxxxxx/*"
				],
				"effect": "allow"
			}
		]
	}
```
