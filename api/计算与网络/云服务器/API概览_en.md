## 1. Region-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| Query region list | [DescribeRegions](https://cloud.tencent.com/document/product/213/9456) | Query region information.
| Query list of availability zones | [DescribeZones](https://cloud.tencent.com/document/product/213/9455) | Query the information on availability zones.
## 2. Instance-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| View instance list | [DescribeInstances](/document/api/213/9388) | Obtain the details of one or more instances.
| View instance status list | [DescribeInstancesStatus](/document/api/213/9389) | Query the status of one of more instances.
| Query instance model list | [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/product/213/9391) | Query the instance model configuration.
| Create instances | [RunInstances](/document/api/213/9384) | Create one or more instances with specified configuration.
| Inquire the prices of created instances | [InquiryPriceRunInstances](/document/api/213/9385) | Inquire the prices of created instances.
| Start instances | [StartInstances](/document/api/213/9386) | Start one or more instances.
| Stop instances| [StopInstances](/document/api/213/9383) | Stop running of one or more instances.
| Return instances | [TerminateInstances](/document/api/213/9395) | Return instances.
| Restart instances | [RebootInstances](/document/api/213/9396) | Restart one or more instances.
| Reinstall instances | [ResetInstance](/document/api/213/9398) | Reinstall the operating system on the specified instance.
| Inquire the prices of reinstalled instances | [InquiryPriceResetInstance](/document/api/213/9490) | Inquire the prices of reinstalled instances.
| Scale up instance disks | [ResizeInstanceDisks](/document/api/213/9387) | Scale up data disks for instances.
| Inquire instance disk scale-up price | [InquiryPriceResizeInstanceDisks](/document/api/213/9487) | Inquire the price of scaling up disks for an instance.
| Renew instances | [RenewInstances](/document/api/213/9392) | Renew prepaid instances.
| Inquire the prices of renewed instances | [InquiryPriceRenewInstances](/document/api/213/9491) | Inquire the prices of renewed instances.
| Adjust instance configurations | [ResetInstancesType](/document/api/213/9394) | Adjust instance models.
| Inquire the prices of bandwidth with adjusted upper limit | [InquiryPriceResetInstancesInternetMaxBandwidth](https://cloud.tencent.com/document/product/213/9488) | Inquire the prices of public network bandwidth with adjusted upper limit.
| Inquire the prices of adjusted instance configurations | [InquiryPriceResetInstancesType](/document/api/213/9489) | Inquire the prices of adjusted instance models.
| Modify instance renewal flags | [ModifyInstancesRenewFlag](/document/api/213/9382) | Modify prepaid instance renewal flags.
| Modify instance attributes | [ModifyInstancesAttribute](/document/api/213/9381) | Modify instance attributes.
| Adjust the upper limit of bandwidth for instances | [ResetInstancesInternetMaxBandwidth](/document/api/213/9393) | Adjust the upper limit of the public network bandwidth for instances.
| Modify the project to which an instance belongs | [ModifyInstancesProject](/document/api/213/9380) | Modify the project to which an instance belongs.
| Modify VPC attributes | [UpdateInstanceVpcConfig](/document/api/213/9379) | Modify VPC attributes, such as IP.
| Reset instance password | [ResetInstancesPassword](/document/api/213/9397) | Reset the password of the instance's operating system to a user-specified value.
| Query instance bandwidth configurations| [DescribeInstanceInternetBandwidthConfigs](/document/api/213/9390) | Query instance bandwidth configurations.

## 3. Image-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| View image list | [DescribeImages](/document/api/213/9418) | Obtain the images that current account can use to create CVM instances.
| Create custom images | [CreateImage](/document/api/213/9415) | Make the current status of instance system disk into a new image, which can be used to quickly create instances.
| Delete images | [DeleteImages](/document/api/213/9416) | Delete one or more images.
| Modify image attributes | [ModifyImageAttribute](/document/api/213/9414) | modify the information of an image such as name and description.
| Synchronize images | [SyncImages](/document/api/213/9417) | Copy (synchronize) a custom image to another region.
| Modify image-sharing information | [ModifyImageSharePermission](/document/api/213/9413) | Set image permissions.
| Query image-sharing information| [DescribeImageSharePermission](/document/api/213/9419) | Query the image-sharing information of current account, including the list of accounts to which the image is shared.

## 4. Elastic Public IP-Related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| Query the list of EIPs | [DescribeAddresses](https://cloud.tencent.com/document/product/213/11663) | Query the details of one or more elastic public IPs (EIPs).
| Query the quota on EIPs | [DescribeAddressQuota](https://cloud.tencent.com/document/product/213/11664) | Query the quota on elastic public IPs (EIPs) in the current region.
| Modify EIP Attributes | [ModifyAddressAttribute](https://cloud.tencent.com/document/product/213/11660) | Modify the name of an elastic public IP (EIP).
| Create an EIP | [AllocateAddresses](https://cloud.tencent.com/document/product/213/11661) | Apply for one or more elastic public IPs (EIPs).
| Release EIP | [ReleaseAddresses](https://cloud.tencent.com/document/product/213/11667) | Release one or more elastic public IPs (EIPs).
| Bind EIP | [AssociateAddress](https://cloud.tencent.com/document/product/213/11665) | Bind an elastic public IP (EIP) to a specified private IP of an instance or ENI.
| Unbind EIP | [DisassociateAddress](https://cloud.tencent.com/document/product/213/11666) | Unbind an elastic public IP (EIP).
| Transform ordinary public IP to EIP | [TransformAddress](https://cloud.tencent.com/document/product/213/11662) | Transform an ordinary public IP into an elastic public IP (EIP).

## 5. Key-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| Query key pair list | [DescribeKeyPairs](/document/api/213/9403) | Query key pair information.
| Create a key pair | [CreateKeyPair](/document/api/213/9400) | Create an OpenSSH RSA key pair that can be used to log in to a Linux instance.
| Modify key pair attributes | [ModifyKeyPairAttribute](/document/api/213/9399) | Modify key pair attributes.
| Delete key pair | [DeleteKeyPairs](/document/api/213/9401) | Delete a key pair hosted on Tencent Cloud.
| Import key pair | [ImportKeyPair](/document/api/213/9402) | Import a key pair.
| Bind key pair | [AssociasteInstancesKeyPairs](/document/api/213/9404) | Bind a key pair to an instance.
| Unbind key pair | [DisassociasteInstancesKeyPairs](/document/api/213/9405) | Unbind a key pair from an instance.



