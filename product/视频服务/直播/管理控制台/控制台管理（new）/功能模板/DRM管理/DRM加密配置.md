云直播提供基于 Widevine、Fairplay、NormalAES 的 DRM 加密协议的视频直播加密、防录制、防盗链等服务，全方位保障用户视频 [内容安全](https://cloud.tencent.com/solution/content-security?from=10680)。本文主要介绍了通过控制台使用 DRM 加密功能的操作步骤。

## 注意事项
腾讯云只提供对视频流的加密操作，DRM 加密的证书管理由第三方服务商华曦达（SDMC）和DRMtoday提供，使用 DRM 加密的证书管理服务会产生费用，费用由华曦达（SDMC）或DRMtoday收取，具体对接及操作可直接与华曦达（SDMC）或DRMtoday联系。

## 前提条件
- 已开通腾讯云直播服务，并添加 [播放域名](https://cloud.tencent.com/document/product/267/20381)。
- 已在 [华曦达 SDMC DRM 服务](https://console.multidrm.tv/setting/drm/index) 或 [DRMtoday](https://castlabs.com/free-trials/drmtoday/) 创建服务账号并设置访问密钥。

## 控制台配置
[](id:step1)

### 设置访问 DRM 密钥信息
1. 登录云直播控制台，进入 **功能配置** > [DRM 管理](https://console.cloud.tencent.com/live/config/drm)。
2. 单击 **编辑** ，填写秘钥信息，选择证书管理提供商，可选择华曦达或DRMtoday，具体配置如下：
 - 证书管理提供商为**华曦达（SDMC）**时：
   - 设置用户访问华曦达（SDMC）DRM 密钥信息，需要设置 UID、SecretID、SecretKey，这些密钥信息需要从证书的第三方服务商处获取。
![](https://qcloudimg.tencent-cloud.cn/raw/8d8aa3647b0efa53dac0518cc9b9d115.png)
 -  证书管理提供商为**DRMtoday**时：
   - 设置用户访问DRMtoday密钥信息，需要设置MerchantName、MerchantUUID、MerchantApiName、MerchantApiPassword、KeySeedID和IvSeedID，这些密钥信息需要从证书的第三方服务商处获取。
![](https://qcloudimg.tencent-cloud.cn/raw/116cbaef261fc1fdd9f830d7ce913735.png)


[](id:step2)
### 设置转码模板并绑定域名
1. 进入 **功能配置** > [直播转码](https://console.cloud.tencent.com/live/config/transcode)。
2. 单击 **创建转码模板** 设置 DRM 加密信息。
![](https://qcloudimg.tencent-cloud.cn/raw/60fc9dbe2afbf5ad0d5461e6a5ed2c59.png)
<table>
<thead><tr><th width=18%>DRM 加密配置项</th><th>是否必填</th><th>说明</th></tr></thead>
<tbody><tr>
<td>DRM 加密</td>
<td>否</td>
<td>DRM 加密开关，默认关闭。开启该功能前要求在 DRM 管理中配置 DRM 密钥</td>
</tr><tr>
<td>加密类型</td>
<td>是</td>
<td>支持 Widevine、Fairplay、NomalAES，使用 Fairplay 需要在播放器端上传从 Apple 申请的证书，具体请参见 <a href="https://cloud.tencent.com/document/product/267/75558">申请 Fairplay 证书</a></td>
</tr>
<td>DRM标签</td>
<td>是</td>
<td>支持选择SD、HD、UHD1和UHD2。</a></td>
</tr>
</tbody></table>
3. 单击 **绑定域名** 将对应转码模板与播放域名绑定。
![](https://qcloudimg.tencent-cloud.cn/raw/701d19bcc158cece55dabffcb33ddee9.png)

[](id:step3)
### 获取 DRM 播放地址
使用 DRM 加密要求播放地址必须是 HLS 播放协议，您可前往 [地址生成器](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator) 选择对应的转码模板，生成播放地址，选择 HLS 播放协议的地址作为 DRM 播放地址。

![](https://qcloudimg.tencent-cloud.cn/raw/c96727b0b70d3ba05fa489e1f66c5083.png) 

[](id:step4)
### 配置播放器
使用直播 DRM 加密功能对播放器有一定要求：
- 播放器需要与 [华曦达（SDMC）](https://www.xmediacloud.com/contact-us/) 做对接，实现通过视频信息获取 License 并解密的能力。
- iOS 平台支持 Fairplay ，Android 平台支持 WideVine 及 NomalAES。
- iOS 平台需要申请证书并上传至 [华曦达（SDMC）平台](https://console.multidrm.tv/licenses/drm/index) 。

>? 在华曦达（SDMC）平台操作，需要先进行注册并获取账号，注册方式可以参考 [获取用户密钥](https://cloud.tencent.com/document/product/267/75689)的操作指引。在您对接 DRM 或者第三方服务商的过程中的任何问题，都可以提工单 [联系我们](https://console.cloud.tencent.com/workorder/category)，我们全程负责帮您解决。
