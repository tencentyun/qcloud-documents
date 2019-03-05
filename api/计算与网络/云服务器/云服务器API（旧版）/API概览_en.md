## 1. Instance-related APIs
| Name | Action ID | Description
|---------|---------|---------|
| View instance list | [DescribeInstances](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8) | Obtain the details of one or more instances.
| Create prepaid instances | [RunInstances](http://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E5%AE%9E%E4%BE%8B%EF%BC%88%E5%8C%85%E5%B9%B4%E5%8C%85%E6%9C%88%EF%BC%89) | Create one or more prepaid instances with specified configuration.
| Create postpaid instances | [RunInstancesHour](http://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E5%AE%9E%E4%BE%8B%EF%BC%88%E6%8C%89%E9%87%8F%E8%AE%A1%E8%B4%B9%EF%BC%89) | Create one or more postpaid instances with specified configuration.
| Start up instances | [StartInstances](http://cloud.tencent.com/doc/api/229/%E5%90%AF%E5%8A%A8%E5%AE%9E%E4%BE%8B) | Start one or more instances.
| Stop instances | [StopInstances](http://cloud.tencent.com/doc/api/229/%E5%85%B3%E9%97%AD%E5%AE%9E%E4%BE%8B) | Stop running of one or more instances.
| Restart instances | [RestartInstances](http://cloud.tencent.com/doc/api/229/%E9%87%8D%E5%90%AF%E5%AE%9E%E4%BE%8B) | Restart one or more instances.
| Reinstall system | [ResetInstances](http://cloud.tencent.com/doc/api/229/%E9%87%8D%E8%A3%85%E7%B3%BB%E7%BB%9F) | Reinstall the operating system on the specified instance.
| Modify instance attributes | [ModifyInstanceAttributes](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%9E%E4%BE%8B%E5%90%8D%E7%A7%B0) | Modify the attributes of an instance, such as instance name.
| Reset password | [ResetInstancePassword](http://cloud.tencent.com/doc/api/229/%E9%87%8D%E7%BD%AE%E5%AF%86%E7%A0%81) | Reset the password of the instance's operating system to a user-specified value.
| Query prepaid instance price | [InquiryInstancePrice](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%9E%E4%BE%8B%E4%BB%B7%E6%A0%BC%EF%BC%88%E5%8C%85%E5%B9%B4%E5%8C%85%E6%9C%88%EF%BC%89) | Obtain the price of prepaid instances.
| Query postpaid instance price | [InquiryInstancePriceHour](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%9E%E4%BE%8B%E4%BB%B7%E6%A0%BC%EF%BC%88%E6%8C%89%E9%87%8F%E8%AE%A1%E8%B4%B9%EF%BC%89) | Obtain the price of postpaid instances.
| Change Configurations of Prepaid Instances | [ResizeInstance](http://cloud.tencent.com/doc/api/229/%E8%B0%83%E6%95%B4%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE%EF%BC%88%E5%8C%85%E5%B9%B4%E5%8C%85%E6%9C%88%EF%BC%89) | Change configuration of specified instance, including CPU, memory, and data disks.
| Change Configurations of Postpaid Instances | [ResizeInstanceHour](http://cloud.tencent.com/doc/api/229/%E8%B0%83%E6%95%B4%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE%EF%BC%88%E6%8C%89%E9%87%8F%E8%AE%A1%E8%B4%B9%EF%BC%89) | Change configuration of specified instance, including CPU, memory, and data disks.
| Renew prepaid instances | [RenewInstance](http://cloud.tencent.com/doc/api/229/%E7%BB%AD%E8%B4%B9%E5%AE%9E%E4%BE%8B%EF%BC%88%E5%8C%85%E5%B9%B4%E5%8C%85%E6%9C%88%EF%BC%89) |Renew the instance with an annual or monthly plan.
| Return postpaid instances | [ReturnInstance](http://cloud.tencent.com/doc/api/229/%E9%80%80%E8%BF%98%E5%AE%9E%E4%BE%8B%EF%BC%88%E6%8C%89%E9%87%8F%E8%AE%A1%E8%B4%B9%EF%BC%89) | Used to return instances.
| Change Projects of Instances | [ModifyInstanceProject](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%9E%E4%BE%8B%E6%89%80%E5%B1%9E%E9%A1%B9%E7%9B%AE) | Modify the project to which an instance belongs.
| Set Intances to Auto-renewal | [SetAutoRenew](/document/product/213/1746) | Set renewal policy for an instance.

## 2. Image-related APIs
| Name | Action ID | Description
|---------|---------|---------|
| View list of available images | [DescribeImages](http://cloud.tencent.com/document/api/213/1272) | Obtain the images that current account can use to create CVM instances.
| Create custom images | [CreateImage](http://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89%E9%95%9C%E5%83%8F) | Make the current status of instance system disk into a new image, which can be used to quickly create instances.
| Delete images | [DeleteImages](http://cloud.tencent.com/doc/api/229/%E5%88%A0%E9%99%A4%E9%95%9C%E5%83%8F) |Delete one or more images.
| Modify image attributes | [ModifyImageAttributes](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E9%95%9C%E5%83%8F%E5%B1%9E%E6%80%A7) | Modify the information of an image such as name and description.
| Copy images | [SyncCvmImage](http://cloud.tencent.com/doc/api/229/%E5%A4%8D%E5%88%B6%E9%95%9C%E5%83%8F) | Copy (synchronize) a custom image to another region.
| Share images | [ShareImage](http://cloud.tencent.com/doc/api/229/%E5%85%B1%E4%BA%AB%E9%95%9C%E5%83%8F) | Share an image to other accounts.
| Cancel image-sharing | [CancelShareImage](http://cloud.tencent.com/doc/api/229/%E5%8F%96%E6%B6%88%E5%85%B1%E4%BA%AB%E9%95%9C%E5%83%8F) | Cancel the sharing of image.
| Query the list of accounts to which the image is shared| [GetImageShareUinInfo](/document/api/213/2391) | Query the image-sharing information of current account, including the list of accounts to which the image is shared.

## 3. Network-related APIs
| Name | Action ID | Description
|---------|---------|---------|
| Adjust the bandwidth of prepaid instances | [UpdateInstanceBandwidth](/document/api/213/1251) | Adjust the bandwidth of public network of instances with an annual or monthly plan.
| Adjust the bandwidth of postpaid instances | [UpdateInstanceBandwidthHour](/document/api/213/1345) | Adjust the bandwidth of public network of postpaid instances.

## 4. Security group-related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query security group list | [DescribeSecurityGroups](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E5%88%97%E8%A1%A8) | Query the list of existing security groups.
| Create security group| [CreateSecurityGroup](http://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E5%AE%89%E5%85%A8%E7%BB%84) | Create a new security group.
| Delete security group | [DeleteSecurityGroup](http://cloud.tencent.com/doc/api/229/%E5%88%A0%E9%99%A4%E5%AE%89%E5%85%A8%E7%BB%84) | Delete a security group.
| Rename security groups | [ModifySecurityGroupAttributes](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E5%90%8D%E7%A7%B0) |Modify the attribute information of an existing security group, including name and description.
| Query security group rules | [DescribeSecurityGroupPolicy](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | Query the rules for existing security groups.
| Modify security group rules | [ModifySecurityGroupPolicy](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | Modify the rules for existing security groups.
| Query the list of instances associated with a security group | [DescribeInstancesOfSecurityGroup](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E5%85%B3%E8%81%94%E7%9A%84%E4%BA%91%E4%B8%BB%E6%9C%BA%E5%88%97%E8%A1%A8) |Query the CVM associated with the specified security group.
| Modify the security group associated with instances | [ModifySecurityGroupsOfInstance](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E4%BA%91%E4%B8%BB%E6%9C%BA%E5%85%B3%E8%81%94%E7%9A%84%E5%AE%89%E5%85%A8%E7%BB%84) | Modify the security group associated with the specified CVM.
| Query the list of associated security groups | [DescribeAssociateSecurityGroups](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E4%B8%8E%E5%AE%89%E5%85%A8%E7%BB%84%E5%85%B3%E8%81%94%E7%9A%84%E5%AE%89%E5%85%A8%E7%BB%84%E5%88%97%E8%A1%A8) | Query which security groups have outbound or inbound rules that contain the entered security group ID.

## 5. Elastic IP-related APIs
| Name | Action ID | Description
|---------|---------|---------|
| Query the list of elastic public IPs (EIPs) | [DescribeEip](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%88%97%E8%A1%A8) | Query EIPs
| Query the quota on EIPs| [DescribeEipQuota](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D) |Query the quota on EIPs for specified region.
| Modify EIP name | [ModifyEipAttributes](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%90%8D%E7%A7%B0) | Modify the EIP name.
| Create an EIP | [CreateEip](http://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Create an EIP, a static IP address designed for dynamic cloud computing. With EIP, you can quickly remap the EIP to another instance, shielding off the instance failures.
| Release EIP | [DeleteEip](http://cloud.tencent.com/doc/api/229/%E9%87%8A%E6%94%BE%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Release an EIP.
| Bind EIP | [EipBindInstance](http://cloud.tencent.com/doc/api/229/%E7%BB%91%E5%AE%9A%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Bind an EIP to the server.
| Unbind EIP| [EipUnBindInstance](http://cloud.tencent.com/doc/api/229/%E8%A7%A3%E7%BB%91%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Unbind the EIP from the server.
| Transform ordinary public IP to EIP | [TransformWanIpToEip](http://cloud.tencent.com/doc/api/229/%E6%99%AE%E9%80%9A%E5%85%AC%E7%BD%91IP%E8%BD%AC%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Convert an ordinary public IP bound to the server to an EIP. After the conversion, the EIP will be retained when the server is released. 

## 6. Key-related APIs
| Name | Action ID | Description
|---------|---------|---------|
| Query keys | [DescribeKeyPairs](http://cloud.tencent.com/doc/api/229/查询密钥) | Query keys
| Create a key | [CreateKeyPair](http://cloud.tencent.com/doc/api/229/创建密钥) | Create a key.
| Modify key name | [ModifyKeyPair](http://cloud.tencent.com/doc/api/229/修改密钥名称) | Modify the key name.
| Delete keys | [DeleteKeyPair](http://cloud.tencent.com/doc/api/229/删除密钥) | Delete keys.
| Import keys | [ImportKeyPair](http://cloud.tencent.com/doc/api/229/导入密钥) | Import keys.
| Bind a key | [BindInstanceKey](http://cloud.tencent.com/doc/api/229/绑定密钥) | Bind a key to a CVM instance.
| Unbind a key | [unBindInstanceKey](http://cloud.tencent.com/doc/api/229/解绑密钥) | Unbind a key from the CVM.


