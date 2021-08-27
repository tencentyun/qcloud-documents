
为方便 iOS 开发者调试和接入腾讯云游戏多媒体引擎产品 API，本文档主要为您介绍 iOS 项目工程导出注意事项。


## 导出配置指引

1. 根据实际情况在 Xcode>Link Binary With Libraries>Build Setting 里，加入以下依赖库，并设置 Framework Search Paths 指向 SDK 所在目录，如下图所示：  
<img src="https://main.qcloudimg.com/raw/79355a317302adccd7f96e898bef7845.png"  style="
    width: 80%;
">
2. 添加依赖库，如下图所示：
   ![](https://main.qcloudimg.com/raw/b6156b8c7a596248c148607070e38f67.png)
3. Bitcode 需要工程依赖的所有类库同时支持，SDK 暂时还不支持 Bitcode，可以先临时关闭。   关闭此设置，只需在 Targets - Build Settings 中搜索 Bitcode 即可，找到相应选项，设置为 NO。
<img src="https://main.qcloudimg.com/raw/7020b4fadc30d29d5760873a53e64124.png"  style="
    width: 80%;
">
4. 游戏多媒体引擎 iOS 平台所需要的隐私权限如下：
 - Required background modes：允许后台运行（可选）。
 - Microphone Usage Description：允许麦克风权限。


