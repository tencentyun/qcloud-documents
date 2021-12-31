流计算 Oceanus 采用腾讯云统一的访问管理 CAM 服务来帮助客户管理企业内不同用户对资源的访问权限，详情请参见 [访问管理](https://cloud.tencent.com/product/cam)。若不需要对子账户进行相关资源的访问管理，可跳过此章节，不影响您对文档中其余部分的理解和使用。

## CAM 简介
访问管理（Cloud Access Management，CAM）是腾讯云提供的一套 Web 服务，它主要用于帮助客户安全管理腾讯云账户下的资源的访问权限。通过 CAM，您可以创建、管理和销毁用户（组），并通过身份管理和策略管理来控制不同用户可使用的腾讯云资源。CAM 策略的详细信息及使用请参见 [CAM 策略](https://cloud.tencent.com/document/product/598/10601)。

## 对子账号访问授权
流计算 Oceanus 目前提供了两种通用策略，全读写策略 QcloudOceanusFullAccess 和只读权限 QcloudOceanusReadOnlyAccess，授权后用户会拥有访问流计算 Oceanus 所有资源的权限。

主帐号默认拥有访问流计算 Oceanus 所有资源的权限，若以子账号访问且子账号未获得主帐号对访问资源的授权时，将会看到如下提示。
![](https://main.qcloudimg.com/raw/f4fe396c89b6414dd3bf9b74f64a655f.png)
可参考 [子用户权限设置](https://cloud.tencent.com/document/product/598/36256) 中的【为子用户授权关联策略】，通过主帐号对子帐号授予策略 QcloudOceanusFullAccess，来帮助子帐号拥有访问流计算 Oceanus 的权限。

## 策略授权图文示例
通过主账号对子账号授予 QcloudOceanusFullAccess 和 QcloudTAGReadOnlyAccess 策略，来帮助子账号拥有访问流计算 Oceanus 的权限。
1. 按策略语法新建一个空白策略模板 [选择策略模板](https://console.cloud.tencent.com/cam/policy/createV2)。
![](https://main.qcloudimg.com/raw/02ac325371c528d9bb863fcbfb6b2908.png)
2. 将策略内容变更为下述语法。
```
{
    "version": "2.0",
    "statement": [        
        {
            "action": [
                "oceanus:*",
                "tag:Describe*",
                "tag:Get*"
            ],
            "resource": "*",
            "effect": "allow"
        }]
}
```
![](https://main.qcloudimg.com/raw/e6285e14fa906ea79af301443a4dee28.png)
修改后并设置策略名称（建议设置成 Oceanus-xxx 的模板，方便以后寻找策略），单击**完成**即可完成按策略语法的策略创建。
![](https://main.qcloudimg.com/raw/9695151507a6f132046fc9e457059375.png)
3. 在 [策略](https://console.cloud.tencent.com/cam/policy/custom) 中搜索刚设置的策略名称，找到策略。在**关联用户/组**中将需要用到 Oceanus 权限的用户添加上，即可完成策略授权。
![](https://main.qcloudimg.com/raw/87b77540da330b6ca27bbdd7c16e976d.png)
