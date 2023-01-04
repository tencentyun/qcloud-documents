## 功能简介

调整资源在节点中缓存的时间长短，优化节点缓存，提升请求资源的加载速度，及时淘汰旧资源。

> ?
> - EdgeOne 会根据节点缓存 TTL 中配置的缓存过期时间，判断节点缓存的资源是否过期。
> - 若客户端访问的资源在节点的缓存未过期，节点直接将缓存返回给客户端。
> - 若客户端访问的资源在节点未缓存该资源或缓存已过期，则节点会回源站获取最新资源并缓存到节点，同时返回给客户端。
> - 若源站资源更新后，需要立刻更新节点的缓存，可使用 [清除缓存](https://cloud.tencent.com/document/product/1552/70759) 功能主动清除节点未过期的旧缓存，保证后续请求可以获取到源站最新的资源。

## 操作步骤

1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**站点加速** > **缓存配置**。
2. 在缓存配置页面，选择所需站点，单击节点缓存 TTL 模块的**设置**。
![](https://qcloudimg.tencent-cloud.cn/raw/923650d5517b0e4155915e242f3d27b4.png)
配置项说明：
 - 遵循源站 Cache-Control 头：
<table>
<thead>
<tr>
<th width="30%">配置项</th>
<th>源站无 Cache-Control 头时</th>
<th>详情</th>
</tr>
</thead>
<tbody><tr>
<td rowspan=3 >遵循源站 Cache-Control 头（<strong>默认配置</strong>）</td>
<td>默认缓存策略（<strong>默认配置</strong>）</td>
<td>详情请参见 <a href="#mr">对应表格</a></td>
</tr>
<tr>
<td>不缓存</td>
<td>-</td>
</tr>
<tr>
<td>自定义时间</td>
<td>-</td>
</tr>
</tbody></table>
<p><a id="mr"></a>遵循默认缓存策略：</p>
<table>
<thead>
<tr>
<th width="30%">分类</th>
<th width="70%">缓存</th>
</tr>
</thead>
<tbody><tr>
<td>源站含 Last-Modified 头</td>
<td>缓存时间= ( 当前时间 - last_modified ) * 0.1。计算结果在10秒~3600秒及之间的，取计算结果时间；小于10秒的，按照10秒处理；大于3600秒的，按照3600秒处理</td>
</tr>
<tr>
<td>源站不含 Last-Modified 头</td>
<td>依据文件后缀缓存<ul><li>动态文件后缀：php、aspx、asp、jsp、do、dwr、cgi、fcgi、action、ashx、axd、json，不缓存。</li><li>静态文件后缀：以下列举的文件后缀缓存2小时，未匹配以下文件后缀的则不缓存。<ul><li> 图片：jpg、png、jpeg、webp、gif、heif、heic、kpg、ico。</li><li>网页：mp4、mp3、m3u8、ts、m4a、avi、m4s、ogg。</li><li>网页：html、js、css。</li><li>zip、7z、tar、br、gz、rar、bz2。</li><li>文档：doc、docx、xls、xlsx、pdf、ppt、pptx。</li><li>应用程序：apk、exe、bin。</li><li>其它：vsv、iso、jar、swf、chunk、atlas。</li></ul></td>
</tr>
</tbody></table>
  - 不缓存：不在节点缓存资源。
  - 自定义时间：自定义资源缓存时长，默认开启“强制缓存”。
> ?
> - 开启“强制缓存”时，节点缓存 TTL 按照配置的自定义时间，即使源站的 `Cache-Control` 为 `no-cache/no-store/private`等不缓存头
> - 关闭“强制缓存”时，当源站的 `Cache-Control` 为 `no-cache/no-store/private` 等不缓存头，即使配置了自定义时间，节点仍不缓存资源，优先遵循源站的不缓存头
> - 关闭“强制缓存”需前往 [规则引擎](https://cloud.tencent.com/document/product/1552/70901) 自定义配置节点缓存 TTL 规则。为了保证缓存效果，建议您保持开启“强制缓存”。
> 

3. 如需针对某个子域名或请求 URL等更细请求维度设置区别于站点全局的配置，请前往 [规则引擎](https://cloud.tencent.com/document/product/1552/70901) 创建自定义规则。


附：整体节点缓存行为如下：

![](https://qcloudimg.tencent-cloud.cn/raw/d59bfcafca7b12a1b258bfdf4047e716.png)
