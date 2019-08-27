## CHDFS 预设策略
CHDFS 预设授权策略如下：

| 策略| 说明 |
|---------|---------|
| QcloudCHDFSReadOnlyAccess | 只读访问 CHDFS 的权限 | 
| QcloudCHDFSFullAccess | 管理 CHDFS 的权限 |


#### CHDFS 授权操作

| **Action**                 | **Resouce**                                                  | **说明**             |
| -------------------------- | ------------------------------------------------------------ | -------------------- |
| chdfs:CreateFileSystem     | qcs::chdfs:${region-id}:uin/${account-id}:filesystem/*       | 创建 CHDFS            |
| chdfs:DeleteFileSystem     | qcs::chdfs:${region-id}:uin/${account-id}:filesystem/${file-system-id} | 删除 CHDFS            |
| chdfs:ModifyFileSystem     | qcs::chdfs:${region-id}:uin/${account-id}:filesystem/${file-system-id} | 修改 CHDFS 属性        |
| chdfs:DescribeFileSystem   | qcs::chdfs:${region-id}:uin/${account-id}:filesystem/${file-system-id} | 查看 CHDFS 详细信息    |
| chdfs:DescribeFileSystems  | qcs::chdfs:${region-id}:uin/${account-id}:filesystem/*       | 查看 CHDFS 列表        |
| chdfs:CreateMountPoint     | qcs::chdfs:${region-id}:uin/${account-id}:mountpoint/*       | 创建挂载点           |
| chdfs:DeleteMountPoint     | qcs::chdfs:${region-id}:uin/${account-id}:mountpoint/${mount-point-id} | 删除挂载点           |
| chdfs:ModifyMountPoint     | qcs::chdfs:${region-id}:uin/${account-id}:mountpoint/${mount-point-id} | 修改挂载点属性       |
| chdfs:DescribeMountPoint   | qcs::chdfs:${region-id}:uin/${account-id}:mountpoint/${mount-point-id} | 查看挂载点详细信息   |
| chdfs:DescribeMountPoints  | qcs::chdfs:${region-id}:uin/${account-id}:mountpoint/*       | 查看挂载点列表       |
| chdfs:CreateAccessGroup    | qcs::chdfs:${region-id}:uin/${account-id}:accessgroup/*      | 创建权限组           |
| chdfs:DeleteAccessGroup    | qcs::chdfs:${region-id}:uin/${account-id}:accessgroup/${access-group-id} | 删除权限组           |
| chdfs:ModifyAccessGroup    | qcs::chdfs:${region-id}:uin/${account-id}:accessgroup/${access-group-id} | 修改权限组属性       |
| chdfs:DescribeAccessGroups | qcs::chdfs:${region-id}:uin/${account-id}:accessgroup/*      | 查看权限组列表       |
| chdfs:CreateAccessRules    | qcs::chdfs:${region-id}:uin/${account-id}:accessrule/*       | 批量创建权限规则     |
| chdfs:DeleteAccessRules    | qcs::chdfs:${region-id}:uin/${account-id}:accessrule/${access-rule-ids} | 批量删除权限规则     |
| chdfs:ModifyAccessRules    | qcs::chdfs:${region-id}:uin/${account-id}:accessrule/${access-group-ids} | 批量修改权限规则属性 |
| chdfs:DescribeAccessRules  | qcs::chdfs:${region-id}:uin/${account-id}:accessrule/*       | 查看权限规则列表     |

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
