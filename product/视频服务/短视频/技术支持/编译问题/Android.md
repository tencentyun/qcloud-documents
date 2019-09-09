

### 集成遇到异常怎么办？

![企业微信截图_18d122ab-812e-4d09-a7f3-f9f5b8220806](https://main.qcloudimg.com/raw/b631f468aca6a2d1e83b868874631030.png)

如果您使用的是 商用企业版，那么您只能使用 armeabi 架构，关闭其他架构，例如armeabi-v7a；如果您使用的是 其他版本，那么您可以使用 armeabi 和 armeabi-v7a 架构。

![企业微信截图_18d122ab-812e-4d09-a7f3-f9f5b8220806](https://main.qcloudimg.com/raw/9d75515640b65d91ab8730991e4c2602.png)

如上图所示，请在app的build.gradle中指定abiFilters为”armeabi“

### SDK 升级后，短视频的功能不能使用？

1、如果使用的是androidstudio，在替换新的aar后，请修改app的build.gradle中的aar引用，是否与您放入工程下/libs目录下的aar**文件名称是否一致**。然后重新clean并且build一下您的工程。

2、确认sdk版本，短视频sdk4.5版本之后需要licence支持

请先申请licence，SDK 有两种版本和两种授权 LICENSE，

- SDK 版本分为基础版和商业版，区别在于AI特效的有无；
- LICENSE 分为基础版和商用版，基础版需要申请基础功能的license；商业版除了要申请基础功能的license外，还需要申请AI动效的license；两种都可申请试用版的license。
- 详细价格请参考[文档](https://cloud.tencent.com/document/product/584/9368)
