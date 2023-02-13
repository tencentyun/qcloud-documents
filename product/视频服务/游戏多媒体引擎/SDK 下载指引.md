为方便开发者接入腾讯云游戏多媒体引擎产品，本文主要为您介绍适用于游戏多媒体引擎 SDK 的下载指引。

## 新手入门

如果是第一次使用 SDK，下载之前可参见 [新手指引](https://cloud.tencent.com/document/product/607/51583) 注册服务。


## 版本更新

v2.9.6 正式版本更新如下：

<table >
<thead>
<tr>
<th width="18%">动态名称</th>
<th width="44%">动态描述</th>
 <th width="14%">发布时间</th>  
<th width="24%">相关文档</th>
</tr>
</thead>
<tbody><tr>
<td>发布 SDK v2.9.6 正式版本</td>
<td ><ul style="margin:0;">
<li >在线 MP3 文件作为伴奏时支持设置伴奏进度</li>
<li >Mac 平台 SDK 新增对 M1 Arm64 架构支持</li>
<li >WebGL适配Unity 2021版本</li>
<li >优化3D语音功能，将3D音频模型内置，无需传入模型路径</li>
<li >修复 Android 5.1 版本的兼容问题</li>
<li >修复循环播放语音消息产生的内存问题</li>
</ul ></td>
<td>2023-01-06</td> 
<td><a href="https://cloud.tencent.com/document/product/607/18218">3D语音</a></td>
</tr>
<tr>
<td>发布 Electorn SDK v2.0.2 正式版本</td>
<td >增加对 Electorn 框架的适配优化</td>
<td>2023-01-12</td> 
<td><a href="https://cloud.tencent.com/document/product/607/85613">集成 SDK</a></td>
</tr>
<tr>
<td>发布 Flutter SDK v2.9.6 正式版本</td>
<td >增加对 Flutter 框架的适配优化</td>
<td>2023-02-08</td> 
<td>-</a></td>
</tr>
</tbody></table>

<dx-alert infotype="notice" title="更新注意">
-  如果从旧版本升级到 2.9.6 版本，请参见 [更新指引](https://cloud.tencent.com/document/product/607/32535) 进行解决。
-  目前 GME SDK 拆分多个动态库，请参见 [更新指引](https://cloud.tencent.com/document/product/607/32535) 查看各动态库功能。
-  如需查看历史版本的更新信息，请查阅 [产品动态](https://cloud.tencent.com/document/product/607/41876)。
</dx-alert> 

## SDK 下载

| 平台/引擎  |   版本          | 更新时间   | SDK 下载| Sample Project 下载| 接入文档|
| ----------------- | ---------- | ---------- | ---------------------------- | ---------------------------- | -------------------------------- |
| Unity   | v2.9.6    | 2023-01-06 | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Unity_Audio_WithPlugins_SDK_2.9.6.b13c65d1.zip) | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Unity_Audio_WithPlugins_Demo_2.9.6.b13c65d1.zip) | [快速入门](https://cloud.tencent.com/document/product/607/18248) |
| Unreal Engine 4.x | v2.9.6 | 2023-01-06 | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Unreal422_Audio_WithPlugins_SDK_2.9.6.b13c65d1.zip) | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Unreal422_Audio_WithPlugins_Demo_2.9.6.b13c65d1.zip) | [快速入门](https://cloud.tencent.com/document/product/607/18267) |
| Unreal Engine 5.x | v2.9.6 |  2023-01-06 | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Unreal5_Audio_WithPlugins_SDK_2.9.6.b13c65d1.zip) | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Unreal5_Audio_WithPlugins_Demo_2.9.6.b13c65d1.zip) | [快速入门](https://cloud.tencent.com/document/product/607/18267) |
| Cocos2D      |v2.9.6       |  2023-01-06 | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Cocos_Audio_WithPlugins_SDK_2.9.6.b13c65d1.zip) | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Cocos_Audio_WithPlugins_Demo_2.9.6.b13c65d1.zip) | [快速入门](https://cloud.tencent.com/document/product/607/18292) |
| Windows      | v2.9.6       | 2023-01-06 | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Windows/GME_Windows_audio_sdk_2.9.6.58d0bafb.zip) | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Windows/GME_Windows_audio_example_project_2.9.6.58d0bafb.zip) | [快速入门](https://cloud.tencent.com/document/product/607/56374) |
| iOS        | v2.9.6         | 2023-01-06 | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/iOS/GME_ios_audio_sdk_2.9.6.58d0bafb.zip) | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/iOS/GME_ios_audio_example_2.9.6.58d0bafb.zip) | [快速入门](https://cloud.tencent.com/document/product/607/56374) |
| Android    | v2.9.6        | 2023-01-06 | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Android/GME_android_audio_sdk_2.9.6.58d0bafb.zip) | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Android/GME_android_audio_example_2.9.6.58d0bafb.zip) | [快速入门](https://cloud.tencent.com/document/product/607/56374) |
| macOS     | v2.9.6          | 2023-01-06 | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Mac/GME_mac_audio_sdk_2.9.6.58d0bafb.zip) | [下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Mac/GME_mac_audio_demo_2.9.6.58d0bafb.zip) | [快速入门](https://cloud.tencent.com/document/product/607/56374) |
|Electron|v2.0.2|2023-01-12|[下载](https://www.npmjs.com/package/gme-electron-sdk)|[下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Electron_Audio_Demo_2.0.2.9fbe5db7.zip)|[接口文档](https://cloud.tencent.com/document/product/607/85614)|
|Flutter|v2.9.6|2023-02-08|[下载](https://www.npmjs.com/package/gme-electron-sdk)|[下载](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.6/Other/GME_Electron_Audio_Demo_2.0.2.9fbe5db7.zip)|[接口文档](https://cloud.tencent.com/document/product/607/85614)|
| Web      | -          | 2021-06-11 | [下载](https://dldir1.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.8.1/H5/GME_Web_SDK_2.8.1.47.zip) | [下载](https://dldir1.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.8.1/H5/GME_Web_Demo_2.8.1.47.zip) | [接口文档](https://cloud.tencent.com/document/product/607/32157) |


> ?
>
> - GME SDK 也支持**主机平台**（PlayStation、Xbox、Nintendo Switch），如果需要请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系 GME 开发者。
> - GME iOS、Mac SDK v2.9.6 版本目前只支持 Xcode 13以上进行构建（[使用 Xcode 13 来构建](https://developer.apple.com/ios/submit/)），如需在 Xcode13 以下编译器调试，可下载 [2.9.0版本](https://dldir1v6.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.0/iOS/GME_ios_audio_sdk_2.9.0.756c12ea.zip)，但不推荐用于发布。
> - 所有平台 SDK 具体编译工具链可参见 [编译工具链文档](https://cloud.tencent.com/document/product/607/71331)。


## Sample Project 指引

### Sample Project 使用

下载 SDK 及 Sample Project 后，如果使用上有问题，您可参见 [Sample Project 使用问题](https://cloud.tencent.com/document/product/607/51456)，或进行 [在线咨询](https://cloud.tencent.com/online-service?from=connect-us) 联系腾讯云工作人员。

> ?下载的 Sample Project 代码中，需要替换为您申请的 SDKAppid 和 Key 才可编译执行，例如 Unity Demo 需要修改 **UserConfig.cs** 代码文件。申请服务详情请参见 [语音服务开通指引](https://cloud.tencent.com/document/product/607/10782)。

### Sample Project 调试

使用 Sample Project 工程进行调试，如果出现问题，可以参考以下文档：

- 进房失败问题请参见 [实时语音进房失败问题](https://cloud.tencent.com/document/product/607/51462) 进行解决。
- 无声问题请参见 [实时语音无声及音频问题](https://cloud.tencent.com/document/product/607/51463) 进行解决。
- 调用服务出错，可以查看 [错误码](https://cloud.tencent.com/document/product/607/15173) 进行解决。
- 如果无法解决，可以获取到日志后，通过 [联系我们](https://cloud.tencent.com/document/product/607/48708) 联系 GME 开发者。



### Sample Project 导出

导出 Sample Project 为可执行文件的过程中，如遇见问题详情请参见 [工程导出问题](https://cloud.tencent.com/document/product/607/51457) 进行解决。
