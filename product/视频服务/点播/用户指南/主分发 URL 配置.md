## 操作场景
成功添加并解析域名后，您便可以通过新域名访问您的视频资源，但使用 API 接口和控制台获取到的视频 URL 中 Host 仍然保持为原始域名。您需要登录 [点播控制台](https://console.cloud.tencent.com/video/cdnlog) 进行主分发 URL 设置，才能更新 URL 中的 Host 信息。
## 操作步骤
1. 登录 [点播控制台](https://console.cloud.tencent.com/video/cdnlog)，在左侧菜单栏中选择【分发播放设置】>【主分发 URL 设置】。
2. 单击配置信息右侧的【编辑】，根据实际情况设置以下参数：
 - 主分发协议类型：支持 HTTP 和 HTTPS。
 - 主分发域名：默认使用系统分配的`xxx.vod2.myqcloud.com`，也可以选择自定义 [添加]() 并完成 [解析]() 的域名作为主分发域名。

 ![](https://main.qcloudimg.com/raw/79f80fab63425e219f44a1f663c43870.png)
