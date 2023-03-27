
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧导航栏中，单击**域名管理**进入域名管理页面，单击**添加域名**。
![](https://qcloudimg.tencent-cloud.cn/raw/cab23bbfda82f8b7f31573ffd9ba4e06.png)
2. 域名配置
根据您的网站信息，配置如下：
<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/b88ea5a51c8a88982b8a611c9ad0ba00.png" width="70%">
<br>
如上图所示，当接入域名为泛域名，或已被其他用户接入，或首次接入一个新域名时，需要验证域名的归属权。若您的域名解析商为腾讯云，可以按照如下图配置 TXT 解析记录（针对主域名添加即可），完成验证即可添加该域名。更多详情请参见 <a href="https://cloud.tencent.com/document/product/228/61702">域名归属权验证</a>。
<img src="https://qcloudimg.tencent-cloud.cn/raw/022e30a743cab94bb4b88a62498f4128.png">
3. 源站配置
源站的用途：源站即为存储网站资源的服务器，当用户请求的资源在 CDN 节点无缓存，节点会读取域名配置的源站信息，回源拉取资源并缓存在节点。因此，源站信息务必填写准确，保证 CDN 能正常回源取到对应的资源。
根据您的源站信息，配置如下。
<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/25988b12fb15f27aafc645ac91923e6d.png" width="70%">
<table>
<thead>
<tr>
<th>配置项</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>源站类型</td>
<td>网站源站为稳定运行业务的自有服务器，<strong>选择“自有源”即可</strong></td>
</tr>
<tr>
<td>回源协议</td>
<td>只支持HTTP回源，<strong>回源协议选择“HTTP”即可。</strong><br>可以根据源站实际支持的协议类型，按需选择，确保选择的回源协议是源站支持的。</td>
</tr>
<tr>
<td>源站地址</td>
<td><strong>填写源站的服务器 IP 即可。</strong><br>• 支持配置多个 IP 作为源站，回源时会进行轮询回源；<br>• 支持增加配置端口（0 - 65535）和权重（1 - 100）：源站:端口:权重（端口可缺省：源站::权重），HTTPS 协议暂时仅支持443端口；<br>• 支持配置域名作为源站，此域名需要与业务加速域名不一致。</td>
</tr>
<tr>
<td>回源 HOST</td>
<td>• 定义：CDN 节点在回源时，在源站访问的站点域名，默认为加速域名。<br>•  源站地址与回源 HOST 的区别：源站配置的 IP/域名能够指引 CDN 节点回源时找到对应的源站服务器，服务器上可能存在若干 Web 站点，回源 HOST 指明了资源所在的站点。根据实际业务场景配置即可<br>• 如何填写：若通过加速域名即可回源获取到资源，无需修改回源 HOST；若需要通过非加速域名才能回源获取到资源，填写对应的域名即可。</td>
</tr>
</tbody></table>
4. 单击**确认添加**后，即可完成添加域名，同时，腾讯云 CDN 根据您的加速类型为您提供了该域名的推荐配置，您可以参考 [推荐配置](https://cloud.tencent.com/document/product/228/3149#.E7.AC.AC.E4.BA.8C.E6.AD.A5.EF.BC.9A.E6.8E.A8.E8.8D.90.E9.85.8D.E7.BD.AE) 来进行配置，或单击**返回域名管理**完成域名添加。
![](https://qcloudimg.tencent-cloud.cn/raw/c1747591525a657b3851ea84b0dd945a.png)
