
## 1. Instance-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| View instance list | [DescribeInstances](/document/api/213/9388) | Obtain the details of one or more instances.
| View instance status list | [DescribeInstancesStatus](/document/api/213/9389) | Query the status of one of more instances.
| Create instances | [RunInstances](/document/api/213/9384) | Create one or more instances with specified configuration.
| Inquire the prices of created instances| [InquiryPriceRunInstances](/document/api/213/9385) | Inquire the prices of created instances
| Start up instances | [StartInstances](/document/api/213/9386) | Start up one or more instances.
| Stop instances| [StopInstances](/document/api/213/9383) | Stop running of one or more instances.
| Return instances | [TerminateInstances](/document/api/213/9395) | Return instances.
| Restart instances | [RebootInstances](/document/api/213/9396) | Restart one or more instances.
| Reinstall system | [ResetInstance](/document/api/213/9398) | Reinstall the operating system on the specified instance.
| Query the prices of reinstalled operating systems | [InquiryPriceResetInstance](/document/api/213/9490) | Inquire the prices of reinstalled operating systems.
| Scale up instance disks | [ResizeInstanceDisks](/document/api/213/9387) | Scale up disks for an instance.
| Inquire the prices of scaled-up disks for an instance | [InquiryPriceResizeInstanceDisks](/document/api/213/9487) | Inquire the prices of scaled-up disks for an instance.
| Adjust instance configurations | [ResetInstancesType](/document/api/213/9394) | Adjust instance models.
| Inquire the prices of adjusted instance configurations | [InquiryPriceResetInstancesType](/document/api/213/9489) | Query the prices of adjusted instance models.
| Modify instance attributes | [ModifyInstancesAttribute](/document/api/213/9381) | Modify instance attributes.
| Adjust the upper limit of bandwidth for instances | [ResetInstancesInternetMaxBandwidth](/document/api/213/9393) | Adjust the upper limit of the public network bandwidth for instances.
| Modify the project to which an instance belongs | [ModifyInstancesProject](/document/api/213/9380) | Modify the project to which an instance belongs.
| Modify VPC attributes | [UpdateInstanceVpcConfig](/document/api/213/9379) | Modify VPC attributes, such as IP.
| Reset instance password | [ResetInstancesPassword](/document/api/213/9397) | Reset the password of the instance's operating system to a user-specified value.



## 2. Image-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| View image list | [DescribeImages](/document/api/213/9418) | Obtain the images that current account can use to create CVM instances.
| Create custom images | [CreateImage](/document/api/213/9415) | Make the current status of instance system disk into a new image, which can be used to quickly create instances.
| Delete images | [DeleteImages](/document/api/213/9416) | Delete one or more images.
| Modify image attributes | [ModifyImageAttribute](/document/api/213/9414) | Modify the information of an image such as name and description.
| Synchronize images | [SyncImages](/document/api/213/9417) | Copy (synchronize) a custom image to another region.
| Modify image-sharing information | [ModifyImageSharePermission](/document/api/213/9413) | Set image permissions.
| Query image-sharing information| [DescribeImageSharePermission](/document/api/213/9419) | Query the image-sharing information of current account, including the list of accounts to which the image is shared.

## 3. Network-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| Bind a server with an Elastic NIC | AttachNetworkInterface | Bind a server with an EIP

## 4. Security group-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| Query security group list | [DescribeSecurityGroups](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E5%88%97%E8%A1%A8) | Query existing security groups.
| Create security groups| [CreateSecurityGroup](/doc/api/229/%E5%88%9B%E5%BB%BA%E5%AE%89%E5%85%A8%E7%BB%84) | Create security groups.
| Delete security groups | [DeleteSecurityGroup](/doc/api/229/%E5%88%A0%E9%99%A4%E5%AE%89%E5%85%A8%E7%BB%84) | Delete security groups.
| Modify security group attributes | [ModifySecurityGroupAttributes](/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E5%90%8D%E7%A7%B0) |Modify the attribute information of an existing security group, including name and description.
| Query security group rules | [DescribeSecurityGroupPolicy](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | Query the rules for existing security groups.
| Modify security group rules | [ModifySecurityGroupPolicy](/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | Modify the rules for existing security groups.
| Query the list of instances associated with a security group | [DescribeInstancesOfSecurityGroup](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E5%85%B3%E8%81%94%E7%9A%84%E4%BA%91%E4%B8%BB%E6%9C%BA%E5%88%97%E8%A1%A8) | Query the CVM associated with the specified security group.
| Modify the security group associated with instances | [ModifySecurityGroupsOfInstance](/doc/api/229/%E4%BF%AE%E6%94%B9%E4%BA%91%E4%B8%BB%E6%9C%BA%E5%85%B3%E8%81%94%E7%9A%84%E5%AE%89%E5%85%A8%E7%BB%84) | Modify the security group associated with the specified CVM.
| Query the list of associated security groups | [DescribeAssociateSecurityGroups](/doc/api/229/%E6%9F%A5%E8%AF%A2%E4%B8%8E%E5%AE%89%E5%85%A8%E7%BB%84%E5%85%B3%E8%81%94%E7%9A%84%E5%AE%89%E5%85%A8%E7%BB%84%E5%88%97%E8%A1%A8) | Query which security groups have outbound or inbound rules that contain the entered security group ID.

## 5. Elastic IP-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| Query the list of elastic public IPs (EIPs) | [DescribeEip](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%88%97%E8%A1%A8) | Query EIPs
| Query the quota on EIPs| [DescribeEipQuota](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D) |Query the quota on EIPs for a specified region.
| Modify EIP name | [ModifyEipAttributes](/doc/api/229/%E4%BF%AE%E6%94%B9%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%90%8D%E7%A7%B0) | Modify the EIP name.
| Create an EIP | [CreateEip](/doc/api/229/%E5%88%9B%E5%BB%BA%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Create an EIP, a static IP address designed for dynamic cloud computing. With EIP, you can quickly remap the EIP to another instance, shielding off the instance failures.
| Release an EIP | [DeleteEip](/doc/api/229/%E9%87%8A%E6%94%BE%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Release an EIP.
| Bind an EIP | [EipBindInstance](/doc/api/229/%E7%BB%91%E5%AE%9A%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Bind an EIP to a server.
| Unbind an EIP| [EipUnBindInstance](/doc/api/229/%E8%A7%A3%E7%BB%91%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Unbind an EIP from a server.
| Transform an ordinary public IP to an EIP | [TransformWanIpToEip](/doc/api/229/%E6%99%AE%E9%80%9A%E5%85%AC%E7%BD%91IP%E8%BD%AC%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | Transform an ordinary public IP bound to the server to an EIP. After the conversion, the EIP will be retained when the server is released.

## 6. Key-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| Query key pair list | [DescribeKeyPairs](/document/api/213/9403) | Query key pair information.
| Create a key pair | [CreateKeyPair](/document/api/213/9400) | Create an OpenSSH RSA key pair that can be used to log in to a Linux instance.
| Modify key pair attributes | [ModifyKeyPairAttribute](/document/api/213/9399) | Modify key pair attributes.
| Delete key pairs | [DeleteKeyPairs](/document/api/213/9401) | Delete a key pair hosted on Tencent Cloud.
| Import a key pair | [ImportKeyPair](/document/api/213/9402) | Import a key pair.
| Bind a key pair | [AssociasteInstancesKeyPairs](/document/api/213/9404) | Bind a key pair to an instance.
| Unbind a key pair | [DisassociasteInstancesKeyPairs](/document/api/213/9405) | Unbind a key pair from an instance.



