Here are security group-related APIs:

| Feature | Action ID | Description
|---------|---------|---------|
| Query security group list | [DescribeSecurityGroups](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E5%88%97%E8%A1%A8) | Query the existing security groups.
| Create security group | [CreateSecurityGroup](http://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E5%AE%89%E5%85%A8%E7%BB%84) | Create a security group.
| Delete security group | [DeleteSecurityGroup](http://cloud.tencent.com/doc/api/229/%E5%88%A0%E9%99%A4%E5%AE%89%E5%85%A8%E7%BB%84) | Delete a security group.
| Modify security group attributes | [ModifySecurityGroupAttributes](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E5%90%8D%E7%A7%B0) | Modify the attribute information of an existing security group, including name and description.
| Query security group rules | [DescribeSecurityGroupPolicy](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | Query the rules of an existing security group.
| Modify security group rules | [ModifySecurityGroupPolicy](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | Modify the rules of an existing security group.
| Query bound CVMs | [DescribeInstancesOfSecurityGroup](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E5%85%B3%E8%81%94%E7%9A%84%E4%BA%91%E4%B8%BB%E6%9C%BA%E5%88%97%E8%A1%A8) | Query the CVM bound with the specified security group.
| Modify bound security group | [ModifySecurityGroupsOfInstance](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E4%BA%91%E4%B8%BB%E6%9C%BA%E5%85%B3%E8%81%94%E7%9A%84%E5%AE%89%E5%85%A8%E7%BB%84) | Modify the security group bound with the specified CVM.
| Query bound security groups | [DescribeAssociateSecurityGroups](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E4%B8%8E%E5%AE%89%E5%85%A8%E7%BB%84%E5%85%B3%E8%81%94%E7%9A%84%E5%AE%89%E5%85%A8%E7%BB%84%E5%88%97%E8%A1%A8) | Query which security groups have outbound or inbound rules that contain the entered security group ID.

