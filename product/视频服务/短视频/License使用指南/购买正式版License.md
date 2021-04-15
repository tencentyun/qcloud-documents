短视频 SDK License 用于激活短视频 SDK 的使用权限，用户可以在控制台上对短视频 SDK 进行新增、升级和续期。

## 注意事项
- **正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于续期 License，请单击【新增 License】重新新增 License 绑定新的包名信息。
- 短视频 SDK License 需要通过 [云点播控制台](https://console.cloud.tencent.com/vod/license) 与 [流量资源包](https://cloud.tencent.com/document/product/266/14667#flow_page) 进行绑定。绑定成功后该资源包视为已使用，不支持5天内无理由退款。


[](id:buy)
## 购买正式版 License
当您的测试 License 到期后，您需要进入 [云点播控制台](https://console.cloud.tencent.com/vod/license) 创建正式 License。当您购买流量资源包10T、流量资源包50T、流量资源包200T中的任意一种，云点播都会赠送一个 License，License 需在控制台和流量资源包绑定后才可以创建成功，且该 License 的有效期和资源包的有效期一致，支持对 License 进行升级、续期、变更。

SDK 版本 License 与您需要购买的点播套餐包对应关系如下：

| SDK 版本                                                     | 套餐包                                                       |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [精简版 SDK（UGC_Smart）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播流量资源包 10TB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv)                                          |
| [基础版 SDK（UGC）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播流量资源包 50TB 或 200TB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv) |
| [企业版 SDK（UGC_Enterprise）](https://cloud.tencent.com/document/product/584/9366#sdk) | 请参见 [申请企业版本 License](#enterpriseli) |
| [企业版 Pro SDK（EnterprisePro）](https://cloud.tencent.com/document/product/584/9366#sdk) | 请参见 [申请企业版本 License](#enterpriseli) |

[](id:add)
## 新增短视频 License
1. 进入云点播控制台，选择 【License 管理】 >【[短视频 SDK License](https://console.cloud.tencent.com/vod/license/video)】。
2. 单击【新增 License】，请选择当前账户可用的资源包来绑定，单击【确定并继续完成 License 设置】。
![](https://main.qcloudimg.com/raw/3daa77e7721ca7a9c482cdfcd15d408d.png)
> ? 
> - 若无已购买资源包，请单击【购买页】前往选购流量资源包10TB、流量资源包50TB、流量资源包200TB中的任意一种。
> - 各规格资源包均有对应的 SDK License 版本，具体请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。
3. 进入 License 设置页，填写正式版 License 的信息，【Package Name】为 Android 的包名，【Bundle Id】为 iOS 的 Bundle ID，单击【确认】即可。
![](https://main.qcloudimg.com/raw/475ab5e49ebf804e4f8d449fd02520e3.png)
> !  购买点播套餐包并绑定 License 后，请确认 [Bundle ID 和 Package Name](https://cloud.tencent.com/document/product/584/54335#que2) 无误再单击【确定】提交。一旦提交，**License 信息不能再做修改**。


[](id:renew)
## 续期正式版 License
您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 查看 License 的有效期，正式版本的 License 有效期为一年。若您对指定 License 进行续期，请保证已购买流量资源包的情况下，可进行如下操作：

1. 进入 [短视频 License](https://console.cloud.tencent.com/vod/license) ，选择将要续期的 License，单击右上角的【续期】，进入短视频 License 续期页。
2. 选择当前账户可绑定的资源包，**License 有效时间和对应的绑定资源包有效时间一致**。
   ![](https://main.qcloudimg.com/raw/60a091abeda3993222829f32898262a8.png)
3. 单击【确认续期】即可。

#### 示例

用户于2019年02月02日购买流量资源包50TB（有效期：2019.02.02 - 2020.02.01），赠送基础版 License，则 License 的有效期为2019.02.02 - 2020.02.01，若用户需要进行续期，续期流量资源包-200TB（2019.07.02 - 2020.07.01），则License 的有效期为2019.07.02 - 2020.07.01。

[](id:update)
## 升级正式版 License
目前仅支持短视频 License 由精简版升级至基础版，升级的 License 为对应的资源包赠送的 License 规格。

#### 示例
用户购买流量资源包10TB（赠送精简版 License），如需升级至基础版 License，则控制台需要存在50TB或200TB资源包。

[](id:pro)[](id:enterpriseli)
## 企业版本 License

相比于基础版，企业版增加了基于腾讯优图实验室专利技术的人脸特效功能。使用企业版 License 可以开启优图实验室的 AI 功能。

> ? 
> - 企业版 License 基本配置方法与基础版 License 相同，具体请参见 配置查看 License。配置完成后需额外配置 [动效变脸](https://cloud.tencent.com/document/product/584/13509) 功能。
> - 若您需开通企业版 License，请 [单击此处](https://cloud.tencent.com/product/x-magic)。



