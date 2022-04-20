## 功能简介
通过调整资源在节点中缓存的时间长短，优化节点缓存，提升请求资源的加载速度，及时淘汰旧资源。
>?目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。


## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**站点加速** > **缓存配置**。
2. 在缓存配置页面，选择所需站点，单击节点缓存 TTL 模块的**设置**。
![](https://qcloudimg.tencent-cloud.cn/raw/842fd8adbd55d3a42d1dd3fc99dea2d2.png)
3. 在节点缓存 TTL 弹窗中，选择所需行为模式，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/ec756b72c67ef9ae47a086a29e91f78f.png)
  **参数说明：**
    - 遵循源站（默认配置）：遵循源站的 Cache-Control 头部或 Last-Modified 头部。
    - 不缓存：不在节点缓存资源。
    - 自定义时间：自定义资源缓存时长。

附：整体缓存策略内容如下：
![](https://qcloudimg.tencent-cloud.cn/raw/2f43a331c94351f9f28b93a78a623625.png)
