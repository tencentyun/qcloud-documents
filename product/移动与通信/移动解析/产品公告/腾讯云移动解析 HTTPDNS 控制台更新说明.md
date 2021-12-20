为了让您有更好的体验，[腾讯云移动解析 HTTPDNS 控制台](https://console.cloud.tencent.com/httpdns) 已全面升级，在原移动解析 HTTPDNS 控制台的基础上进行了优化体验。新版控制台新增域名管理、开发配置、流量包管理等功能模块，提供更全面更便捷的配置和管理。本文档将对新版移动解析 HTTPDNS 控制台的使用进行简要说明。
如果在使用过程中有任何疑问、建议或意见，请 [联系我们](https://cloud.tencent.com/document/product/400/35259)，感谢您的使用。

## 功能概述
<table width="100%" height="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<th style="width:15%;">模块</th>
<th>说明</th>
</tr>
<tr>
<td  style="padding:10px 15px">HTTPDNS 概览</td>
<td>HTTPDNS 概览页主要用于展示服务概览，如解析中域名数、解析量、流量消耗情况等。</li></td>
</tr>
<tr>
<td>域名管理</td>
<td>域名管理页面主要用于添加解析域名和查看解析域名使用情况。详情请参见：<a href="https://cloud.tencent.com/document/product/379/54588">添加解析域名</a> 与 <a href="https://cloud.tencent.com/document/product/379/54589">查看域名解析详情。</a></td>
</tr>
<tr>
<td>开发配置</td>
<td>开发配置主要用于申请应用（HTTPDNS SDK）和相关鉴权信息的查看和管理。包含以下功能：<li>域名解析状态、DES 加密、AES 加密、HTTPS 加密的开启与关闭。</li><li>密钥信息查看。</li><li>申请应用（HTTPDNS SDK）和查看申请应用的信息。</li></td>
</tr>
<tr>
<td>流量包管理</td>
<td>主要用于移动解析 HTTPDNS 流量包管理。如流量包购买和查看使用情况等。</td>
</tr>
<tr>
<td>API</td>
<td>新版本 API 更新为使用 119.29.29.99/98 接入，同时原移动解析 HTTPDNS 服务地址 119.29.29.29 仅供开发调试使用，无 SLA 保障，不建议用于正式业务，请您尽快将正式业务迁移至 119.29.29.99/98。详情请参见：<a href="https://cloud.tencent.com/document/product/379/54976">API 说明。</a></td>
</tr>
</table>

## 新版本特性
与原移动解析 HTTPDNS 提供的服务相比，新版本具有以下新的特性：
- 支持 AES/DES/HTTPS 数据加密。
- 支持批量查询功能。
- 支持查询结果内返回被查询域名。
- 支持使用 IPv6 地址作为 ECS（EDNS-Client-Subnet）查询参数。
>?ECS（EDNS-Client-Subnet）协议在 DNS 请求包中附加请求域名解析的用户 IP 地址，DNS 服务器可以根据该地址返回用户更容快速访问的服务器 IP 地址。
