安全组相关接口如下：

| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询安全组列表 | [DescribeSecurityGroupEx](https://cloud.tencent.com/document/api/213/1232) | 用于查询已经存在的安全组。
| 创建安全组 | [CreateSecurityGroup](https://cloud.tencent.com/document/api/213/1238) | 用于创建新的安全组。
| 删除安全组 | [DeleteSecurityGroup](https://cloud.tencent.com/document/api/213/1362) | 用于删除新的安全组。
| 修改安全组名称 | [ModifySecurityGroupAttributes](https://cloud.tencent.com/document/api/213/1363) | 用于修改已经存在的安全组的属性信息，包括名称和描述。
| 查询安全组规则 | [DescribeSecurityGroupPolicys](https://cloud.tencent.com/document/api/213/1364) | 用于查询已经存在的安全组的规则。
| 修改安全组规则 | [ModifySecurityGroupPolicys](https://cloud.tencent.com/document/api/213/1365) | 用于修改已经存在的安全组的规则。
| 查询安全组关联的实例列表 | [DescribeInstancesOfSecurityGroup](https://cloud.tencent.com/document/api/213/1366) | 用于查询已关联指定的安全组的云服务器。
| 修改实例关联的安全组 | [ModifySecurityGroupsOfInstance](https://cloud.tencent.com/document/api/213/1367) | 用于修改指定云服务器关联的安全组。
| 查询关联的安全组列表 | [DescribeAssociateSecurityGroups](https://cloud.tencent.com/document/api/213/1383) | 查询有哪些安全组的出站或入站规则中包含了输入的安全组 ID。
