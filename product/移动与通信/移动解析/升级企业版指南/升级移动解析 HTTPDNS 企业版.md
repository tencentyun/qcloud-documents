
## 背景
移动解析 HTTPDNS 是面向多端应用（移动端APP、小程序、PC客户端应用）的域名解析服务，基于 HTTP 协议向腾讯云的 DNS 服务器发送域名解析请求，替代了基于 DNS 协议向运营商 LocalDNS 发起解析请求的传统方式，避免在不同的网络环境中面临 LocalDNS 造成的域名劫持和跨网访问问题，根治移动互联网服务中域名解析异常的问题。

由于某些客户过度使用 119.29.29.29 的开放公共解析服务，近一年 119.29.29.29 免费测试服务的解析量快速增涨造成大量公共资源消耗，并且造成该公共服务的高质量解析效果得不到保障，损害了广大互联网用户的体验，所以为提升用户的解析质量，进⽽推出企业版（接入IP：119.29.29.98/99）。并且开放公共解析服务将于2022年1⽉1⽇0时停⽌服务，在此之前将根据监控的用量情况逐步缩减免费测试服务的容量，因此，为避免影响客户业务，请您尽快完成企业版升级。

## 企业版功能特性
HTTPDNS ⾮企业版仅提供基础的域名解析服务，以下功能特性均为企业版独享。

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
    <td>⾮企业版，测试使⽤时，单个 IP 请求上限100QPS，单个域名上限1000QPS。</td>
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

>?
>- ECS（EDNS-Client-Subnet）协议在 DNS 请求包中附加请求域名解析的用户 IP 地址，DNS 服务器可以根据该地址返回用户更容快速访问的服务器 IP 地址。
>- 移动解析 HTTPDNS 公共服务已经不再维持 ECS IP 库的常态化更新，仅保持每周更新一次。
>
## 迁移指引
>?针对在**2021年9⽉30⽇23:59:59前**以及**2021年10⽉31⽇23:59:59前**迁移 HTTPDNS 企业版的客户，分别提供相关补贴政策。具体可查看 [过渡期补贴政策说明](https://cloud.tencent.com/document/product/379/59288)。
>
### 步骤1：开通移动解析HTTPDNS
详细操作请参见：[开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577)。

### 步骤2：绑定授权ID 
- 若您已拥有授权ID，请先进行绑定授权 ID 操作，详细请参见：[已拥有授权 ID](https://cloud.tencent.com/document/product/379/54577#.E5.B7.B2.E6.8B.A5.E6.9C.89.E6.8E.88.E6.9D.83-id)。
- 若无授权ID，完成开通移动解析HTTPDNS 操作后可跳过此步骤。

### 步骤3：添加域名
详细操作请参见：[添加域名](https://cloud.tencent.com/document/product/379/54588)。

### 步骤4：接入移动解析 HTTPDNS 企业版

请根据您的业务与使用情况选择接入移动解析 HTTPDNS 企业版方式：

<dx-tabs>
::: 使用 HTTPDNS API 接口解析域名
#### 已经使用移动解析 HTTPDNS 企业版服务，但目前接入的是119.29.29.29
无需在控制台进行任何操作。
您只需在业务代码中将接入 IP 切换为 `119.29.29.99`（HTTPS 加密方式）或者 `119.29.29.98`（AES/DES 加密方式）。接入指引参见：[接入移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/3522#2.-.E4.BD.BF.E7.94.A8-httpdns-api-.E6.8E.A5.E5.8F.A3.E8.A7.A3.E6.9E.90.E5.9F.9F.E5.90.8D)。


#### 使用免授权方式访问119.29.29.29，没有授权 ID，直接通过 HTTP 请求服务
1. 在 [移动解析 HTTPDNS 控制台](https://console.cloud.tencent.com/httpdns) 开通服务，详情请查看 [开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577)。
2. 开通成功后，您将获得相关授权信息进行调用服务，此过程不会影响 `119.29.29.29` 的使用。为确保您的业务正常运行，开通后建议您逐步切量，将请求从 `119.29.29.29` 切换至 `119.29.29.99/98`。详情请查看 [接入移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/3522#2.-.E4.BD.BF.E7.94.A8-httpdns-api-.E6.8E.A5.E5.8F.A3.E8.A7.A3.E6.9E.90.E5.9F.9F.E5.90.8D)。

#### 使用授权方式访问119.29.29.29，但未开通过移动解析 HTTPDNS 企业版服务，有授权 ID，但没有控制台权限
1. 在 [移动解析 HTTPDNS 控制台](https://console.cloud.tencent.com/httpdns) 开通服务，开通过程中将已有授权 ID 进行绑定，详情请查看 [开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577#.E5.B7.B2.E6.8B.A5.E6.9C.89.E6.8E.88.E6.9D.83-id)。
2. 绑定成功后，您只需在业务代码中将接入 IP 切换为 `119.29.29.99`（HTTPS  加密方式）或者 `119.29.29.98`（AES/DES 加密方式）。详情请查看 [接入移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/3522#2.-.E4.BD.BF.E7.94.A8-httpdns-api-.E6.8E.A5.E5.8F.A3.E8.A7.A3.E6.9E.90.E5.9F.9F.E5.90.8D)。
:::
::: 使用最新的 HTTPDNS SDK 接口解析域名
1. 使用最新的 HTTPDNS SDK 接口解析域名需在移动解析 HTTPDNS 管理控制台提交接入 SDK 的申请，详情参见：[SDK 开通流程](https://cloud.tencent.com/document/product/379/12544)。
2. 开通成功后，HTTPDNS 服务提供腾讯云⾃研的 SDK，高度定制化、可直接嵌入 App 内调用，已经广泛应用于腾讯各类游戏客户端，功能成熟稳定。您可根据您需接入的环境选择以下指引进行接入：
	- [iOS SDK 文档](https://cloud.tencent.com/document/product/379/17669)
	- [Android SDK](https://cloud.tencent.com/document/product/379/17655)
	- [特殊场景-HTTPS](https://cloud.tencent.com/document/product/379/6471)
	- [特殊场景-Unity接入](https://cloud.tencent.com/document/product/379/6472)
	- [特殊场景-H5页面](https://cloud.tencent.com/document/product/379/6473)
:::
</dx-tabs>


## 常见问题
#### 什么是授权ID、密钥、token？
授权ID：腾讯云移动解析  HTTPDNS 授予客户的唯一标识，允许客户通过该标识以 HTTP DES/AES 方式接入移动解析 HTTPDNS 。
密钥：腾讯云移动解析 HTTPDNS 授予客户的唯一加密密钥，与授权 ID 对应，根据加密方式分为 DES/AES 密钥，用于对请求参数进行加密，以及对解析结果进行解密。
token：腾讯云移动解析 HTTPDNS 授予客户的唯一令牌，允许客户通过该令牌以 HTTPS 方式接入移动解析 HTTPDNS。

#### 如何以 HTTP DES/AES 方式接入 119.29.29.98？
1. 在业务代码中将接入 IP 切换为 119.29.29.98（AES/DES 加密方式） 

2. 利用控制台提供的 DES/AES 密钥对域名和 IP 参数进行加密处理，例如： 
```
 http://119.29.29.98/d?dn=cloud.tencent.com&id=xxx&ip=1.2.3.4 
```                
其中的 `cloud.tencent.com` 和 `1.2.3.4` 为域名和IP，DES加密后的信息，授权 ID xxx 不需要进行加密。 
3. 利用控制台提供的 DES/AES 密钥对解析结果进行解密处理。

#### 如何以 HTTPS 方式接入119.29.29.99？

1. 在业务代码中将接入 IP 切换为 119.29.29.99（HTTPS 加密方式）

2. 加入控制台提供的参数 token，例如：
```
https://119.29.29.99/d?dn=cloud.tencent.com&token=xxxxx&ip=1.2.3.4
```

