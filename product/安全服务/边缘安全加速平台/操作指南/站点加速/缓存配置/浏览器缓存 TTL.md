## 功能简介
通过调整资源在浏览器缓存的时间长短，优化浏览器缓存，提升请求资源的加载速度。


## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**站点加速** > **缓存配置**。
2. 在缓存配置页面，选择所需站点，单击浏览器缓存 TTL 模块的**设置**。
![](https://qcloudimg.tencent-cloud.cn/raw/f9c7bd71c7d644ca4b032ad72a827166.png)
3. 在浏览器缓存 TTL 弹窗中，选择所需模式，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/d2528c20648a18c7a91341c980f3e845.png)
参数说明：
 - 遵循源站（默认配置）：遵循源站的 Cache-Control 头部或 Last-Modified 头部。
  - 不缓存：不在浏览器缓存资源。
 - 自定义时间：自定义资源缓存时长。
   

附：整体缓存策略内容如下：
![](https://qcloudimg.tencent-cloud.cn/raw/0082dc53a7827647e011f5e8ff037407.png)


