
## 1. 实例相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查看实例列表 | [DescribeInstances](/document/api/213/9388) |  用于获取一个或多个实例的详细信息。
| 查看实例状态列表 | [DescribeInstancesStatus](/document/api/213/9389) |  用于查询一个或多个实例的状态。
| 创建实例 | [RunInstances](/document/api/213/9384) | 用于创建一台或多台指定配置的实例。
| 创建实例询价 | [InquiryPriceRunInstances](/document/api/213/9385) | 用于创建实例询价。
| 启动实例 | [StartInstances](/document/api/213/9386) | 用于启动一个或者多个实例。
| 关闭实例 | [StopInstances](/document/api/213/9383) | 用于关闭一个或者多个实例。
| 退还实例 | [TerminateInstances](/document/api/213/9395) | 用于主动退还实例。
| 重启实例 | [RebootInstances](/document/api/213/9396) | 用于重启一个或者多个实例。
| 重装实例 | [ResetInstance](/document/api/213/9398) | 用于重装指定实例上的操作系统。
| 重装实例询价 | [InquiryPriceResetInstance](/document/api/213/9490) | 用于重装系统询价。
| 扩容实例磁盘 | [ResizeInstanceDisks](/document/api/213/9387) | 用于扩容实例的数据盘。
| 扩容实例磁盘询价 | [InquiryPriceResizeInstanceDisks](/document/api/213/9487) | 用于扩容实例的数据盘询价。
| 续费实例 | [RenewInstances](/document/api/213/9392) | 用于续费包年包月实例。
| 续费实例询价 | [InquiryPriceRenewInstances](/document/api/213/9491) | 用于续费包年包月实例询价。
| 调整实例配置 | [ResetInstancesType](/document/api/213/9394) | 用于调整实例的机型。
| 调整实例配置询价 | [InquiryPriceResetInstancesType](/document/api/213/9489) |用于调整实例的机型询价。
| 修改实例续费标识 | [ModifyInstancesRenewFlag](/document/api/213/9382) | 用于修改包年包月实例续费标识。
| 修改实例的属性 | [ModifyInstancesAttribute](/document/api/213/9381) | 用于修改实例的属性。
| 调整实例带宽上限 | [ResetInstancesInternetMaxBandwidth](/document/api/213/9393) | 用于调整实例公网带宽上限。
| 修改实例所属项目 | [ModifyInstancesProject](/document/api/213/9380) | 用于修改实例所属项目。
| 修改实例vpc属性 | [UpdateInstanceVpcConfig](/document/api/213/9379) | 用于修改实例vpc属性，如私有网络ip。
| 重置实例密码 | [ResetInstancesPassword](/document/api/213/9397) | 用于将实例操作系统的密码重置为用户指定的密码。
| 查询实例带宽配置 | [DescribeInstanceInternetBandwidthConfigs](/document/api/213/9390) | 用于查询实例带宽配置。



## 2. 镜像相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查看镜像列表 | [DescribeImages](/document/api/213/9418) | 用于获取本账户能够使用的镜像，用户可以使用这些镜像来创建CVM实例。
| 创建自定义镜像 | [CreateImage](/document/api/213/9415) | 用于将实例系统盘的当前状态制作成全新的镜像，使用此镜像可以快速创建实例。
| 删除镜像 | [DeleteImages](/document/api/213/9416) | 用于删除一个或者多个镜像。
| 修改镜像属性 | [ModifyImageAttribute](/document/api/213/9414) | 用于修改镜像的名称和描述等信息。
| 同步镜像 | [SyncImages](/document/api/213/9417) | 用于将自定义镜像复制（同步）到其它地区。
| 修改镜像分享信息 | [ModifyImageSharePermission](/document/api/213/9413) | 用于设置镜像权限。
| 查询镜像分享信息 | [DescribeImageSharePermission](/document/api/213/9419) | 用于查询本账户的镜像共享情况，包括共享的账户列表。

## 3. 网络相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 绑定主机与弹性网卡 | [AttachNetworkInterface](/document/api/213/8836)|  用于绑定主机与弹性网卡。

## 4. 安全组相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询安全组关联的网卡列表 | [DescribeNetworkInterfacesOfSecurityGroup](https://cloud.tencent.com/document/api/213/5437) | 用于查询已关联指定的安全组的弹性网卡。
| 修改弹性网卡关联的安全组 | [ModifySecurityGroupsOfNetworkInterface](https://cloud.tencent.com/document/api/213/5438) | 用于修改指定弹性网卡关联的安全组。
| 删除安全组 | [DeleteSecurityGroup](http://cloud.tencent.com/doc/api/229/%E5%88%A0%E9%99%A4%E5%AE%89%E5%85%A8%E7%BB%84) | 用于删除新的安全组。
| 修改安全组名称 | [ModifySecurityGroupAttributes](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E5%90%8D%E7%A7%B0) | 用于修改已经存在的安全组的属性信息，包括名称和描述。
| 查询安全组规则 | [DescribeSecurityGroupPolicys](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | 用于查询已经存在的安全组的规则。
| 修改安全组规则 | [ModifySecurityGroupPolicys](http://cloud.tencent.com/doc/api/229/%E4%BF%AE%E6%94%B9%E5%AE%89%E5%85%A8%E7%BB%84%E8%A7%84%E5%88%99) | 用于修改已经存在的安全组的规则。
| 查询安全组关联的云主机列表 | [DescribeInstancesOfSecurityGroup](https://cloud.tencent.com/document/api/213/1366) | 用于查询已关联指定的安全组的云服务器。
| 修改云主机关联的安全组 | [ModifySecurityGroupsOfInstance](https://cloud.tencent.com/document/api/213/1367) | 用于修改指定云服务器关联的安全组。
| 查询与安全组关联的安全组列表 | [DescribeAssociateSecurityGroups](https://cloud.tencent.com/document/api/213/1383) | 查询有哪些安全组的出站或入站规则中包含了输入的安全组 ID。
| 添加安全组规则 | [CreateSecurityGroupPolicy](https://cloud.tencent.com/document/api/213/10144) | 用于添加安全组规则。
| 编辑单条安全组规则 | [ModifySingleSecurityGroupPolicy](https://cloud.tencent.com/document/api/213/10145) | 用于编辑单条安全组规则。
| 查询安全组列表 | [DescribeSecurityGroupEx](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AE%89%E5%85%A8%E7%BB%84%E5%88%97%E8%A1%A8) | 用于查询已经存在的安全组的规则。
| 创建安全组 | [CreateSecurityGroup](http://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E5%AE%89%E5%85%A8%E7%BB%84) | 用于创建新的安全组。
| 删除安全组规则 | [DeleteSecurityGroupPolicy](https://cloud.tencent.com/document/api/213/10225) | 用于删除安全组规则。

## 5. 弹性IP相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询弹性公网IP列表 | [DescribeEip](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%88%97%E8%A1%A8) | 查询弹性公网IP。
| 查询弹性公网IP配额 | [DescribeEipQuota](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D) | 查询指定地域弹性公网IP配额。
| 修改弹性公网IP名称 | [ModifyEipAttributes](/doc/api/229/%E4%BF%AE%E6%94%B9%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%90%8D%E7%A7%B0) | 修改弹性公网IP名称。
| 创建弹性公网IP | [CreateEip](/doc/api/229/%E5%88%9B%E5%BB%BA%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | 创建弹性公网IP（EIP），弹性公网IP是专为动态云计算设计的静态IP地址。借助弹性公网IP，您可以快速将EIP重新映射到您的另一个实例上，从而屏蔽实例故障。
| 释放弹性公网IP | [DeleteEip](/doc/api/229/%E9%87%8A%E6%94%BE%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | 释放弹性公网IP。
| 绑定弹性公网IP | [EipBindInstance](/doc/api/229/%E7%BB%91%E5%AE%9A%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | 弹性公网IP与服务器绑定。
| 解绑弹性公网IP | [EipUnBindInstance](/doc/api/229/%E8%A7%A3%E7%BB%91%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | 弹性公网IP与服务器解绑。
| 普通公网IP转弹性公网IP | [TransformWanIpToEip](/doc/api/229/%E6%99%AE%E9%80%9A%E5%85%AC%E7%BD%91IP%E8%BD%AC%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP) | 普通公网IP转弹性公网IP，将服务器当前绑定的普通公网IP转换成弹性公网IP，转换后随着服务器的释放，该弹性公网IP将会保留。

## 6. 密钥相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询密钥对列表 | [DescribeKeyPairs](/document/api/213/9403) | 用于查询密钥对信息。
| 创建密钥对 | [CreateKeyPair](/document/api/213/9400) | 用于创建一个OpenSSH RSA密钥对，可以用于登录Linux实例。
| 修改密钥对属性 | [ModifyKeyPairAttribute](/document/api/213/9399) | 用于修改密钥对属性。
| 删除密钥对 | [DeleteKeyPairs](/document/api/213/9401) | 用于删除已在腾讯云托管的密钥对。
| 导入密钥对 | [ImportKeyPair](/document/api/213/9402) | 用于导入密钥对。
| 绑定密钥对 | [AssociasteInstancesKeyPairs](/document/api/213/9404) | 用于将密钥绑定到实例上。
| 解绑密钥对 | [DisassociasteInstancesKeyPairs](/document/api/213/9405) | 用于解除实例的密钥绑定关系。


