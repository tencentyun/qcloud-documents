流计算 Oceanus 采用腾讯云统一的访问管理 CAM 服务来帮助客户管理企业内不同用户对资源的访问权限，详情请参见 [访问管理](https://cloud.tencent.com/product/cam)。若不需要对子账户进行相关资源的访问管理，可跳过此章节，不影响您对文档中其余部分的理解和使用。

## CAM 简介
访问管理（Cloud Access Management，CAM）是腾讯云提供的一套 Web 服务，它主要用于帮助客户安全管理腾讯云账户下的资源的访问权限。通过 CAM，您可以创建、管理和销毁用户（组），并通过身份管理和策略管理来控制不同用户可使用的腾讯云资源。CAM 策略的详细信息及使用请参见 [CAM 策略](https://cloud.tencent.com/document/product/598/10601)。

## 对子账号访问授权
流计算 Oceanus 目前提供了两种通用策略，全读写策略 QcloudOceanusFullAccess 和只读权限 QcloudOceanusReadOnlyAccess（舍弃，不建议用），授权后用户会拥有访问流计算 Oceanus 所有资源的权限。
主帐号默认拥有访问流计算 Oceanus 所有资源的权限，若子账号未获得主帐号对访问资源的授权时，将会看到如下提示。
![](https://qcloudimg.tencent-cloud.cn/raw/c253d6dbbf3f372dc2c5434135e5e38a.png)
可参考 [授权管理](https://cloud.tencent.com/document/product/598/10602)，将预设策略 QcloudOceanusFullAccess 授权给用户。通过主帐号对子帐号授予策略 QcloudOceanusFullAccess，来帮助子帐号拥有访问流计算 Oceanus 的权限。
![](https://qcloudimg.tencent-cloud.cn/raw/9ef6af08079f8d209b64113f2dde5eaf.png)

>? 
>- QcloudOceanusFullAccess 的策略。该策略是通过让用户对流计算 Oceanus 中所有资源都具有操作的权限来达到目的。
>- QcloudOceanusReadOnlyAccess 的策略。该策略是通过让用户分别对流计算 Oceanus 中以单词 “Describe” 和 “Check” 开头的所有操作具有操作的权限来达到目的。(该策略已不推荐使用，建议 Oceanus 预设空间角色来进行细粒度控制)


