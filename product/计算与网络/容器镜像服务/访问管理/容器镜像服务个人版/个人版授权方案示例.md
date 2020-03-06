## 典型场景策略配置
>!以下场景策略均只面向个人版使用场景。
>
- 授予子账号容器镜像服务（TCR）个人版（原容器服务 TKE 内镜像仓库）内全部资源的全读写操作权限。
```
{
	"version": "2.0",
	"statement": [{
		"action": [
			"tcr:*"
		],
		"resource": [
			"qcs::tcr:::repo/*"
		],
		"effect": "allow"
	}]
}
```
- 授予子账号 TCR 个人版（原容器服务 TKE 内镜像仓库）内全部资源的只读操作权限。
```
{
	"version": "2.0",
	"statement": [{
		"action": [
			"tcr:Describe*",
			"tcr:PullRepository*"
		],
		"resource": [
			"qcs::tcr:::repo/*"
		],
		"effect": "allow"
	}]
}
```
- 授权子账号管理指定地域内的指定命名空间，例如默认地域内命名空间 team-01。
```
{
	"version": "2.0",
	"statement": [{
			"action": [
				"tcr:*"
			],
			"resource": [
				"qcs::tcr:ap-guangzhou:*:repo/team-01/*"
			],
			"effect": "allow"
		}
	]
}
```
- 授权子账号只读某个镜像仓库，即仅能拉取该仓库内镜像，无法删除仓库、修改仓库属性及推送镜像，例如默认地域内命名空间 team-01 内的镜像仓库 repo-demo。
```
{
	"version": "2.0",
	"statement": [{
			"action": [
				"tcr:Describe*",
				"tcr:PullRepositoryPersonal"
			],
			"resource": [
				"qcs::tcr:ap-guangzhou:*:repo/team-01/repo-demo/*"
			],
			"effect": "allow"
		},
		{
			"action": [
				"tcr:Describe*"
			],
			"resource": [
				"qcs::tcr:ap-guangzhou:*:repo/team-01/*"
			],
			"effect": "allow"
		}
	]
}
```
