## CHDFS 预设策略
CHDFS 预设授权策略如下：

| 策略| 说明 |
|---------|---------|
| QcloudCHDFSReadOnlyAccess | 只读访问 CHDFS 的权限 | 
| QcloudCHDFSFullAccess | 管理 CHDFS 的权限 |


#### CHDFS 授权操作

| **Action**                 | **Resouce**                                                  | **说明**             |
| -------------------------- | ------------------------------------------------------------ | -------------------- |
| chdfs:CreateFileSystem     | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/*       | 创建 CHDFS            |
| chdfs:DeleteFileSystem     | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 删除 CHDFS            |
| chdfs:ModifyFileSystem     | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 修改 CHDFS 属性        |
| chdfs:DescribeFileSystem   | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 查看 CHDFS 详细信息    |
| chdfs:DescribeFileSystems  | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 查看 CHDFS 列表        |
| chdfs:CreateMountPoint     | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 创建挂载点           |
| chdfs:DeleteMountPoint     | qcs::chdfs:${region-id}:uin/${account-uin}:mountpoint/${mount-point-id} | 删除挂载点           |
| chdfs:ModifyMountPoint     | qcs::chdfs:${region-id}:uin/${account-uin}:mountpoint/${mount-point-id} | 修改挂载点属性       |
| chdfs:DescribeMountPoint   | qcs::chdfs:${region-id}:uin/${account-uin}:mountpoint/${mount-point-id} | 查看挂载点详细信息   |
| chdfs:DescribeMountPoints  | qcs::chdfs:${region-id}:uin/${account-uin}:mountpoint/${mount-point-id} | 查看挂载点列表       |
| chdfs:AssociateAccessGroups   | qcs::chdfs:${region-id}:uin/${account-uin}:mountpoint/${mount-point-id} | 绑定权限组列表  |
| chdfs:DisassociateAccessGroups| qcs::chdfs:${region-id}:uin/${account-uin}:mountpoint/${mount-point-id} | 解绑权限组列表 |
| chdfs:CreateAccessGroup    | qcs::chdfs:${region-id}:uin/${account-uin}:vpc/${vpc-id}<br>或qcs::chdfs:${region-id}:uin/${account-uin}:unVpcId/${unVpcId}     | 创建权限组           |
| chdfs:DeleteAccessGroup    | qcs::chdfs:${region-id}:uin/${account-uin}:accessgroup/${access-group-id} | 删除权限组           |
| chdfs:ModifyAccessGroup    | qcs::chdfs:${region-id}:uin/${account-uin}:accessgroup/${access-group-id} | 修改权限组属性       |
| chdfs:DescribeAccessGroup  | qcs::chdfs:${region-id}:uin/${account-uin}:accessgroup/${access-group-id} | 查看权限组详细信息  |
| chdfs:DescribeAccessGroups | qcs::chdfs:${region-id}:uin/${account-uin}:accessgroup/${access-group-id} | 查看权限组列表       |
| chdfs:CreateAccessRules    | qcs::chdfs:${region-id}:uin/${account-uin}:accessgroup/${access-group-id}  | 批量创建权限规则     |
| chdfs:DeleteAccessRules    | qcs::chdfs:${region-id}:uin/${account-uin}:accessgroup/${access-group-id} | 批量删除权限规则     |
| chdfs:ModifyAccessRules    | qcs::chdfs:${region-id}:uin/${account-uin}:accessgroup/${access-group-id} | 批量修改权限规则属性 |
| chdfs:DescribeAccessRules  | qcs::chdfs:${region-id}:uin/${account-uin}:accessgroup/${access-group-id} | 查看权限规则列表     |
| chdfs:CreateLifeCycleRules | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id}  | 批量创建生命周期规则 |
| chdfs:DeleteLifeCycleRules | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 批量删除生命周期规则 |
| chdfs:ModifyLifeCycleRules | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 批量修改生命周期规则属性 |
| chdfs:DescribeLifeCycleRules | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 查看生命周期规则列表  |
| chdfs:CreateRestoreTasks    | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id}  | 批量创建回热任务    |
| chdfs:DescribeRestoreTasks  | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 查看回热任务列表    |
| chdfs:CreateInventoryConfig | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id}  | 创建清单配置 |
| chdfs:DeleteInventoryConfig | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 删除清单配置 |
| chdfs:ModifyInventoryConfig | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 修改清单配置属性 |
| chdfs:DescribeInventoryConfigs | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 查看清单配置列表  |
| chdfs:CreatePathProtectionRule | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id}  | 创建路径保护规则 |
| chdfs:DeletePathProtectionRule | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 删除路径保护规则 |
| chdfs:ModifyPathProtectionRule | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 修改路径保护规则属性 |
| chdfs:DescribePathProtectionRules | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 查看路径保护规则列表  |
| chdfs:ModifyResourceTags    | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id}  | 修改资源标签列表    |
| chdfs:DescribeResourceTags  | qcs::chdfs:${region-id}:uin/${account-uin}:filesystem/${file-system-id} | 查看资源标签列表     |


## CHDFS 授权策略示例
授予子账号 CHDFS 管控系统只读权限的策略示例如下：
```
{
	"version": "2.0",
	"statement": [{
		"effect": "allow",
		"action": [
			"name/chdfs:Describe*"
		],
		"resource": [
	 		"*"
		]
	}]
}
```

授予子账号查看 CHDFS 的策略示例如下：
```
{
	"version": "2.0",
	"statement": [{
		"effect": "allow",
		"action": [
 			"name/chdfs:DescribeFileSystem"
  		],
		"resource": [
			"qcs::chdfs::uin/ownerUin:filesystem/fileSystemId"
		]
	}]
}
```
