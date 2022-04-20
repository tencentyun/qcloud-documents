[](id:que1)
### 集成遇到异常怎么办？
![](https://main.qcloudimg.com/raw/b631f468aca6a2d1e83b868874631030.png)
您可以使用 armeabi 和 armeabi-v7a 架构。
![](https://main.qcloudimg.com/raw/9d75515640b65d91ab8730991e4c2602.png)
如上图所示，请在`app`的 build.gradle 中指定 abiFilters 为“armeabi”。

[](id:que2)
### 同时集成两款以上 LiteAV 体系的 SDK 出现冲突怎么办？
如果您的项目中同时集成了两款以上的 LiteAV 体系的 SDK，就会出现符号冲突（symbol duplicate）的问题，这是由于 LiteAV 体系的 SDK 都使用了相同的基础模块。

要避免符号冲突问题，正确的做法是不要同时集成两个 SDK，而是集成全功能版 SDK：

<table>
   <tr>
      <th width="0px" style="text-align:center">所属平台</td>
      <th width="0px" style="text-align:center">ZIP 包</td>
      <th width="0px"  style="text-align:center">Github</td>
      <th width="0px" style="text-align:center">64位支持</td>
      <th width="0px" style="text-align:center">安装包增量</td>
      <th width="0px" style="text-align:center">安装包瘦身</td>
   </tr>
   <tr>
      <td style="text-align:center">iOS</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_ios_professional") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_iOS">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">4.08M（arm64）</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_android_professional") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_Android">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">jar：1.5M<br> so(armeabi)：6.5M<br> so(armv7)：6.1M<br>so(arm64)：7.3M</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
</table>

[](id:que3)
### SDK 升级后，短视频的功能不能使用？
1. 如果使用的是 androidstudio，在替换新的 aar 后，请修改`app`的 build.gradle 中的 aar 引用，是否与您放入工程下 /libs 目录下的 aar **文件名称是否一致**。然后重新 clean 并且 build 一下您的工程。
2. 确认 SDK 版本，短视频 SDK 4.5 版本之后需要 License 支持。

请先申请 License，SDK 有**精简版**和**基础版**两种版本 License：
- 区别请参考[SDK 功能及对应的 License 版本](https://cloud.tencent.com/document/product/584/9368#sdk-.E5.8A.9F.E8.83.BD.E5.8F.8A.E5.AF.B9.E5.BA.94.E7.9A.84-license-.E7.89.88.E6.9C.AC)。
- 详细价格请参见 [价格文档](https://cloud.tencent.com/document/product/584/9368)
- 如需使用美颜特效等高级功能，请参见 [腾讯特效 SDK](https://cloud.tencent.com/document/product/616/65890)。

[](id:que5)
### Android 端短视频如何设置暂停和进度条？
短视频播放是基于短视频的播放器进行实现的，因此进度条功能需要您**自行研发**，相关功能实现说明可参见 [播放器 SDK—进度展示](https://cloud.tencent.com/document/product/881/20216#14.E3.80.81.E8.BF.9B.E5.BA.A6.E5.B1.95.E7.A4.BA)。

