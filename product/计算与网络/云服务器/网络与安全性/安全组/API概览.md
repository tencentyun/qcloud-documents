安全组相关接口如下：

| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询安全组列表 | [DescribeSecurityGroups](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E5%88%97%E8%A1%A8) | 用于查询已经存在的安全组。
| 创建安全组 | [CreateSecurityGroup](http://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E5%AE%89%E5%85%A8%E7%BB%84) | 用于创建新的安全组。
| 删除安全组 | [DeleteSecurityGroup](http://cloud.tencent.com/doc/api/229/%E5%88%A0%E9%99%A4%E5%AE%89%E5%85%A8%E7%BB%84) | 用于删除新的安全组。
| 修改安全组名称 | [ModifySecurityGroupAttributes](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E5%90%8D%E7%A7%B0) | 用于修改已经存在的安全组的属性信息，包括名称和描述。
| 查询安全组规则 | [DescribeSecurityGroupPolicy](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | 用于查询已经存在的安全组的规则。
| 修改安全组规则 | [ModifySecurityGroupPolicy](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | 用于修改已经存在的安全组的规则。
| 查询安全组关联的实例列表 | [DescribeInstancesOfSecurityGroup](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E5%85%B3%E8%81%94%E7%9A%84%E4%BA%91%E4%B8%BB%E6%9C%BA%E5%88%97%E8%A1%A8) | 用于查询已关联指定的安全组的云服务器。
| 修改实例关联的安全组 | [ModifySecurityGroupsOfInstance](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E4%BA%91%E4%B8%BB%E6%9C%BA%E5%85%B3%E8%81%94%E7%9A%84%E5%AE%89%E5%85%A8%E7%BB%84) | 用于修改指定云服务器关联的安全组。
| 查询关联的安全组列表 | [DescribeAssociateSecurityGroups](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E4%B8%8E%E5%AE%89%E5%85%A8%E7%BB%84%E5%85%B3%E8%81%94%E7%9A%84%E5%AE%89%E5%85%A8%E7%BB%84%E5%88%97%E8%A1%A8) | 查询有哪些安全组的出站或入站规则中包含了输入的安全组 ID。
