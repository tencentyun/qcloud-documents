## 手动安装证书
证书安装目前有下列15种方式，您可以根据您购买的证书加密标准类型和搭建的服务器类型进行证书安装。
>? 
>- 使用一键 HTTPS 功能，您无需进行繁琐的 SSL 证书部署操作，即可帮助您实现从 HTTP 到 HTTPS 的能力升级。详情请参考 [一键 HTTPS](https://cloud.tencent.com/document/product/400/58062)。
>- 目前仅提供以下15种安装证书的方式。
>

<table>
<tr>
<th>证书类型</th>
<th>服务器系统</th>
<th>证书安装方式</th>
</tr>
<tr>
<td rowspan="12">国际标准证书（RSA/ECC）</td>
<td rowspan="8">Linux 系统</td>
<td> <a href="https://cloud.tencent.com/document/product/400/50874">宝塔面板 SSL 证书安装</a></td>
</tr>
<tr><td> <a href="https://cloud.tencent.com/document/product/400/35243">Apache 服务器证书安装</a></td></tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/35244">Nginx 服务器证书安装</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/35224">Tomcat 服务器 SSL 证书安装部署（JKS 格式）</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/65706">Tomcat 服务器 SSL 证书安装部署（PFX 格式）</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/44759">GlassFish 服务器证书安装</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/44760">JBoss 服务器证书安装</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/44761">Jetty 服务器证书安装</a></td>
</tr>
<tr>
<td rowspan="4">Windows 系统</td>
<td><a href="https://cloud.tencent.com/document/product/400/35225">IIS 服务器证书安装</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/47358">Weblogic 服务器证书安装</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/61400">Apache 服务器 SSL 证书安装部署（Windows）</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/67502">Tomcat 服务器 SSL 证书安装部署（JKS 格式）（Windows）</a></td>
</tr>
<tr>
<td rowspan="3">国密标准证书（SM2）</td>
<td rowspan="2">Linux 系统</td>
<td><a href="https://cloud.tencent.com/document/product/400/47359">Apache 服务器国密证书安装</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/400/47360">Nginx For Linux 国密证书安装</a></td>
</tr>
<tr>
<td>Windows 系统</td>
<td><a href="https://cloud.tencent.com/document/product/400/47361">Nginx For Windows 服务器国密证书安装</a></td>
</tr>
</table>

## 根证书下载
如果您的业务需要通过非浏览器客户端访问您的服务，则需要下载安装根证书，详情请参考 [SSL 根证书下载](https://cloud.tencent.com/document/product/400/67038)。

## 证书部署至云服务
目前证书支持以下方式部署至云服务，请您根据实际需求进行部署操作。
- [安装部署 SSL 证书到负载均衡（CLB）指引](https://cloud.tencent.com/document/product/400/6502)
- [安装部署 SSL 证书到内容分发网络（CDN）指引 ](https://cloud.tencent.com/document/product/400/51804)
- [安装部署 SSL 证书到 Web 应用防火墙（WAF）指引](https://cloud.tencent.com/document/product/400/51803)
- [安装部署 SSL 证书到 DDoS 防护指引](https://cloud.tencent.com/document/product/400/56290)
- [安装部署 SSL 证书到云直播（CSS）指引](https://cloud.tencent.com/document/product/400/56291)
- [安装部署 SSL 证书到容器服务 Ingress](https://cloud.tencent.com/document/product/400/67651)
- [腾讯云实现全站 HTTPS 方案](https://cloud.tencent.com/document/product/400/6813)

