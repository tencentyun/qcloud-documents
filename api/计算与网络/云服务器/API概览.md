>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 地域相关接口

| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询地域列表 | [DescribeRegions](https://cloud.tencent.com/document/product/213/9456) | 用于查询地域信息。
| 查询可用区列表 | [DescribeZones](https://cloud.tencent.com/document/product/213/9455) | 用于查询可用区信息。

## 2. 实例相关接口

| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查看实例列表 | [DescribeInstances](/document/api/213/9388) |  用于获取一个或多个实例的详细信息。
| 查看实例状态列表 | [DescribeInstancesStatus](/document/api/213/9389) |  用于查询一个或多个实例的状态。
| 查询实例机型列表 | [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/product/213/9391) | 用于查询实例机型配置。
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
| 调整实例带宽上限询价 | [InquiryPriceResetInstancesInternetMaxBandwidth](https://cloud.tencent.com/document/product/213/9488) | 用于调整实例公网带宽上限询价。
| 调整实例配置询价 | [InquiryPriceResetInstancesType](/document/api/213/9489) |用于调整实例的机型询价。
| 修改实例续费标识 | [ModifyInstancesRenewFlag](/document/api/213/9382) | 用于修改包年包月实例续费标识。
| 修改实例的属性 | [ModifyInstancesAttribute](/document/api/213/9381) | 用于修改实例的属性。
| 调整实例带宽上限 | [ResetInstancesInternetMaxBandwidth](/document/api/213/9393) | 用于调整实例公网带宽上限。
| 修改实例所属项目 | [ModifyInstancesProject](/document/api/213/9380) | 用于修改实例所属项目。
| 修改实例vpc属性 | [UpdateInstanceVpcConfig](/document/api/213/9379) | 用于修改实例VPC属性，如私有网络IP。
| 重置实例密码 | [ResetInstancesPassword](/document/api/213/9397) | 用于将实例操作系统的密码重置为用户指定的密码。
| 查询实例带宽配置 | [DescribeInstanceInternetBandwidthConfigs](/document/api/213/9390) | 用于查询实例带宽配置。

## 3. 镜像相关接口

| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查看镜像列表 | [DescribeImages](/document/api/213/9418) | 用于获取本账户能够使用的镜像，用户可以使用这些镜像来创建CVM实例。
| 创建自定义镜像 | [CreateImage](/document/api/213/9415) | 用于将实例系统盘的当前状态制作成全新的镜像，使用此镜像可以快速创建实例。
| 删除镜像 | [DeleteImages](/document/api/213/9416) | 用于删除一个或者多个镜像。
| 修改镜像属性 | [ModifyImageAttribute](/document/api/213/9414) | 用于修改镜像的名称和描述等信息。
| 同步镜像 | [SyncImages](/document/api/213/9417) | 用于将自定义镜像复制（同步）到其它地区。
| 修改镜像分享信息 | [ModifyImageSharePermission](/document/api/213/9413) | 用于设置镜像权限。
| 查询镜像分享信息 | [DescribeImageSharePermission](/document/api/213/9419) | 用于查询本账户的镜像共享情况，包括共享的账户列表。

## 4. 弹性公网IP相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 查询弹性公网IP列表 | [DescribeAddresses](https://cloud.tencent.com/document/product/213/11663)|  用于查询一个或多个弹性公网IP（简称 EIP）的详细信息.
| 查询弹性公网IP配额 | [DescribeAddressQuota](https://cloud.tencent.com/document/product/213/11664) | 用于查询账户的弹性公网IP（简称 EIP）在当前地域的配额信息。
| 修改弹性公网IP属性 | [ModifyAddressAttribute](https://cloud.tencent.com/document/product/213/11660) | 用于修改弹性公网IP（简称 EIP）的名称。
| 创建弹性公网IP | [AllocateAddresses](https://cloud.tencent.com/document/product/213/11661) | 用于申请一个或多个弹性公网IP（简称 EIP）。
| 释放弹性公网IP | [ReleaseAddresses](https://cloud.tencent.com/document/product/213/11667) | 用于释放一个或多个弹性公网IP（简称 EIP）。
| 绑定弹性公网IP | [AssociateAddress](https://cloud.tencent.com/document/product/213/11665) | 用于将弹性公网IP（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。
| 解绑定弹性公网IP | [DisassociateAddress](https://cloud.tencent.com/document/product/213/11666) | 用于解绑弹性公网IP（简称 EIP）。
| 普通IP转弹性IP | [TransformAddress](https://cloud.tencent.com/document/product/213/11662) | 用于将实例的普通公网 IP 转换为弹性公网IP（简称 EIP）。

## 5. 密钥相关接口

| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 查询密钥对列表 | [DescribeKeyPairs](/document/api/213/9403) | 用于查询密钥对信息。|
| 创建密钥对 | [CreateKeyPair](/document/api/213/9400) | 用于创建一个OpenSSH RSA密钥对，可以用于登录Linux实例。|
| 修改密钥对属性 | [ModifyKeyPairAttribute](/document/api/213/9399) | 用于修改密钥对属性。|
| 删除密钥对 | [DeleteKeyPairs](/document/api/213/9401) | 用于删除已在腾讯云托管的密钥对。|
| 导入密钥对 | [ImportKeyPair](/document/api/213/9402) | 用于导入密钥对。|
| 绑定密钥对 | [AssociasteInstancesKeyPairs](/document/api/213/9404) | 用于将密钥绑定到实例上。|
| 解绑密钥对 | [DisassociasteInstancesKeyPairs](/document/api/213/9405) | 用于解除实例的密钥绑定关系。|


