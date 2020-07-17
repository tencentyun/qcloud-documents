## 配置场景

若在您的业务场景下，资源 URL 路径中大小写差异与资源内容无关，可通过开启忽略大小写缓存配置，一定程度上提升命中率。

## 配置指南

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可进入域名配置页面，第三栏【缓存配置】中最下方可以看到【忽略大小写缓存】，默认情况下为关闭状态：
![](https://main.qcloudimg.com/raw/95ccb4da3a7589d085658e3965572dee.png)

## 配置示例

CDN 节点在缓存资源时，是按照 Key-Value 形式建立索引，其 Key 即 CDN 节点的缓存键(Cache Key)，除了通过过滤参数配置来进行优化外，也可配置忽略大小写缓存进行优化。
假设加速域名为`cloud.tencent.com`，用户访问场景如下：

- 用户 A 访问资源：`http://cloud.tencent.com/abc.JPG`
- 用户 B 访问资源：`http://cloud.tencent.com/abc.jpg`
  
假设 A/B 用户均访问到 CDN 节点 X，节点 X 上无上述两个资源的缓存，默认情况下，忽略大小写缓存为关闭状态，访问流程如下：
- 用户 A 的访问回源站获取`http://cloud.tencent.com/abc.JPG`图片，并缓存在 CDN 节点 X 上，其对应的缓存键为 `http://cloud.tencent.com/abc.JPG`
- 用户 B 的访问回源站获取`http://cloud.tencent.com/abc.jpg`图片，并缓存在 CDN 节点 X 上，其对应的缓存键为`http://cloud.tencent.com/abc.jpg`
  
开启了忽略大小写缓存配置后，上述场景的访问流程如下：
- 用户 A 的访问回源站获取`http://cloud.tencent.com/abc.JPG`图片，并缓存在 CDN 节点 X 上，其对应的缓存键为 `http://cloud.tencent.com/abc.jpg`
- 用户 B 的访问在 CDN 节点 X 命中资源，直接获取所需内容。
