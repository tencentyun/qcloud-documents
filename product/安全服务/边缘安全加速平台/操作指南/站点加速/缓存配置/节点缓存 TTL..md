## 功能简介
通过调整资源在节点中缓存的时间长短，优化节点缓存，提升请求资源的加载速度，及时淘汰旧资源。

>?EdgeOne 会根据节点缓存 TTL 中配置的缓存过期时间，判断节点缓存的资源是否过期。<br>
若客户端访问的资源在节点的缓存未过期，节点直接将缓存返回给客户端；<br>
若客户端访问的资源在节点未缓存该资源或缓存已过期，则节点会回源站获取最新资源并缓存到节点，同时返回给客户端。<br>
若源站资源更新后，需要立刻更新节点的缓存，可使用 [清除缓存](https://cloud.tencent.com/document/product/1552/70759) 功能主动清除节点未过期的旧缓存，保证后续请求可以获取到源站最新的资源。



## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**站点加速** > **缓存配置**。
2. 在缓存配置页面，选择所需站点，单击节点缓存 TTL 模块的**设置**。
![](https://qcloudimg.tencent-cloud.cn/raw/4b22413eadf893f0d9027ef03024eea8.png)
3. 在节点缓存 TTL 弹窗中，选择所需行为模式，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/2ea82c188322279546ac16acafb9bace.png)
  **参数说明：**
    - 遵循源站（默认配置）：遵循源站的 Cache-Control 头部，若源站无 CC 头则不缓存，也可设置一个默认的缓存时间覆盖。
    - 不缓存：不在节点缓存资源。
    - 自定义时间：自定义资源缓存时长。

附：整体缓存策略内容如下：
![](https://qcloudimg.tencent-cloud.cn/raw/89f2fc4aa8e41ceb6057cc55dffb277c.png)
>?强制缓存：自定义时间式，站点默认启用了“强制缓存”，节点缓存 TTL 按照此处配置的时间，即使源站的 `Cache-Control` 为 `no-cache/no-store/private`。若您需要关闭“强制缓存”，即当源站的 `Cache-Control` 为 `no-cache/no-store/private` 时，即使此处配置了自定义节点缓存 TTL，节点仍不缓存资源，遵循源站的不缓存头，可前往 [规则引擎](https://cloud.tencent.com/document/product/1552/70901) 自定义配置节点缓存 TTL 规则。
