1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧导航栏中，单击**域名管理**进入域名管理页面，单击**添加域名**。
![](https://qcloudimg.tencent-cloud.cn/raw/0087b126c9ab20a9ca88cac1f5b7da2b.png)
2. 域名配置
根据您的网站信息，配置如下：
<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/4174695327716c620ac6548f4a15b867.png" width="70%">
<br>
如上图所示，当接入域名为泛域名，或已被其他用户接入，或首次接入一个新域名时，需要验证域名的归属权。若您的域名解析商为腾讯云，可以按照如下图配置TXT解析记录（针对主域名添加即可），完成验证即可添加该域名。更多详情请参见 <a href="https://cloud.tencent.com/document/product/228/61702">域名归属权验证</a>。
<img src="https://qcloudimg.tencent-cloud.cn/raw/83ac2aa53904274c22c7649f73f37581.png">
3. 源站配置
源站的用途：源站即为存储网站资源的服务器，当用户请求的资源在 CDN 节点无缓存，节点会读取域名配置的源站信息，回源拉取资源并缓存在节点。因此，源站信息务必填写准确，保证 CDN 能正常回源取到对应的资源。
根据您的源站信息，配置如下。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c7d4c13b20f3a53e0a8e87ab4d3726b3.png" width="80%">
4. 服务配置
根据您的平均文件大小和文件更新频率，分片回源无需开启，节点缓存过期配置如下：
其中：
	- 若开启分片回源，且文件大于4M，默认会按照1M分片大小逐片回源拉取；
	- 若配置了缓存策略，CDN 节点会按照设定的缓存策略缓存资源，但并不是严格按照配置的时间生效，可能会由于资源访问热度低触发缓存淘汰机制，在设置的缓存时间前就从节点上删除。更多详情请参见 [节点缓存过期配置](https://cloud.tencent.com/document/product/228/47672)。
	- **若源站资源更新后，需要立刻更新 CDN 节点的缓存，您可使用 [缓存刷新](https://console.cloud.tencent.com/cdn/refresh) 功能主动更新 CDN 节点未过期的缓存，使 CDN 节点缓存与源站资源保持一致。注意，刷新 UR L需使用CDN加速域名，而非 COS 源站域名。**
<img src="https://qcloudimg.tencent-cloud.cn/raw/7b5bd45507691aa7a99025463ed49010.png" width="80%">
<table>
<thead>
<tr>
<th>配置项</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>分片回源</td>
<td>平均文件大小500KB，无需勾选“开启分片回源”<br>• 若您的资源都是静态小文件（&lt;4M），或源站为 COS 源站且已使用数据处理类功能（例如：图片处理），不建议开启分片回源，开启后会影响回源；<br>• 若您的资源都是静态大文件，且源站已支持 Range 请求，或源站为 COS 源站且未使用数据处理类功能（例如：图片处理），建议开启分片回源，提升分发效率和响应速度。</td>
</tr>
<tr>
<td>节点缓存过期配置</td>
<td>根据网站资源的更新频率设置自定义的缓存策略，若无特殊需求，采用默认的即可。缓存策略配置方法请参见&nbsp;  <a href="https://cloud.tencent.com/document/product/228/47672">节点缓存过期配置</a>。</td>
</tr>
</tbody></table>
5. 用量封顶配置
希望将访问带宽控制在5000Mbps，配置如下：
<img src="https://qcloudimg.tencent-cloud.cn/raw/e754e3766a8f85325d45ddccb329fd9b.png" width="80%">
6. 单击**确认提交**，在弹出的页面中单击**返回域名管理**即可在域名列表中看到您添加的域名。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ff47244b3c32375334887f6e33977ac0.png" width="80%">
