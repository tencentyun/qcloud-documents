
## 背景
移动解析 HTTPDNS 是面向多端应用（移动端 App、小程序、PC 客户端）的域名解析服务，基于 HTTP 协议向腾讯云的 DNS 服务器发送域名解析请求，替代了基于 DNS 协议向运营商 LocalDNS 发起解析请求的传统方式，避免在不同的网络环境中面临 LocalDNS 造成的域名劫持和跨网访问的问题，根治移动互联网服务中域名解析异常的问题。
>?
- 由于技术架构升级和新特性支持，产品团队推出移动解析 HTTPDNS 服务企业版 `119.29.29.98/99`。并且移动解析 HTTPDNS 服务免费版会逐步裁撤，并最终将于 **2022年1月1日0时** 停止服务。
- 移动解析 HTTPDNS **原 IP `119.29.29.29` 的企业版**容量也将随着服务器资源到期而逐渐缩容，最终完全下线。建议您 [切换至119.29.29.98/99](https://cloud.tencent.com/document/product/379/59133)，以消除可能遇到的突发风险。

移动解析 HTTPDNS 产品团队将提供 [服务支持](https://cloud.tencent.com/document/product/379/56872)，协助客户切换至移动解析服务企业版`119.29.29.98/99`。因此，为了避免影响贵司业务，请尽快完成接入 IP 切换。

## 企业版功能特性
HTTPDNS `119.29.29.29` 仅提供基础的域名解析服务，以下功能特性均为 `119.29.29.98/99` 独享。

<table>
<thead>
  <tr>
    <th>功能特性</th>
    <th>说明<br></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>⽆限请求 </td>
    <td><ul style="margin:0"><li>`119.29.29.98/99`，客户端 App 的接口请求频率没有上限。</li><li>`119.29.29.29`，测试使⽤时，单个 IP 请求上限100QPS，单个域名上限1000QPS。</li></ul></td>
  </tr>
  <tr>
    <td>境外节点 </td>
    <td>近⼏年重点扩充企业版的境外节点，建⽴基于 BGP Anycast ⽹络架构的⾼防集群。<br></td>
  </tr>
  <tr>
    <td>解析联动加速 </td>
    <td>⾯向权威解析托管在 DNSPod 的域名有加成的缓存加速能⼒。</td>
  </tr>
  <tr>
    <td>HTTP SDK 方式接入 HTTPDNS</td>
    <td>通过 SDK 实现快速接入，可兼容 IOS/Android 多平台移动应⽤。<br></td>
  </tr>
  <tr>
    <td>DES、AES、HTTPS <br>数据加密</td>
    <td>使⽤ DES、AES 、HTTPS 加密，可以防⽌明⽂请求在传输过程中被恶意篡改。<br></td>
  </tr>
  <tr>
    <td>新特性支持</td>
    <td>所有正在研发的新功能特性只在企业版上发布。</td>
  </tr>
  <tr>
    <td>预警提醒</td>
    <td>告警通知。</td>
  </tr>
  <tr>
    <td>域名管理</td>
    <td>在控制台中管理客户域名。<br></td>
  </tr>
  <tr>
    <td>报表统计 </td>
    <td>统计和查看域名解析量的变化情况。<br></td>
  </tr>
  <tr>
    <td>服务升级</td>
    <td>针对重点客户的数据审计分析，⾏业解决⽅案⽀持。<br></td>
  </tr>
  <tr>
    <td>SLA 保障</td>
    <td>承诺99.99%服务可⽤性。<br></td>
  </tr>
</tbody>
</table>

>?ECS（EDNS-Client-Subnet）协议在 DNS 请求包中附加请求域名解析的用户 IP 地址，DNS 服务器可以根据该地址返回用户更容快速访问的服务器 IP 地址。
>
## 切换指引
>?
>- 针对在**2021年9⽉30⽇23:59:59前**以及**2021年10⽉31⽇23:59:59前**迁移 HTTPDNS 企业版的客户，分别提供相关补贴政策。具体请参见：[过渡期补贴政策说明](https://cloud.tencent.com/document/product/379/59288)。
- 若您已经使用移动解析 HTTPDNS 企业版服务，但目前接入的是 `119.29.29.29`，则无需在控制台进行任何操作。您只需在业务代码中将接入 IP 切换为 `119.29.29.99`（HTTPS 加密方式）或者 `119.29.29.98`（AES/DES 加密方式）。接入指引请参见：[接入移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/3522#2.-.E4.BD.BF.E7.94.A8-httpdns-api-.E6.8E.A5.E5.8F.A3.E8.A7.A3.E6.9E.90.E5.9F.9F.E5.90.8D)。
- 若您已经使用移动解析 HTTPDNS SDK 企业版服务，请更新为最新版 SDK，并替换接入 IP 为 `119.29.29.99/98`。

### 步骤1：开通移动解析 HTTPDNS
详细操作请参见：[开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577)。

### 步骤2：绑定授权 ID 
- 若您已拥有授权 ID，请先进行绑定授权 ID 操作，详细请参见：[已拥有授权 ID](https://cloud.tencent.com/document/product/379/54577#.E5.B7.B2.E6.8B.A5.E6.9C.89.E6.8E.88.E6.9D.83-id)。
- 若无授权 ID，完成开通移动解析 HTTPDNS 操作后可跳过此步骤。

### 步骤3：添加域名
详细操作请参见：[添加域名](https://cloud.tencent.com/document/product/379/54588)。

### 步骤4：接入移动解析 HTTPDNS 企业版

请根据您的业务与使用情况选择接入移动解析 HTTPDNS 企业版方式：

<dx-tabs>
::: 使用 HTTPDNS API 接口解析域名
1. 
 您可以使用以下两种方式进行查询：
	- 单个查询方式
		- HTTPS 加密方式：
		` https://119.29.29.99/d?dn=[域名]&token=[HTTPS Token]&ttl=1`
		- AES/DES 加密方式：
		 `http://119.29.29.98/d?dn=[域名加密后的字符串]&id=[授权ID]&ttl=1`
		- 具体加密方式请参见：[加密指引](https://cloud.tencent.com/document/product/379/3530)。
		- 具体请求格式请参见：[API 说明](https://cloud.tencent.com/document/product/379/54976)。
	- 批量查询方式
移动解析 HTTPDNS 支持批量查询域名操作，一次性可输入多个域名数据进行查询。域名之间使用 `,` 分隔，查询结果以 `\n` 分隔。
例如，同时查询 `cloud.tencent.com,www.qq.com,www.dnspod.cn`。
2. 客户端改造：将客户端的解析方式改为 HTTPDNS 解析，注意在接入过程中需要**保留 LocalDNS 的解析方式作为备选**，具体请参见：[最佳实践](https://cloud.tencent.com/document/product/379/3523)。

:::
::: 使用最新的 HTTPDNS SDK 接口解析域名

1. HTTPDNS SDK 接口解析域名需在移动解析 HTTPDNS 管理控制台提交接入 SDK 的申请，详情请参见：[SDK 开通流程](https://cloud.tencent.com/document/product/379/12544)。
2. 开通成功后，HTTPDNS 服务提供腾讯云⾃研的 SDK，高度定制化、可直接嵌入 App 内调用，已经广泛应用于腾讯各类游戏客户端，功能成熟稳定。您可根据您需接入的环境选择以下指引进行操作：
 	- [iOS SDK 文档](https://cloud.tencent.com/document/product/379/17669)
 	- [Android SDK](https://cloud.tencent.com/document/product/379/17655)
 	- [特殊场景-HTTPS](https://cloud.tencent.com/document/product/379/6471)
 	- [特殊场景-Unity 接入](https://cloud.tencent.com/document/product/379/6472)
 	- [特殊场景-H5 页面](https://cloud.tencent.com/document/product/379/6473)
:::
</dx-tabs>


>?原企业版用户迁移 IP 后，可继续使用每月赠送的免费资源包，原购买的解析套餐额度，也可以延续使用，套餐的额度和折扣与之前保持一致，计费规则也保持一致。

