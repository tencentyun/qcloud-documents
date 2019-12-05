缓存刷新方式有 URL 刷新、目录刷新和 URL 预热。URL 刷新是以文件为单位进行缓存刷新。目录刷新是以目录为单位，将目录下的所有文件进行缓存刷新。URL 预热是以文件为单位进行资源预热。
刷新与预热的区别：
- 刷新后，会删除该资源在全网 CDN 节点上的缓存。当用户请求到达节点时，节点会回源站拉取对应资源，返回给用户并缓存到节点，保证用户获取到最新资源。
- 预热后，该资源会提前缓存到全网 CDN 节点。当用户请求到达节点时，可以直接在节点获取到资源。

您在源站上更新资源后，如果希望用户访问不再获取旧资源，直接获取新资源，您可以使用 **URL 刷新** 或 **目录刷新** 功能。如果希望 CDN 预先将资源由源站主动缓存至 CDN 节点，则可以使用 **URL 预热** 功能。
> **注意**：CDN 中节点缓存资源的更新机制，一般是通过缓存过期时间来控制，配置合适的缓存过期时间策略，可以有效的降低回源率，更多详情可参考 [缓存过期配置](https://cloud.tencent.com/doc/product/228/6290)。

## URL 刷新
> **注意**：
> + 每日 URL 刷新数量最多不超过 10000 个，每次刷新提交的 URL 数量不超过 1000 个，刷新任务生效时间约为 5 分钟。
> + URL 刷新的生效时间约为 5 分钟，当文件配置的缓存过期时间少于 5 分钟时，建议不使用刷新工具，而是等待超时更新。

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧菜单栏【缓存刷新】进入缓存刷新页面，选择【URL 刷新】。
![](https://mc.qcloudimg.com/static/img/9cf5812a8141253d8dbcf24520804568/urlrefresh.png)
在文本框中输入刷新对象 URL（需要输入前缀“http://” 或 “https://” ），每行输入一个，如：
<blockquote style="background-color:#F5F5F5">http://www.abc.com/test.html<br/>
http://www.def.com/image.png</blockquote>

完成后单击【提交并刷新】即可。提交后，您可以在页面左下角看到今日剩余的 URL 刷新量。

## 目录刷新
> **注意**：
> + 每日目录刷新数量最多不超过 100 个，每次刷新提交的 URL 目录数量不超过 20 个，刷新任务生效时间约为 5 分钟。
> + 目录刷新的生效时间约为 5 分钟，当文件夹配置的缓存过期时间少于 5 分钟，建议不使用刷新工具，而是等待超时更新。

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧菜单栏【缓存刷新】进入缓存刷新页面，选择【目录刷新】。
![](https://mc.qcloudimg.com/static/img/a2495006697a0e4d86711699b70bd28c/dirrefresh.png)
输入刷新目录 URL（需要输入前缀“http://” 或 “https://” ），每行输入一个，如：
<blockquote style="background-color:#F5F5F5">http://www.abc.com/test/<br/>
http://www.def.com/image/</blockquote>

完成后单击【提交并刷新】即可。提交后，您可以在页面左下角看到今日剩余的目录刷新量。

## URL 预热
> **注意**：
> + URL 预热功能暂时仅对 CDN 大客户开放。
> + 若节点上已缓存该资源且尚未过期，则不会更新为最新的资源，若您需要更新所有 CDN 节点上的资源到最新，可以在预热前先进行刷新操作。
> + 每日 URL 预热数量最多不超过 1000 个，每次预热提交的 URL 数量不超过 20 个，预热任务生效时间依据预热文件大小而定，约需要 5 到 30 分钟。

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧菜单栏【缓存刷新】进入缓存刷新页面，选择【URL 预热】。
![](https://mc.qcloudimg.com/static/img/ff5591130c83e2c664a334663c87d1a4/urlpreheat.png)
输入需要预热对象的 URL（需要输入前缀“http://” 或 “https://” ），每行输入一个，如：
<blockquote style="background-color:#F5F5F5">http://www.abc.com/test.html<br/>
http://www.def.com/image.png</blockquote>

完成后单击【提交并预热】即可。提交后，您可以在页面左下角看到今日剩余的 URL 预热量。

## 操作记录
您可以查看一个时间段内 URL 刷新，目录刷新及 URL 预热的操作记录。
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，进入【缓存刷新】页面，选择【操作记录】。完成 **选择日期**，**查询关键字**，**查询类型** 的选择或填写后，单击【查询】，操作记录将显示在下方表格中。
![](https://mc.qcloudimg.com/static/img/f3041594895d363095ab19c3293754a0/oprecord.png)