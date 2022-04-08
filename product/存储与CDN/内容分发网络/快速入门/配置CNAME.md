![](https://main.qcloudimg.com/raw/705a1315248316e32c25a8093fd9f799.png)

## 准备工作

### 接入域名
配置 CNAME 前，您需要完成 [域名接入](https://cloud.tencent.com/document/product/228/41215)。如果您已完成域名接入，请继续后续操作步骤


## 操作步骤

### 配置步骤

您需要在您的域名注册商处，配置您的加速域名解析到腾讯云 CDN 分配的 CNAME 域名上。在您完成 CNAME 解析配置后，当用户请求您的加速域名时，DNS 才会将用户请求解析到腾讯云 CDN 平台，实现加速效果。
根据您在域名接入时输入的加速域名的方式，您在域名注册商处建议按如下示例进行配置：

<table width="718px">
<tbody>
<tr>
<th colspan="2">腾讯云 CDN</th>
<th colspan="3">域名注册商</th>
<th rowspan="2">说明</th>
</tr>
<tr>
<td>加速域名</td>
<td>CNAME 域名</td>
<td>主机记录 / Host (Name)</td>
<td>记录类型 / Type</td>
<td>记录值/Value (Points to)</td>
</tr>
<tr>
<td>dnspod.com</td>
<td>dnspod.com.cdn.dnsv1.com</td>
<td>@</td>
<td>CNAME</td>
<td>dnspod.com.cdn.dnsv1.com</td>
<td>支持用户直接请求域名 dnspod.com</td>
</tr>
<tr>
<td>www.dnspod.com</td>
<td>www.dnspod.com.cdn.dnsv1.com</td>
<td>www</td>
<td>CNAME</td>
<td>www.dnspod.com.cdn.dnsv1.com</td>
<td>支持用户请求www.dnspod.com</td>
</tr>
<tr>
<td>support.dnspod.com</td>
<td>support.dnspod.com.cdn.dnsv1.com</td>
<td>support</td>
<td>CNAME</td>
<td>support.dnspod.com.cdn.dnsv1.com</td>
<td>支持用户请求二级域名support.dnspod.com</td>
</tr>
<tr>
<td>*.dnspod.com</td>
<td>a31aea03.dnspod.com.cdn.dnsv1.com</td>
<td>*</td>
<td>CNAME</td>
<td>a31aea03.dnspod.com.cdn.dnsv1.com</td>
<td>泛解析，支持用户访问其他所有域名*.dnspod.com</td>
</tr>
</tbody></table>

>!
>1. 为避免解析冲突，若域名解析原来有配置 A 记录或 MX 记录，则添加 CNAME 记录时，应当将原 A 或 MX 记录暂停解析或删除。
>2. 因为 DNS 变更解析到实际生效需要一段时间，期间可能会导致网站暂时不可访问，请您留意变更操作对业务的影响。
>3. 为避免业务受到影响，当暂停或停用 CDN 加速时，域名解析应注意从 CDN CNAME 域名改回到源站。

如下提供腾讯云和阿里云的域名解析配置步骤说明：

[](id:m1)
### 腾讯云设置方法

#### 一键配置

如果您的域名商为腾讯云，推荐您使用 CNAME 一键配置功能，详情请参见 [DNSPod 一键配置 CNAME](https://cloud.tencent.com/document/product/228/59152)。

![](https://main.qcloudimg.com/raw/bce6d4d2207f120dfe69a4732b5c82a3.png)

#### 手动配置

1. 在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 复制 CNAME 地址。
   在您域名成功解析前，CNAME 处会有提示 icon。复制此处的 CNAME 值。
![](https://main.qcloudimg.com/raw/953d05b2e06eb8de643a52bc8d175285.png)
2. 登录 [DNS 解析 DNSPod 控制台](https://console.cloud.tencent.com/cns)，单击**解析**按钮。
![](https://main.qcloudimg.com/raw/5ad4678bc71367d14e97cf038fe131e2.png)
3. 添加 CNAME 记录，单击**确认**。
![](https://main.qcloudimg.com/raw/a76c964c1008726ff39eb237338c2a52.png)
4. 等待配置生效。

**配置项详解：**

| 配置项   | 配置说明                                                     |
| :------- | :----------------------------------------------------------- |
| 主机记录 | 主机记录相当于域名的前缀。<br><br>**例:** 添加 `dnspod.com` 域名的解析，在 “主机记录” 处选择 “@” ；添加 `www.dnspod.com` 域名的解析，在 “主机记录” 处选择 “www” 。 |
| 记录类型 | 选择 “CNAME”。                                               |
| 线路类型 | 选择 “默认” 类型。DNSPod 支持按多种方式划分线路，让指定用户访问该记录。详细说明请查看 [解析线路说明](https://docs.dnspod.cn/dns/5f4775898ae73e11c5b01afc/)。 |
| 记录值   | 指向的域名，填写加速域名的 CNAME 值：xxx.xxx.com.cdn.dnsv1.com。记录生成后会自动在域名后面补一个“.”。 |
| 权重     | 同一条主机记录相同的线路，可以针对不同的记录值设置权重。解析时将根据设置的权重比例进行返回。输入范围：0-100 |
| MX       | 优先级设置。数值越低，优先级别越高，推荐保持默认空值。       |
| TTL      | 缓存时间。数值越小，修改记录各地生效时间越快，默认为600秒。  |

[](id:m2)
### 阿里云设置方法

若您的 DNS 服务商为阿里云，您可通过如下步骤添加 CNAME 记录。

1. 在 [腾讯云 CDN 控制台](https://console.cloud.tencent.com/cdn) 复制 CNAME 地址
   在您域名成功解析前，CNAME 处会有提示 icon。复制此处的 CNAME 值。
![](https://main.qcloudimg.com/raw/1103227249112935d45d0c963446e1cc.png)
2. 登录阿里云控制台云解析DNS。
3. 单击要解析的域名，进入解析记录页。
4. 进入解析记录页后，单击**添加记录**按钮，开始设置解析记录。
5. 将记录类型选择为 CNAME。主机记录即域名前缀，可任意填写（如：www）。记录值填写为步骤1中复制的CNAME值。解析线路，TTL 默认即可。
<img src="https://main.qcloudimg.com/raw/19d27d39d0ed39d3fe319410b5ef6439.png" width="80%">
6. 填写完成后，单击**确认**，即可完成解析设置。

## 后续步骤

### 验证 CNAME 是否生效

不同的 DNS 服务商CNAME 生效的时间略有不同，一般在半个小时之内生效。您可以通过 nslookup 或 dig 的方式来查询 CNAME 是否生效，若应答的CNAME记录是我们配置的CNAME，则说明配置成功，此时您已成功开启加速服务。

- nslookup -qt=cname <加速域名>
<img src="https://main.qcloudimg.com/raw/1f94ea7e3ee46fc761e8e839ce68a86d.png" width="70%">
- dig <加速域名></br>
<img src="https://main.qcloudimg.com/raw/fe9b8f9a1a26d3a7df5db614762caeaf.png" width="70%">

### 配置指南

您已完成 CDN 服务的基础配置，有关 CDN 服务的更多配置，可以在 [配置指南](https://cloud.tencent.com/document/product/228/37851) 目录下对应的项目进行了解。

