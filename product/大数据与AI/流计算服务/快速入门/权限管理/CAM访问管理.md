流计算 Oceanus 采用腾讯云统一的访问管理 CAM 服务来帮助客户管理企业内不同用户对资源的访问权限，详情请参见 [访问管理](https://cloud.tencent.com/product/cam)。若不需要对子账户进行相关资源的访问管理，可跳过此章节，不影响您对文档中其余部分的理解和使用。

## CAM 简介

访问管理（Cloud Access Management，CAM）是腾讯云提供的一套 Web 服务，它主要用于帮助客户安全管理腾讯云账户下的资源的访问权限。通过 CAM，您可以创建、管理和销毁用户（组），并通过身份管理和策略管理来控制不同用户可使用的腾讯云资源。CAM 策略的详细信息及使用请参见 [CAM 策略](https://cloud.tencent.com/document/product/598/10601) 。

## 对子账号访问授权

流计算 Oceanus 目前只提供了一种通用策略如下，未来会提供更多细粒度策略：
全读写策略 QcloudOceanusFullAccess，让用户拥有访问流计算 Oceanus 所有资源的权限。

主帐号默认拥有访问流计算 Oceanus 所有资源的权限，若以子账号访问且子账号未获得主帐号对访问资源的授权时，将会看到如下提示。
![](https://main.qcloudimg.com/raw/242bc9269e092634198e7cecb8cc2764.png)

请参考 [子用户权限设置](https://cloud.tencent.com/document/product/598/36256) 中的【为子用户授权关联策略】，通过主帐号对子帐号授予策略 QcloudOceanusFullAccess，来帮助子帐号拥有访问流计算 Oceanus 的权限。

