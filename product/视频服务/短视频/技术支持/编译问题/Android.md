
 
### 集成遇到异常怎么办？

![](https://main.qcloudimg.com/raw/b631f468aca6a2d1e83b868874631030.png)
如果您使用的是企业版，那么您只能使用 armeabi 架构，关闭其他架构，例如 armeabi-v7a。如果您使用的是其他版本，那么您可以使用 armeabi 和 armeabi-v7a 架构。
![](https://main.qcloudimg.com/raw/9d75515640b65d91ab8730991e4c2602.png)
如上图所示，请在`app`的 build.gradle 中指定 abiFilters 为“armeabi”。

### 同时集成两款以上 LiteAV 体系的 SDK 出现冲突怎么办？
如果您的项目中同时集成了两款以上的 LiteAV 体系的 SDK，就会出现符号冲突（symbol duplicate）的问题，这是由于 LiteAV 体系的 SDK 都使用了相同的基础模块。

要避免符号冲突问题，正确的做法是不要同时集成两个 SDK，而是集成一个具备完整功能的专业版 SDK：

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
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_ios_professional") href="https://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Professional_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_iOS">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">4.08M（arm64）</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_android_professional") href="https://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Professional_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_Android">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">jar：1.5M<br> so(armeabi)：6.5M<br> so(armv7)：6.1M<br>so(arm64)：7.3M</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
</table>


### SDK 升级后，短视频的功能不能使用？

1. 如果使用的是 androidstudio，在替换新的 aar 后，请修改`app`的 build.gradle 中的 aar 引用，是否与您放入工程下 /libs 目录下的 aar **文件名称是否一致**。然后重新 clean 并且 build 一下您的工程。
2. 确认 SDK 版本，短视频 SDK 4.5 版本之后需要 License 支持。

请先申请 License，SDK 有两种版本和两种授权 License。

- SDK 版本分为基础版和企业版，区别在于 AI 特效的有无。
- License 分为基础版和商用版，基础版需要申请基础功能的 License；企业版除了要申请基础功能的 License 外，还需要申请 AI 动效的 License；两种都可申请试用版的 License。
- 详细价格请参考 [价格文档](https://cloud.tencent.com/document/product/584/9368)。
