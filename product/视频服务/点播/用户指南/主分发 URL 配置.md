## 操作场景
添加并解析域名后，您可以通过新域名访问您的视频资源，但使用 API 接口和控制台获取到的视频 URL 中，Host 仍保持为原始域名。因此，您需要登录控制台，在主分发 URL 设置中更新 URL 的 Host 信息。
## 操作步骤
1. 登录 [云点播控制台](https://console.cloud.tencent.com/vod/overview)，选择左侧导航栏的【分发播放设置】>【主分发 URL 设置】，进入“主分发 URL 设置”页面。
2. 单击右上角的【编辑】，设置相应参数：
 - 主分发协议类型：支持 HTTP 和 HTTPS。
 - 主分发域名：默认使用系统分配的`xxx.vod2.myqcloud.com`，也可以选择自定义 [添加](https://cloud.tencent.com/document/product/266/33371#.E6.B7.BB.E5.8A.A0.E5.9F.9F.E5.90.8D) 并完成 [解析](https://cloud.tencent.com/document/product/266/33371#.E8.A7.A3.E6.9E.90.E5.9F.9F.E5.90.8D) 的域名作为主分发域名。
 
![](https://main.qcloudimg.com/raw/caa58845fa283c0fe72c6126fa386b8b.png)
