您在 CDN 控制台完成域名的添加和配置后，为了保证现网业务不受影响，建议您进行 CDN 访问测试，若访问正常，再切换 DNS 解析至腾讯云。
>! 模拟访问等同于正常的 CDN 访问，因此也会产生 CDN 基础服务和增值服务费用（如果测试的是增值服务），计费方式与正常使用 CDN 的计费方式相同。详细信息请参见 [计费说明](https://cloud.tencent.com/document/product/228/2949)。


## 操作步骤
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧导航栏中，单击域名管理进入域名管理页面，搜索到需要测试      的加速域名，如 `www.qcdntest.cn`。
![](https://qcloudimg.tencent-cloud.cn/raw/8e7ef6c09ac3bdf99a335f1e99db6789.png)
2. 复制分配的 CNAME 域名，获取 CDN 节点 IP
CNAME地址：`www.qcdntest.cn.cdn.dnsv1.com.cn`
打开终端命令窗口，在命令行中执行命令：`ping www.qcdntest.cn.cdn.dnsv1.com.cn`，返回的 IP 即为 CDN 加速节点。
<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/811c8e9ca1f21e89c55734c935cad9b2.png" width="70%">
<br>
3. 设置本地 hosts 文件
将步骤2获取的节点 IP（110.185.117.235）和加速域名（`www.qcdntest.cn`）绑定到电脑本地 hosts 文件中，填写方法为 IP 域名，其中IP地址在前，加速域名在后，中间用空格分隔。
Windows系统：hosts 文件路径位置为C:\Windows\System32\drivers\etc\hosts，按照下图所示进行绑定。
<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/2d63afd6bb4abec0e064efd795eec39b.png" width="70%">
<br>
Mac系统：进入终端（命令窗口）里，输入 sudo vi/etc/hosts ，回车后再输入密码，再回车就可以打开 hosts 文件。进入后，输入 i 就可以编辑了。填写方法参照上述 Windows 的即可。
4. 进行模拟访问测试
打开本地浏览器，访问加速域名对应的测试 URL，建议通过浏览器自带的开发者工具查看请求/响应头。示例如下：
开发者工具打开方法：打开谷歌浏览器窗口右上方的菜单，选择工具 > 开发者工具(Tools > Developer Tools)；或使用快捷键 F12。
![](https://qcloudimg.tencent-cloud.cn/raw/d4411cda802c92549f30b9fc15c4153b.png)


>?
> 1. 您需要确认 Remote Address 的 IP 是否与您在步骤3中绑定的 IP 一致
 - 若一致，表明访问 CDN 节点正常，您可以将域名解析切换至腾讯云 CDN；
 - 若不一致，说明没有请求到绑定的CDN节点IP，您需要确认hosts设置是否正确并生效
2. 若返回4xx、5xx等异常状态码，可以绑定源站进行测试，若与源站一致，请检查源站；若与源站不一致，请检查 CDN 回源配置是否正确，如源站IP，回源协议、回源HOST等。
3. 首次访问可能会因为节点没有缓存导致响应慢，您可以预热后再进行访问测试。
	-  预热方法：登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的刷新预热，进入后可按需提交 URL 预热任务：
	-  判断是否缓存命中的方法：有返回以下任意一个，即代表缓存命中，否则代表缓存未命中。
X-Cache-Lookup: Hit From MemCache
X-Cache-Lookup: Hit From Disktank
X-Cache-Lookup: Cache Hit
