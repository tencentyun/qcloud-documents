[](id:que1)
### 集成实时音视频 SDK 前需要做哪些准备工作？

1. 创建腾讯云实时音视频应用，购买相应的套餐，并获取到 SDKAppID 和密钥信息。
2. 小程序服务器域名配置。
3. 开通小程序类目与推拉流标签权限。
   出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
   - 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
   - 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
   - 符合类目要求的小程序，需要在【[微信公众平台](https://mp.weixin.qq.com)】>【开发】>【开发管理】>【接口设置】中自助开通该组件权限，如下图所示：
![](https://main.qcloudimg.com/raw/6d408801ac20792d29cc887e7a872a7f.png)

更多详情请参见 [跑通Demo(小程序)](https://cloud.tencent.com/document/product/647/32399) 和 [快速集成(小程序)](https://cloud.tencent.com/document/product/647/32183)。


[](id:que2)
### 运行出错，该如何排查？

1. 请检查开通的小程序类目是否正确，&lt;live-pusher&gt; 和 &lt;live-player&gt; 标签是否已开启。
2. 请确认已将 [小程序域名白名单](https://cloud.tencent.com/document/product/647/34399#.E5.BE.AE.E4.BF.A1.E5.B0.8F.E7.A8.8B.E5.BA.8F.E9.9C.80.E8.A6.81.E9.85.8D.E7.BD.AE.E5.93.AA.E4.BA.9B.E5.9F.9F.E5.90.8D.E4.B8.BA.E7.99.BD.E5.90.8D.E5.8D.95.EF.BC.9F) 添加到小程序 request 合法域名，或已开启调试模式。
3. 请重新解压小程序端 Demo 直接运行，若运行正常，建议参考 [快速集成(小程序)](https://cloud.tencent.com/document/product/647/32183) 重新集成 SDK。
4. 若问题依然存在，可以登录 [微信小程序开发者社区](https://developers.weixin.qq.com/community/develop/question) 查找相关资料，也可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 或致电 4009100100 联系我们。



